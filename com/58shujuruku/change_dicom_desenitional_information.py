# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/25 下午5:05
Author: ybx
"""
import os
import shutil
import time
import pydicom
start = time.time()

path = '/media/tx-eva-data/Data1/58server/dcm/2018.03.31_ct_ShangHaiTongJiYiYuan_detection/tmp1/dicom'
save_path = '/media/tx-eva-data/Data1/58server/dcm/2018.03.31_ct_ShangHaiTongJiYiYuan_detection/tmp1/tmp'
for file in os.listdir(path):
    if file.endswith('.csv'):
        continue
    a_folder = os.path.join(path, file)
    for sfile in os.listdir(a_folder):
        dcm_path = os.path.join(a_folder, sfile)
        info = pydicom.read_file(dcm_path, force=True)
        info.PatientAddress = 'Anonymized by inferVISION'
        info.ReferringPhysicianName= 'Anonymized by inferVISION'
        info.PatientName = 'Anonymized by inferVISION'

        out_path = os.path.join(save_path, file)
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        try:
            info.save_as(os.path.join(out_path, sfile))
        except:
            print(sfile)

end = time.time()
print('程序消耗的时间:', float(end-start))  # 25




