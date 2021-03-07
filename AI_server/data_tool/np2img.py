import numpy as np
import multiprocessing as mp
import os, shutil
import cv2
import pandas as pd

if __name__ == '__main__':
    path = './near_field_01/res_224x224/'
    class_names = {0: 'fault', 1: 'pass'}
    X = np.load(path + 'X.npy')
    Y = np.load(path + 'Y.npy').reshape(-1)
    N = pd.read_csv(path + 'dataset.csv').to_numpy()[:, 0]
    # check the folder
    try:
        shutil.rmtree(path+class_names[0])
        shutil.rmtree(path + class_names[1])
    except:
        pass
    os.mkdir(path+class_names[0])
    os.mkdir(path + class_names[1])
    # write the image from npy
    for i in range(len(N)):
        if Y[i] in class_names:
            cv2.imwrite(path+class_names[Y[i]]+'/' + str(i+1) + '.jpg', X[i])
            # cv2.imshow('resize', X[i])
            # cv2.imshow('raw', cv2.resize(cv2.imread(N[i]), (750, 980)))
            # cv2.waitKey(1)








