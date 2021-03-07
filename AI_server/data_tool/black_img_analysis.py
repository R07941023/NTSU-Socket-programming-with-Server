import numpy as np
import multiprocessing as mp
import os, shutil
import cv2
import pandas as pd

# historgram
# sum, number

if __name__ == '__main__':
    path = '../../near_field_01/raw/Black/'
    img_type = ['.jpg', '.JPG', '.png', '.PNG']
    dirs = os.listdir(path)
    sum_total, pos_total, name_total = ['sum'], ['number'], ['name']

    # histogram
    his_folder = path+'histogram/'
    try:
        shutil.rmtree(his_folder)
    except:
        pass
    os.mkdir(his_folder)

    for file in dirs:
        if os.path.splitext(file)[1] in img_type:
            img = cv2.imread(path+file, cv2.IMREAD_GRAYSCALE)
            his_img = cv2.equalizeHist(img)
            cv2.imwrite(his_folder+file, his_img)
            name_total.append(file)
            sum_total.append(str(np.sum(img)))
            pos_total.append(str(np.argwhere(img != 0).shape[0]))
    sum_total = np.array(sum_total).reshape(-1, 1)
    pos_total = np.array(pos_total).reshape(-1, 1)
    name_total = np.array(name_total).reshape(-1, 1)
    dataframe = np.hstack((name_total, sum_total))
    dataframe = np.hstack((dataframe, pos_total))
    df = pd.DataFrame(dataframe)
    df.to_csv(path+'black_result.csv', encoding="gbk", index=False, header=False)
    # analysis
    sum_total, pos_total = sum_total[1:], pos_total[1:]
    sum_total, pos_total = sum_total.astype(np.float), pos_total.astype(np.float)
    sum_max, n_max = np.max(sum_total), np.max(pos_total)
    print('Max (sum/number) = ', sum_max, '/', n_max)









