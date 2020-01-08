# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/5 下午5:41
Author: ybx
"""
import pydicom
import os
path = '/media/tx-eva-data/Data4/CE_DATA/原始数据库'

for dirpaths, dirname, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('.log'):
            continue
        dcm_path = os.path.join(dirpaths, filename)
        if 'old' in dcm_path:
            continue
        instance_number = os.path.split(dcm_path)[-1]
        info = pydicom.read_file(dcm_path, force=True)
        if len(str(info.PatientID)) == 0 and len(str(info.AccessionNumber)) != 0:
            info.PatientID = str(info.AccessionNumber)
            # list_1.append(dcm)
        elif len(str(info.PatientID)) != 0 and len(str(info.AccessionNumber)) == 0:
            # list_2.append(dcm)
            info.AccessionNumber = str(info.PatientID)
        elif len(str(info.PatientID)) == 0 and len(str(info.AccessionNumber)) == 0:
            # list_3.append(dcm)
            info.PatientID = instance_number.split('-')[1]
            info.AccessionNumber = instance_number.split('-')[1]
        else:
            continue
        info.save_as(dcm_path)




























