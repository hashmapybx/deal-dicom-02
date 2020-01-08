# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/6 下午9:02
Author: ybx
"""

import os
import csv
import pydicom
import logging
import time

start = time.time()

root_path = "/media/tx-eva-data/NAS/基础数据库/肺部计算机辅助诊断软件/CN635001/2017_06_05_CN635001_data"
try:
    for ttfile in os.listdir(root_path):
        b_name = root_path.split('/')[-1]
        a_path = '/'.join(root_path.split('/')[:-1])
        c_folder_path = os.path.join(root_path, ttfile)
        desensitization_path = os.path.join(a_path, b_name + "_data_clean.log")
        # print(desensitization_path)
        date =  "[ " + b_name[:10] + " ]"
        os.system('touch %s' % desensitization_path)
        for dirpath, dirnames, filenames in os.walk(c_folder_path):
            for filename in filenames:
                dcm_path = os.path.join(dirpath, filename)
                info = pydicom.read_file(dcm_path, force=True, stop_before_pixels=True)
                xx = os.path.split(dcm_path)[-1]
                SeriesInstanceUID = info.SeriesInstanceUID
                StudyInstanceUID = info.StudyInstanceUID
                SOPInstanceUID = info.SOPInstanceUID
                pid = dcm_path.split('/')[-2][9:-5]
                original_path = "/" + pid + "/" + StudyInstanceUID + "/" + SeriesInstanceUID + "/" + SOPInstanceUID + ".dcm"
                dcm_file_name = SOPInstanceUID + ".dcm"
                filepath = dcm_path.replace(root_path, "")
                # print(filepath)
                with open(desensitization_path, 'a+') as b:
                    writer = csv.writer(b)
                    writer.writerow(['%s %s\n%s\n' % (date, dcm_file_name, original_path + " >> " + filepath)])
                    # writer.writerow(


except:
    print(c_folder_path)


print('programm spend time is: ', (time.time() - start))




