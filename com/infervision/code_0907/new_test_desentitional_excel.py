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
这个脚本是用来拆分 脱敏记录表格的 

'''


def write_excel():
    list_0 = []
    list_1 = []
    list_2 = []
    list_3 = []

    list_date = {}
    data = xlrd.open_workbook("/media/tx-eva-data/Data1/CFDA_file/整改文件/数据脱敏检查记录.xlsx")
    # 获取每一个sheet的name?
    table = data.sheets()[3]  # 第一张表
    print(type(table))
    rows = table.nrows

    for i in range(rows):
        workboot = xlwt.Workbook()  # 每次写的时候创建一个新的xlwt的对象
        # workboot.footer_str = b''
        # workboot.header_str = b''
        sheet1 = workboot.add_sheet('sheet1', cell_overwrite_ok=True)
        sheet1.set_header_str(b'')
        sheet1.set_footer_str(b'')
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
                date_i = str(date_i).replace('.', '-')
            except:
                pass
            if re.match('^\d\-*', date_i):
                if date_i not in list_date:
                    # 表示在前面没有出现过
                    list_date[date_i] = 1
                    # 开始写入数据 前面4行书表头
                    # list_0[0] = ''
                    sheet1.write_merge(0, 0, 0, 8, ''.join(list_0).strip(), set_style_1('宋体', 400, False))
                    sheet1.write_merge(1, 1, 0, 8, ''.join(list_1).strip(), set_style_2('Time New Roman', 205, False))
                    sheet1.write_merge(2, 2, 0, 8, ''.join(list_2).strip(), set_style_1('宋体', 205, False))
                    for a in range(0, len(list_3)):
                        sheet1.write(3, a, list_3[a].strip(), set_style_1('宋体', 205, False))
                    for a in range(0, len(table.row_values(i))):
                        if a == 1:
                            hosp_dict_ids = get_hosp_dict()
                            sheet1.write(4, a, hosp_dict_ids[table.row_values(i)[a]],
                                         set_style_1('Time New Roman', 205, False))
                        else:
                            sheet1.write(4, a, datetime.datetime(*xldate_as_tuple(table.row_values(i)[a], 0)).strftime('%Y-%m-%d') if a == 3 else table.row_values(i)[a],
                                         set_style_1('宋体', 205, False) if a == 4 or a == 8 else set_style_1(
                                             'Times New Roman', 205, False))
                    sheet1.write(10, 5, '记录人签字', set_style_3('宋体', 205, False))
                    sheet1.write(10, 7, '日期', set_style_3('宋体', 205, False))
                    sheet1.write(12, 5, '审核人签字', set_style_3('宋体', 205, False))
                    sheet1.write(12, 7, '日期', set_style_3('宋体', 205, False))

                    for i in range(0, 9):
                        if i == 8:
                            first_col = sheet1.col(i)  # xlwt中是行和列都是从0开始计算的
                            first_col.width = 256 * 24
                        elif i == 6:
                            first_col = sheet1.col(i)  # xlwt中是行和列都是从0开始计算的
                            first_col.width = 256 * 14
                        else:
                            first_col = sheet1.col(i)  # xlwt中是行和列都是从0开始计算的
                            first_col.width = 256 * 12
                    # workboot.header_str = b''
                    # workboot.footer_str = b''
                    workboot.save("/media/tx-eva-data/Data1/CFDA_file/整改文件/脱敏文件/3/%s.xls" % date_i)
                else:
                    # 表示某一天有多条数据了
                    read_work = xlrd.open_workbook(
                        "/media/tx-eva-data/Data1/CFDA_file/整改文件/脱敏文件/3/%s.xls" % date_i)
                    xlrd_table = read_work.sheets()[0]
                    workboot1 = xlwt.Workbook()  # 每次写的时候创建一个新的xlwt的对象

                    # workboot1.footer_str = b''
                    # workboot1.header_str = b''
                    sheet2 = workboot1.add_sheet('sheet1', cell_overwrite_ok=True)
                    sheet2.set_header_str(b'')
                    sheet2.set_footer_str(b'')

                    for ii in range(xlrd_table.nrows):
                        if ii <= 3:
                            if ii == 0:
                                sheet2.write_merge(0, 0, 0, 8, ''.join(xlrd_table.row_values(ii)).strip(), set_style_1('宋体', 225, False))
                            elif ii == 1:
                                sheet2.write_merge(1, 1, 0, 8, ''.join(xlrd_table.row_values(ii)).strip(),
                                                   set_style_2('Times New Roman', 205, False))
                            elif ii == 2:
                                sheet2.write_merge(2, 2, 0, 8, ''.join(xlrd_table.row_values(ii)).strip(), set_style_1('宋体', 205, False))
                            else:
                                for a in range(0, len(xlrd_table.row_values(ii))):
                                    sheet2.write(ii, a, xlrd_table.row_values(ii)[a], set_style_1('宋体', 205, False))
                            continue
                        else:
                            if xlrd_table.row_values(ii)[0] == '':
                                break
                            else:
                                for a in range(0, len(xlrd_table.row_values(ii))):

                                    sheet2.write(ii, a, xlrd_table.row_values(ii)[a],
                                                 set_style_1('Times New Roman', 205, False))
                    for a in range(0, len(table.row_values(i))):
                        if a == 1:
                            hosp_dict_ids = get_hosp_dict()
                            sheet2.write(4 + list_date[date_i], a, hosp_dict_ids[table.row_values(i)[a]],
                                         set_style_1('Time New Roman', 205, False))
                        else:
                            sheet2.write(4 + list_date[date_i], a, datetime.datetime(*xldate_as_tuple(table.row_values(i)[a], 0)).strftime('%Y-%m-%d') if a == 3 else table.row_values(i)[a],
                                         set_style_1('宋体', 205, False) if a == 4 or a == 8 else set_style_1(
                                             'Times New Roman', 205, False))
                    list_date[date_i] = list_date[date_i] + 1  # 对应的日期重复次数加1

                    sheet2.write(10, 5, '记录人签字: ', set_style_3('宋体', 205, False))
                    sheet2.write(10, 7, '日期: ', set_style_3('宋体', 205, False))

                    sheet2.write(12, 5, '审核人签字: ', set_style_3('宋体', 205, False))
                    sheet2.write(12, 7, '日期: ', set_style_3('宋体', 205, False))

                    for i in range(0, 9):
                        if i == 8:
                            first_col = sheet2.col(i)  # xlwt中是行和列都是从0开始计算的
                            first_col.width = 256 * 24
                        elif i == 6:
                            first_col = sheet2.col(i)  # xlwt中是行和列都是从0开始计算的
                            first_col.width = 256 * 14
                        else:
                            first_col = sheet2.col(i)  # xlwt中是行和列都是从0开始计算的
                            first_col.width = 256 * 12

                    workboot1.save("/media/tx-eva-data/Data1/CFDA_file/整改文件/脱敏文件/3/%s.xls" % date_i)


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


def deal_date(date_str):
    if '.' in date_str:
        ss = str(date_str).replace('.', '-')
        dateTime_p = datetime.datetime.strptime(ss, '%Y-%m-%d')
        tomorrow = dateTime_p + datetime.timedelta(days=1)  # 在当前的时间基础上面进行加1天
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
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    borders.left_colour = 0x40
    borders.right_colour = 0x40
    borders.top_colour = 0x40
    borders.bottom_colour = 0x40
    # 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
    alignment.horz = 0x03
    # 0x00(上端对齐)、 0x01(垂直方向上居中对齐)、0x02(底端对齐)
    # alignment.vert = 0x02
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    style.alignment = align
    style.borders = borders
    return style


# #设置表格样式
def set_style_3(name, height, bold=False):

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




# #设置表格样式
def set_style_1(name, height, bold=False):

    style = xlwt.XFStyle()
    font = xlwt.Font()
    align = xlwt.Alignment()
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    # borders.diag = xlwt.Borders.THIN
    borders.left_colour = 0x40
    borders.right_colour = 0x40
    borders.top_colour = 0x40
    borders.bottom_colour = 0x40
    # borders.bottom_colour = 0x3A

    align.horz = 0x02   # 设置水平居中
    align.vert = 0x01  # 设置垂直居中
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    style.alignment = align
    style.borders = borders
    return style


if __name__ == '__main__':
    # print(deal_date('2017.12.12'))
    write_excel()
