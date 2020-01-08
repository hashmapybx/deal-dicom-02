# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/16 下午1:25
Author: ybx
"""
from multiprocessing import Pool, JoinableQueue, Process, cpu_count
import time
import datetime
import pandas as pd
import os
import pydicom
import csv

def generate_csv(dcm_dir, csv_path, lists):
    '''
    关于产生.csv文件的内容 的操作
    :param dcm_dir: dcm文件的上一层目录
    :param df:
    :param lists:
    :return:
    '''
    counter = 0
    for file in os.listdir(dcm_dir):
        if file.endswith('.csv'):
            continue
        dcm_path = os.path.join(dcm_dir, file)
        info = pydicom.read_file(dcm_path, force=True,
                                 stop_before_pixels=True)
        windowCenter = str(info.WindowCenter).strip()
        collectPath = '/' + '/'.join(os.path.split(dcm_path)[0].split('/')[-4:])
        if windowCenter.startswith('['):
            #     # 类似数据['-0020', '-0020'] ['0030','0030']
            windowCenter = windowCenter.split(',')[0][:-1][2:]
            if windowCenter.startswith('-'):
                # 表示小于0
                try:
                    name = 'lungWindows'
                    thickness = info.SliceThickness  # 层厚
                    image_thick = '{:g}'.format(float('%.3f' % thickness))
                    markPurpose = image_thick + 'mm_' + name
                except:
                    markPurpose = 'Xray_chest'
                # t = pd.concat([pd.DataFrame(
                #     [lists[0], lists[1], lists[2], lists[3], markPurpose, collectPath, lists[4]]).T])
                # t.columns = df.columns
                # df = pd.concat([df, t], ignore_index=True)
                with open(csv_path, 'a+') as b:
                    writer = csv.writer(b)
                    writer.writerow(
                        [str(lists[0]), str(lists[1]), str(lists[2]), str(lists[3]), markPurpose, collectPath,
                         str(lists[4])])
            else:
                # 表示大于0
                try:
                    name = 'Mediastinal'
                    thickness = info.SliceThickness  # 层厚
                    image_thick = '{:g}'.format(float('%.3f' % thickness))
                    markPurpose = image_thick + 'mm_' + name
                except:
                    markPurpose = 'Xray_chest'
                # t = pd.concat(
                #     [pd.DataFrame(
                #         [lists[0], lists[1], lists[2], lists[3], markPurpose, collectPath, lists[4]]).T])
                # t.columns = df.columns
                # df = pd.concat([df, t], ignore_index=True)
                with open(csv_path, 'a+') as b:
                    writer = csv.writer(b)
                    writer.writerow(
                        [str(lists[0]), str(lists[1]), str(lists[2]), str(lists[3]), markPurpose, collectPath,
                         str(lists[4])])
        else:
            # 表示是0070 -0060 类似
            # windowCenter = windowCenter.split(',')[0][:-1][2:]
            if windowCenter.startswith('-'):
                # 表示小于0
                try:
                    name = 'lungWindows'
                    thickness = info.SliceThickness  # 层厚
                    image_thick = '{:g}'.format(float('%.3f' % thickness))
                    markPurpose = image_thick + 'mm_' + name
                except:
                    markPurpose = 'Xray_chest'
                # t = pd.concat(
                #     [pd.DataFrame(
                #         [lists[0], lists[1], lists[2], lists[3], markPurpose, collectPath, lists[4]]).T])
                # t.columns = df.columns
                # df = pd.concat([df, t], ignore_index=True)
                with open(csv_path, 'a+') as b:
                    writer = csv.writer(b)
                    writer.writerow(
                        [str(lists[0]), str(lists[1]), str(lists[2]), str(lists[3]), markPurpose, collectPath,
                         str(lists[4])])
            else:
                # 表示大于0
                try:
                    name = 'Mediastinal'
                    thickness = info.SliceThickness  # 层厚
                    image_thick = '{:g}'.format(float('%.3f' % thickness))
                    markPurpose = image_thick + 'mm_' + name
                except:
                    markPurpose = 'Xray_chest'
                # t = pd.concat(
                #     [pd.DataFrame(
                #         [lists[0], lists[1], lists[2], lists[3], markPurpose, collectPath, lists[4]]).T])
                # t.columns = df.columns
                # df = pd.concat([df, t], ignore_index=True)
                with open(csv_path, 'a+') as b:
                    writer = csv.writer(b)
                    writer.writerow(
                        [str(lists[0]), str(lists[1]), str(lists[2]), str(lists[3]), markPurpose, collectPath,
                         str(lists[4])])
        counter += 1
        break
    print("this total of %s dicom data" % counter)

    # df.to_csv(src_path + '/source.csv', index=0, mode='a+')  # index = 0表示不保存索引

def Worker(q):
    '''
    item = [image_path, df, lists]
    :param q: 阻塞队列
    :return:
    '''
    while True:
        item = q.get()
        if item is None:
            break
        generate_csv(item[0], item[1], item[2])
        q.task_done()



if __name__ == '__main__':
    start = time.time()
    src_path = "/media/tx-eva-data/Data1/tmp/2019-12-13_hainanyiyuan_71/dicom/CS898001/2019-12-14_DATA-1109"
    # df = pd.DataFrame(
    #     columns=['hospitalName', 'importDate', 'device', 'project', 'markPurpose', 'collectPath', 'source'])
    csv_path = src_path + '/source.csv'
    with open(csv_path, 'w') as a:
        writer = csv.writer(a)
        writer.writerow(['hospitalName', 'importDate', 'device', 'project', 'markPurpose', 'collectPath', 'source'])

    hospitalName = "CS898001"
    importDate = str(datetime.datetime.now()).split(' ')[0]
    device = "CT"
    project = "CT_Chest"
    source = "-1"
    lists = [hospitalName, importDate, device, project, source]
    q = JoinableQueue()
    multiprocessing = []
    for i in range(cpu_count()-2):
        p = Process(target=Worker, args=(q,))
        p.daemon = True
        p.start()
        multiprocessing.append(p)
    for filename in os.listdir(src_path):
        if filename.endswith('.csv'):
            continue
        dcm_dir = os.path.join(src_path, filename)
        q.put([dcm_dir, csv_path, lists])
    q.join()
    for i in range(0, cpu_count() - 2):
        q.put(None)
    for p in multiprocessing:
        p.join()

    print('消耗的时间: ', float(time.time() - start))

