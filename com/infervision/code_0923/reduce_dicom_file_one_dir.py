# # -*- coding: utf-8 -*-
# """
# Create Time: 2019/9/23 下午6:31
# Author: ybx
# """
# '''
# 把dicom的路径往上提一层
# '''
import os
import shutil

'''
将清洗后的dicom文件的目录往上提一层
'''


#
# # # # #

def reduce_dir(dcm_path):
    for dirpath, dirname, filenames in os.walk(dcm_path):
        for filename in filenames:
            dcm_path = os.path.join(dirpath, filename)
            # print(dcm_path)
            new_path = '/'.join(dcm_path.split('/')[:-2])
            instance_number = os.path.split(dcm_path)[-1]
            # print(os.path.join(new_path, instance_number))
            shutil.move(dcm_path, os.path.join(new_path, instance_number))


def delete_dir(dcm_path):
    for sfile in os.listdir(dcm_path):
        b_path = os.path.join(dcm_path, sfile)
        for tfile in os.listdir(b_path):
            c_path = os.path.join(b_path, tfile)
            if os.path.isdir(c_path):
                os.system('rm -rf %s' % c_path)




if __name__ == '__main__':
    dcm_path = "/media/tx-eva-data/Data4/河南/2019-11-01_中平能化医疗总院_105/CT/1.25mm"
    # reduce_dir(dcm_path)
    delete_dir(dcm_path)
