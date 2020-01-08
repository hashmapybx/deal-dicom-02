# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/20 下午4:35
Author: ybx
"""

import os


def get_id():
    src_path = "/media/tx-eva-data/NAS/基础数据库/青海省人民医院/2017_03_15_CW971001_data"
    list_a = []
    for file in os.listdir(src_path):
        list_a.append(file)

    return list_a


def get_markData():
    '''
    该方法先是获取到对应项目的标注数据的 这里是detection的train
    :return:
    '''
    src_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/detection/train"
    list_pid_a = []  # detection 2.0 第一批的pid
    list_pid_b = []  # detection 2.0 第二批的pid
    list_pid_c = []  # detection 2.1 第一批的pid
    list_pid_d = []  # detection 2.1 第二批pid

    for version in os.listdir(src_path):  # 2.0 2.1
        for sfile in os.listdir(os.path.join(src_path, version)):
            if sfile == '2017_11_16':
                pici_path = os.path.join(os.path.join(src_path, version), sfile)
                for tfile in os.listdir(pici_path):
                    if tfile == "anno":
                        anno_path = os.path.join(pici_path, tfile)
                        for anno_name in os.listdir(anno_path):
                            # 这里想到一个问题 标注数据库中的dcm 和anno必须是匹配的要不然就比较麻烦了 先写程序匹配一下
                            list_pid_a.append(anno_name)
            elif sfile == '2018_01_15':
                pici_path = os.path.join(os.path.join(src_path, version), sfile)
                for tfile in os.listdir(pici_path):
                    if tfile == "anno":
                        anno_path = os.path.join(pici_path, tfile)
                        for anno_name in os.listdir(anno_path):
                            list_pid_b.append(anno_name)
            elif sfile == '2018_07_15':
                pici_path = os.path.join(os.path.join(src_path, version), sfile)
                for tfile in os.listdir(pici_path):
                    if tfile == "anno":
                        anno_path = os.path.join(pici_path, tfile)
                        for anno_name in os.listdir(anno_path):
                            list_pid_c.append(anno_name)
            else:
                pici_path = os.path.join(os.path.join(src_path, version), sfile)
                for tfile in os.listdir(pici_path):
                    if tfile == "anno":
                        anno_path = os.path.join(pici_path, tfile)
                        for anno_name in os.listdir(anno_path):
                            list_pid_d.append(anno_name)

    return list_pid_a + list_pid_b + list_pid_c + list_pid_d


if __name__ == '__main__':

    list_1 = get_markData()
    list_2 = get_id()
    count = 0
    list_3 = []
    for id in list_1:
        if 'CW971001' in id:
            list_3.append(id)
    count = 0
    for id in list_3:
        if id not in list_2:
            print(id)
            count +=1
    print(count)


