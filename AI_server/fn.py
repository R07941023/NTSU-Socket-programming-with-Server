import socket
import struct
from datetime import datetime
import threading
from tqdm import tqdm, trange
import json
import pickle
import hashlib
import sys, shutil, os, pynvml
import time
import torch
from torch.utils.data import TensorDataset
import numpy as np
import cv2
# my script
from opt import opt
from nn_model import DL_Model, DL_VAE
from data_tool import Data_loder, img2np, fn_data



class tool(object):

    def __init__(self):
        pass

    def pwd2encode(self, pwd, type=None):
        if type == 'MD5':
            m = hashlib.md5()
            m.update( pwd.encode( "utf-8" ) )
            pwd = m.hexdigest()
        if type == 'SHA':
            m = hashlib.sha1()
            m.update( pwd.encode( "utf-8" ) )
            pwd = m.hexdigest()
        return pwd

class AI_model(object):

    def __init__(self):
        pass

class socket_model(object):

    def __init__(self, host, port, max_transfer_speed=1024):
        self.max_transfer_speed = max_transfer_speed
        self.host = host
        self.port = port

    def common_filter(self, whitelist, candidate, encode=None):
        candidate = tool().pwd2encode(candidate, encode)
        validation_results = False
        if candidate in whitelist:
            validation_results = True
        return validation_results

    def socket_server(self, channel_max, filter_PWD, pwd_whitelist):
        try:
            s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
            s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
            s.bind( (self.host, self.port) )
            s.listen( channel_max )
        except socket.error as msg:
            print( msg )
            sys.exit( 1 )
        while True:
            print('', '\n')
            print('Server Online...')
            try:
                conn, addr = s.accept()
                vert_pwd = True
                # password filter
                pwd = conn.recv( 1024 ).decode()
                if filter_PWD is True:
                    vert_pwd = self.common_filter( pwd_whitelist, pwd, encode='MD5')
                conn.send( str(vert_pwd)[0].encode() )
                print( 'Pwssword security verification: ', vert_pwd )
                if vert_pwd:
                    print('Pass security verification!')
                    t = threading.Thread( target=self.deal_data, args=(conn, addr) )
                    t.start()
                else:
                    print('Login block: ', addr[0], '\n' )
                    conn.close()
            except:
                print('Attack form ', addr[0])

    def deal_data(self, conn, addr):
        ti = time.time()
        # progress = tqdm( total=100 )
        print( 'Accept new connection from {0}'.format( addr ) )
        # conn.settimeout(500)
        type = conn.recv(1024).decode()
        if type == 'AIT':
            opt.gpu_model = False
            image_type = ['.bmp', '.jpg', '.png']

            # model
            # pretrain = '../../Test_AI_model.pth'
            pretrain = None
            model = DL_Model.model_selection(opt.image_dim, opt.image_size, opt.model_type, pretrain)
            # Check if GPU is available, otherwise CPU is used
            use_cuda = torch.cuda.is_available()
            if use_cuda and opt.gpu_model:
                model.cuda()
            print('Model = ', opt.model_type)
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

            # AOT signal
            conn.send('T'[0].encode())
            while True:
                image_path = conn.recv(1024).decode()
                if os.path.isfile(image_path) and os.path.splitext(image_path)[1] in image_type:
                    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    img = img2np.fn_tool().preprocessing(img, opt.image_size, pre_his=False, pre_gauss_blur=False, blur_winsize=0, blur_sigma=0)
                    X = img[np.newaxis, np.newaxis, :, :].astype(np.float) / 255.
                    Y = np.zeros((X.shape[0],))
                    test_set = TensorDataset(torch.FloatTensor(X), torch.LongTensor(Y))
                    test_loader = torch.utils.data.DataLoader(dataset=test_set, batch_size=1, shuffle=False)
                    test_pre, test_detail = DL_Model.model_build(epoch=1, model=model, loss_function=loss_function, optimizer=optimizer, model_type=opt.model_type).run(data_loader=test_loader, type='validation')
                    # if test_pre[0] == 1:
                    #     conn.send(('T' + image_path).encode())
                    # else:
                    #     conn.send(('F' + image_path).encode())
                    conn.send(('T' + image_path).encode())
                else:
                    conn.send(('F'+image_path).encode())
        conn.close()
        tf = time.time()
        print('Runtime = ', tf-ti, '[s]', '\n' )
        print( '' )


