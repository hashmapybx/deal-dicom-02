# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/6 上午10:06
Author: ybx
"""

import os
import pydicom
import pandas as pd
path = '/media/tx-eva-data/CE_DR/train/data_2634/基础数据库/广州中山大学附属第一医院/dcm'
save_path = '/media/tx-eva-data/CE_DR/train/data_2634/基础数据库/广州中山大学附属第一医院'
list_pid =[]
list_manfanu = []
count = 0
for dirpath, dirname, filenames in os.walk(path):
    for file in filenames:
        count +=1
        dcm_path = os.path.join(dirpath, file)

        info = pydicom.read_file(dcm_path, force=True, stop_before_pixels=True)
        try:
            pid = info.PatientID
        except:
            pid = 'NA'
        try:
            manuf = info.Manufacturer
        except:
            gender = 'NA'
        list_pid.append(pid)
        list_manfanu.append(manuf)
        # break
writer = pd.ExcelWriter(save_path + '/' + '标记_info.xls', encoding='unicode_escape')

df = pd.DataFrame(data={'pid':list_pid, 'manufacture': list_manfanu})

df.to_excel(writer, index=False)
writer.save()
print(count)

