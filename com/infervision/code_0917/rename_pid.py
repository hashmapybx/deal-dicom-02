# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/18 下午9:50
Author: ybx
"""

'''
这个脚本的代码是去修改注释量的pid 在report.txt 文件中的pid加上医院编号

'''
import xlrd

def get_hosp_dict():

    '''
    根据36家有协议医院name和编号
    :return: dict_a  返回dict
    '''
    xls_path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_0907/医院对应编号.xlsx'
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


def write_txt(path):
    file = open(path, 'a+', encoding='utf-8')
    dict_a = get_hosp_dict()
    with open('/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_0917/report.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            hosp_name = line.split('|')[0]
            symptom = line.split('|')[1]
            pid = dict_a[hosp_name]+"-"+line.split('|')[2]
            new_line = hosp_name+'|'+symptom+'|'+pid
            file.write(new_line + '\n')

    file.close()


if __name__ == '__main__':
    path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_0917/new_report.txt'
    write_txt(path)