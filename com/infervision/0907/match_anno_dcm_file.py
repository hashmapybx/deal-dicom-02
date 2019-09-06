# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/6 下午4:43
Author: ybx
"""

'''
该脚本是去匹配标注数据库中的anno和dcm 的文件名是否是匹配
'''

import os

anno_path ="/media/tx-eva-data/NAS/标注数据库/交付数据/segmention/train/2018.01.16/anno"
dcm_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/segmention/train/2018.01.16/dcm"
list_pid = []
for file in os.listdir(anno_path):
    list_pid.append(file)
count = 0
list_pid_2 = []


for file in os.listdir(dcm_path):
    # if file not in list_pid:
    #     print(file)
    #     count +=1
    list_pid_2.append(file)


# 两个list求差集 a 中有b 中没有的  或者b中有的a中没有的e

difference = list(set(list_pid_2).difference(set(list_pid)))
print(difference)

#  CE027001-16016489-T125 anno 华中科技大学同济医学院附属同济医院   dcm  CN635001-16016489-T125 聊城市第二人民医院





