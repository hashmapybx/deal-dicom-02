# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/5 下午3:52
Author: ybx
"""

import os
import pydicom
path = '/media/tx-eva-data/DR/标注数据库/Computer-Aided-Diagnostic-Software'

dict_a = {}
for folders_path, folders, files in os.walk(path):
    for dcm_file in files:
        dcm_file_path = os.path.join(folders_path, dcm_file)
        if dcm_file_path.endswith('.xml'):
            continue
        info = pydicom.read_file(dcm_file_path, force=True, stop_before_pixels=True)
        # hosp_file_name = dcm_file_path.split('/')[-2]
        try:
            manufacture = str(info.Manufacturer)

        except:
            manufacture = 'N/A'

        if manufacture not in dict_a.keys():
            dict_a[manufacture] = 1
        else:
            dict_a[manufacture] = dict_a[manufacture] + 1



print(dict_a)

