# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/6 上午10:06
Author: ybx
"""

import os
import pydicom
import pandas as pd
path = '/media/tx-eva-data/Data4/CE_DATA/标注数据库/segmentation/dcm'
save_path = '/media/tx-eva-data/Data4/CE_DATA/标注数据库/segmentation'
list_age =[]
list_gender = []
count = 0
for dirpath, dirname, filenames in os.walk(path):
    for file in filenames:
        count +=1
        dcm_path = os.path.join(dirpath, file)
        info = pydicom.read_file(dcm_path, force=True, stop_before_pixels=True)
        try:
            age = info.PatientAge
        except:
            age = 'NA'
        try:
            gender = info.PatientSex
        except:
            gender = 'NA'
        list_age.append(age)
        list_gender.append(gender)
        break
writer = pd.ExcelWriter(save_path + '/' + 'info.xls', encoding='unicode_escape')

df = pd.DataFrame(data={'age':list_age, 'gender': list_gender})

df.to_excel(writer, index=False)
writer.save()


