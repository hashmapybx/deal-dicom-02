# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/6 上午11:52
Author: ybx
"""

''''
这个程序是用来产生清洗日志的 并且在文件在日志上面加上pid
'''
import os
import time
import sys
import shutil
import logging
import pydicom
from pydicom.tag import TupleTag
from multiprocessing import cpu_count, Process, JoinableQueue

'''
这个脚本是用来修改脱敏日志的 记得要加上对应的版本的日期作为日志的生成时间
'''


def desensitization(filepath, originalDataPath, tuomin_path):
    necessary_tag = [
        (0x0008, 0x0090),  # Referring Physician's Name
        (0x0010, 0x0010),  # Patient's Name
        (0x0010, 0x1040),  # Patient's Address
    ]
    unnecessar_tag = [
        (0x0008, 0x0080),  # Institution Name
        (0x0008, 0x0081),  # Institution Address
        (0x0008, 0x0092),  # Referring Physician Address
        (0x0008, 0x1040),  # Institutional Department Name
        (0x0008, 0x1048),  # Physician(s) of Record
        (0x0008, 0x1050),  # Performing Physician's Name
        (0x0010, 0x2154),  # Patient's Telephone Numbers
        (0x0032, 0x1032),  # Requesting Physician
        (0x0008, 0x0000),  # [Patient's Name]
        (0x0018, 0x1151),

    ]
    # 标签脱敏
    try:
        info = pydicom.read_file(filepath, force=True)
        try:
            if hasattr(info, 'PatientID'):
                ID = str(info.PatientID)
            else:
                ID = str(info.PatientID)
        except:
            if hasattr(info, 'AccessionNumber'):
                ID = str(info.AccessionNumber)
            else:
                ID = str(info.AccessionNumber)
        file_date = filepath.split('/')[6][:10]
        file_name = filepath.split('/')[-1]
        folder_name = filepath.replace(originalDataPath, '')
        folder_name1 = folder_name.replace(file_name, '')
        # folder_path = save_path + folder_name1
        # try:
        #     os.makedirs(folder_path)
        # except OSError:
        #     pass
        for necessary in necessary_tag:
            name = necessary[1]
            tag = TupleTag(necessary)
            try:
                info[tag].value = 'Anonymized by inferVISION '
                # print info[tag].value
            except KeyError:
                if name == 144:
                    info.add_new(0x80090, 'PN', 'Anonymized by inferVISION ')
                if name == 16:
                    info.add_new(0x100010, 'PN', 'Anonymized by inferVISION ')
                if name == 4160:
                    info.add_new(0x101040, 'LO', 'Anonymized by inferVISION ')
        for unnecessar in unnecessar_tag:
            tag = TupleTag(unnecessar)
            info.pop(tag, None)
        print(filepath + "relative information of dicom files have been renamed and cleaned!!!")
        #
        # out_path = os.path.join(folder_path, file_name)
        # try:
        #     st = info.SliceThickness
        try:
            #     info[0x0018,0x1151].value = int(float(info[0x0018,0x1151].value))
            print(file_date)
            # info.save_as(out_path)
        except:
            # 由于源文件file_meta缺失导致文件无法重写保存的原因
            # info.file_meta.MediaStorageSOPClassUID = info.SOPClassUID
            # info.file_meta.MediaStorageSOPInstanceUID = info.SOPInstanceUID
            # info.file_meta.ImplementationClassUID = info.SOPClassUID
            # info.save_as(out_path)
            pass
        # os.system('gdcmconv  -raw %s %s' % (out_path, out_path))
        logging.basicConfig(level=logging.INFO,
                            format='%(message)s',
                            filename=tuomin_path,  # 此处为脱敏日志路径
                            filemode='w')
        # format = '%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
        # datefmt = '%Y-%m-%d %H:%M:%S %p',
        # level = 10
        logging.info('--[%s]-- %s\t%s\t%s\t' % (file_date, ID, '/'.join(filepath.split('/')[4:]), "relative information of dicom files have been renamed and cleaned!!!"))
    except:
        # with open(originalDataPath + '/'+str(i) + '_error.log', 'a+') as errorfile:
        #     print >> errorfile, filepath
        pass

def Worker(tuomin_path):
    while True:
        item = q.get()
        if item is None:
            break
        desensitization( item[0], item[1], tuomin_path)
        q.task_done()


if __name__ == '__main__':

    start = time.time()

    originalDataPath = "/media/tx-eva-data/Data3/aaaa/中日友好"
    cpuCount = cpu_count()  # 计算本机CPU核数
    # save_path = originalDataPath + '_save'#脱敏文件保存路径
    # save_path = originalDataPath + '/'+"_save"
    q = JoinableQueue()
    multiprocessing = []
    for i in range(0, cpuCount - 2):  # 创建cpu_count()个进程
        tuomin_path = originalDataPath + '/'+ str(i) + '_qingxi.log'  # 每个进程打印出一份脱敏日志
        if not os.path.exists(tuomin_path):
            os.system('touch %s' % tuomin_path)
        p = Process(target=Worker, args=(tuomin_path,))
        p.daemon = True
        p.start()
        multiprocessing.append(p)
    for dirpath, dirnames, filenames in os.walk(originalDataPath):
        for file in filenames:
            filepath = os.path.join(dirpath, file)
            pici_time = filepath.split('/')[6][:10]
            q.put([filepath, originalDataPath])
    q.join()
    for i in range(0, cpuCount - 2):
        q.put(None)
    for p in multiprocessing:
        p.join()
    with open(originalDataPath + '/'+pici_time+'_dataClean.log', 'a+') as outfile:
        for i in range(0, cpuCount - 2):
            tuominPath = originalDataPath + '/'+str(i) + '_qingxi.log'
            with open(tuominPath) as infile:
                for line in infile:
                    outfile.write(line)
            os.remove(tuominPath)
    with open(originalDataPath + '/' + '_error.log', 'a+') as errorfile:
        for i in range(0, cpuCount):
            errorPath = originalDataPath + '/'+str(i) + '_error.log'
            try:
                with open(errorPath) as infile:
                    for line in infile:
                        errorfile.write(line)
                os.remove(errorPath)
            except:
                continue
    elapsed = (time.time() - start)
    print(elapsed)
