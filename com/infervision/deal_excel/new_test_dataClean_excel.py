#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4/0004 22:00
# @Author  : Mat

import xlrd
import xlwt
import re
from xlutils.copy import copy
from xlrd import xldate_as_tuple
import datetime
# 创建workboot对象

'''
这个脚本是用来拆分数据清洗表格 脱敏记录表格的 

'''


def write_excel():
    list_0 = []
    list_1 = []
    list_2 = []
    list_3 =[]

    list_date = {}
    data = xlrd.open_workbook("/media/tx-eva-data/Data1/dailyFile/数据清洗记录copy.xlsx")
    # 获取每一个sheet的name?
    table = data.sheets()[0]  # 第一张表
    print(type(table))
    rows = table.nrows

    for i in range(rows):
        workboot = xlwt.Workbook() #每次写的时候创建一个新的xlwt的对象
        sheet1 = workboot.add_sheet('sheet1', cell_overwrite_ok=True)
        if i == 0:
            print(table.row_values(i))
            list_0 = table.row_values(i)
        elif i == 1:
            print(table.row_values(i))
            list_1 = table.row_values(i)
        elif i == 2:
            print(table.row_values(i))
            list_2 = table.row_values(i)
        elif i == 3:
            print(table.row_values(i))
            list_3 = table.row_values(i)
        else:
            try:
                date_i = table.row_values(i)[3]
                # 转成datetime对象
                date = datetime.datetime(*xldate_as_tuple(date_i, 0))
                date_i = date.strftime('%Y-%m-%d')
            except:
                pass
            if re.match('^\d\-*', date_i):
                if date_i not in list_date:
                    # 表示在前面没有出现过
                    list_date[date_i] = 1
                    #开始写入数据 前面4行书表头
                    for a in range(0, len(list_0)):
                        sheet1.write(0, a, str(list_0[a])[-10:], set_style_1('宋体', 400, False))
                    for a in range(0, len(list_1)):
                        sheet1.write(1, a, list_1[a].strip(), set_style_2('Time New Roman', 205, False))
                    for a in range(0, len(list_2)):
                        sheet1.write(2, a, list_2[a].strip(), set_style_1('宋体', 205, False))
                    for a in range(0, len(list_3)):
                        sheet1.write(3, a, list_3[a].strip(), set_style_1('宋体', 205, False))
                    for a in range(0, len(table.row_values(i))):
                        sheet1.write(4, a, datetime.datetime(*xldate_as_tuple(table.row_values(i)[a], 0)).strftime('%Y-%m-%d') if a == 3 else  table.row_values(i)[a], set_style_1('Times New Roman', 205, False) if a ==3 else set_style_1('宋体', 205, False))
                        # datetime.datetime(*xldate_as_tuple(table.row_values(i)[a], 0))
                    sheet1.merge(0, 0, 0, 9)
                    sheet1.merge(1, 1, 0, 9)
                    sheet1.merge(2, 2, 0, 9)
                    sheet1.write(10, 5, '记录人签字', set_style_1('宋体', 205, False))
                    sheet1.write(10, 6, '钏兴炳', set_style_1('宋体', 205, False))
                    sheet1.write(10, 7, '日期', set_style_1('宋体', 205, False))
                    sheet1.write(10, 8,  deal_date(date_i), set_style_2('Times New Roman', 205, False))

                    sheet1.write(11, 5, '审核人签字', set_style_1('宋体', 205, False))
                    sheet1.write(11, 6, '刘丰恺', set_style_1('宋体', 205, False))
                    sheet1.write(11, 7, '日期', set_style_1('宋体', 205, False))
                    sheet1.write(11, 8, deal_date(date_i), set_style_2('Times New Roman', 205, False))
                    workboot.save("/media/tx-eva-data/Data1/dailyFile/qingxi/%s.xls" % date_i)
                else:
                    # 表示某一天有多条数据了

                    read_work = xlrd.open_workbook("/media/tx-eva-data/Data1/dailyFile/test/%s.xls" % date_i)
                    xlrd_table = read_work.sheets()[0]
                    workboot1 = xlwt.Workbook()  # 每次写的时候创建一个新的xlwt的对象
                    sheet2 = workboot1.add_sheet('sheet1', cell_overwrite_ok=True)

                    for ii in range(xlrd_table.nrows):
                        if ii <=3:
                            if ii ==0:
                                for a in range(0, len(xlrd_table.row_values(ii))):
                                    sheet2.write(ii, a, xlrd_table.row_values(ii)[a], set_style_1('宋体', 400, False))
                            elif ii == 1:
                                for a in range(0, len(xlrd_table.row_values(ii))):
                                    sheet2.write(ii, a, xlrd_table.row_values(ii)[a], set_style_1('Times New Roman', 205, False))
                            else:
                                for a in range(0, len(xlrd_table.row_values(ii))):
                                    sheet2.write(ii, a, xlrd_table.row_values(ii)[a], set_style_1('宋体', 205, False))
                            continue
                        else:
                            if xlrd_table.row_values(ii)[0] == '':
                                break
                            else:
                                for a in range(0, len(xlrd_table.row_values(ii))):
                                    sheet2.write(ii, a, xlrd_table.row_values(ii)[a], set_style_1('宋体', 205, False))

                    for a in range(0, len(table.row_values(i))):
                        sheet2.write(4+list_date[date_i], a, datetime.datetime(*xldate_as_tuple(table.row_values(i)[a], 0)).strftime('%Y-%m-%d') if a == 3 else table.row_values(i)[a], set_style_1('Times New Roman', 205, False) if a ==3 else set_style_1('宋体', 205, False))
                    list_date[date_i] = list_date[date_i] +1 # 对应的日期重复次数加1
                    sheet2.merge(0, 0, 0, 9)  #合并表头
                    sheet2.merge(1,1,0,9)
                    sheet2.merge(2,2,0,9)

                    sheet2.write(10, 5, '记录人签字: ', set_style_1('宋体', 205, False))
                    sheet2.write(10, 6, '钏兴炳', set_style_1('宋体', 205, False))
                    sheet2.write(10, 7, '日期: ', set_style_1('宋体', 205, False))
                    sheet2.write(10, 8, deal_date(date_i), set_style_1('宋体', 205, False))

                    sheet2.write(11, 5, '审核人签字: ', set_style_1('宋体', 205, False))
                    sheet2.write(11, 6, '刘丰恺', set_style_1('宋体', 205, False))
                    sheet2.write(11, 7, '日期: ', set_style_1('宋体', 205, False))
                    sheet2.write(11, 8, deal_date(date_i), set_style_1('宋体', 205, False))
                    workboot1.save("/media/tx-eva-data/Data1/dailyFile/qingxi/%s.xls" % date_i)


