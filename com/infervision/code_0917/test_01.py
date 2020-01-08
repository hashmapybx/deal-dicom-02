# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/17 上午10:54
Author: ybx
"""
import os
import shutil

dcm_path = "/media/tx-eva-data/Data1/tmp/2019_09_09_ShengJIng_fracture/dcm"
anno_path = "/media/tx-eva-data/Data1/tmp/2019_09_09_ShengJIng_fracture/anno"
save_path = "/media/tx-eva-data/Data1/tmp/2019_09_09_ShengJIng_fracture/other"
#
list_pid =[]
for file in os.listdir(anno_path):
    list_pid.append(file)

for file in os.listdir(dcm_path):
    if file not in list_pid:
        shutil.move(os.path.join(dcm_path, file), os.path.join(save_path, file))

# for file in os.listdir(dcm_path):
#     a_path = os.path.join(dcm_path, file)
#     # print(a_path)
#     for sfile in os.listdir(a_path):
#         if os.path.isdir(os.path.join(a_path, sfile)):
#             os.system('rm -rf %s' % os.path.join(a_path, sfile))
