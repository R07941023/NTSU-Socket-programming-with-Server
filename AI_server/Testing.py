import sys, shutil, os, pynvml
import time
import torch
import numpy as np
# my scrip
from nn_model import DL_Model, DL_VAE
from data_tool import Data_loder, img2np
# ip
import uuid, socket
import requests
# file log
from tkinter import filedialog
from data_tool import fn_data
from opt import opt
from socket_tool import fn as fn_socket

def gpu_info():
    pynvml.nvmlInit()
    gpu_count = pynvml.nvmlDeviceGetCount()
    use_rate = []
    for i in range(gpu_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
        use_rate.append(meminfo.used / meminfo.total)
    return use_rate

def fail2coord(data):
    try:
        data_coord = [['number', 'NFT', 'X', 'Y']]
        for mini_data in data:
            mini_data = os.path.splitext(mini_data)[0]
            # # number
            # number_index = mini_data.index('_')
            # number_data = mini_data[:number_index]
            # # xy_data
            # xy_index = -mini_data[::-1].index('_')
            # xy_data = mini_data[xy_index:][2:].replace("Y", "")
            # x_data = xy_data[:xy_data.index('-')]
            # y_data = xy_data[xy_data.index('-')+1:]
            # # NFT
            # data preprocessing
            X_index, Y_index = -mini_data[::-1].index('X')-1, -mini_data[::-1].index('Y')-1
            mini_data = list(mini_data)
            mini_data[X_index], mini_data[Y_index] = '_', '_'
            mini_data.append('_')
            mini_data = ''.join(mini_data)
            sub_data, temp_data = [], []
            for str_data in mini_data:
                if str_data in ['-', '_']:
                    if temp_data:
                        sub_data.append(''.join(temp_data))
                        temp_data = []
                else:
                    temp_data.append(str_data)
            number_data, x_data, y_data = sub_data[0], sub_data[-2], sub_data[-1]
            NFT_index = sub_data.index(data_coord[0][1])-1
            NFT_number = sub_data[NFT_index]
            data_coord.append([number_data, NFT_number, x_data, y_data])
    except:
        data_coord.append(['X', 'X', 'X', 'X'])
        print('Loding bug on creating the csv file')
    data_coord = np.array(data_coord)
    return data_coord


if __name__ == "__main__":

    # Specifiy data folder path and model type(fully/conv)
    # pretrain = '../pretrain_model/20210217/AE_vgg19/23_model.pth'
    pretrain = '../pretrain_model/20210217/vgg19/8_model.pth'
    data_set = 'liteon_near_field_01_testing'
    dim = opt.image_dim
    batch_size = 1  # 8
    opt.gpu_model, multi_gpu = False, False
    safe_model, software_model = False, True  # don't modify the file
    # folder, model_type = ['../raw/2024705347/', '../raw/2024820003/'], 'vgg19_1d'
    folder, model_type = [], opt.model_type  # vgg19_1d / mobile2_1d
    AI_record_title = ['Date', 'IP', 'Hostname', 'MAC', 'Product (folder)', 'AI_model', 'Total Units Processed (N)', 'AI Inference (N)', 'AI Pass (N)', 'AI Pass (%)', 'AI Fail (N)', 'AI Fail (%)', 'AI idle time (s)', 'Runtime (s)', 'UPH', 'Note']
    AI_record_data = ['None']*len(AI_record_title)
    try:
        ip = requests.get('https://checkip.amazonaws.com').text.strip()
    except:
        ip = 'None'

    if software_model:
        pretrain = '../pretrain_model/20210217/vgg19/8_model.pth'
    # folder.append('../near_field_01/raw/2033920380/')
    # folder.append('../dataset/testing/NG/')
    # folder.append('../dataset/testing/PASS/')
    folder.append('../dataset/testing/Mix/')
    # folder.append('../dataset/testing/Black/')

    # Specify the type of model
    model = DL_Model.model_selection(dim, opt.image_size, model_type, pretrain)
    print('Model = ', model_type)

    # Check if GPU is available, otherwise CPU is used
    use_cuda = torch.cuda.is_available()
    if use_cuda and opt.gpu_model:
        model.cuda()
        if torch.cuda.device_count() > 1:
            if multi_gpu:
                # os.environ['CUDA_VISIBLE_DEVICES'] = '0'
                model = torch.nn.DataParallel(model)
                # torch.distributed.init_process_group(backend='nccl', init_method='tcp://localhost:23456', rank=0, world_size=1)
                # model = nn.parallel.DistributedDataParallel(model)
            else:
                sleep_gpu = (np.argwhere(np.array(gpu_info()) < 0.5).reshape(-1)).tolist()
                if sleep_gpu:
                    print('Use GPU %d' % (sleep_gpu[0]))
                    os.environ['CUDA_VISIBLE_DEVICES'] = str(sleep_gpu[0])
                    # torch.cuda.set_device = str(1)
                else:
                    print('GPUs all are busy!')

    # pretrain
    if pretrain:
        if use_cuda and opt.gpu_model:
            model.load_state_dict(torch.load(pretrain)['model_state_dict'])
            opt.loss_lambda = torch.load(pretrain)['loss_lambda']
            model_version = torch.load(pretrain)['model_version']
        else:
            model.load_state_dict(torch.load(pretrain, map_location=torch.device('cpu'))['model_state_dict'])
            opt.loss_lambda = torch.load(pretrain, map_location=torch.device('cpu'))['loss_lambda']
            model_version = torch.load(pretrain, map_location=torch.device('cpu'))['model_version']
    if model_version != opt.model_version:
        print('Error: Please update the newest version! Software and AI model version do not match')
        exit()

    # Set the type of gradient optimizer and the model it update
    optimizer = DL_Model.optimizer_selection(opt.optimizer_type, model)
    print('optimizer = ', opt.optimizer_type)

    # Choose loss function
    loss_function = DL_Model.loss_selection()
    print('loss type = ', opt.loss_type)

    loop_state = True
    while loop_state:
        AI_record_data = ['None'] * len(AI_record_title)
        if software_model:
            folder = []
            manual_folder = filedialog.askdirectory()
            if os.path.isdir(manual_folder):
                folder.append(manual_folder)
            else:
                print('The system can not find the folder in this PC!')
                break
        # Get data loaders of training set and validation set
        TIME_LOAD_DATA_i = time.time()
        try:
            X, Y, test_loader, N, ret = Data_loder.get_dataloader(folder, data_set, opt.image_size, batch_size, val_proportion=None, random_seed=None)
        except:
            print('Error code: load data!')
            continue
        if ret:
            TIME_LOAD_DATA_f = time.time()
            TIME_LOAD_DATA = TIME_LOAD_DATA_f - TIME_LOAD_DATA_i
            if not safe_model:
                # build the NG and PASS folder
                path_set = []
                for file in N:
                    path_set.append( os.path.dirname( file ) )
                path_set = set(path_set)

                temp_set = path_set
                pass_path_set, fail_path_set, black_path_set, ng_path_set = {}, {}, {}, {}
                for mini_path in temp_set:
                    pass_path_set[mini_path], fail_path_set[mini_path], black_path_set[mini_path], ng_path_set[mini_path] = [], [], [], []
            # testing
            test_pre, test_detail = DL_Model.model_build(epoch=1, model=model, loss_function=loss_function, optimizer=optimizer, model_type=model_type).run(data_loader=test_loader, type='validation')
            test_acc, test_loss, loss_lambda, test_loss_sum, test_recons, class_test_acc, test_kill_loss, test_gt, test_data = test_detail[0], test_detail[1], test_detail[2], test_detail[3], test_detail[4], test_detail[5], test_detail[6], test_detail[7], test_detail[8]
            test_pre = test_pre.reshape(-1)
            fault_index = np.argwhere(test_pre == 0).reshape(-1)

        if not software_model:
            loop_state = False










