# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/18 下午5:57
Author: ybx
"""
import os
import pydicom


root_path = "/media/tx-eva-data/CE_DR/基础数据库/train_data_2634/中国人民解放军陆军军医大学第一附属医院/error_2"
save_path = '/media/tx-eva-data/CE_DR/原始数据库/train_data_2634/清华大学医院/tmp'
hosp = 'CW023007'
for folders_path, folders, files in os.walk(root_path):
    for dcm_file in files:
        dcm_file_path = os.path.join(folders_path, dcm_file)
        info = pydicom.read_file(dcm_file_path, force=True, stop_before_pixels=True)
        instance_number = os.path.split(dcm_file_path)[-1]
        new_name = hosp +'-'+ instance_number
        # hosp_file_name = dcm_file_path.split('/')[-2]
        # manufacturer = info.Manufacturer.strip().replace(' ', '')
        # study_date = info.StudyDate[:-2]
        # patientid = info.AccessionNumber.replace(" ", "")
        # seriesInstanceUID = info.SeriesInstanceUID.rstrip("\x00")
        # studyInstanceUID = info.StudyInstanceUID.rstrip("\x00")
        # SOPInstanceUID = info.SOPInstanceUID
        # out_path = os.path.join(save_path, instance_number,studyInstanceUID, seriesInstanceUID)
        # if not os.path.exists(out_path):
        #     os.makedirs(out_path)
        # print(os.path.join(out_path, SOPInstanceUID + '.dcm'))
        # print(os.path.join(os.path.split(dcm_file_path)[0], new_name))
        os.rename(dcm_file_path, os.path.join(os.path.split(dcm_file_path)[0], new_name))
