# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/5 下午5:14
Author: ybx
"""
import pydicom
path = '/media/tx-eva-data/CE_DR/test/China_internal_data_591/tmp/956151-20130826.dcm'
info = pydicom.read_file(path)

# info.PatientID = str(int(str(info.PatientID)) - 1)
# info.save_as(path)
print(str(info.PatientID))