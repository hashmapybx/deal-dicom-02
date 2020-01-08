# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/11 下午6:35
Author: ybx
"""

import os
import shutil
path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/assgin/2019-11-12_cjw/anno'
dcm_path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/tmp'
save_path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/assgin/2019-11-12_cjw/dcm'

list_a = []

for file in os.listdir(path):
    list_a.append(file)
count = 0
for sfile in os.listdir(dcm_path):
    if sfile  in list_a:
        print(sfile)
        count += 1
        shutil.move(os.path.join(dcm_path, sfile), os.path.join(save_path, sfile))

print(count)

# for file in os.listdir(path):
#     new_name = file[:-8]
#     out_path = os.path.join(save_path, new_name)
#     if not os.path.exists(out_path):
#         os.makedirs(out_path)
#     shutil.move(os.path.join(path, file), os.path.join(out_path, file))
