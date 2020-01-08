# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/12 下午3:50
Author: ybx
"""
import os
import random
path = '/media/tx-eva-data/Data4/2019_09_24_XiaMen_xray/other'
hosp = 'CSX00001'
save_path = '/media/tx-eva-data/Data4/2019_09_24_XiaMen_xray/tmp'
for file in os.listdir(path):
    a_folder = os.path.join(path, file)
    new_folder = hosp +'-'+ file
    for sfile in os.listdir(a_folder):
        new_name = hosp +'-'+file + '-'+str(random.randint(000, 999)).zfill(3)
        out_path = os.path.join(save_path, new_folder)
        print(os.path.join(out_path, new_name + '.dcm'))
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        os.rename(os.path.join(a_folder, sfile), os.path.join(out_path, new_name + '.dcm'))



