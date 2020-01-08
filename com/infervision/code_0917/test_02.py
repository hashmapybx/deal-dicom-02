# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/17 下午1:14
Author: ybx
"""
'''
这个方法是整理anno的操作
'''

import  os
import shutil
dcm_path = "/media/tx-eva-data/Data1/tmp/2019_09_09_ShengJIng_fracture/dcm"

anno_path =  "/media/tx-eva-data/Data1/tmp/2019_09_09_ShengJIng_fracture/anno"

dict_a = {}
for file in os.listdir(anno_path):
    pid = file[:-8]
    if pid not in dict_a.keys():
        list_a = []
        list_a.append(os.path.join(anno_path, file))
        dict_a[pid] = list_a
    else:
        list_b = dict_a[pid]
        list_b.append(os.path.join(anno_path, file))
        dict_a[pid] = list_b

save_path = "/media/tx-eva-data/Data1/tmp/2019_09_09_ShengJIng_fracture/tmp"

for key, value in dict_a.items():
    new_path = os.path.join(save_path, key)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    for a_path in value:
        shutil.move(a_path, new_path)

