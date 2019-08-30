# -*- coding: utf-8 -*-
"""
Create Time: 2019/8/30 下午4:15
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
            windowCenter = str(info.WindowCenter).strip()
            collectPath = '/' + '/'.join(os.path.split(image_path)[0].split('/')[6:])
            if windowCenter.startswith('['):
                #     # 类似数据['-0020', '-0020'] ['0030','0030']
                windowCenter = windowCenter.split(',')[0][:-1][2:]
                if windowCenter.startswith('-'):
                    # 表示小于0
                    name = 'lungWindows'
                    thickness = info.SliceThickness  # 层厚
                    image_thick = '{:g}'.format(float('%.3f' % thickness))
                    markPurpose = image_thick + 'mm_' + name
                    #
                    t = pd.concat([pd.DataFrame(
                        [lists[0], lists[1], lists[2], lists[3], markPurpose, collectPath, lists[4]]).T])
                    t.columns = df.columns
                    df = pd.concat([df, t], ignore_index=True)
                else:
                    # 表示大于0
                    name = 'Mediastinal'
                    thickness = info.SliceThickness  # 层厚
                    image_thick = '{:g}'.format(float('%.3f' % thickness))
                    markPurpose = image_thick + 'mm_' + name
                    t = pd.concat(
                        [pd.DataFrame(
                            [lists[0], lists[1], lists[2], lists[3], markPurpose, collectPath, lists[4]]).T])
                    t.columns = df.columns
                    df = pd.concat([df, t], ignore_index=True)
            else:
                # 表示是0070 -0060 类似
                # windowCenter = windowCenter.split(',')[0][:-1][2:]
                if windowCenter.startswith('-'):
                    # 表示小于0
                    name = 'lungWindows'
                    thickness = info.SliceThickness  # 层厚
                    image_thick = '{:g}'.format(float('%.3f' % thickness))
                    markPurpose = image_thick + 'mm_' + name

                    t = pd.concat(
                        [pd.DataFrame(
                            [lists[0], lists[1], lists[2], lists[3], markPurpose, collectPath, lists[4]]).T])
                    t.columns = df.columns
                    df = pd.concat([df, t], ignore_index=True)
                else:
                    # 表示大于0
                    name = 'Mediastinal'
                    thickness = info.SliceThickness  # 层厚
                    image_thick = '{:g}'.format(float('%.3f' % thickness))
                    markPurpose = image_thick + 'mm_' + name

                    t = pd.concat(
                        [pd.DataFrame(
                            [lists[0], lists[1], lists[2], lists[3], markPurpose, collectPath, lists[4]]).T])
                    t.columns = df.columns
                    df = pd.concat([df, t], ignore_index=True)
            counter += 1
            break

    print("this total of %s dicom data" % counter)
    df.to_csv(src_path + '/source.csv', index=0)  # index = 0表示不保存索引

if __name__ == '__main__':
    src_path = "/media/tx-eva-data/Data1/tmp/2019_08_30_testData_CS734001/dicom/CS734001/DATA"
    # 先创建一个空的dataframe
    df = pd.DataFrame(
        columns=['hospitalName', 'importDate', 'device', 'project', 'markPurpose', 'collectPath', 'source'])
    hospitalName = "CS734001"
    importDate = str(datetime.datetime.now()).split(' ')[0]
    device = "CT"
    project = "CT_Detection"
    source = "-1"
    lists = [hospitalName, importDate, device, project, source]
    get_csv(src_path, df, lists)
