# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/1 上午11:07
Author: ybx
"""
import os
import shutil

label_path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/chw/anno'
save_path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/chw/dcm'
list_pid = []
for file in os.listdir(label_path):
    list_pid.append(file)

dicom_path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/dcm'
for sfile in os.listdir(dicom_path):
    if sfile in list_pid:
        shutil.move(os.path.join(dicom_path, sfile), os.path.join(save_path, sfile))



