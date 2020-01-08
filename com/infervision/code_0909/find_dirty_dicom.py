# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/10 下午8:32
Author: ybx
"""


import os



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

    # print('a: %d' % len(list_pid_a))
    # print( 'b: %d' %len(list_pid_b))
    # print('c: %d'%len(list_pid_c))
    # print('d: %d' % len(list_pid_d))
    return list_pid_a+ list_pid_b + list_pid_c + list_pid_d


def get_test():
    src_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/detection/test"
    list_id = []
    for file in os.listdir(src_path):
        a_path = os.path.join(src_path, file)
        for sfile in os.listdir(a_path):
            if sfile == 'dcm':
                for tfile in os.listdir(os.path.join(a_path, sfile)):
                    list_id.append(tfile)
    return list_id



def get_a():
    src_path = "/media/tx-eva-data/NAS/基础数据库/首都医科大学附属北京潞河医院"
    list_a = []
    for file in os.listdir(src_path):
        if file == 'TMP':
            continue
        else:
            for sfile in os.listdir(os.path.join(src_path, file)):
                list_a.append(sfile)

    return list_a

if __name__ == '__main__':
    path = '/media/tx-eva-data/NAS/new_addData/aaa/首都医科大学附属北京潞河医院'
    if not os.path.exists(path):
        os.makedirs(path)
    list_a = get_markData()
    # print(len(list_a))
    list_b = get_test()
    list_all = list_a + list_b
    count = 0
    list_hosp = get_a()
    print(len(list_hosp))
    for id in list_hosp:
        if id not in list_all:
            os.system('mkdir %s' % (os.path.join(path, id)))
            # print(id)
            # count += 1

    # print(count)