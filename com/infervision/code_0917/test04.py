# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/17 下午2:30
Author: ybx
"""
'''
rename dicom 和anno 文件 
医院_pid_层厚
'''
import os
import pydicom
import shutil

src_path = "/media/tx-eva-data/NAS/基础数据库/首都医科大学附属北京潞河医院/TMP"
save_path = '/media/tx-eva-data/NAS/基础数据库/首都医科大学附属北京潞河医院/other'
hosp_id = "CN010011"

for file in os.listdir(src_path):
    for dcm in os.listdir(os.path.join(src_path, file)):
        dcm_path = os.path.join(os.path.join(src_path, file), dcm)
        instence_number = os.path.split(dcm_path)[-1][-8:]
        new_name = hosp_id+'-'+file
        new_path = os.path.join(save_path, new_name)
        # print(new_path)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        os.rename(dcm_path, os.path.join(new_path, new_name+instence_number))
