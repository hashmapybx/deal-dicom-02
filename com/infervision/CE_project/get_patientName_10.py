# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/7 下午6:53
Author: ybx
"""
import os
import pydicom
import random
path = '/media/tx-eva-data/Data4/CE_10_new'
for file in os.listdir(path):
    a_folder = os.path.join(path, file)
    name = 'Anonymous' + str(random.randint(0, 999)).zfill(4)
    for sfile in os.listdir(a_folder):
        dcm_path = os.path.join(a_folder, sfile)
        info = pydicom.read_file(dcm_path)
        name = info.PatientName
        print(name)
        # break
        # info.save_as(dcm_path)
