# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/5 下午6:52
Author: ybx
"""
import os
import shutil
path_1 = "/media/tx-eva-data/Data3/bejiingdaxueshenzhenfushuyiyuan/test_data/bdsz_test_data_save/CT/1mm"
path_2 = "/media/tx-eva-data/Data3/bejiingdaxueshenzhenfushuyiyuan/test_data/bdsz_test_data_save/CT/dicom"
# save_path = path_2 + '_save'
for file in os.listdir(path_2):
    pid_folder = os.path.join(path_2, file)
    for sfile in os.listdir(pid_folder):
        ser_folder = os.path.join(pid_folder, sfile)
        # print(ser_folder)
        if os.path.isdir(ser_folder):
            try:
                os.system('rm -rf %s' % ser_folder)
            except:
                pass
#
# list_1 = []
#
# for file in os.listdir(path_1):
#     list_1.append(file)
#
# count = 0
# for sfile in os.listdir(path_2):
#     if sfile not in list_1:
#         print(sfile)
#         count += 1
#
#
# print(count)


