# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/12 下午4:20
Author: ybx
"""
import os
import shutil
path = '/media/tx-eva-data/Data3/58server_数据整理/dcm/2017.8.15_ct_LiaoChengHuaMeiYiYuan_detection/dcm'
label_path = '/media/tx-eva-data/Data3/58server_数据整理/dcm/2017.8.15_ct_LiaoChengHuaMeiYiYuan_detection/label'
save_path = '/media/tx-eva-data/Data3/58server_数据整理/dcm/2017.8.15_ct_LiaoChengHuaMeiYiYuan_detection/tmp'
list_a = []
for file in os.listdir(label_path):
    list_a.append(file)


for sfile in os.listdir(path):
    if sfile  in list_a:
        shutil.move(os.path.join(path, sfile), os.path.join(save_path, sfile))


