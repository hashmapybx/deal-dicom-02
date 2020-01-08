# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/18 下午4:55
Author: ybx
"""
import os
import pydicom


root_path = "/media/tx-eva-data/Data4/CE_DATA/Spain/Manchon/2018_12_12_testData/dcm"
save_path = '/media/tx-eva-data/Data4/CE_DATA/Spain/Manchon/2018_12_12_testData/other'

for folders_path, folders, files in os.walk(root_path):
    for dcm_file in files:
        try:
            dcm_file_path = os.path.join(folders_path, dcm_file)
            info = pydicom.read_file(dcm_file_path)
            instance_number = os.path.split(dcm_file_path)[-1]
            hosp_file_name = dcm_file_path.split('/')[-2]
            manufacturer = info.Manufacturer.strip()
            study_date = str(info.SeriesDate)[:-2]

            patientid = info.AccessionNumber.replace(" ", "")
            seriesInstanceUID = info.SeriesInstanceUID.rstrip("\x00")
            studyInstanceUID = info.StudyInstanceUID.rstrip("\x00")
            SOPInstanceUID = info.SOPInstanceUID
            out_path = os.path.join(save_path, manufacturer, study_date, hosp_file_name)
            if not os.path.exists(out_path):
                os.makedirs(out_path)
            print(out_path)
            # info.save_as(dcm_file_path)
            os.rename(dcm_file_path, os.path.join(out_path, instance_number))
        except:
            print(dcm_file)
            pass

