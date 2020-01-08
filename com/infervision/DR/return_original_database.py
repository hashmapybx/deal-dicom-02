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

root_path = "/media/tx-eva-data/CE_DR/train/data_2634/基础数据库"
save_path = '/media/tx-eva-data/CE_DR/train/data_2634/原始数据库'
# hosp_name = 'CN010016'
for folders_path, folders, files in os.walk(root_path):
    for dcm_file in files:
        dcm_file_path = os.path.join(folders_path, dcm_file)
        hosp_name  = dcm_file_path.split('/')[-3]
        info = pydicom.read_file(dcm_file_path, force=True)
        instance_number = os.path.split(dcm_file_path)[-1][9:-4]
        if len(instance_number) < 30:
            new_pid = instance_number
            seriesInstanceUID = info.SeriesInstanceUID.rstrip("\x00")
            studyInstanceUID = info.StudyInstanceUID.rstrip("\x00")
            SOPInstanceUID = info.SOPInstanceUID
            out_path = os.path.join(save_path, hosp_name, new_pid, studyInstanceUID, seriesInstanceUID)
            # print(out_path)
            if not os.path.exists(out_path):
                os.makedirs(out_path)
            # print(os.path.join(out_path, SOPInstanceUID +'.dcm'))
            info.save_as(os.path.join(out_path, SOPInstanceUID +'.dcm'))
        else:
            new_pid = info.PatientID
            seriesInstanceUID = info.SeriesInstanceUID.rstrip("\x00")
            studyInstanceUID = info.StudyInstanceUID.rstrip("\x00")
            SOPInstanceUID = info.SOPInstanceUID
            out_path = os.path.join(save_path, hosp_name, new_pid, studyInstanceUID, seriesInstanceUID)
            # print(out_path)
            if not os.path.exists(out_path):
                os.makedirs(out_path)
            # print(os.path.join(out_path, SOPInstanceUID +'.dcm'))
            info.save_as(os.path.join(out_path, SOPInstanceUID +'.dcm'))

        # # hosp_file_name = dcm_file_path.split('/')[-2]
        # manufacturer = info.Manufacturer.strip().replace(' ', '')
        #
        # patientid = info.PatientID
        # new_name = hosp_name + '_'+ instance_number
        # study_date = info.StudyDate[:-2]
        # # patientid = info.AccessionNumber.replace(" ", "")
        #
        # seriesInstanceUID = info.SeriesInstanceUID.rstrip("\x00")
        # studyInstanceUID = info.StudyInstanceUID.rstrip("\x00")
        # SOPInstanceUID = info.SOPInstanceUID
        # out_path = os.path.join(save_path, patientid)
        # print(out_path)
        # if not os.path.exists(out_path):
        #     os.makedirs(out_path)
        # print(os.path.join(save_path, new_name +'.dcm'))
        # os.rename(dcm_file_path, os.path.join(save_path, new_name +'.dcm'))




