# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/20 下午8:01
Author: ybx
"""
import os
import csv
import pydicom
import logging
import time

start = time.time()

root_path = "/media/tx-eva-data/yushiyan/基础数据库"
for h_folder in os.listdir(root_path):
    h_folder_path = os.path.join(root_path, h_folder)
    try:
        for b_folder in os.listdir(h_folder_path):
            if b_folder == 'anno' or b_folder.endswith('.txt'):
                continue
            b_folder_path = os.path.join(h_folder_path, b_folder)
            desensitization_path = os.path.join(h_folder_path, b_folder + "_data_clean.log")
            # print(desensitization_path)

            date = b_folder[:10].replace('_', '-')
            os.system('touch %s' % desensitization_path)
            for p_folder in os.listdir(b_folder_path):
                p_folder_path = os.path.join(b_folder_path, p_folder)
                for dcm_file in os.listdir(p_folder_path):
                    dcm_file_path = os.path.join(p_folder_path, dcm_file)
                    info = pydicom.read_file(dcm_file_path, force=True, stop_before_pixels=True)
                    SeriesInstanceUID = info.SeriesInstanceUID
                    StudyInstanceUID = info.StudyInstanceUID
                    SOPInstanceUID = info.SOPInstanceUID
                    pid = p_folder[9:p_folder.rfind('T')-1]
                    original_path = "/" + pid + "/" + StudyInstanceUID + "/" + SeriesInstanceUID + "/" + SOPInstanceUID + ".dcm"
                    dcm_file_name = SOPInstanceUID + ".dcm"
                    filepath = dcm_file_path.replace(b_folder_path, "")
                    #print(filepath)

                    with open(desensitization_path, 'a+') as b:
                        writer = csv.writer(b)
                        writer.writerow(['%s %s\n%s\n' % (date, dcm_file_name, original_path + " >> " + filepath)])
    except:
        print(h_folder_path)


print('programm spend time is: ', (time.time() - start))



