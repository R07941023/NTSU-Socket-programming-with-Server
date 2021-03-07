import torch as t
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torch.autograd import Variable
from nn_model import DL_VAE
import numpy as np
import sys, time
from nn_model import model_tool
import torch.optim as optim
from opt import opt

def loss_selection():
    loss_type = opt.loss_type
    if loss_type == 'cross_entropy':
        loss = nn.CrossEntropyLoss()
    elif loss_type == 'L1':
        loss = nn.L1Loss()
    elif loss_type == 'L2':
        loss = nn.MSELoss()  # nn.MSELoss()
    elif loss_type == 'VAE':
        pass
    return loss

def optimizer_selection(optimizer_type, model):
    if optimizer_type[0] == 'Adam':
        optimizer = optim.Adam( model.parameters(), lr=optimizer_type[1], weight_decay=opt.l2_norm)
    elif optimizer_type[0] == 'SGD':
        optimizer = optim.SGD(model.parameters(), lr=optimizer_type[1], momentum=optimizer_type[2])
    return optimizer

def model_selection(dim, image_size, model_type, pretrain=None, features_layer=None):
    output_n = opt.output_n
    if model_type == 'conv':
        model = ConvNet(output_n, dim, image_size)
    elif model_type == 'fully':
        model = Fully(output_n, image_size)
    elif model_type == 'densenet161_1d':
        model = densenet161_1d()
    elif model_type == 'vgg19_1d':
        model = vgg19_1d(output_n, pretrain, features_layer)
    elif model_type == 'mobile2_1d':
        model = mobile2_1d(pretrain)
    elif model_type == 'resnet152_1d':
        model = resnet152_1d()
    elif model_type == 'densenet201_1d':
        model = densenet201_1d(output_n, image_size, dim)
    elif model_type == 'TA_2018_Classifier':
        model = TA_2018_Classifier( output_n, image_size )
    elif model_type == 'mini_AE':
        model = DL_VAE.mini_AE(dim)
    elif model_type == 'AE':
        model = DL_VAE.AE(dim, image_size)
    elif model_type == 'AE_vgg19':
        model = DL_VAE.AE_vgg19(dim, image_size, pretrain)
    elif model_type == 'VAE':
        model = DL_VAE.VAE(dim, image_size)
    return model

