# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/1 下午4:07
Author: ybx
"""
import pandas as pd
import shutil
import os
import sys
import xlrd




path = '/media/tx-eva-data/Data3/2019-09-02-德化医院/德化县医院/6/2019-09-08_dehuaxianyiyuan_ct_liuyue/dicom'
xls_path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/CE_project/id_list.xlsx'
save_path = "/media/tx-eva-data/Data3/2019-09-02-德化医院/德化县医院/6/2019-09-08_dehuaxianyiyuan_ct_liuyue/save_dcm"

info = pd.read_excel(xls_path,decoding = 'utf-8')
ID = info.Patient_ID

patientList = []
for index,val in enumerate(ID):
    patientList.append(int(val))
for folder in os.listdir(path):
    folder_path = os.path.join(path,folder)
    try:
        if int(folder) in patientList:
            shutil.move(folder_path,save_path)
    except:
        pass



