# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/15 下午6:14
Author: ybx
"""

import multiprocessing
import os
import time
import random


'''
文件拷贝器 
多进程操作
'''


def copy_file(q, file_name, source_folder_name, dest_folder_name):
    """拷贝文件"""
    # print("正在拷贝文件:%s，%s ==> %s" % (file_name, source_folder_name, dest_folder_name))
    f_read = open(source_folder_name + "/" + file_name, "rb")
    f_write = open(dest_folder_name + "/" + file_name, "wb")

    while True:
        content = f_read.read(1024)
        if content:
            f_write.write(content)
        else:
            break
    f_write.close()
    f_read.close()

    time.sleep(random.random())

    # 放入已经拷贝完成的文件
    q.put(file_name)


def main():
    # 获取要复制的文件夹名称
    source_folder_name = input("请输入要复制的文件夹名称：")

    # 目标文件夹
    dest_folder_name = source_folder_name + "[副本]"

    if not os.path.exists(dest_folder_name):
        os.mkdir(dest_folder_name)

    # 获取文件夹中的所有普通文件名
    file_names = os.listdir(source_folder_name)

    # 创建Queue
    q = multiprocessing.Manager().Queue()

    # 创建pool
    po = multiprocessing.Pool(7)

    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, source_folder_name, dest_folder_name))

    po.close()

    all_file_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        copy_ok_num += 1
        print("\r拷贝的进度为：%.2f%%" % (copy_ok_num * 100 / all_file_num), end="")
        if copy_ok_num >= all_file_num:
            break
    print("")





if __name__ == "__main__":
    start = time.time()
    main()
    end_time = time.time() - start
    print(end_time)





