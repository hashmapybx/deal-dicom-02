#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4/0004 22:00
# @Author  : Mat

import xlrd
import xlwt
import re
from xlutils.copy import copy
import datetime
# 创建workboot对象

def write_excel():
    list_1 = []
    list_2 = []
    list_date = {}
    data = xlrd.open_workbook("d:/aa/a/数据标注记录_正式标注_分割_V1.1.xlsx")
    # 获取每一个sheet的name?
    table = data.sheets()[0]  # 第一张表
    rows = table.nrows

    for i in range(rows):
        workboot = xlwt.Workbook() #每次写的时候创建一个新的xlwt的对象
        sheet1 = workboot.add_sheet('sheet1', cell_overwrite_ok=True)
        if i == 0:
            list_1 = table.row_values(i)
        elif i == 1:
            list_2 = table.row_values(i)
        # 从数据的第一行开始操作
        # 获取每一行的数据的date 并判断是不是同一天  如果是同一天就放到一个excel里面
        else:
            date_i = table.row_values(i)[0]
            if re.match('^\d\.*', date_i):
                if date_i not in list_date:
                    # 表示在前面没有出现过
                    list_date[date_i] = 1
                    #开始写入数据 前面两行书表头
                    for a in range(0, len(list_1)):
                        sheet1.write(0, a, list_1[a], set_style('宋体', 205, False))
                    for a in range(0, len(list_2)):
                        sheet1.write(1, a, list_2[a], set_style('宋体', 205, False))
                    for a in range(0, len(table.row_values(i))):
                        sheet1.write(2, a, table.row_values(i)[a], set_style('宋体', 205, False))
                    sheet1.merge(0, 0, 0, 10)
                    sheet1.write(10, 5, '记录人签字', set_style('宋体', 205, False))
                    sheet1.write(10, 6, '钏兴炳', set_style('宋体', 205, False))
                    sheet1.write(10, 7, '日期', set_style('宋体', 205, False))
                    sheet1.write(10, 8,  date_i, set_style('宋体', 205, False))

                    sheet1.write(11, 5, '审核人签字', set_style('宋体', 205, False))
                    sheet1.write(11, 6, '刘丰恺', set_style('宋体', 205, False))
                    sheet1.write(11, 7, '日期', set_style('宋体', 205, False))
                    sheet1.write(11, 8, date_i, set_style('宋体', 205, False))
                    workboot.save("d:/aa/a/segment/%s.xls" % date_i)
                else:
                    # 表示某一天有多条数据了
                    read_work = xlrd.open_workbook("d:/aa/a/segment/%s.xls" % date_i)
                    excel = copy(read_work)  # 将xlrd的对象转化为xlwt的对象
                    table_1 = excel.get_sheet(0) #获取要操作的table
                    for a in range(0, len(table.row_values(i))):
                        table_1.write(2+list_date[date_i], a, table.row_values(i)[a], set_style('宋体', 205, False))
                    list_date[date_i] = list_date[date_i] +1 # 对应的日期重复次数加1
                    table_1.merge(0, 0, 0, 10)  #合并表头
                    sheet1.write(10, 5, '记录人签字', set_style('宋体', 205, False))
                    sheet1.write(10, 6, '钏兴炳', set_style('宋体', 205, False))
                    sheet1.write(10, 7, '日期', set_style('宋体', 205, False))
                    sheet1.write(10, 8, str(deal_date(date_i)), set_style('宋体', 205, False))

                    sheet1.write(11, 5, '审核人签字', set_style('宋体', 205, False))
                    sheet1.write(11, 6, '刘丰恺', set_style('宋体', 205, False))
                    sheet1.write(11, 7, '日期', set_style('宋体', 205, False))
                    sheet1.write(11, 8, str(deal_date(date_i)), set_style('宋体', 205, False))
                    excel.save("d:/aa/a/segment/%s.xls" % date_i)


def deal_date(date_str):
    if '.' in date_str:
        ss = str(date_str).replace('.', '-')
        dateTime_p = datetime.datetime.strptime(ss, '%Y-%m-%d')
        tomorrow = dateTime_p + datetime.timedelta(days=1) #在当前的时间基础上面进行加1天
        return str(tomorrow)[:10]
    else:
        dateTime_p = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        tomorrow = dateTime_p + datetime.timedelta(days=1)  # 在当前的时间基础上面进行加1天
        return str(tomorrow.time())[:10]

# #设置表格样式
def set_style(name, height, bold=False):
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