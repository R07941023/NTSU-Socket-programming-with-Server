import torch
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import TensorDataset
# from sklearn.model_selection import StratifiedKFold
import sys
import glob, os
from os import listdir
import cv2
import numpy as np
import pandas as pd
# sript
from data_tool import fn_data
from data_tool import img2np
# from keras.preprocessing.image import ImageDataGenerator

def image_generation_colormap(feature, label):
    new_feature = []
    new_label = []
    for img in range(len(feature)):
        new_feature.append(feature[img])
        new_label.append(label[img])

        gan = cv2.applyColorMap(feature[img].copy(), cv2.COLORMAP_JET)

        new_feature.append(gan)
        new_label.append(label[img])

        # cv2.imshow('img', gan)
        # cv2.waitKey(0)
    return new_feature, new_label

def image_generation_historgram(feature, label):
    new_feature = []
    new_label = []
    for img in range(len(feature)):
        new_feature.append(feature[img])
        new_label.append(label[img])

        ycrcb = cv2.cvtColor(feature[img], cv2.COLOR_BGR2YCR_CB)
        channels = cv2.split(ycrcb)
        cv2.equalizeHist(channels[0], channels[0])
        cv2.merge(channels, ycrcb)
        gan = cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, feature[img])
        # cv2.imshow('img', gan)
        # cv2.waitKey(0)

        new_feature.append(gan)
        new_label.append(label[img])

    return new_feature, new_label

def image_generation_threshold(feature, label):
    new_feature = []
    new_label = []
    for img in range(len(feature)):
        new_feature.append(feature[img])
        new_label.append(label[img])

        gray = cv2.cvtColor(feature[img], cv2.COLOR_BGR2GRAY)
        gan = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        gan = cv2.cvtColor(gan, cv2.COLOR_GRAY2BGR)

        new_feature.append(gan)
        new_label.append(label[img])

        # cv2.imshow('img', gan)
        # cv2.waitKey(0)
    return new_feature, new_label

def image_generation_GaussianBlur(feature, label, kernel):
    new_feature = []
    new_label = []
    for img in range(len(feature)):
        new_feature.append(feature[img])
        new_label.append(label[img])

        gan = cv2.GaussianBlur(feature[img].copy(), kernael, 0)

        new_feature.append(gan)
        new_label.append(label[img])

        # cv2.imshow('img', gan)
        # cv2.waitKey(0)
    return new_feature, new_label

def image_generation_keypoint(feature, label):
    new_feature = []
    new_label = []
    for img in range(len(feature)):
        new_feature.append(feature[img])
        new_label.append(label[img])

        gan = feature[img].copy()
        gray = cv2.cvtColor(feature[img], cv2.COLOR_BGR2GRAY)
        keypoint = cv2.goodFeaturesToTrack(gray, 40, 0.06, 10)
        if not keypoint is None:
            for i in keypoint:
                cv2.circle(gan, tuple(i[0]), 3, (0, 0, 255), 0)
        new_feature.append(gan)
        new_label.append(label[img])

        # cv2.imshow('img', gan)
        # cv2.waitKey(0)
    return new_feature, new_label

def image_generation_noise(feature, label):
    new_feature = []
    new_label = []
    for img in range(len(feature)):
        new_feature.append(feature[img])
        new_label.append(label[img])

        gan = cv2.randn(feature[img].copy(), (0,0,0), (255,255,255))
        gan = feature[img]+gan

        new_feature.append(gan)
        new_label.append(label[img])

        # cv2.imshow('img', gan)
        # cv2.waitKey(0)
    return new_feature, new_label

def image_generation_Contrast(feature, label):
    new_feature = []
    new_label = []
    for img in range(len(feature)):
        new_feature.append(feature[img])
        new_label.append(label[img])

        gan = cv2.randn(feature[img].copy(), (0,0,0), (255,255,255))
        gan = feature[img]+gan

        new_feature.append(gan)
        new_label.append(label[img])

        # cv2.imshow('img', gan)
        # cv2.waitKey(0)
    return new_feature, new_label

