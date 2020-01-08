# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/27 下午6:14
Author: ybx
"""

import os
path_1 = '/media/tx-eva-data/Data4/河南/dcm_save/CT/1.5mm'
path_2 = '/media/tx-eva-data/Data4/河南/dcm_save/CT/1.25mm'

list_1 = []
for file in  os.listdir(path_1):
    pid = file[9:file.rfind('T')-1]
    list_1.append(pid)


for file in os.listdir(path_2):
    pid = file[9:file.rfind('T')-1]
    if pid in list_1:
        print(file)
