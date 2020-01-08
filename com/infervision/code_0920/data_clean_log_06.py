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

root_path = "/media/tx-eva-data/DR/基础数据库/Computer-Aided-Diagnostic-Software/europe_PublicTest/2019-10-24_europe_data"
a_name = root_path.split('/')[-1]
a_folder = '/'.join(root_path.split('/')[:-1])

try:

    for ttfile in os.listdir(root_path):
        c_folder_path = os.path.join(root_path, ttfile)
        desensitization_path = os.path.join(a_folder, a_name + "_data_clean.log")
        # print(desensitization_path)
        date =  "[ " + a_name[:10] + " ]"
        os.system('touch %s' % desensitization_path)
        for dirpath, dirnames, filenames in os.walk(c_folder_path):
            for filename in filenames:
                dcm_path = os.path.join(dirpath, filename)
                info = pydicom.read_file(dcm_path, force=True, stop_before_pixels=True)
                xx = os.path.split(dcm_path)[-1]
                SeriesInstanceUID = info.SeriesInstanceUID
                StudyInstanceUID = info.StudyInstanceUID
                SOPInstanceUID = info.SOPInstanceUID
                pid = ttfile
                original_path = "/" + pid + "/" + StudyInstanceUID + "/" + SeriesInstanceUID + "/" + SOPInstanceUID + ".dcm"
                dcm_file_name = SOPInstanceUID + ".dcm"
                filepath = dcm_path.replace(c_folder_path, "")
                # print(filepath)
                with open(desensitization_path, 'a+') as b:
                    writer = csv.writer(b)
                    writer.writerow(['%s %s\n%s\n' % (date, dcm_file_name, original_path + " >> " + filepath)])

except:
    print(c_folder_path)


print('programm spend time is: ', (time.time() - start))