def image_generation_Affine(feature, label):
    new_feature = []
    new_label = []
    for img in range(len(feature)):
        new_feature.append(feature[img])
        new_label.append(label[img])
        pts1 = np.float32([[5, 5], [40, 5], [5, 40]])
        pts2 = np.float32([[0,0], [48, 0], [10, 40]])
        rows, cols = feature[img].shape[:2]
        M = cv2.getAffineTransform(pts1, pts2)
        gan = cv2.warpAffine(feature[img].copy(), M, (rows, cols))
        # gan = feature[img]+gan

        new_feature.append(gan)
        new_label.append(label[img])

        # cv2.imshow('img', gan)
        # cv2.waitKey(0)
    return new_feature, new_label

def image_generation_rotate(feature, label, rotate):
    new_feature = []
    new_label = []
    for img in range(len(feature)):
        new_feature.append(feature[img])
        new_label.append(label[img])

        (h, w) = feature[img].shape[:2]
        center = (w / 2, h / 2)
        for i in rotate:
            M = cv2.getRotationMatrix2D(center, i, 1.0)
            gan = cv2.warpAffine(feature[img].copy(), M, (h, w))
            new_feature.append(gan)
            new_label.append(label[img])

        # cv2.imshow('img', gan)
        # cv2.waitKey(0)
    return new_feature, new_label

def image_generation_Flip(feature, label, type):
    new_feature = []
    new_label = []
    for img in range(len(feature)):
        new_feature.append(feature[img])
        new_label.append(label[img])

        for i in type:
            gan = cv2.flip(feature[img], i)
            new_feature.append(gan)
            new_label.append(label[img])

            # cv2.imshow('img', gan)
            # cv2.waitKey(1000)
    return new_feature, new_label

def image_generation_canny(feature, label):
    new_feature = []
    new_label = []
    for img in range(len(feature)):
        new_feature.append(feature[img])
        new_label.append(label[img])

        gan = cv2.Canny(feature[img].copy(), 100, 200)
        gan = cv2.cvtColor(gan, cv2.COLOR_GRAY2BGR)

        new_feature.append(gan)
        new_label.append(label[img])

        # cv2.imshow('img', gan)
        # cv2.waitKey(200)
    return new_feature, new_label

def image_gray(feature, label):
    new_feature = []
    new_label = []
    for img in range(len(feature)):

        gray = cv2.cvtColor(feature[img], cv2.COLOR_BGR2GRAY)

        new_feature.append(gray)
        new_label.append(label[img])

    return new_feature, new_label

def self_define_data_number(X, Y, class_pass=1, class_fault=0, pass_n=1e10, fault_n=1e10):
    total_pass_index = np.argwhere(Y == class_pass)
    total_fault_index = np.argwhere(Y == class_fault)
    # check the number is enough
    pass_n = total_pass_index.shape[0] if pass_n > total_pass_index.shape[0] else pass_n
    fault_n = total_fault_index.shape[0] if fault_n > total_fault_index.shape[0] else fault_n
    training_index = np.vstack((total_pass_index[:pass_n], total_fault_index[:fault_n])).reshape(-1).tolist()
    validation_index = np.vstack((total_pass_index[pass_n:], total_fault_index[fault_n:])).reshape(-1).tolist()
    x_train, x_label = X[training_index], Y[training_index]
    val_data, val_label = X[validation_index], Y[validation_index]
    return x_train, x_label, val_data, val_label

def val_define_data_number(X, Y, val_rate=0.2):
    val_n = int(val_rate*X.shape[0])
    x_train, x_label = X[val_n:], Y[val_n:]
    val_data, val_label = X[:val_n], Y[:val_n]
    return x_train, x_label, val_data, val_label

