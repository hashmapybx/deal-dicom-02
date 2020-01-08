# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/12 上午9:57
Author: ybx
"""
import os
import shutil
# path = "/media/tx-eva-data/Data1/tmp/淄博市第一医院测试数据/label/CT/2019-10-12_DATA-444"
# save_path = '/media/tx-eva-data/Data1/tmp/淄博市第一医院测试数据/label/CT/tmp'
# for file in os.listdir(path):
#     hid = file.split('-')[0] + '001'
#     new_file_name = hid +'-'+file.split('-')[1] +'-'+file.split('-')[2]
#     pid_folder = os.path.join(path, file)
#     for sfile in os.listdir(pid_folder):
#         tail = sfile[-8:]
#         new_name = new_file_name + tail
#         new_path = os.path.join(save_path, new_file_name)
#         if not os.path.exists(new_path):
#             os.makedirs(new_path)
#
#         # print(os.path.join(pid_folder, sfile))
#         print(os.path.join(new_path, new_name))
#         os.rename(os.path.join(pid_folder, sfile), os.path.join(new_path, new_name))

path = '/media/tx-eva-data/Data1/download_data_from_S3/data/2019-10-12_DATA-444/dicom'
list_pid = []
for file in os.listdir(path):
    list_pid.append(file)
a_path = '/media/tx-eva-data/Data1/tmp/淄博市第一医院测试数据/dicom/ZBSY001/2019-10-12_DATA-444'
for file in os.listdir(a_path):
    if file not in list_pid:
        print(file)
