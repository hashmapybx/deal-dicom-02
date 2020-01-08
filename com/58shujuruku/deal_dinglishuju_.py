# -*- coding: utf-8 -*-
"""
Create Time: 2020/1/6 下午6:41
Author: ybx
"""
'''
该程序的目的是处理病例的文本数据
按照标点符号来切分词语 
首先是按照中文里面的！ 。来切分句子
'''

def spilt_sentence(path, punctuation_list='!?。！？'):
    sentence_set = []
    inx_position = 0  # 索引标点符号的位置
    char_position = 0  # 移动字符指针位置
    with open(path, 'r') as fin:
        text = fin.read()
    for char in text:

        if char in punctuation_list:
            next_char = list(text[inx_position:char_position + 1]).pop()
            if next_char not in punctuation_list:
                sentence_set.append(text[inx_position:char_position])
                inx_position = char_position
    if inx_position < len(text):
        sentence_set.append(text[inx_position:])

    res = [vv for vv in sentence_set if len(vv) >1]

    return res








if __name__ == '__main__':
    path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/58shujuruku/bingli.txt'
    res = spilt_sentence(path)
    print(res)