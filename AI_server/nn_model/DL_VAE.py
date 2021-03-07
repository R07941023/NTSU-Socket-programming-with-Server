import torch as t
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torch.autograd import Variable
import sys
from nn_model import model_tool
import numpy as np
import matplotlib.pyplot as plt


class operation():

    def __init__(self):  # Run it once
        pass

    def determine_loss_lambda(self, recons_data, data, gt, normal_weight, anomaly_weight):
        pre_set,factory_loss  = [], []
        loss_sum = np.sum(np.sum(np.abs(recons_data - data), axis=-1), axis=-1)
        nor_index = np.argwhere(gt == 1).reshape(-1)
        anomal_index = np.argwhere(gt == 0).reshape(-1)
        # find the loss_lamda
        for i in loss_sum:
            pre = i - loss_sum
            pre[pre >= 0] = 1  # normal
            pre[pre < 0] = 0  # anomaly
            pre_set.append(pre)
            temp_loss = (nor_index.shape[0] - np.sum(pre[nor_index])) * normal_weight
            temp_loss += (np.sum(pre[anomal_index])) * anomaly_weight
            factory_loss.append(temp_loss)
        factory_loss = np.array(factory_loss)
        min_loss = np.argwhere(factory_loss == np.min(factory_loss)).reshape(-1)[0]
        loss_lambda = loss_sum[min_loss]
        pre = pre_set[min_loss]
        return loss_lambda, pre, loss_sum

    def classfiy_by_loss_lambda(self, loss_lambda, recons_data, data):
        loss_sum = np.sum(np.sum(np.abs(recons_data - data), axis=-1), axis=-1)
        pre = loss_lambda - loss_sum
        pre[pre >= 0] = 1  # normal
        pre[pre < 0] = 0  # anomaly
        return pre, loss_sum

    def visiualize_distribution(self, output_path, gt, loss_lambda, loss_sum, middle_name):
        plt.figure()
        nor_index = np.argwhere(gt == 1).reshape(-1)
        anom_index = np.argwhere(gt == 0).reshape(-1)
        plt.axvline(loss_lambda, c='b')
        if len(nor_index) > 0:
            plt.scatter(loss_sum[nor_index], nor_index, c='g')
        if len(anom_index) > 0:
            plt.scatter(loss_sum[anom_index], anom_index, c='r')
        plt.savefig(output_path + middle_name)

class mini_AE(nn.Module):
    def __init__(self, dim):
        super(mini_AE, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(dim, 128, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1)),
            nn.Conv2d(128, 64, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1)),
            nn.Conv2d(64, 64, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1)),
            nn.Conv2d(64, 64, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1)),
        )
        # define: decoder
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(64, 64, 2, 2),
            nn.ConvTranspose2d(64, 64, 2, 2),
            nn.ConvTranspose2d(64, 128, 2, 2),
            nn.ConvTranspose2d(128, dim, 2, 2),
            nn.Tanh(),
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return encoded, decoded

class AE(nn.Module):
    def __init__(self, dim, image_size):
        super(AE, self).__init__()
        self.cnn_encoder = nn.Sequential(
            nn.Conv2d(in_channels=dim, out_channels=16, kernel_size=3, stride=2,  padding=1),
            nn.BatchNorm2d(num_features=16),
            nn.RReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),

            nn.Conv2d(in_channels=16, out_channels=8, kernel_size=3, stride=2,  padding=1),
            nn.BatchNorm2d(num_features=8),
            nn.RReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            )

        output_size = model_tool.model_parameter_operation().linear_input((dim, image_size, image_size))

        self.dnn_encoder = nn.Sequential(
            nn.Linear(output_size, 1024),
            nn.ReLU(),
            nn.Dropout(p=0.5),
        )

        self.dnn_decoder = nn.Sequential(
            nn.Linear(1024, output_size),
            nn.ReLU(),
            nn.Dropout(p=0.5),
        )


        self.cnn_decoder = nn.Sequential(
            nn.ConvTranspose2d(in_channels=8, out_channels=16, kernel_size=2, stride=2, padding=0),
            nn.BatchNorm2d(num_features=16),
            nn.RReLU(inplace=True),

            nn.ConvTranspose2d(in_channels=16, out_channels=8, kernel_size=2, stride=2, padding=0),
            nn.BatchNorm2d(num_features=8),
            nn.RReLU(inplace=True),

            nn.ConvTranspose2d(in_channels=8, out_channels=16, kernel_size=2, stride=2, padding=0),
            nn.BatchNorm2d(num_features=16),
            nn.RReLU(inplace=True),

            nn.ConvTranspose2d(in_channels=16, out_channels=dim, kernel_size=2, stride=2, padding=0),
            nn.Tanh()
        )

        self.cnn_encoder.apply(model_tool.model_parameter_operation().gaussian_weights_init)
        self.dnn_encoder.apply(model_tool.model_parameter_operation().gaussian_weights_init)
        self.dnn_decoder.apply(model_tool.model_parameter_operation().gaussian_weights_init)
        self.cnn_decoder.apply(model_tool.model_parameter_operation().gaussian_weights_init)

    def forward(self, out):
        cnn_encoder = self.cnn_encoder(out)
        cnn_shape = cnn_encoder.shape
        out = cnn_encoder.view(cnn_encoder.size()[0], -1)
        dnn_encoder = self.dnn_encoder(out)
        dnn_decoder = self.dnn_decoder(dnn_encoder)
        out = dnn_decoder.view([-1, cnn_shape[1], cnn_shape[2], cnn_shape[3]])
        cnn_decoder = self.cnn_decoder(out)
        return dnn_encoder, cnn_decoder

