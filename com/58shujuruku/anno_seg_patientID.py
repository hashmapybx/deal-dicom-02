# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/21 下午2:44
Author: ybx
"""
import os
import shutil
path = '/media/tx-eva-data/Data4/东营区人民医院/2019_11_21_no_check_testData/dicom/DYQRM-220790-T125'
save_path = '/media/tx-eva-data/Data4/东营区人民医院/dicom/DYQRM/2019-11-21_DATA-936'
a_path = '/media/tx-eva-data/Data4/东营区人民医院/dicom/DYQRM/tmp'
list_a = []
for file in os.listdir(path):
    list_a.append(file)


for sfile in os.listdir(save_path):
    if sfile not in list_a:
        shutil.move(os.path.join(save_path, sfile), os.path.join(a_path, sfile))