def errer_img(output_path, pre, gt, data, type, class_name=['Fault', 'Pass']):
    model_path = output_path + type + '/'
    try:
        shutil.rmtree(model_path)
    except:
        pass
    os.mkdir(model_path)
    class_error_index = dict.fromkeys(set(gt), [])
    for mini_name in class_error_index:
        # make the error folder
        if class_name:
            error_path = model_path + 'Error_' + class_name[mini_name] + '/'
        else:
            error_path = model_path + 'Error_' + str(mini_name) + '/'
        try:
            shutil.rmtree(error_path)
        except:
            pass
        os.mkdir(error_path)
        # get the error image index
        candidate_index = []
        gt_index = np.argwhere(gt == mini_name).reshape(-1)
        pre_index = np.argwhere(pre == mini_name).reshape(-1)
        for mini_index in pre_index:
            if not mini_index in gt_index:
                candidate_index.append(mini_index)
                img = data[mini_index]
                # cv2.imshow('123', img)
                # cv2.waitKey(1)
                cv2.imwrite(error_path+str(mini_index)+'.jpg', img*255.)
        class_error_index[mini_name] = candidate_index

def list2csv(output_path, data, type=None):
    if os.path.isfile(output_path) and type == 'record':
        old_data = pd.read_csv(output_path, header=None).values
        new_data = []
        for mini_data in old_data:
            new_data.append(list(mini_data))
        new_data.append(data[1])
        data = new_data
    dataframe = np.array(data).astype( np.str )
    df = pd.DataFrame( dataframe )
    df.to_csv( output_path, encoding="gbk", index=False, header=False )

def padding_old_data(X, Y):
    max_n = 0
    padding_index = None
    class_set = {}
    index_set = list(set(Y))
    # extraction the class info
    for i in index_set:
        class_set[i] = np.argwhere(Y == i).reshape(-1)
        if class_set[i].shape[0] > max_n:
            max_n = class_set[i].shape[0]
    # determine the padding index
    for i in class_set:
        if class_set[i].shape[0] < max_n:
            padding_n = max_n - class_set[i].shape[0]
            if padding_index is None:
                padding_index = class_set[i][(np.random.rand(padding_n) * class_set[i].shape[0]).astype(np.int)]
            else:
                padding_index = np.hstack((padding_index, class_set[i][(np.random.rand(padding_n)*class_set[i].shape[0]).astype(np.int)]))
    # padding
    X = np.concatenate((X, X[padding_index]), axis=0)
    Y = np.concatenate((Y, Y[padding_index]), axis=0)
    return X, Y

def imgage_rotate_filp(feature, label, class_index=[0, 1]):
    new_feature = []
    new_label = []
    for i in range(len(feature)):
        img = feature[i][0].copy()
        new_feature.append(img)
        new_label.append(label[i])
        if label[i] in class_index:
            (h, w) = img.shape[:2]
            center = (w / 2, h / 2)
            img_filp1 = cv2.flip(img, 1)
            img_filp2 = cv2.flip(img, 0)
            img_filp3 = cv2.flip(img, -1)
            img_rotate1 = cv2.warpAffine(img, cv2.getRotationMatrix2D(center, 90, 1.0), (h, w))
            img_rotate2 = cv2.warpAffine(img, cv2.getRotationMatrix2D(center, 270, 1.0), (h, w))
            img_rotate_filp1 = cv2.flip(img_rotate1, 1)
            img_rotate_filp2 = cv2.flip(img_rotate1, 0)
            # save to dataset
            new_feature.append(img_filp1)  # origin/padding 32/10
            new_label.append(label[i])
            # new_feature.append(img_filp2)  # N/12
            # new_label.append(label[i])
            # new_feature.append(img_filp3)
            # new_label.append(label[i])

            # new_feature.append(img_rotate1)
            # new_label.append(label[i])
            # new_feature.append(img_rotate2)
            # new_label.append(label[i])
            # new_feature.append(img_rotate_filp1)
            # new_label.append(label[i])
            # new_feature.append(img_rotate_filp2)
            # new_label.append(label[i])
    new_feature, new_label = np.array(new_feature), np.array(new_label)
    new_feature = new_feature.reshape(-1, 1, new_feature.shape[1], new_feature.shape[2])
    return new_feature, new_label

