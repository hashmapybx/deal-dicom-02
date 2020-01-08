# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/15 下午3:49
Author: ybx
"""
'''
这个程序是用来生成脱落记录表的
'''

import os
import xlrd, xlwt, xlutils
import math
import random

list_tmp_pid = []  # 保存从每家医读取到pid  以经使用过的


def get_file(src_path):
    '''
    逻辑是先读取detection train 的标注记录拆分的小表
    按照月的时间段来读取 并且把这个月的pid放到一个list里面  比如这个月的数据量是300 那么就去按照120的总量的六分之五去分配 100这个的数据
    然后六分之一的烂肺多发的数据需要去到tmp文件夹下面去读取的操作
    :param src_path:
    :return:
    '''

    list_date_file = []  # 保存的就是,每一个excel的绝对路径
    list_month = []
    dict_a = {}
    for file in os.listdir(src_path):
        # 这里需要注意的是key相同的话会覆盖操作的
        list_date_file.append(os.path.join(src_path, file))
    # 对于dict的key日期进行排序的操作 升序排序操作
    list_date_file_sorted = sorted(list_date_file)
    count = 0
    for key in list_date_file_sorted:
        # print(key, list_date_file[key])
        # 按月来划分数据操作
        key_new = os.path.split(key)[-1]
        # 这里是找到2017的数据库
        file_date = key_new[:7]
        if file_date not in dict_a.keys():
            list_a = []
            list_a.append(key)
            dict_a[file_date] = list_a
        else:
            list_b = dict_a[file_date]
            list_b.append(key)
            dict_a[file_date] = list_b
    for key, value in dict_a.items():
        # 每一个key表示的是一个月现在把每一个月的数据去处理
        deal_month_excel(key, value)
    #
    # # 把list_tmp_pid 的内容写到一个文件里面
    # file = open('/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_0915/pid.txt', 'w', encoding='utf-8')
    # for pid in list_tmp_pid:
    #     file.write(pid+'\n')
    # file.close()


def deal_month_excel(mark_date, list_a):
    '''
    这个方法是去处理对应的每一个月份的所有的标注记录表的操作 把每一个table 里面的pid 放到list里面
    把这个list的全部id需要拆分到小的excel 表里面其中每一个excel 保存100+ [10-30]个tmp文件的数据
    :param list_a: 标注的同一个月的excel文件的绝对路径
    :param mark_date: 这个参数是标注数据对应的月份 在最后保存脱落记录的时候需要使用
    :return:
    '''

    # base_path = "/media/tx-eva-data/NAS/基础数据库"
    list_pid = []  # 保存一个月的所有的pid

    for excel_path in list_a:
        table = xlrd.open_workbook(excel_path)
        sheet1 = table.sheets()[0]
        rows = sheet1.nrows
        for row in range(0, rows):
            if row == 0:
                # 跳过表的表头
                continue
            else:
                list_pid.append(sheet1.row_values(row)[4])  # pid
    print(len(list_pid))  # 打印每一个月的标记的pid数量

    dict_pid = {}
    # 这里需要把每个月的pid 按医院分开
    for key in list_pid:
        h_id = key[:8]
        if h_id not in dict_pid.keys():
            list_a = []
            list_a.append(key)
            dict_pid[h_id] = list_a
        else:
            list_b = dict_pid[h_id]
            list_b.append(key)
            dict_pid[h_id] = list_b

    if 'CN010001' in dict_pid:
        dict_pid.pop('CN010001')
    # 这个dict里面的key是对应的医院编号 value是这家医院的pid
    for key, value_list in dict_pid.items():

        pici = math.ceil(len(value_list) / 100)
        # 进行分数据的操作  比如说4月份标注了300例 那么这个300 里面需要分到多个excel表里面
        i = 0
        while pici > 0:
            workboot = xlwt.Workbook()  # 每次写的时候创建一个新的xlwt的对象
            sheet2 = workboot.add_sheet('sheet1', cell_overwrite_ok=True)
            new_clo = ['日期', 'PID', '检查医生', '检查结果']  # 新表格的列的title
            for col_name in range(len(new_clo)):
                sheet2.write(0, col_name, new_clo[col_name], set_style_1('宋体', 230, True))  # 写进表格里面去
            # 0-100 100-200 (i*100 - (i+1)* 100
            list_row_data = []  # 用来保存每行数据 在xieru excel 的时候是按照行来写数据的
            # list_hosp_id = set()  # 用来保存截取的100例数据中的医院编号
            for value in value_list[i * 100: (i + 1) * 100]:
                # list_hosp_id.add(value[:8])  # 把写入的数据的医院编号提取出来 放到set
                list_row_data.append(['', value, '', '通过'])
            # 再加上一个tmp文件的数据量[10,30] 的数据量 需要定义全局变量list 来保存每次用过的tmp的pid
            # 去到set对应的医院去读取tmp文件 返回tmp -->  key: pid value:symptom 的 dict

            dict_a = get_hosp_dict()
            # dict_a.pop('西安交通大学第一附属医院')
            dict_b = {k: v for v, k in dict_a.items()}  # dict的key value 互换位置
            # if 'CW029003' in dict_b:
            #     dict_b.pop('CW029003')
            hosp_Name = dict_b[key]

            d_a = get_hosp_tmp(hosp_Name)

            bb = list(d_a.keys())
            random.shuffle(bb)
            # 从每次获取的的tmp dict 的key的list里面去重
            # 去除上次已经用过的pid
            # for name_pid in list_tmp_pid:
            #     # 这个list记录的已经用过的pid
            #     if name_pid in bb:
            #         bb.remove(name_pid)
            # 再从去除已经用过的list里面截取新的数据
            list_new_pid = bb[:random.randint(15, 26)]  # 对于脱落数据量是120六分之一在上下波动+-5
            for ppid in list_new_pid:
                list_row_data.append(['', ppid, '', d_a[ppid]])
                list_tmp_pid.append(ppid)

            # 开始把每一行的数据写入到excel里面
            for a in range(0, len(list_row_data)):
                for b in range(0, len(list_row_data[a])):
                    sheet2.write(a + 1, b, list_row_data[a][b],
                                 set_style_1('Times New Roman', 205, False) if b == 1 else set_style_1('宋体', 205, False))

            file_name = mark_date + '_' + hosp_Name + '_'+str(i)  # file
            workboot.save("/media/tx-eva-data/Data1/CFDA_file/数据标注/detection/new_train/shed_table/华中科技大学_第三批/%s.xls" % file_name)
            i += 1
            pici -= 1


# TODO 设置表格样式
def set_style_1(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    align = xlwt.Alignment()
    align.horz = 0x02  # 设置水平居中
    align.vert = 0x01  # 设置垂直居中
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    style.alignment = align
    return style


def get_hosp_tmp(hosp_name):
    dict_a = {}
    with open('/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_0917/new_report.txt', 'r',
              encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            hos_name = line.split('|')[0]
            symptom = line.split('|')[1]
            pid = line.split('|')[2]
            if hosp_name == hos_name:
                dict_a[pid] = symptom

    return dict_a


def get_tmp_data(hosp_path):
    '''
    :param hosp_path: 医院的TMP文件的绝对路径
    :return dict_sym: 表示的是 对应的pid 所属的症状 弥漫 多发等等
    '''
    dict_sym = {}

    for symptom_file in os.listdir(hosp_path):
        symptom_path = os.path.join(hosp_path, symptom_file)
        for sfile in os.listdir(symptom_path):
            dict_sym[sfile] = symptom_file

    return dict_sym


def get_hosp_dict():
    '''
    根据36家有协议医院name和编号
    :return: dict_a  返回dict
    '''

    xls_path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_0915/医院对应编号.xlsx'
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
    src_path = "/media/tx-eva-data/Data1/CFDA_file/数据标注/detection/new_train/华中科技大学_第三批"
    get_file(src_path)
