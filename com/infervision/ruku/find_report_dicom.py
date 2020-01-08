# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/17 下午4:04
Author: ybx
"""

import os
import pydicom
path = '/media/tx-eva-data/Data4/河南/2019-11-01_中平能化医疗总院_105/CT/dicom/CN375002/2019-12-17_DATA-11'

for file in os.listdir(path):
    a_folder = os.path.join(path, file)
    for sfile in os.listdir(a_folder):
        dcm_path = os.path.join(a_folder, sfile)
        info = pydicom.read_file(dcm_path, force=True, stop_before_pixels=True)
        patientId = info.PatientID
        accessionNumber = info.accessionNumber
        print('patientID: %s, accessionNumber: %s' % (patientId, accessionNumber))
        break