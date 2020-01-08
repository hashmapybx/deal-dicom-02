# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/6 下午5:35
Author: ybx
"""
import os
import pydicom
import random
label_path = '/media/tx-eva-data/CE_DR/train/data_2634/标记数据库/清华大学医院/anno'
path = '/media/tx-eva-data/CE_DR/train/data_2634/标记数据库/清华大学医院/dcm'
save_path ='/media/tx-eva-data/CE_DR/train/data_2634/标记数据库/清华大学医院/b'

hosp = 'CW023007'
count = 0

dict = {}

for file in os.listdir(path):
    dcm_path = os.path.join(path, file)
    # info = pydicom.read_file(dcm_path, force=True, stop_before_pixels=True)
    # seriesInstanceUID = info.SeriesInstanceUID.rstrip("\x00")
    # studyInstanceUID = info.StudyInstanceUID.rstrip("\x00")
    if file[9:-4] not in dict:
        dict[file[9:-4]] = file[:-4]
count = 0
for sfile in os.listdir(label_path):
    for key, value in dict.items():
        if sfile[:-4] == key:
            os.rename(os.path.join(label_path, sfile), os.path.join(save_path, value + '.xml'))
            count += 1
            # print('a')



    # info.PatientID = str(random.randint(0,99999999)).zfill(8)
    # print(new_name)
    # count += 1
    # info.save_as(dcm_path)
    # os.rename(dcm_path, os.path.join(save_path, new_name + '.dcm'))


print(count)

