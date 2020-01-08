# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/10 上午11:01
Author: ybx
"""
import os
import xlrd
src_path = "/media/tx-eva-data/NAS/new_addData/tmp1"

dcom_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/detection/test/2017_11_16/dcm"

def get_miss_data():
    count = 0
    hosp_dict = get_hosp_dict()
    dict_new = {value: key for key, value in hosp_dict.items()}
    for file in os.listdir(src_path):
        hosp_name = dict_new[file]
        a = os.path.join(src_path, file)
        for sfile in os.listdir(a):
            count = count + len(os.listdir(os.path.join(a, sfile)))
        print(hosp_name, count)
        count = 0


def get_hosp_dict():
    '''
    根据36家有协议医院name和编号
    :return: dict_a  返回dict
    '''
    xls_path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/0907/医院对应编号.xlsx'
    read_word = xlrd.open_workbook(xls_path)
    table = read_word.sheets()[0]
    rows = table.nrows
    # print(table.nrows)
    dict_a = {}
    for row in range(rows):
        hosp_name = table.row_values(row)[0]  # 对excel表里面的36有协议的医院的名称和编号对应起来放到dict里面去
        hosp_id = table.row_values(row)[1]
        dict_a[hosp_name] = hosp_id
    return dict_a


if __name__ == '__main__':
    get_miss_data()