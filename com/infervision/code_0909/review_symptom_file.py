# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/10 下午9:20
Author: ybx
"""
'''
根据id在excel文件中找对应的症状

'''

import xlrd
import os

def get_symptom():
    excel_path = "/media/tx-eva-data/Data1/dailyFile/zhushi.xlsx"

    boot = xlrd.open_workbook(excel_path)
    table = boot.sheets()[0]
    rows = table.nrows
    print(rows)
    dict = {}
    for row in range(rows):
        dict[table.row_values(row)[0]] = table.row_values(row)[1]
    return dict

def get_archive(dict_a):
    src_path = "/media/tx-eva-data/NAS/new_addData/aaa"
    for file in os.listdir(src_path):
        hosp_path = os.path.join(src_path, file)
        if len(os.listdir(hosp_path)) == 0:
            continue
        else:
            for sfile in os.listdir(hosp_path):
                index = sfile.rfind('-T')
                pid = sfile[9:index]
                for key, value in dict_a.items():
                    if pid in str(key):
                        new_path = os.path.join(hosp_path, value, sfile)
                        try:
                            os.makedirs(new_path)
                        except:
                            pass



if __name__ == '__main__':
    dict_a = get_symptom()
    get_archive(dict_a)



