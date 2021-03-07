import numpy as np
import multiprocessing as mp
import os, shutil, time
import cv2
import pandas as pd
from tqdm import trange
import torch


class load_near_field(object):

    def __init__(self):  # Run it once
        pass

    def find_black_index(self, data, fail_index, threshold=6.9*1e-4):
        black_index, else_index = [], []
        data = data.reshape(data.shape[0], data.shape[-2], data.shape[-1])
        for i in fail_index:
            average_brightness = np.sum(data[i])/(data[i].shape[0]*data[i].shape[1])
            if average_brightness < threshold:
                black_index.append(i)
            else:
                else_index.append(i)
        return black_index, else_index

    def rewrite_img(self, raw_path, new_path, img_size):
        img = cv2.imread(raw_path, cv2.IMREAD_GRAYSCALE)
        if img.shape[0] != img.shape[1]:
            padding_size = np.max(img.shape)
            zero_padding_img = np.zeros((padding_size, padding_size))
            if img.shape[0] != padding_size:
                w = int((padding_size - img.shape[0])/2)
                zero_padding_img[w:-w, :] = img
            elif img.shape[1] != padding_size:
                w = int((padding_size - img.shape[1]) / 2)
                zero_padding_img[:, w:-w] = img
            img = zero_padding_img
        img = img.astype(np.uint8)
        img_resize = cv2.resize(img, (img_size[0], img_size[1]), interpolation=cv2.INTER_AREA)
        pre_img = img_resize
        pre_img = cv2.GaussianBlur(pre_img, (5, 5), 80)

        # pre_img1 = cv2.equalizeHist(pre_img)
        # first_pre_img = cv2.GaussianBlur(pre_img1, (5, 5), 40)
        # second_pre_img = cv2.GaussianBlur(pre_img1, (5, 5), 80)
        #
        # first_pre_img_1 = cv2.GaussianBlur(pre_img, (5, 5), 40)
        # second_pre_img_1 = cv2.GaussianBlur(pre_img, (5, 5), 80)
        #
        #
        # dis_img1 = np.hstack((img_resize, first_pre_img, second_pre_img ))
        # dis_img2 = np.hstack((img_resize, first_pre_img_1, second_pre_img_1))
        # cv2.imshow('eq+blur', dis_img1)
        # cv2.imshow('blur', dis_img2)
        # cv2.waitKey(0)
        img = np.hstack((img_resize, pre_img ))
        cv2.imwrite(new_path, img)

    def load_img(self, path, img_size):
        img = cv2.imread( path, cv2.IMREAD_GRAYSCALE )
        img = cv2.resize( img, (img_size, img_size), interpolation=cv2.INTER_AREA )
        return img

    def get_all_img(self, img_set, img_names, aim_folder, img_size, multi=False, file_type=['.jpg', '.png', '.JPG', '.PNG'], block_folder=['NG_AI']):
        new_img_names = []
        for root, dirs, files in os.walk( aim_folder ):
            if files:
                for mini_file in files:
                    # print(root, mini_file)
                    file_name = root + '/' + mini_file
                    block = False
                    for folder in block_folder:
                        if folder in root:
                            block = True
                            break
                    if block is False:
                        if os.path.splitext(file_name)[1] in file_type:
                            img_names.append( file_name )
                            new_img_names.append( file_name )
                            # img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
                            # img = cv2.resize(img, (img_size[0], img_size[1]), interpolation=cv2.INTER_AREA)
                            # img_set.append(img)
                            # cv2.imshow('HI', img)
                            # cv2.waitKey(0)
        if img_names:
            if multi:
                p = mp.Pool()
                multi_res = [p.apply_async( self.load_img, args=(new_img_names[i], img_size,) ) for i in range( len( new_img_names ) )]
                for res in trange( len( multi_res ) ):
                    img_set.append( multi_res[res].get() )
            else:
                for i in trange( len(new_img_names) ):
                    img_set.append( self.load_img( new_img_names[i], img_size ) )
        return img_set, img_names

    def re_create_folder(self, path):
        try:
            shutil.rmtree(path)
        except:
            pass
        print('Sleep 3 second to delete old data...')
        time.sleep(3)
        os.mkdir(path)

    # load_near_field().resize_folder_tree(input_folder='./near_field_01/raw/', output_folder='./haha/', img_size=[224, 244])
    def resize_folder_tree(self, input_folder, output_folder, img_size, type_set=['.jpg', 'JPG', 'png', 'PNG'], multi=False):
        bad_path = ['', '.', '..']
        raw_image_path, new_image_path, base_folder = [], [], []
        self.re_create_folder(output_folder)
        read_folder = input_folder.split('/')[:-1]
        for sub_folder in read_folder:
            if sub_folder not in bad_path:
                base_folder.append(sub_folder)
        tmp_folder = output_folder
        # build the folder tree
        for folder in base_folder:
            tmp_folder += folder + '/'
            os.mkdir(tmp_folder)
            # self.re_create_folder(tmp_folder)
        # record the image path
        for root, dirs, files in os.walk(input_folder):
            new_root_list = []
            new_root = output_folder
            for sub_folder in root.split('/'):
                if sub_folder not in bad_path:
                    new_root_list.append(sub_folder)
            for folder in new_root_list:
                new_root += folder + '/'
            if not os.path.isdir(new_root):
                os.mkdir(new_root)
            if files:
                for mini_file in files:
                    img_path = root+'/'+mini_file
                    if os.path.splitext(img_path)[1] in type_set:
                        raw_image_path.append(img_path)
                        new_image_path.append(new_root + '/' + mini_file)
        if raw_image_path:
            if multi:
                p = mp.Pool()
                multi_res = [p.apply_async(self.rewrite_img, args=(raw_image_path[i], new_image_path[i], img_size,)) for i in range(len(new_image_path))]
                for res in trange(len(multi_res)):
                    multi_res[res].get()
            else:
                for i in trange( len(new_image_path) ):
                    self.rewrite_img(raw_image_path[i], new_image_path[i], img_size)


if __name__ == '__main__':
    input_folder = '../../near_field_01/raw/20201130/test/'
    output_folder = './demo/'
    multi = True
    image_size = [224, 244]
    load_near_field().resize_folder_tree(input_folder=input_folder, output_folder=output_folder, img_size=image_size, multi=multi)

    # folder = '../raw/NG/NG-20E1534-006-30/'
    # image_scale = 224
    # X, N = load_near_field().get_all_img( img_set=[], img_names=[], aim_folder=folder, img_size=image_scale )
    # X = np.array( X )
    # N = np.array( N )
    # print(N)
    # print(X.shape)
    # print( N.shape )