# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/7 下午9:31
Author: ybx
"""

'''
 去掉数据命名的尾巴 tail
'''

import os
import random
import shutil
path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/2019_11_13_testData/label'
# list_a = []
# for file in os.listdir(path):
#     list_a.append(file)
save_path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/2019_11_13_testData/tmp'
# path_1 = '/media/tx-eva-data/Data4/nanhuaDaxue/2019_10_18_NanHuaFuEr_fracture/2019-11-13_DATA-485_test/label/CT/2019-11-11_DATA-485'
# for file in os.listdir(path_1):
#     if file in list_a:
#         shutil.move(os.path.join(path_1, file), os.path.join(save_path, file))
# save_path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/bbb'
for file in os.listdir(path):
    new_file = file[:-4]
    a_folder = os.path.join(path, file)
    for sfile in os.listdir(a_folder):
        dcm_path = os.path.join(a_folder, sfile)
        dcm_name = new_file + '_'+ sfile.split('_')[1]
        out_path = os.path.join(save_path, new_file)
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        # print(os.path.join(out_path, dcm_name))
        os.rename(dcm_path, os.path.join(out_path, dcm_name))