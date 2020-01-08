# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/10 上午10:00
Author: ybx
"""
import os
import pydicom
import shutil
import sys
import time

root_path = "/media/tx-eva-data/CE_DR/test/ShenZhenSanYuan_test_data_894/normal_694/dcm"
save_path = '/media/tx-eva-data/CE_DR/test/ShenZhenSanYuan_test_data_894/normal_694/tmp'

for folders_path, folders, files in os.walk(root_path):
    for dcm_file in files:
        dcm_file_path = os.path.join(folders_path, dcm_file)
        info = pydicom.read_file(dcm_file_path, force=True)
        # instance_number = os.path.split(dcm_file_path)[-1]
        # hosp_file_name = dcm_file_path.split('/')[-2]
        # manufacturer = info.Manufacturer.strip()
        patientid = info.PatientID
        print(patientid)
        # study_date = info.StudyDate[:-2]
        # patientid = info.AccessionNumber.replace(" ", "")

        # seriesInstanceUID = info.SeriesInstanceUID.rstrip("\x00")
        # studyInstanceUID = info.StudyInstanceUID.rstrip("\x00")
        # SOPInstanceUID = info.SOPInstanceUID
        out_path = os.path.join(save_path, study_date)
        # if not os.path.exists(out_path):
        #     os.makedirs(out_path)
        # print(out_path)
        # os.rename(dcm_file_path, os.path.join(out_path, ))
        # os.rename(dcm_file_path, os.path.join(out_path, str(SOPInstanceUID.rstrip("\x00")) + ".dcm"))










# 删除文件加下面的空的目录
# #
# for file in os.listdir(root_path):
#     a_folder = os.path.join(root_path, file)
#
#     for sfile in os.listdir(a_folder):
#         b_folder = os.path.join(a_folder, sfile)
#
#         if len(os.listdir(b_folder)) == 0:
#             # print(b_folder)
#             os.system('rm -rf %s' % a_folder)

