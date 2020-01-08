# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/6 下午6:10
Author: ybx
"""

import os
import shutil
import cv2
import numpy as np
import pylab
import matplotlib.pyplot as plt
path = '/media/tx-eva-data/Data4/大连中山肺不张/tmp'
path_1 = '/media/tx-eva-data/Data4/大连中山肺不张/2019_07_08_pulmonary_atelectasis/_dcm'
save_path = '/media/tx-eva-data/Data4/大连中山肺不张/save'
# list_a = []
# for file in os.listdir(path_1):
#     list_a.append(file)
#
# for file in os.listdir(path):
#     if file not in list_a:
#         shutil.move(os.path.join(path, file), os.path.join(save_path, file))

import numpy as np
from PIL import Image

img  = np.array(Image.open('/media/tx-eva-data/Data4/大连中山肺不张/save/R00035080/1.2.392.200046.100.2.1.1.53906.20101101090101.2/1.2.392.200046.100.2.1.1.53906.20101101090101.2.1.1.dcm'))
print(img)


