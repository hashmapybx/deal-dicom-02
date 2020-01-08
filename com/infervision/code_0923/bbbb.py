# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/10 下午9:37
Author: ybx

清洗完的数据添加后缀数据 001 002 003 文件夹和dcm 都需要添加 tail 编号

"""
import os

root_path = "/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/2019-10-29_佛山时人民医院_208/2019-11-07_dicom"

i = 1

id_list = []
for folder_name in os.listdir(root_path):
    id_list.append(folder_name)
id_list.sort()
for folder in id_list:
    print(folder)
    new_number = format(int(i), '03d')
    i += 1
    new_folder = folder + "-" + new_number
    folder_path = os.path.join(root_path, folder)
    for dcm_file in os.listdir(folder_path):
        dcm_file_path = os.path.join(folder_path, dcm_file)
        os.rename(dcm_file_path, os.path.join(folder_path, dcm_file.replace(folder, new_folder)))
    os.rename(folder_path, os.path.join(root_path, folder.replace(folder, new_folder)))






