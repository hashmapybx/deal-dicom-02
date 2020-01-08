# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/6 下午5:09
Author: ybx
"""
import os


'''
统计这个文件下面各位医院的数据量
'''

dcm_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/lobe/train/2018.01.15/anno"

hosp_dict = {}
for file in os.listdir(dcm_path):
    hosp = file.split('-')[0]
    if hosp not in hosp_dict.keys():
        hosp_dict[hosp] = 1
    else:
        hosp_dict[hosp] = hosp_dict[hosp] + 1

for key in hosp_dict.keys():
    print('医院: %s, 数量: %s' % (key, str(hosp_dict[key])))