def deal_date(date_str):
    if '.' in date_str:
        ss = str(date_str).replace('.', '-')
        dateTime_p = datetime.datetime.strptime(ss, '%Y-%m-%d')
        tomorrow = dateTime_p + datetime.timedelta(days=1) #在当前的时间基础上面进行加1天
        return tomorrow.strftime('%Y-%m-%d')
    elif '/' in date_str:
        ss = str(date_str).replace('/', '-')
        dateTime_p = datetime.datetime.strptime(ss, '%Y-%m-%d')
        tomorrow = dateTime_p + datetime.timedelta(days=1)  # 在当前的时间基础上面进行加1天
        return tomorrow.strftime('%Y-%m-%d')
    else:
        dateTime_p = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        tomorrow = dateTime_p + datetime.timedelta(days=1)  # 在当前的时间基础上面进行加1天
        return tomorrow.strftime('%Y-%m-%d')


def set_style_2(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    align = xlwt.Alignment()
    # 设置单元格对齐方式
    alignment = xlwt.Alignment()
    # 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
    alignment.horz = xlwt.Alignment.HORZ_RIGHT
    # 0x00(上端对齐)、 0x01(垂直方向上居中对齐)、0x02(底端对齐)
    # alignment.vert = xlwt.Alignment.
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    style.alignment = align
    return style

# #设置表格样式
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


if __name__ == '__main__':
    # print(deal_date('2017.12.12'))
    write_excel()