class AE_vgg19(nn.Module):
    def __init__(self, dim, image_size, pretrain):
        super(AE_vgg19, self).__init__()
        if pretrain:
            self.vgg19_model = torchvision.models.vgg19_bn(pretrained=False)
        else:
            self.vgg19_model = torchvision.models.vgg19_bn(pretrained=True)

        # 1D vgg19
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 3, kernel_size=1),
            torchvision.models.vgg19_bn(pretrained=True)
        )

        self.dnn_decoder = nn.Sequential(
            nn.Linear(1000, 4096),
            nn.Dropout(p=0.5),
            nn.ReLU(inplace=True),
            nn.Linear(4096, 4096),
            nn.Dropout(p=0.5),
            nn.ReLU(inplace=True),
            nn.Linear(4096, 25088),
        )

        self.cnn_decoder = nn.Sequential(
            # 55
            nn.AdaptiveAvgPool2d(output_size=(7, 7)),
            # 54
            nn.ConvTranspose2d(in_channels=512, out_channels=512, kernel_size=2, stride=2, padding=0),
            nn.BatchNorm2d(num_features=512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            # 51-48-45-42
            nn.ConvTranspose2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            # 41
            nn.ConvTranspose2d(in_channels=512, out_channels=512, kernel_size=2, stride=2, padding=0),
            nn.BatchNorm2d(num_features=512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            # 38-35-32-29
            nn.ConvTranspose2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            # 28
            nn.ConvTranspose2d(in_channels=512, out_channels=256, kernel_size=2, stride=2, padding=0),
            nn.BatchNorm2d(num_features=256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            # 25-22-19-16
            nn.ConvTranspose2d(in_channels=256, out_channels=256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(in_channels=256, out_channels=256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(in_channels=256, out_channels=256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(in_channels=256, out_channels=256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            # 15
            nn.ConvTranspose2d(in_channels=256, out_channels=128, kernel_size=2, stride=2, padding=0),
            nn.BatchNorm2d(num_features=128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            # 12-9
            nn.ConvTranspose2d(in_channels=128, out_channels=128, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(in_channels=128, out_channels=128, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            # 8
            nn.ConvTranspose2d(in_channels=128, out_channels=64, kernel_size=2, stride=2, padding=0),
            nn.BatchNorm2d(num_features=64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            # 5-2
            nn.ConvTranspose2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(in_channels=64, out_channels=3, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=3, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            # 1
            nn.ConvTranspose2d(in_channels=3, out_channels=1, kernel_size=1),
        )

        self.dnn_decoder.apply(model_tool.model_parameter_operation().gaussian_weights_init)
        self.cnn_decoder.apply(model_tool.model_parameter_operation().gaussian_weights_init)

    def forward(self, out):
        encoder = self.encoder(out)
        dnn_decoder = self.dnn_decoder(encoder)
        out = dnn_decoder.view([-1, 512, 7, 7])
        cnn_decoder = self.cnn_decoder(out)
        return encoder, cnn_decoder

class VAE(nn.Module):
    def __init__(self, dim, image_size):
        super(VAE, self).__init__()
        self.cnn_encoder = nn.Sequential(
            nn.Conv2d(in_channels=dim, out_channels=16, kernel_size=3, stride=1),
            nn.BatchNorm2d(num_features=16),
            nn.RReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),

            nn.Conv2d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(num_features=8),
            nn.RReLU(inplace=True),
            nn.MaxPool2d(kernel_size=1, stride=2),
            )
        output_size = model_tool.model_parameter_operation().linear_input((dim, image_size, image_size))
        self.dnn_encoder = nn.Sequential(nn.Linear(output_size, 100),)

        # VAE: These two layers are for getting logvar and mean
        self.mean = nn.Linear(100, 64)
        self.var = nn.Linear(100, 64)

        self.dnn_decoder = nn.Sequential(
            nn.Linear(64, output_size),
            nn.ReLU(),
            nn.Dropout(p=0.5),
            )
        self.cnn_decoder = nn.Sequential(
            nn.ConvTranspose2d(in_channels=8, out_channels=16, kernel_size=3, stride=2),
            nn.BatchNorm2d(num_features=16),
            nn.RReLU(inplace=True),
            nn.ConvTranspose2d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(num_features=8),
            nn.RReLU(inplace=True),
            nn.ConvTranspose2d(in_channels=8, out_channels=dim, kernel_size=2, stride=2, padding=1),
            nn.Tanh()
        )
        self.cnn_encoder.apply(model_tool.model_parameter_operation().gaussian_weights_init)
        self.dnn_encoder.apply(model_tool.model_parameter_operation().gaussian_weights_init)
        self.dnn_decoder.apply(model_tool.model_parameter_operation().gaussian_weights_init)
        self.cnn_decoder.apply(model_tool.model_parameter_operation().gaussian_weights_init)


    def forward(self, out):
        # encoder
        out = self.cnn_encoder(out)
        cnn_shape = out.shape
        out = out.view(out.size()[0], -1)
        out= self.dnn_encoder(out)
        encoder, var = self.de_noise(out)
        # decoder
        out = self.dnn_decoder(encoder)
        out = out.view([-1, cnn_shape[1], cnn_shape[2], cnn_shape[3]])
        decoder = self.cnn_decoder(out)
        return encoder, var, decoder

    def de_noise(self, out):
        mean = self.mean(out)
        var = self.var(out)
        if self.pretrain:
            return mean, var
        noise = t.randn_like(mean)
        std = t.exp(0.5 * var)
        return noise.mul(std).add_(mean), var
