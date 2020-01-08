# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/10 上午10:14
Author: ybx
"""

import os
from collections import Counter
a_path = "/media/tx-eva-data/NAS/基础数据库/北京中医药大学东直门医院/TMP/弥漫"
b_path = "/media/tx-eva-data/NAS/原始数据库/北京中医药大学东直门医院/TMP/弥漫"
list_pid = []
for file in os.listdir(b_path):
    list_pid.append(file)

list_a  =[]
for file in os.listdir(a_path):
    pid_index = file.rfind('-T')
    pid = file[:pid_index]
    list_a.append(pid)

b = dict(Counter(list_a))
print([key for key, value in b.items() if value > 1])



# print(list(set(list_pid).difference(set(list_a))))

