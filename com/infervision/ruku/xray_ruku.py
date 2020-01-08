# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/11 下午6:10
Author: ybx
"""
import os
import re
import pandas as pd
import time
import datetime
import pydicom

"""
WindowCenter >0 Mediastinal <0 lungWindows
"""


def get_csv(src_path, df, lists):
    counter = 0
    for filename in os.listdir(src_path):
        for dcm in os.listdir(os.path.join(src_path, filename)):
            image_path = os.path.join(os.path.join(src_path, filename), dcm)
            info = pydicom.read_file(image_path, force=True,
                                     stop_before_pixels=False)
            collectPath = '/' + '/'.join(os.path.split(image_path)[0].split('/')[6:])
            try:
                name = 'lungWindows'
                thickness = info.SliceThickness  # 层厚
                image_thick = '{:g}'.format(float('%.3f' % thickness))
                markPurpose = image_thick + 'mm_' + name
            except:
                markPurpose = 'Xray_chest'
            #
            t = pd.concat([pd.DataFrame(
                [lists[0], lists[1], lists[2], lists[3], markPurpose, collectPath, lists[4]]).T])
            t.columns = df.columns
            df = pd.concat([df, t], ignore_index=True)
            counter += 1
            break

    print("this total of %s dicom data" % counter)
    df.to_csv(src_path + '/source.csv', index=0)  # index = 0表示不保存索引

if __name__ == '__main__':

    src_path = "/media/tx-eva-data/Data2/Xray/XiaMen/2019_09_24_XiaMen_xray/tmp/dicom"
    # 先创建一个空的dataframe
    df = pd.DataFrame(
        columns=['hospitalName', 'importDate', 'device', 'project', 'markPurpose', 'collectPath', 'source'])
    hospitalName = "xiamen"
    importDate = str(datetime.datetime.now()).split(' ')[0]
    device = "Xray"
    project = "Xray_Chest"
    source = "-1"
    lists = [hospitalName, importDate, device, project, source]
    get_csv(src_path, df, lists)
