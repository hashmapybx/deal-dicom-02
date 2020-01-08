# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/18 下午5:42
Author: ybx
"""

import os
import pydicom


root_path = "/media/tx-eva-data/Data4/CE_DATA/Spain/ParcTauliHospital/2018_10_25_ParcTauliHospital/dcm"
save_path = '/media/tx-eva-data/Data4/CE_DATA/Spain/ParcTauliHospital/2018_10_25_ParcTauliHospital/other'

for folders_path, folders, files in os.walk(root_path):
    for dcm_file in files:
        dcm_file_path = os.path.join(folders_path, dcm_file)
        info = pydicom.read_file(dcm_file_path, force=True, stop_before_pixels=True)
        instance_number = os.path.split(dcm_file_path)[-1]
        hosp_file_name = dcm_file_path.split('/')[-2]
        manufacturer = info.Manufacturer.strip()
        study_date = info.StudyDate
        patientid = info.AccessionNumber.replace(" ", "")
        # seriesInstanceUID = info.SeriesInstanceUID.rstrip("\x00")
        # studyInstanceUID = info.StudyInstanceUID.rstrip("\x00")
        # SOPInstanceUID = info.SOPInstanceUID
        out_path = os.path.join(save_path, study_date, manufacturer, hosp_file_name)
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        # print(out_path)
        os.rename(dcm_file_path, os.path.join(out_path, instance_number))