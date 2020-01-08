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

root_path = "/media/tx-eva-data/CE_DR/test/China_internal_data_591/原始数据库/广州中山大学附属第一医院/error"
save_path = '/media/tx-eva-data/CE_DR/test/China_internal_data_591/原始数据库/广州中山大学附属第一医院/tmp'
hosp_name = 'CN010016'
for folders_path, folders, files in os.walk(root_path):
    for dcm_file in files:
        dcm_file_path = os.path.join(folders_path, dcm_file)
        # hosp_name  = dcm_file_path.split('/')[-4]
        # print(hosp_name)
        info = pydicom.read_file(dcm_file_path, force=True)
        instance_number = os.path.split(dcm_file_path)[-1][9:-4]
        # # hosp_file_name = dcm_file_path.split('/')[-2]
        # manufacturer = info.Manufacturer.strip().replace(' ', '')
        #
        # patientid = info.PatientID
        # new_name = hosp_name + '-'+ instance_number
        # study_date = info.StudyDate[:-2]
        # # patientid = info.AccessionNumber.replace(" ", "")
        #
        seriesInstanceUID = info.SeriesInstanceUID.rstrip("\x00")
        studyInstanceUID = info.StudyInstanceUID.rstrip("\x00")
        SOPInstanceUID = info.SOPInstanceUID
        out_path = os.path.join(save_path, instance_number, studyInstanceUID, seriesInstanceUID)
        # print(out_path)
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        # print(os.path.join(out_path, SOPInstanceUID +'.dcm'))
        os.rename(dcm_file_path, os.path.join(out_path, SOPInstanceUID +'.dcm'))




