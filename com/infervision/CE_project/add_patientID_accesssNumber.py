# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/5 下午5:41
Author: ybx
"""
import pydicom
import os
path = '/media/tx-eva-data/Data4/CE_DATA/基础数据库'
list_1 = []
list_2 = []
list_3 = []

for file in os.listdir(path):
    hosp_path = os.path.join(path, file)
    for sfile in os.listdir(hosp_path):
        if sfile.endswith('.log'):
            continue
        a_folder = os.path.join(hosp_path, sfile)
        for bfile in os.listdir(a_folder):
            b_folder = os.path.join(a_folder, bfile)
            for dcm in os.listdir(b_folder):
                dcm_path = os.path.join(b_folder, dcm)
                instance_number = os.path.split(dcm_path)[-1]
                info = pydicom.read_file(dcm_path, force=True)
                # print(info.PatientID, info.AccessionNumber, file)
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

print(list_1)

print(list_2)

print(list_3)



























