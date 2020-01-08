# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/11 上午11:44
Author: ybx
"""
import os
import shutil
dcm_path = "/media/tx-eva-data/Data1/tmp/2019_09_11-DATA-249/dicom"
label_path = "/media/tx-eva-data/Data1/tmp/2019_09_11-DATA-249/label"
save_path = "/media/tx-eva-data/Data1/tmp/2019_09_11-DATA-249/other"

list_a = []
for file in os.listdir(label_path):
    list_a.append(file)

count = 0
for file in os.listdir(dcm_path):
    if file not in list_a:
        shutil.move(os.path.join(dcm_path, file), os.path.join(save_path, file))


