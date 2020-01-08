# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/30 下午7:05
Author: ybx
"""

import os
import pydicom
import xlwt
path  = '/media/tx-eva-data/Data4/CE_DATA/标注数据库'
list_rows = []
dict_age = {}

for file in os.listdir(path):
    pro_folder = os.path.join(path, file)
    for sfile in os.listdir(pro_folder):
        # print(sfile)
        if sfile == 'dcm':
            dcm_folder = os.path.join(pro_folder, sfile)
            for dfile in os.listdir(dcm_folder):
                dcm_path = os.path.join(dcm_folder, dfile)
                for dcm_f in os.listdir(dcm_path):
                    image_path = os.path.join(dcm_path, dcm_f)
                    instance_number = os.path.split(image_path)[-1]
                    info = pydicom.read_file(image_path, force=True, stop_before_pixels=True)
                    try:
                        patientAge = info.PatientAge
                    except:
                        patientAge = 'N/A'

                    dict_age[instance_number[:-8]] = patientAge

                    # list_rows.append([instance_number[:-8], patientAge])
                    break

for key, value in dict_age.items():
    list_rows.append([key, value])


boot = xlwt.Workbook()
sheet = boot.add_sheet('sheet1', cell_overwrite_ok=True)

for a in range(len(list_rows)):
    for b in range(len(list_rows[a])):
        sheet.write(a, b , list_rows[a][b])


boot.save('/media/tx-eva-data/Data4/CE_DATA/CE_三四级文件/info.xls')
