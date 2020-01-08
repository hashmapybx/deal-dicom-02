# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/19 上午11:17
Author: ybx
"""

'''
从s3 下载的数据的数量不一致
'''
import os
import shutil
path = '/media/tx-eva-data/Data1/58server/dcm/2018.03.31_ct_ShangHaiTongJiYiYuan_detection/tmp3/dicom'
list_a= []

for tfile in os.listdir(path):

    list_a.append(tfile)

path_1 = '/media/tx-eva-data/Data1/58server/dcm/2018.03.31_ct_ShangHaiTongJiYiYuan_detection/tmp3/label'
save_path = '/media/tx-eva-data/Data1/58server/dcm/2018.03.31_ct_ShangHaiTongJiYiYuan_detection/tmp3/tmp'
count = 0

for file in os.listdir(path_1):
    if file  not in list_a:
        # print(file)
        count += 1
        shutil.move(os.path.join(path_1, file), os.path.join(save_path, file))

print(count)



