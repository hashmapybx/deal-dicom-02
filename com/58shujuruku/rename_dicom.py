# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/18 下午4:24
Author: ybx
"""

import os
import time

path = '/media/tx-eva-data/Data1/58server/dcm/2018.03.31_ct_ShangHaiTongJiYiYuan_detection/tmp3/label'
save_path = '/media/tx-eva-data/Data1/58server/dcm/2018.03.31_ct_ShangHaiTongJiYiYuan_detection/tmp3/tmp'
hosp = 'CE021003'
start = time.time()
for file in os.listdir(path):
    a_folder = os.path.join(path, file)
    new_name = hosp + '-' + file[4:file.rfind('T')] + '-' + file[file.rfind('T'):]
    # print(new_name)
    for sfile in os.listdir(a_folder):
        tail_ = sfile[sfile.rfind('_'):]
    # #     # print(tail_)
        instance_name = new_name + tail_
        out_path = os.path.join(save_path, new_name)
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        # print(os.path.join(out_path, instance_name))
        # print(os.path.join(a_folder, sfile))
        os.rename(os.path.join(a_folder, sfile), os.path.join(out_path, instance_name))
print('end time %d ' %(time.time() - start))