class model_build():

    def __init__(self, epoch, model, loss_function, optimizer, model_type):  # Run it once
        self.epoch = epoch
        self.model = model
        self.loss_function = loss_function
        self.optimizer = optimizer
        self.model_type = model_type
        self.normal_weight = opt.normal_weight
        self.anomaly_weight = opt.anomaly_weight
        self.anomaly_model_set = opt.anomaly_model_set

    def mini_pre_analysis(self, acc, pre, gt, data, mini_pre_data, mini_gt, mini_data):
        acc += np.sum(mini_gt.reshape(-1) == mini_pre_data.reshape(-1))
        # pre.extend(mini_pre_data.tolist())
        pre = mini_pre_data if pre is None else np.vstack((pre, mini_pre_data))
        gt.extend(mini_gt.tolist())
        mini_data = mini_data.reshape(-1, mini_data.shape[2], mini_data.shape[3])
        data = mini_data if data is None else np.vstack((data, mini_data))
        return acc, pre, gt, data

    def run(self, data_loader, type):
        gt = []
        acc, loss = 0.0, 0.0
        pre, total_data = None, None
        # AE
        loss_sum, recons = None, None
        epoch_start_time = time.time()
        if type == 'training':
            self.model.train()
        elif type == 'validation':
            self.model.eval()
        for i, data in enumerate(data_loader):
            if type == 'training':
                self.optimizer.zero_grad()
            ####start####
            data_cuda = data[0].cuda() if opt.gpu_model else data[0]
            #####VAE-start#######
            if self.model_type in self.anomaly_model_set:
                if t.sum(data[1]) == 0 and type == 'training':  # all are anomaly
                    continue
                _, pred = self.model(data_cuda)
                nor_index = t.where(data[1] == 1)[0]
                batch_loss = self.loss_function(pred[nor_index], data_cuda[nor_index])
                pred = pred.cpu().data.numpy()
            #####VAE-end#######
            else:
                pred = self.model(data_cuda)
                gt_cuda = data[1].cuda() if opt.gpu_model else data[1]
                batch_loss = self.loss_function(pred, gt_cuda)
                pred = np.argmax(pred.cpu().data.numpy(), axis=1).reshape(-1, 1)
            loss += batch_loss.item()
            ####end####
            if type == 'training':
                batch_loss.backward()
                self.optimizer.step()
            # analysis
            acc, pre, gt, total_data = self.mini_pre_analysis(acc=acc, pre=pre, data=total_data, gt=gt, mini_pre_data=pred, mini_gt=data[1].numpy(), mini_data=data[0].data.numpy())
            progress = ('#' * int(float(i) / len(data_loader) * 40)).ljust(40)
            print('[%03d] %2.2f sec(s) | %s |' % (self.epoch, (time.time() - epoch_start_time), progress), end='\r', flush=True)
            # plt_pause_time = time.time() - epoch_start_time
        gt = np.array(gt)
        #####VAE-start#######
        if self.model_type in self.anomaly_model_set:
            recons = pre[:, 0, :, :]
            if type == 'training':
                opt.loss_lambda, pre, loss_sum = DL_VAE.operation().determine_loss_lambda(recons_data=recons, data=total_data, gt=gt, normal_weight=self.normal_weight, anomaly_weight=self.anomaly_weight)
            elif type == 'validation':
                pre, loss_sum = DL_VAE.operation().classfiy_by_loss_lambda(loss_lambda=opt.loss_lambda, recons_data=recons, data=total_data)
            acc = np.sum(pre == gt)
        #####VAE-end####c###
        # the detail
        acc = acc / total_data.shape[0]
        loss = loss / total_data.shape[0] * 1000
        pre = pre.reshape(-1)
        class_acc = {0: 0, 1: 0}
        for class_name in class_acc:
            class_index = np.argwhere(gt == class_name).reshape(-1)
            class_acc[class_name] = np.sum(pre[class_index] == gt[class_index]) / (class_index.shape[0]+1e-10)
        kill_loss = self.anomaly_weight*(1 - class_acc[0]) + self.normal_weight*(1 - class_acc[1])
        return pre, [acc, loss, opt.loss_lambda, loss_sum, recons, class_acc, kill_loss, gt, total_data]

class alexnet_features(nn.Module):
    def __init__(self):
        super(alexnet_features, self).__init__()
        self.alexnet = torchvision.models.alexnet(pretrained=True).features  # 21.69/5.94

    def forward(self, x):
        x = self.alexnet(x)
        return x

class resnet152_1d(nn.Module):
    def __init__(self):
        super(resnet152_1d, self).__init__()
        self.conv = nn.Conv2d(1, 3, kernel_size=1)
        self.resnet = torchvision.models.resnet152(pretrained=True)  # 21.69/5.94

    def forward(self, x):
        x = self.conv(x)
        x = self.resnet(x)
        return x

class densenet161_1d(nn.Module):
    def __init__(self):
        super(densenet161_1d, self).__init__()
        self.conv = nn.Conv2d(1, 3, kernel_size=1)
        self.densenet = torchvision.models.densenet161(pretrained=True)  # 22.35/6.20

    def forward(self, x):
        x = self.conv(x)
        x = self.densenet(x)
        return x

class densenet201_1d(nn.Module):
    def __init__(self, output_n, image_size, dim):
        super(densenet201_1d, self).__init__()
        self.dim = dim
        if dim != 3:
            self.conv = nn.Conv2d(dim, 3, kernel_size=1)
        self.densenet = torchvision.models.densenet201(pretrained=True)
        # # del the last layer
        removed = list(self.densenet.classifier.children())[:-1]
        self.densenet.classifier = nn.Sequential(*removed)

        output_size = self.linear_input((3, image_size, image_size))

        self.fc = nn.Sequential(
            nn.Linear(output_size, 512),
            nn.ReLU(),
            nn.Dropout(p=0.5),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(p=0.5),
            nn.Linear(256, 125),
            nn.ReLU(),
            nn.Dropout(p=0.5),
            nn.Linear(125, output_n)
        )

    def forward(self, x):
        if self.dim != 3:
            x = self.conv(x)

        # # visualize---------------------
        # for name, midlayer in self.densenet._modules.items():
        #     test = x
        #     for i in range(len(midlayer)):
        #         test = midlayer[i](test)
        #         # if i == 4:
        #         #     break
        #         #     # print(i, test.shape)
        #     return test
        # -------------------------------------

        x = self.densenet(x)
        x = x.view(x.size()[0], -1)
        x = self.fc(x)

        return x

    def linear_input(self, shape):
        bs = 2
        input = Variable(t.rand(bs, *shape))
        output_feat = self._forward_features(input)
        n_size = output_feat.data.view(bs, -1).size(1)
        return n_size

    def _forward_features(self, x):
        out = self.densenet(x)
        return out

