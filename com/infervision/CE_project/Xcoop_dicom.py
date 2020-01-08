# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/4 下午4:07
Author: ybx
"""

import os
# path = '/media/tx-eva-data/Data4/CE_DATA/原始数据库/XCoop/dcm'
# list_pid = []
#
# for file in os.listdir(path):
#     list_pid.append(file)

path_1 = '/media/tx-eva-data/Data4/CE_DATA/基础数据库/XCoop/dcm'

list_pid = set()
for sfile in os.listdir(path_1):
    pid = sfile.split('-')[1]
    list_pid.add(pid)





print(len(list_pid))