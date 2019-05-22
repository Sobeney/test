# -*- coding:utf-8 -*-
# from PIL import Image
import torch
import numpy as np
import os
# import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# test for load code and data from hdfs
# PATH = '/yijpan'
# rgb1 = mpimg.imread(os.path.join(PATH, 'cat.jpg'))
rgb1 = mpimg.imread('cat.jpg')



# test for pytorch and gpu
n = torch.from_numpy(rgb1)
if torch.cuda.is_available():
    n = n.cuda()
    n = n + n

n = n.cpu()
a = n.numpy()




# test for save data to hdfs
with open('result', 'w') as file:
    for i in range(3):
        np.savetxt(file, a[:,:,i])