import cv2
import os, shutil
import numpy as np

path = './'
output_path = './result/'
kernel_size, sigma = (5, 5), 40
img_size = 224
dirs = os.listdir(path)
img_type = ['.png', '.PNG', '.jpg', '.JPG']

try:
    shutil.rmtree(output_path)
except:
    pass
os.mkdir(output_path)
for file in dirs:
    if os.path.splitext(file)[1] in img_type:
        img = cv2.imread(path+file, cv2.IMREAD_GRAYSCALE)
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
        img = cv2.resize(img, (img_size, img_size), interpolation=cv2.INTER_AREA)
        img = cv2.GaussianBlur(img, kernel_size, sigma)
        cv2.imwrite(output_path+file, img)


