import numpy as np
import multiprocessing as mp
import os, shutil
import cv2
import pandas as pd
from tqdm import trange

class fn_tool():

    def re_create_folder(self, path):
        try:
            shutil.rmtree(path)
        except:
            pass
        os.mkdir(path)

    def dict2csv(self, output_path, data):
        # data2str
        for key in data:
            data[key] = str(data[key])
        df = pd.DataFrame.from_dict(data, orient='index')
        df.to_csv(output_path, header=False)

    def csv2dict(self, path):
        # data2str
        data = {}
        df = pd.read_csv(path).to_numpy()
        for mini_data in df:
            data[mini_data[0]] = mini_data[1]
        return data

    def str2tuple(self, data, int_type=False):
        tuple_data = []
        number = []
        for mini_str in data:
            if mini_str.isdigit():
                number.append(mini_str)
            else:
                if number:
                    unit_n = len(number)-1
                    count_number = 0
                    for mini_n in number:
                        count_number += float(mini_n)*10**unit_n
                        unit_n -= 1
                    if int_type:
                        count_number = int(count_number)
                    tuple_data.append(count_number)
                    number = []
        tuple_data = tuple(tuple_data)
        return tuple_data

    def preprocessing(self, img, img_size, pre_his, pre_gauss_blur, blur_winsize, blur_sigma, display=False):
        # print(img_size, pre_his, pre_gauss_blur, blur_winsize, blur_sigma)
        # exit()
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
        img = cv2.resize(img, (img_size, img_size), interpolation=cv2.INTER_AREA)
        if display:
            cv2.imshow('origin', img)
        if pre_his:
            img = cv2.equalizeHist(img.astype(np.uint8))
            if display:
                cv2.imshow('hist', img)
        if pre_gauss_blur:
            img = cv2.GaussianBlur(img, blur_winsize, blur_sigma)
            if display:
                pass
                cv2.imshow('blur', img)
                cv2.waitKey(1)
        return img

    def load_img(self, path, img_size, pre_his, pre_gauss_blur, blur_winsize, blur_sigma, display=False):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img = self.preprocessing(img, img_size, pre_his, pre_gauss_blur, blur_winsize, blur_sigma, display=display)
        return img

    def get_all_img(self, img_set, img_names, aim_folder, img_size, pre_his, pre_gauss_blur, blur_winsize, blur_sigma, multi=False, file_type=['.jpg', '.png', '.JPG', '.PNG'], block_folder=['NG_AI', 'Black_AI']):
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
                display = False
                multi_res = [p.apply_async( self.load_img, args=(new_img_names[i], img_size, pre_his, pre_gauss_blur, blur_winsize, blur_sigma, display, ) ) for i in range( len( new_img_names ) )]
                for res in trange( len( multi_res ) ):
                    img_set.append( multi_res[res].get() )
            else:
                display = False
                for i in trange( len(new_img_names) ):
                    img_set.append( self.load_img( new_img_names[i], img_size, pre_his, pre_gauss_blur, blur_winsize, blur_sigma, display ) )
        return img_set, img_names

    def data2csv(self, title, data, output_path):
        dataframe = np.hstack((title, data)).astype(np.str).T
        df = pd.DataFrame(dataframe)
        df.to_csv(output_path + 'dataset.csv', encoding="gbk", index=False, header=False)

    def check_file_name(self, dataset, file_type=['.jpg', '.png', '.JPG', '.PNG'], block_folder=['NG_AI'], move=False):
        # read the file names
        img_names, path_names = [], []
        for aim_folder in dataset:
            for root, dirs, files in os.walk(aim_folder):
                if files:
                    for mini_file in files:
                        file_name = root + '/' + mini_file
                        block = False
                        for folder in block_folder:
                            if folder in root:
                                block = True
                                break
                        if block is False:
                            if os.path.splitext(file_name)[1] in file_type:
                                path_names.append(root)
                                img_names.append(mini_file)
        # check the file names
        img_names, history_index, repeat_index = np.array(img_names), [], []
        for i in range(len(img_names)):
            if i not in history_index and img_names[i] in img_names[i+1:]:
                overlap_index = np.argwhere(img_names == img_names[i]).reshape(-1)
                print('')
                print(img_names[i])
                repeat_index.append(i)
                for j in overlap_index:
                    history_index.append(j)
                    print(path_names[j])
                    if move:
                        if not os.path.isdir(path_names[j]+'/repeat/'):
                            os.mkdir(path_names[j]+'/repeat/')
                        print(path_names[j] + '/' + img_names[i], path_names[j]+'/repeat/'+img_names[i])
                        shutil.move(path_names[j] + '/' + img_names[i], path_names[j]+'/repeat/'+img_names[i])
        if len(history_index) != 0:
            for i in repeat_index:
                print(img_names[i])
            print('Repeated number = ', len(repeat_index))
            exit()
        else:
            print('Check the file name : OK!')

    def collect_run(self, pass_folder, fault_folder, random_seed, img_size, output_path, pre_his, pre_gauss_blur, blur_winsize, blur_sigma, multi=False):
        np.random.seed( random_seed )
        pass_feature, fault_feature = [], []
        pass_names, fault_names = [], []
        # load data
        for aim_folder in pass_folder:
            print( 'loading=', aim_folder, '.....' )
            pass_feature, pass_names = self.get_all_img( pass_feature, pass_names, aim_folder, img_size, pre_his=pre_his, pre_gauss_blur=pre_gauss_blur, blur_winsize=blur_winsize, blur_sigma=blur_sigma, multi=multi )
        pass_target = np.ones( (len( pass_feature ), 1) )
        for aim_folder in fault_folder:
            print( 'loading=', aim_folder, '.....' )
            fault_feature, fault_names = self.get_all_img( fault_feature, fault_names, aim_folder, img_size, pre_his=pre_his, pre_gauss_blur=pre_gauss_blur, blur_winsize=blur_winsize, blur_sigma=blur_sigma, multi=multi )
        fault_target = np.zeros( (len( fault_feature ), 1) )
        # check the data size
        pass_feature, fault_feature = np.array( pass_feature ), np.array( fault_feature )
        pass_names, fault_names = np.array( pass_names ).reshape( -1, 1 ), np.array( fault_names ).reshape( -1, 1 )
        print( pass_feature.shape, pass_target.shape, fault_feature.shape, fault_target.shape )
        if pass_feature.shape[0] != 0 and fault_feature.shape[0] != 0:
            X = np.vstack( (pass_feature, fault_feature) )
            Y = np.vstack( (pass_target, fault_target) )
            N = np.vstack( (pass_names, fault_names) )
        elif pass_feature.shape[0] == 0 and fault_feature.shape[0] == 0:
            print( 'No any data in these folder....' )
            exit()
        elif pass_feature.shape[0] == 0:
            X, Y, N = fault_feature, fault_target, fault_names
        elif fault_feature.shape[0] == 0:
            X, Y, N = pass_feature, pass_target, pass_names
        random_map = np.random.choice( X.shape[0], X.shape[0], replace=False )
        X, Y, N = X[random_map], Y[random_map], N[random_map]
        np.save( output_path + 'X', X ), np.save( output_path + 'Y', Y ), np.save( output_path + 'N', N )
        # data2csv
        title = np.array( ['path', 'type'] ).reshape( -1, 1 )
        data = np.hstack( (N.astype( np.str ), Y) ).T
        self.data2csv( title=title, data=data, output_path=output_path )

