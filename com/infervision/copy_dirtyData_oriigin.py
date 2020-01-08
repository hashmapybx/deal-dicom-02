# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/9 下午2:05
Author: ybx
"""
import os
import pydicom
import multiprocessing
import time

'''
for file in os.listdir(src_path):
    sympotm_path = os.path.join(src_path, file)
    for sfile in os.listdir(sympotm_path):
        pid_path = os.path.join(sympotm_path, sfile)
        for tfile in os.listdir(pid_path):
            dcm_path = os.path.join(pid_path, tfile)
            pid = dcm_path.split('/')[-2].split('-')[0]
            new_path = '/'.join(dcm_path.split('/')[6:-2])
            out_path = os.path.join(dec_path, new_path, pid)
            # print(out_path)
            info = pydicom.read_file(dcm_path, force=True)
            studyInstanceUID = info.StudyInstanceUID
            seriesInstanceUID = info.SeriesInstanceUID
            sopInstanceUID = info.SOPInstanceUID
            new_name = os.path.join(studyInstanceUID, seriesInstanceUID)
            save_path = os.path.join(out_path, new_name)
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            info.save_as(os.path.join(save_path, sopInstanceUID + '.dcm'))
            print('finished')
'''

def deal_data(dcm_path, dec_path):
    try:
        pid_index = dcm_path.split('/')[-2].index('-T')
        pid = dcm_path.split('/')[-2][:pid_index]
    except:
        pid = dcm_path.split('/')[-2]
    new_path = '/'.join(dcm_path.split('/')[6:-2])
    out_path = os.path.join(dec_path, new_path, pid)
    # print(out_path)
    info = pydicom.read_file(dcm_path, force=True)
    try:
        studyInstanceUID = info.StudyInstanceUID
    except:
        studyInstanceUID = "info.StudyInstanceUID"

    try:
        seriesInstanceUID = info.SeriesInstanceUID
    except:
        seriesInstanceUID = "info.SeriesInstanceUID"
    try:
        sopInstanceUID = info.SOPInstanceUID
    except:
        sopInstanceUID = "no_sopInstanceUID"
    new_name = os.path.join(studyInstanceUID, seriesInstanceUID)
    save_path = os.path.join(out_path, new_name)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    info.save_as(os.path.join(save_path, sopInstanceUID + '.dcm'))
    print('finished')

def Worker(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        deal_data(item[0], item[1])
        queue.task_done()



if __name__ == '__main__':
    start = time.time()
    src_path = "/media/tx-eva-data/NAS/基础数据库/华中科技大学同济医学院附属同济医院/2017_07_13_abnormal"
    dec_path = "/media/tx-eva-data/NAS/原始数据库/华中科技大学同济医学院附属同济医院"

    queue = multiprocessing.JoinableQueue()
    list_p = []
    for i in range(multiprocessing.cpu_count()-2):
        process = multiprocessing.Process(target=Worker, args=(queue, ))
        process.daemon = True
        process.start()
        list_p.append(process)

    for dirpath, dirnames, filenames in os.walk(src_path):
        for file in filenames:
            dcm_path = os.path.join(dirpath, file)
            queue.put([dcm_path, dec_path])

    queue.join()

    for i in range(multiprocessing.cpuCount() - 2):
        queue.put(None)

    for p in list_p:
        p.join()

    elapsed = time.time() - start
    print('main end! %f' % elapsed)