class vgg19_1d(nn.Module):
    def __init__(self, output_n, pretrain, features_layer=None):
        # sys.setrecursionlimit(int(2e4))
        super(vgg19_1d, self).__init__()

        self.input_layer = nn.Sequential(
            nn.Conv2d(1, 3, kernel_size=1),
        )

        if pretrain:
            self.model = torchvision.models.vgg19_bn(pretrained=False)  # 25.766/8.15
        else:
            self.model = torchvision.models.vgg19_bn(pretrained=True)  # 25.766/8.15

        self.output_layer = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.ReLU(inplace=True),
            nn.Linear(1000, 2),
        )

        # init
        self.input_layer.apply(model_tool.model_parameter_operation().gaussian_weights_init)
        self.output_layer.apply(model_tool.model_parameter_operation().gaussian_weights_init)

        # feature
        self.features_layer = features_layer

    def forward(self, x):
        x = self.input_layer(x)
        if self.features_layer:
            x = self.model.features[:self.features_layer-2](x)
        else:
            x = self.model(x)
            x = self.output_layer(x)
        return x


class mobile2_1d(nn.Module):
    def __init__(self, pretrain):
        # sys.setrecursionlimit(int(2e4))
        super(mobile2_1d, self).__init__()
        self.conv = nn.Conv2d(1, 3, kernel_size=1)
        if pretrain:
            self.mobile2 = torchvision.models.mobilenet_v2(pretrained=False)  # 25.766/8.15
        else:
            self.mobile2 = torchvision.models.mobilenet_v2(pretrained=True)  # 25.766/8.15

    def forward(self, x):
        x = self.conv(x)
        x = self.mobile2(x)
        return x

# LeNet-5
class ConvNet(nn.Module):
    def __init__(self, output_n, dim, imgae_size):
        super(ConvNet, self).__init__()
        self.dim = dim
        if dim != 3:
            self.conv = nn.Conv2d(dim, 3, kernel_size=1)

        self.cnn = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=6, kernel_size=5, stride=1),
            nn.BatchNorm2d(num_features=6),
            nn.RReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),

            nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5, stride=1),
            nn.BatchNorm2d(num_features=16),
            nn.RReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            )

        output_size = self.linear_input((3, imgae_size, imgae_size))

        self.fc = nn.Sequential(
            nn.Dropout(p=0.2),
            nn.Linear(in_features=output_size, out_features=120),
            nn.RReLU(inplace=True),

            nn.Dropout(p=0.5),
            nn.Linear(in_features=120, out_features=84),
            nn.RReLU(inplace=True),

            nn.Dropout(p=0.5),
            nn.Linear(in_features=84, out_features=output_n),
            )

        self.cnn.apply(model_parameter_operation().gaussian_weights_init)
        self.fc.apply(model_parameter_operation().gaussian_weights_init)

    def forward(self, x):
        if self.dim != 3:
            x = self.conv(x)
        out = self.cnn(x)
        out = out.view(out.size()[0], -1)
        out = self.fc(out)
        return out

    def linear_input(self, shape):
        bs = 1
        input = Variable(t.rand(bs, *shape))
        output_feat = self._forward_features(input)
        n_size = output_feat.data.view(bs, -1).size(1)
        return n_size

    def _forward_features(self, x):
        out = self.cnn(x)
        return out

    def name(self):
        return "ConvNet"

class Fully(nn.Module):
    def __init__(self, output_n, imgae_size):
        super(Fully, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(in_features=imgae_size*imgae_size*3, out_features=1024),
            nn.RReLU(inplace=True),

            nn.Dropout(p=0.5),
            nn.Linear(in_features=1024, out_features=512),
            nn.RReLU(inplace=True),

            nn.Dropout(p=0.5),
            nn.Linear(in_features=512, out_features=256),
            nn.RReLU(inplace=True),

            nn.Dropout(p=0.5),
            nn.Linear(in_features=256, out_features=128),
            nn.RReLU(inplace=True),

            nn.Dropout(p=0.5),
            nn.Linear(in_features=128, out_features=64),
            nn.RReLU(inplace=True),

            nn.Dropout(p=0.5),
            nn.Linear(in_features=16, out_features=output_n),
        )
        self.fc.apply(model_parameter_operation().gaussian_weights_init)

    def forward(self, x):
        out = x
        out = out.view(out.size()[0], -1)
        out = self.fc(out)
        return out

    def name(self):
        return "Fully"

