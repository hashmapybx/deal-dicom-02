# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/15 下午12:20
Author: ybx
"""

import cv2
import numpy as np
from matplotlib import pyplot

image = cv2.imread('/home/tx-eva-data/Pictures/girl.webp')
# print(img.shape) # (600, 400, 3) 返回值是一个行宽 列高, 通道数 彩色图一般是三通道RGB
head = image[27:124,159:260]
image[200:297,299:400] = head
cv2.imshow('New', image)
cv2.waitKey()
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()