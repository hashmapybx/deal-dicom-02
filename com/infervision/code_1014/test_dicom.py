# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/15 下午9:37
Author: ybx
"""

import os

path_1 = '/media/tx-eva-data/Data4/贵港市人民医院8.2测试数据/media/tx-deepocean/Data/DICOMS/CT_Lung_save/CT/1mm'
path_2 = '/media/tx-eva-data/Data4/贵港市人民医院8.2测试数据/media/tx-deepocean/Data/DICOMS/CT_Lung_save/CT/2mm'

list_a = []
for file in os.listdir(path_1):
    pid = file[9:file.rfind('T')-1]
    list_a.append(pid)



for file in os.listdir(path_2):
    pid = file[9:file.rfind('T')-1]
    if pid in list_a:
        print(file)