class ResidualBlock( nn.Module ):
    def __init__(self, inchannel, outchannel, stride=1, shortcut=None):
        super( ResidualBlock, self ).__init__()
        # normal
        self.left = nn.Sequential(
            nn.Conv2d( inchannel, outchannel, 3, stride, 1, bias=False ),
            nn.BatchNorm2d( outchannel ),
            nn.ReLU( inplace=True ),
            nn.Conv2d( outchannel, outchannel, 3, 1, 1, bias=False ),
            nn.BatchNorm2d( outchannel ) )
        # skip the layer
        self.right = shortcut

    def forward(self, x):
        out = self.left( x )
        residual = x if self.right is None else self.right( x )
        out += residual
        return F.relu( out )

class ResNet( nn.Module ):
    def __init__(self, num_classes=1000):
        super( ResNet, self ).__init__()
        # 前几层图像转换
        self.pre = nn.Sequential(
            nn.Conv2d( 3, 64, 7, 2, 3, bias=False ),
            nn.BatchNorm2d( 64 ),
            nn.ReLU( inplace=True ),
            nn.MaxPool2d( 3, 2, 1 ) )

        # 重复的layer，分别有3，4，6，3个residual block
        self.layer1 = self._make_layer( 64, 64, 3 )
        self.layer2 = self._make_layer( 64, 128, 4, stride=2 )
        self.layer3 = self._make_layer( 128, 256, 6, stride=2 )
        self.layer4 = self._make_layer( 256, 512, 3, stride=2 )

        # 分类用的全连接
        self.fc = nn.Linear( 512, num_classes )

    def _make_layer(self, inchannel, outchannel, block_num, stride=1):
        '''
        构建layer,包含多个residual block
        '''
        shortcut = nn.Sequential(
            nn.Conv2d( inchannel, outchannel, 1, stride, bias=False ),
            nn.BatchNorm2d( outchannel ) )

        layers = []
        layers.append( ResidualBlock( inchannel, outchannel, stride, shortcut ) )

        for i in range( 1, block_num ):
            layers.append( ResidualBlock( outchannel, outchannel ) )
        return nn.Sequential( *layers )

    def forward(self, x):
        x = self.pre( x )

        x = self.layer1( x )
        x = self.layer2( x )
        x = self.layer3( x )
        x = self.layer4( x )

        x = F.avg_pool2d( x, 7 )
        x = x.view( x.size( 0 ), -1 )
        return self.fc( x )

class TA_2018_Classifier(nn.Module):
    def __init__(self, output_n, imgae_size):
        super(TA_2018_Classifier, self).__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(1, 64, 4, 2, 1),  # [64, 24, 24]
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2),
            nn.Conv2d(64, 64, 3, 1, 1),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2),
            nn.MaxPool2d(2, 2, 0),      # [64, 12, 12]

            nn.Conv2d(64, 128, 3, 1, 1),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2),
            nn.Conv2d(128, 128, 3, 1, 1),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2),
            nn.MaxPool2d(2, 2, 0),      # [128, 6, 6]

            nn.Conv2d(128, 256, 3, 1, 1),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2),
            nn.Conv2d(256, 256, 3, 1, 1),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2),
            nn.MaxPool2d(2, 2, 0)       # [256, 3, 3]
        )

        self.fc = nn.Sequential(
            nn.Linear(256*3*3, 1024),
            nn.LeakyReLU(0.2),
            nn.Dropout(p=0.5),
            nn.Linear(1024, 512),
            nn.LeakyReLU(0.2),
            nn.Dropout(p=0.5),
            nn.Linear(512, output_n)
        )

        self.cnn.apply(model_parameter_operation().gaussian_weights_init)
        # self.fc.apply(model_parameter_operation().gaussian_weights_init)

    def forward(self, x):
        out = self.cnn(x)
        out = out.view(out.size()[0], -1)
        # out = self.fc(out)
        return out