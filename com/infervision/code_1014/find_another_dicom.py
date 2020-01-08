# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/14 下午2:21
Author: ybx
"""

import os
import shutil
list_pid = []

path_3 = "/media/tx-eva-data/NAS/标注数据库/交付数据/detection/test/2017_11_16/dcm"
path_4 = '/media/tx-eva-data/NAS/标注数据库/交付数据/detection/test/2018_01_15/dcm'
# fout_1 = open('/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_1014/outer_pid_lobe.txt', 'a')
# fout_2 = open('/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_1014/outer_pid_seg.txt', 'a')
count = 0
for file in os.listdir(path_4):
    list_pid.append(file)

for file in os.listdir(path_3):
    list_pid.append(file)

# path = '/media/tx-eva-data/NAS/标注数据库/交付数据/lobe/test/2018_01_15/dcm'
path_2 = '/media/tx-eva-data/NAS/标注数据库/交付数据/segmentation/test/2018_01_16/dcm'
# save_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/lobe/tmp"
save_path_2 = '/media/tx-eva-data/NAS/标注数据库/交付数据/segmentation/test/2018_01_16/tmp'
# for file in os.listdir(path):
#     if file not in list_pid:
#         shutil.copytree(os.path.join(path, file), os.path.join(save_path, file))



for file in os.listdir(path_2):
    if file not in list_pid:
        shutil.copytree(os.path.join(path_2, file), os.path.join(save_path_2, file))



print(count)

# import xlrd
# def get_hosp_dict():
#     '''
#     根据36家有协议医院name和编号
#     :return: dict_a  返回dict
#     '''
#
#     xls_path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_0915/医院对应编号.xlsx'
#     read_word = xlrd.open_workbook(xls_path)
#     table = read_word.sheets()[0]
#     rows = table.nrows
#     # print(table.nrows)
#     dict_a = {}
#
#     for row in range(rows):
#         hosp_name = table.row_values(row)[0]  # 对excel表里面的36有协议的医院的名称和编号对应起来放到dict里面去
#         hosp_id = table.row_values(row)[1]
#         dict_a[hosp_name] = hosp_id
#
#     return dict_a
#
# def get_hosp_name():
#     dict_a = get_hosp_dict()
#     hosp_id = set()
#     with open('/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_1014/outer_pid.txt', 'r') as fin:
#         for file in fin.readlines():
#             h_id = file.strip().split('-')[0]
#             hosp_id.add(h_id)
#
#     dict_new = {value: key for key, value in dict_a.items()}
#
#     for id in hosp_id:
#         print(dict_new[id])
#
#
#
#
# get_hosp_name()











