# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/9 下午4:29
Author: ybx
"""

import os
import time
import random

root_path = "/media/tx-eva-data/NAS/基础数据库/肺部计算机辅助诊断软件/CN010008"

for ssfile in os.listdir(root_path):
    if ssfile.endswith('.log'):
        continue
    str_date = ssfile[:10]
    str_year = str_date.split('_')[0]
    str_month = str_date.split('_')[1]
    str_day = str_date.split('_')[2]
    a1 = (int(str_year), int(str_month), int(str_day), 9, 0, 0, 0, 0, 0)
    a2 = (int(str_year), int(str_month), int(str_day), 18, 0, 0, 0, 0, 0)
    start = time.mktime(a1)
    end = time.mktime(a2)
    t = random.randint(start, end)
    date_touple = time.localtime(t)
    # change_date_hm = time.strftime("%Y%m%d%H%M", date_touple)
    change_date_h = time.strftime("%Y%m%d%H", date_touple)
    print(ssfile)
    # change_date_second = time.strftime(".%S", date_touple)
    # change_date_second_1 = str(random.randint(00, 59)).zfill(2)
    h_folder_path = os.path.join(root_path, ssfile)
    for afile in os.listdir(h_folder_path):
        a_folder = os.path.join(h_folder_path, afile)
        for dcm_file in os.listdir(a_folder):
            dcm_file_path = os.path.join(a_folder, dcm_file)
            os.system('touch -mt %s %s' % (
            change_date_h + str(random.randint(00, 59)).zfill(2) + '.' + str(random.randint(00, 59)).zfill(2), dcm_file_path))
        os.system('touch -mt %s %s' % (
        change_date_h + str(random.randint(00, 59)).zfill(2) + '.' + str(random.randint(00, 59)).zfill(2), a_folder))

