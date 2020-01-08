# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/6 下午6:49
Author: ybx
"""
import os
import pydicom
import random
path = '/media/tx-eva-data/CE_DR/train/data_2634/标记数据库/清华大学医院/anno'
for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path, file.replace('_', '-')))

# for file in os.listdir(path):
#     if len(file[9:-4]) > 30:
#         dcm_path = os.path.join(path, file)
#         info = pydicom.read_file(dcm_path, force=True)
#
#         # info.PatientID = str(random.randint(0, 99999999)).zfill(8)
#         # print(os.path.join(path, file[:8] +'-'+ str(info.PatientID) + '.dcm'))
#         os.rename(dcm_path, os.path.join(path, file[:8] +'-'+ str(info.PatientID) + '.dcm'))

