# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/20 下午8:01
Author: ybx
"""
import os
import csv
import pydicom
import logging

root_path = "/media/tx-eva-data/NAS/原始数据库"
# save_path = "/media/tx-eva-data/Data4/CE_DATA/tmp"

for h_folder in os.listdir(root_path):
    h_folder_path = os.path.join(root_path, h_folder)
    try:
        for b_folder in os.listdir(h_folder_path):

            b_folder_path = os.path.join(h_folder_path, b_folder)
            for sfile in os.listdir(b_folder_path):
                dd_folder = os.path.join(b_folder_path, sfile)
                # new_path = os.path.join(save_path, h_folder)
                # if not os.path.exists(new_path):
                #     os.makedirs(new_path)
                desensitization_path = os.path.join(h_folder_path, b_folder + "_data_desenitional.log")
                # print(desensitization_path)

                date = "[ " + '2019-04-01' + " ]"
                os.system('touch %s' % desensitization_path)
                for p_folder in os.listdir(dd_folder):
                    p_folder_path = os.path.join(dd_folder, p_folder)
                    for dcm_file in os.listdir(p_folder_path):
                        p_path = os.path.join(p_folder_path, dcm_file)
                        for xx in os.listdir(p_path):
                            dcm_file_path = os.path.join(p_path, xx)
                            # print(dcm_file_path)
                            info = pydicom.read_file(dcm_file_path, force=True, stop_before_pixels=True)
                            SeriesInstanceUID = info.SeriesInstanceUID
                            StudyInstanceUID = info.StudyInstanceUID
                            SOPInstanceUID = info.SOPInstanceUID
                            pid = dcm_file_path.split('/')[-4]
                            original_path = "/" + pid + "/" + StudyInstanceUID + "/" + SeriesInstanceUID + "/" + SOPInstanceUID + ".dcm"
                            dcm_file_name = SOPInstanceUID + ".dcm"
                            filepath = dcm_file_path.replace(b_folder_path, "")
                            # print(filepath)
                            with open(desensitization_path, 'a+') as b:
                                writer = csv.writer(b)
                                writer.writerow(['%s %s\n%s\n%s\n' %(date,xx,filepath,"Sensitive information has been removed ")])

    except:
        print(h_folder_path)





