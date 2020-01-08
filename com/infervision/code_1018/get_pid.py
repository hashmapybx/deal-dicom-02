# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/30 上午11:40
Author: ybx
"""

'''
CE的相关文件代码
'''
import os
path = '/media/tx-eva-data/Data4/CE_DATA/标注数据库/detection/dcm'
fout = open('/media/tx-eva-data/Data4/CE_DATA/CE_三四级文件/数据脱落记录/tmp.txt', 'a+')
count =0
for file in os.listdir(path):
    fout.write(file + '\n')
    count += 1
fout.close()
print(count)


