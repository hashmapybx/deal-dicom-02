# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/28 上午11:45
Author: ybx
"""

import os
import shutil
label_path = "/media/tx-eva-data/Data4/CE_DATA/标注数据库/segmentation/anno"
dcm_path = '/media/tx-eva-data/Data4/CE_DATA/基础数据库/XCoop/dcm'
save_path = '/media/tx-eva-data/Data4/CE_DATA/标注数据库/segmentation/a'

list_a = []

for file in os.listdir(label_path):
    # file = file[:file.rfind('T')]
    list_a.append(file)



for file in os.listdir(dcm_path):

    pid = file.split('-')[1]
    if pid in list_a:
        shutil.copytree(os.path.join(dcm_path, file), os.path.join(save_path, file))