if __name__ == '__main__':

    random_seed = 100
    img_size = 224
    output_path = './'
    multi = True

    # histogram
    pre_his = False
    # Gaussian Blur
    pre_gauss_blur = False
    blur_winsize = (5, 5)
    blur_sigma = 80

    pass_folder, fault_folder = [], []
    # pass_folder.append('../../near_field_01/raw/20201127/')  # 422
    # pass_folder.append('../../near_field_01/raw/20201130/')  # 152
    pass_folder.append('../../dataset/raw/20210209/')  # 166
    pass_folder.append('../../dataset/raw/20201214/')  # 891
    pass_folder.append('../../dataset/raw/20201201/training/')  # 984
    # pass_folder.append('../../near_field_01/raw/20J1904-026-01/')

    fault_folder.append('../../dataset/raw/NG/20210208')  # 301
    fn_tool().check_file_name(dataset=pass_folder+fault_folder, move=False)

    # record the parameter
    para_data = {}
    para_data['index'] = 'parameter'
    para_data['his'] = pre_his
    para_data['gauss_blur'] = pre_gauss_blur
    para_data['winsize'] = str(blur_winsize)
    para_data['sigma'] = str(blur_sigma)
    fn_tool().dict2csv(output_path=output_path+'parameter.csv', data=para_data)
    # loading data...
    fn_tool().collect_run( pass_folder=pass_folder, fault_folder=fault_folder, random_seed=random_seed, img_size=img_size, output_path=output_path, pre_his=pre_his, pre_gauss_blur=pre_gauss_blur, blur_winsize=blur_winsize, blur_sigma=blur_sigma, multi=multi )




