# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/26 上午10:48
Author: ybx
"""

import os
import shutil

path = "/media/tx-eva-data/Data1/tmp/2019_09_16_fracture_KLMY_test/anno"
save_path = "/media/tx-eva-data/Data1/tmp/2019_09_16_fracture_KLMY_test/tmp"
dcm_path = "/media/tx-eva-data/Data1/tmp/2019_09_16_fracture_KLMY_test/dicom/CW990001/DATA-312"


list_pid = []

for file in os.listdir(dcm_path):
    list_pid.append(file)


for file in os.listdir(save_path):
    if file not in list_pid:
        print(file)




# for file in os.listdir(path):
#     pid = file[:-8]
#     file_path = os.path.join(path, file)
#     new_path = os.path.join(save_path, pid)
#     if not os.path.exists(new_path):
#         os.makedirs(new_path)
#     shutil.move(file_path, os.path.join(new_path, file))




