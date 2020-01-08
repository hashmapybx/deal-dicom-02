# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/7 下午4:10
Author: ybx
"""
import shutil
import os
path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/tmp/dcm'
save_path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/tmp/tmp'
list_a = []

for file in os.listdir(path):
    a_folder = os.path.join(path, file)
    new_file = file[:-4]

    for sfile in os.listdir(a_folder):
        xml_path = os.path.join(a_folder, sfile)
        sfile_name = new_file + '_' +sfile.split('_')[1]
        out_path = os.path.join(save_path, new_file)
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        # print(os.path.join(out_path, sfile_name))
        os.rename(xml_path, os.path.join(out_path, sfile_name))




# path_2 = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/tmp_first_mark/dcm'
#
# count = 0
# for file in os.listdir(path_2):
#     if file in list_a:
#         shutil.move(os.path.join(path_2, file), os.path.join(save_path, file))
#
#
# print(count)
