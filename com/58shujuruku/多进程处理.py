

from multiprocessing import JoinableQueue, Process, cpu_count
import time
import os

import pydicom




def dealDicom(dcm_path, out_path):
    instanceNumber = os.path.split(dcm_path)[-1]

    info = pydicom.read_file(dcm_path, force=True)
    info.PatientAddress = 'Anonymized by inferVISION'
    info.ReferringPhysicianName = 'Anonymized by inferVISION'
    info.PatientName = 'Anonymized by inferVISION'

    try:
        info.save_as(os.path.join(out_path, instanceNumber))
        print('finished')
    except:
        print(dcm_path)

def Worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        dealDicom(item[0], item[1])
        q.task_done()

if __name__ == '__main__':

    start = time.time()

    q = JoinableQueue()

    originalDataPath = "/media/tx-eva-data/Data1/58server/dcm/2018.03.31_ct_ShangHaiTongJiYiYuan_detection/tmp1/dicom"
    save_path = os.path.join('/'.join(originalDataPath.split('/')[:-1]), 'tmp_save')
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    cpuCount = cpu_count()

    list_process = []
    for i in range(0, cpuCount):
        process = Process(target=Worker, args=(q,))
        process.daemon = True
        process.start()
        list_process.append(process)

    for dirpath, dirnames, filenames in os.walk(originalDataPath):
        for file in filenames:
            dcm_path = os.path.join(dirpath, file)
            sfile = dcm_path.split('/')[-2]
            out_path = os.path.join(save_path, sfile)
            if not os.path.exists(out_path):
                os.makedirs(out_path)
            q.put([dcm_path, out_path])

    q.join()
    for i in range(0, cpuCount):
        q.put(None)
    for p in list_process:
        p.join()

    elapsed = (time.time() - start)
    print('程序消耗的时间', float(elapsed))  # 133second




