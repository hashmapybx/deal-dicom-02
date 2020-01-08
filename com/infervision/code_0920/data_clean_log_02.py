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

root_path = "/media/tx-eva-data/NAS/原始数据库/肺部计算机辅助诊断软件/CE027001/2017_04_20_CE027001_data"
a_name = root_path.split('/')[-1]
a_folder = '/'.join(root_path.split('/')[:-1])
for h_folder in os.listdir(root_path):
    h_folder_path = os.path.join(root_path, h_folder)
    try:
        for b_folder in os.listdir(h_folder_path):
            if b_folder == 'anno' or b_folder.endswith('.txt'):
                continue
            b_folder_path = os.path.join(h_folder_path, b_folder)
            for ttfile in os.listdir(b_folder_path):
                c_folder_path = os.path.join(b_folder_path, ttfile)
                desensitization_path = os.path.join(a_folder, a_name + "_data_desenitional.log")
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
                        pid = dcm_path.split('/')[-4]
                        original_path = "/" + pid + "/" + StudyInstanceUID + "/" + SeriesInstanceUID + "/" + SOPInstanceUID + ".dcm"
                        dcm_file_name = SOPInstanceUID + ".dcm"
                        filepath = dcm_path.replace(root_path, "")
                        # print(filepath)
                        with open(desensitization_path, 'a+') as b:
                            writer = csv.writer(b)
                            # writer.writerow(['%s %s\n%s\n' % (date, dcm_file_name, original_path + " >> " + filepath)])
                            writer.writerow(
                                ['%s %s\n%s\n%s\n' % (date, xx, filepath, "Sensitive information has been removed ")])
                #
                # for p_folder in os.listdir(c_folder_path):
                #     p_folder_path = os.path.join(b_folder_path, p_folder)
                #     for dcm_file in os.listdir(p_folder_path):
                #         dcm_file_path = os.path.join(p_folder_path, dcm_file)

    except:
        print(h_folder_path)


print('programm spend time is: ', (time.time() - start))