def get_dataloader(folder, dataset, image_scale, batch_size, val_proportion, random_seed=100):

    if image_scale:
        trans = transforms.Compose([transforms.Grayscale(), transforms.Resize(image_scale), transforms.Pad(4), transforms.RandomHorizontalFlip(), transforms.RandomCrop(image_scale-4), transforms.ToTensor(), transforms.Normalize((0.5,), (1.0,))])
    else:
        trans = transforms.Compose( [transforms.Grayscale(), transforms.Pad(4), transforms.RandomHorizontalFlip(), transforms.RandomCrop(image_scale-4), transforms.ToTensor(), transforms.Normalize( (0.5,), (1.0,) )] )

    if dataset == 'liteon_near_field_01_training':
        training_pass_n, training_fault_n, self_define = 30, 10, False
        X = np.load(folder+'X.npy').astype(np.float)/255.
        X = (X.reshape(X.shape[0], 1, X.shape[1], X.shape[2]))
        label = np.load(folder+'Y.npy')  # 0:fault, 1:pass
        label = label.astype(np.int).reshape(-1)
        # random order setting
        if random_seed != -1:
            np.random.seed(random_seed)
            random_map = np.random.choice(X.shape[0], X.shape[0], replace=False)
        else:
            random_map = np.arange(X.shape[0])
        X, label = X[random_map], label[random_map]
        if self_define:
            x_train, x_label, val_data, val_label = self_define_data_number(X=X, Y=label, class_pass=1, class_fault=0, pass_n=training_pass_n, fault_n=training_fault_n)
        else:
            x_train, x_label, val_data, val_label = val_define_data_number(X=X, Y=label, val_rate=val_proportion)
        print('Gan the data for filing and rotation...')
        x_train, x_label = imgage_rotate_filp(x_train, x_label, class_index=[0])  # 1, 0, -1
        print('Gan the data for padding old data...')
        x_train, x_label = padding_old_data(x_train, x_label)
        print('data number = ', len(x_train))
        print(' Total Pass / Fault number = ', np.sum(label), '/', label.shape[0] - np.sum(label))
        print(' Training Pass / Fault number = ', np.sum(x_label), '/', x_label.shape[0]-np.sum(x_label))
        print(' Validation Pass / Fault number = ', np.sum(val_label), '/', val_label.shape[0] - np.sum(val_label))
        print('training / validation number = %d/%d' %(x_train.shape[0], val_data.shape[0]))
        x_train = torch.FloatTensor(x_train)
        val_data = torch.FloatTensor(val_data)
        x_label = torch.LongTensor(x_label)
        val_label = torch.LongTensor(val_label)
        # dataset
        train_set = TensorDataset(x_train, x_label)
        # val_set = TensorDataset(x_train, x_label)
        val_set = TensorDataset(val_data, val_label)

    elif dataset == 'liteon_near_field_01_validation':
        X = np.load(folder+'X.npy').astype(np.float)/255.
        X = (X.reshape(X.shape[0], 1, X.shape[1], X.shape[2]))
        Y = np.load(folder+'Y.npy')  # 0:fault, 1:pass
        Y = Y.astype(np.int).reshape(-1)
        X = torch.FloatTensor(X)
        Y = torch.LongTensor(Y)
        val_set = TensorDataset(X, Y)
        val_loader = torch.utils.data.DataLoader(dataset=val_set, batch_size=batch_size, shuffle=False)
        # data normalization
        print('total data is {}'.format(len(Y)))
        print('==>>> total testing batch number: {}'.format(len(val_loader)))
        return val_set, val_loader

    elif dataset == 'liteon_near_field_01_testing':
        # load data
        X, N = [], []

        # preprocessing
        pre_para_path = './preprocess/parameter.csv'
        pre_para = img2np.fn_tool().csv2dict(pre_para_path)
        pre_para['his'] = bool(pre_para['his'] == 'True')
        pre_para['gauss_blur'] = bool(pre_para['gauss_blur'] == 'True')
        pre_para['winsize'] = img2np.fn_tool().str2tuple(pre_para['winsize'], int_type=True)
        pre_para['sigma'] = int(pre_para['sigma'])

        for aim_folder in folder:
            print( 'loading=', aim_folder, '.....' )
            X, N = img2np.fn_tool().get_all_img(X, N, aim_folder, image_scale, pre_his=pre_para['his'], pre_gauss_blur=pre_para['gauss_blur'], blur_winsize=pre_para['winsize'], blur_sigma=pre_para['sigma'], multi=False)

        # data normalization
        if len(X) == 0:
            print('==>>> total testing batch number: {}'.format(0))
            return None, None, None, False
        else:
            X = np.array(X).astype(np.float) / 255.
            N = np.array(N)
            X = X.reshape(X.shape[0], -1, X.shape[1], X.shape[2])
            Y = np.zeros((X.shape[0],))
            # np to torch
            test_set = TensorDataset( torch.FloatTensor( X ), torch.LongTensor( Y ) )
            test_loader = torch.utils.data.DataLoader( dataset=test_set, batch_size=batch_size, shuffle=False )
            print( '==>>> total testing batch number: {}'.format( len( test_loader ) ) )
            return X, Y, test_loader, N, True

    elif dataset == 'MNIST':  # download data
        train_set = MNIST( root=folder, train=True, download=True, transform=trans )
        val_set = MNIST( root=folder, train=False, download=True, transform=trans )

    elif dataset == 'cv_hw2_p1':
        def hw_rule(x):
            data = []
            normailize = transforms.Compose(
                [transforms.ToTensor(), transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
            x = np.array(x)
            for i in range(x.shape[0]):
                data.append(normailize(x[i]).numpy())
            data = np.array(data)
            data = torch.tensor(data)
            return data
        # hw rule
        kind = 10
        x_train = []
        x_label = []
        val_data = []
        val_label = []
        # training date
        for i in range(kind):
            print('class', str(i), '...')
            x_data = '../../CV/hw2/hw2-4_data/problem1/train/class_' + str(i) + '/'
            imgs = listdir(x_data)
            imgs = sorted(imgs)
            label = i
            drop_label = []
            for img in range(len(imgs)):  # len(imgs)
                if not img in drop_label:
                    tmp = cv2.imread(x_data + imgs[img])
                    tmp = cv2.resize(tmp, (image_scale, image_scale), interpolation=cv2.INTER_CUBIC)
                    # preprocessing
                    ycrcb = cv2.cvtColor(tmp, cv2.COLOR_BGR2YCR_CB)
                    channels = cv2.split(ycrcb)
                    cv2.equalizeHist(channels[0], channels[0])
                    cv2.merge(channels, ycrcb)
                    tmp = cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, tmp)
                    tmp = cv2.GaussianBlur(tmp, (3, 3), 0)
                    # load the data
                    x_train.append(tmp)
                    x_label.append(label)

            print('training data number = ', len(x_train))
        # validation date
        for i in range(kind):
            print('class', str(i), '...')
            x_data = '../../CV/hw2/hw2-4_data/problem1/valid/class_' + str(i) + '/'
            imgs = listdir(x_data)
            imgs = sorted(imgs)
            label = i
            drop_label = []
            for img in range(len(imgs)):  # len(imgs)
                if not img in drop_label:
                    tmp = cv2.imread(x_data + imgs[img])
                    tmp = cv2.resize(tmp, (image_scale, image_scale), interpolation=cv2.INTER_CUBIC)
                    # preprocessing
                    ycrcb = cv2.cvtColor(tmp, cv2.COLOR_BGR2YCR_CB)
                    channels = cv2.split(ycrcb)
                    cv2.equalizeHist(channels[0], channels[0])
                    cv2.merge(channels, ycrcb)
                    tmp = cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, tmp)
                    tmp = cv2.GaussianBlur(tmp, (3, 3), 0)
                    # load the data
                    val_data.append(tmp)
                    val_label.append(label)
            print('validation data number = ', len(val_data))

        # hw rule
        x_train = hw_rule(x_train)
        val_data = hw_rule(val_data)

        # list to np
        val_label = np.array(val_label, dtype=float)
        val_label = np.array(val_label, dtype=float)

        # np to tensor
        x_label = torch.LongTensor(x_label)
        val_label = torch.LongTensor(val_label)

        # dataset
        train_set = TensorDataset(x_train, x_label)
        val_set = TensorDataset(val_data, val_label)

    elif dataset == 'cv_hw2_p2':
        def hw_rule(x):
            data = []
            normailize = transforms.Compose(
                [transforms.ToTensor(), transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
            x = np.array(x)
            for i in range(x.shape[0]):
                data.append(normailize(x[i]).numpy())
            data = np.array(data)
            data = torch.tensor(data)
            return data
        kind = 100
        x_train = []
        x_label = []
        val_data = []
        val_label = []
        # training date
        for i in range(kind):
            print('class', str(i), '...')
            x_data = '../../CV/hw2/hw2-4_data/problem2/train/class_' + str(i) + '/'
            imgs = listdir(x_data)
            imgs = sorted(imgs)
            label = i
            drop_label = []
            for img in range(len(imgs)):  # len(imgs)
                if not img in drop_label:
                    tmp = cv2.imread(x_data + imgs[img])
                    tmp = cv2.resize(tmp, (image_scale, image_scale), interpolation=cv2.INTER_CUBIC)
                    # preprocessing
                    ycrcb = cv2.cvtColor(tmp, cv2.COLOR_BGR2YCR_CB)
                    channels = cv2.split(ycrcb)
                    cv2.equalizeHist(channels[0], channels[0])
                    cv2.merge(channels, ycrcb)
                    tmp = cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, tmp)
                    tmp = cv2.GaussianBlur(tmp, (3, 3), 0)
                    # load the data
                    x_train.append(tmp)
                    x_label.append(label)
            print('training data number = ', len(x_train))

        # validation date
        for i in range(kind):
            print('class', str(i), '...')
            x_data = '../../CV/hw2/hw2-4_data/problem2/valid/class_' + str(i) + '/'
            imgs = listdir(x_data)
            imgs = sorted(imgs)
            label = i
            drop_label = []
            for img in range(len(imgs)):  # len(imgs)
                if not img in drop_label:
                    tmp = cv2.imread(x_data + imgs[img])
                    tmp = cv2.resize(tmp, (image_scale, image_scale), interpolation=cv2.INTER_CUBIC)
                    # preprocessing
                    ycrcb = cv2.cvtColor(tmp, cv2.COLOR_BGR2YCR_CB)
                    channels = cv2.split(ycrcb)
                    cv2.equalizeHist(channels[0], channels[0])
                    cv2.merge(channels, ycrcb)
                    tmp = cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, tmp)
                    tmp = cv2.GaussianBlur(tmp, (3, 3), 0)
                    # load the data
                    val_data.append(tmp)
                    val_label.append(label)
            print('validation data number = ', len(val_data))

        # hw rule
        x_train = hw_rule(x_train)
        val_data = hw_rule(val_data)

        # list to np
        val_label = np.array(val_label, dtype=float)
        val_label = np.array(val_label, dtype=float)

        # np to tensor
        x_label = torch.LongTensor(x_label)
        val_label = torch.LongTensor(val_label)

        # dataset
        train_set = TensorDataset(x_train, x_label)
        val_set = TensorDataset(val_data, val_label)

    elif dataset == 'hw3':
        # face_file = 'face.xml'
        # face_web = 'https://raw.githubusercontent.com/a1996850622/FaceDetection/master/Source/haarcascade_frontalface_default.xml'
        # urlretrieve(face_web, face_file)
        # face_cascade = cv2.CascadeClassifier(face_file)
        label = pd.read_csv( folder_csv ).values[:, 1]
        x_data = folder+'/'
        imgs = listdir(x_data)
        # imgs = imgs.sort()
        imgs = sorted(imgs)
        x_train = []
        x_label = []
        val_data = []
        val_label = []
        # tmp = cv2.bilateralFilter(tmp, 9, 75, 75)
        print('original...')
        drop_label = [6, 177, 774, 1039, 2018, 3658, 3968, 3991, 4002, 5574, 5839, 5855, 6923, 6940, 7070, 7134, 7415, 7497, 7902, 8601, 8923, 10762, 10807, 11143, 11468, 12230, 12353, 12874, 13593, 14769, 16101, 16800, 17043, 17389, 17875, 18065, 18087, 18221, 18584, 18991, 19582, 20568, 23043, 24111, 24938, 24978, 25340, 25457, 25797, 26054, 26466, 26542, 26546, 27100, 27424, 27586, 28585, 28601]  # ~20000
        for img in range(len(imgs)):  # len(imgs)
            if not img in drop_label:
                tmp = cv2.imread(x_data + imgs[img])
                # preprocessing
                ycrcb = cv2.cvtColor(tmp, cv2.COLOR_BGR2YCR_CB)
                channels = cv2.split(ycrcb)
                cv2.equalizeHist(channels[0], channels[0])
                cv2.merge(channels, ycrcb)
                tmp = cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, tmp)
                tmp = cv2.GaussianBlur(tmp, (3, 3), 0)


                if (img % (1 / val_proportion) == 0):
                    tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
                    val_label.append(label[img])
                    val_data.append(tmp)
                else:
                    # origin
                    x_train.append(tmp)
                    x_label.append(label[img])

                ###
                if len(x_train) > 100:
                    break
                ###
        print('data number = ', len(x_train))

        # print('canny...')
        # x_train, x_label = image_generation_canny(x_train, x_label)  # 1, 0, -1
        # print('data number = ', len(x_train))

        # print('keypoint...')
        # x_train, x_label = image_generation_keypoint(x_train, x_label)  # for keypoint
        # print('data number = ', len(x_train))

        # print('Affine...')
        # x_train, x_label = image_generation_Affine(x_train, x_label)
        # print('data number = ', len(x_train))

        # print('Flip...')
        # x_train, x_label = image_generation_Flip(x_train, x_label, [1])  # 1, 0, -1
        # print('data number = ', len(x_train))
        #
        # print('rotate...')
        # x_train, x_label = image_generation_rotate(x_train, x_label, [45, -45, 90, -90])  # 0/45/-45/90/-90/180
        # print('data number = ', len(x_train))

        # print('noise...')
        # x_train, x_label = image_generation_noise(x_train, x_label)
        # print('data number = ', len(x_train))

        # print('GaussianBlur...')
        # x_train, x_label = image_generation_GaussianBlur(x_train, x_label, (3, 3))
        # print('data number = ', len(x_train))

        # print('colormap...')
        # x_train, x_label = image_generation_colormap(x_train, x_label)
        # print('data number = ', len(x_train))

        # print('threshold...')
        # x_train, x_label = image_generation_threshold(x_train, x_label)
        # print('data number = ', len(x_train))

        print('gray...')
        x_train, x_label = image_gray(x_train, x_label)
        print('data number = ', len(x_train))

        # list to np
        x_train = np.array(x_train, dtype=float) / 255.0
        x_train = x_train.reshape(x_train.shape[0], 1, x_train.shape[1], x_train.shape[2])
        x_label = np.array( x_label, dtype=float )
        # datagen.fit(x_train)
        # generator = datagen.flow(x_train, x_label)
        # print(x_train.shape)
        # print('generator...')
        # x_train = np.concatenate((x_train, generator[0][0], generator[1][0]))
        # print('data number = ', x_train.shape[0])
        # x_label = np.concatenate((x_label, generator[0][1], generator[1][1]))
        # splits = list(StratifiedKFold(n_splits=5, shuffle=True).split(x_train, x_label))
        # print(splits[:3])
        # exit()

        val_data = np.array( val_data, dtype=float ) / 255.0
        val_data = val_data.reshape(val_data.shape[0], 1, val_data.shape[1], val_data.shape[2])
        val_label = np.array( val_label, dtype=float )
        # np to tensor
        x_train = torch.FloatTensor( x_train )
        val_data = torch.FloatTensor( val_data )
        x_label = torch.LongTensor( x_label )
        val_label = torch.LongTensor( val_label )
        # dataset
        train_set = TensorDataset( x_train, x_label )
        val_set = TensorDataset( val_data, val_label )

    elif dataset == 'hw3_testing':
        x_data = folder + '/'
        imgs = listdir(x_data)
        imgs = sorted(imgs)
        x_train = []
        x_zero = []
        for img in range(len(imgs)):  # len(imgs)
            tmp = cv2.imread(x_data + imgs[img])

            # preprocessing
            ycrcb = cv2.cvtColor(tmp, cv2.COLOR_BGR2YCR_CB)
            channels = cv2.split(ycrcb)
            cv2.equalizeHist(channels[0], channels[0])
            cv2.merge(channels, ycrcb)
            tmp = cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, tmp)
            tmp = cv2.GaussianBlur(tmp, (3, 3), 0)

            tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
            tmp = tmp.reshape(1, tmp.shape[0], tmp.shape[1])

            x_train.append(tmp)
            x_zero.append(img)
        # list to np
        x_train = np.array(x_train, dtype=float) / 255.0
        x_zero = np.array(x_zero)
        # np to tensor
        x_train = torch.FloatTensor(x_train)
        x_zero = torch.FloatTensor(x_zero)
        # dataset
        train_set = TensorDataset(x_train, x_zero)
        train_loader = torch.utils.data.DataLoader(dataset=train_set, batch_size=batch_size, shuffle=False)
        print('==>>> total trainning batch number: {}'.format(len(train_loader)))
        return train_set, train_loader

    elif dataset == 'hw3_plt_inf':
        x_data = folder + 'train/'
        label = pd.read_csv(folder + 'train.csv').values[:, 1][:15]  # !!!!!!!!!
        imgs = listdir(x_data)
        imgs = sorted(imgs)
        x_train = []
        x_zero = []
        for img in range(len(imgs)):  # len(imgs)
            tmp = cv2.imread(x_data + imgs[img])
            # preprocessing
            ycrcb = cv2.cvtColor(tmp, cv2.COLOR_BGR2YCR_CB)
            channels = cv2.split(ycrcb)
            cv2.equalizeHist(channels[0], channels[0])
            cv2.merge(channels, ycrcb)
            tmp = cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, tmp)
            tmp = cv2.GaussianBlur(tmp, (3, 3), 0)

            tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
            tmp = tmp.reshape(1, tmp.shape[0], tmp.shape[1])

            x_train.append(tmp)
            x_zero.append(img)
        # list to np
        x_train = np.array(x_train, dtype=float) / 255.0
        x_zero = np.array(x_zero)
        # np to tensor
        x_train = torch.FloatTensor(x_train)
        x_zero = torch.FloatTensor(x_zero)
        # dataset
        train_set = TensorDataset(x_train, x_zero)
        train_loader = torch.utils.data.DataLoader(dataset=train_set, batch_size=batch_size, shuffle=False)
        print('==>>> total trainning batch number: {}'.format(len(train_loader)))
        return train_set, train_loader, label

    else:
        print('Custom data...')
        train_path, test_path = os.path.join(folder,'train'), os.path.join(folder,'valid')
        # print(train_path)
        #

        # Get dataset using pytorch functions
        train_set = ImageFolder(root='./data/train/00000', transform=trans)
        # test_set =  ImageFolder(test_path,  transform=trans)
        exit()

    train_loader = torch.utils.data.DataLoader(dataset=train_set, batch_size=batch_size, shuffle=False, pin_memory=True, drop_last=False)
    val_loader = torch.utils.data.DataLoader(dataset=val_set,  batch_size=batch_size, shuffle=False, pin_memory=True, drop_last=False)
    print ('==>>> total trainning batch number: {}'.format(len(train_loader)))
    print ('==>>> total validation batch number: {}'.format(len(val_loader)))
    return train_loader, val_loader

