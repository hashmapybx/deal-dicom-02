# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/34 下午5:33
Author: ybx
"""

import xlwt
import xlrd
import os
from xlrd import xldate_as_tuple
import datetime


''''
这个脚本是用来合并excel表格的代码
'''


def deal_excel(index, file_name, path, book, list_style):
    list_0 = []
    list_1 = []
    list_2 = []
    workboot = xlrd.open_workbook(path)
    # file_name = path.split('/')[-1]
    table = workboot.sheets()[0]
    # print(table.nrows)
    rows = table.nrows
    list_0 = table.row_values(0)
    list_1 = table.row_values(1)
    list_2 = table.row_values(2)

    # cols = table.ncols
    # print(cols)
    list_row_data = []

    # book = xlwt.Workbook(encoding='utf-8')
    # sheet = book.add_sheet('sheet1')
    # book = xlwt.Workbook()  # 每次写的时候创建一个新的xlwt的对象
    sheet = book.add_sheet('sheet{0}'.format(index), cell_overwrite_ok=True)
    sheet.set_header_str(b'')
    sheet.set_footer_str(b'')
    for row in range(rows):
        if row == 0:
            sheet.write_merge(0, 0, 0, 8, ''.join(list_0).strip(), set_style_1('宋体', 400, False))
        elif row == 1:
            sheet.write_merge(1, 1, 0, 8, ''.join(list_1).strip(), set_style_2('Time New Roman', 205, False))
        elif row == 2:
            sheet.write_merge(2, 2, 0, 8, ''.join(list_2).strip(), set_style_1('宋体', 205, False))
        elif row == 3:
            new_col = [table.row_values(row)[0],table.row_values(row)[1], table.row_values(row)[2], table.row_values(row)[3],
                       table.row_values(row)[4]
                ,table.row_values(row)[5], table.row_values(row)[6],
                       table.row_values(row)[7], table.row_values(row)[8]
                       ]
            for a in range(len(new_col)):
                sheet.write(row, a, new_col[a], list_style[0])

        elif row == 10 or row == 12:
            continue
        else:
            if str(table.row_values(row)[0]) == '':
                print('空的数据')
                break
            else:
                list_row_data.append([table.row_values(row)[0],table.row_values(row)[1], table.row_values(row)[2], table.row_values(row)[3],
                                  table.row_values(row)[4]
                                     , table.row_values(row)[5], table.row_values(row)[6],
                                  table.row_values(row)[7],table.row_values(row)[8]
                                  ])

    for a in range(0, len(list_row_data)):
        for b in range(0, len(list_row_data[a])):
            sheet.write(4 + a, b, list_row_data[a][b], list_style[1] if b == 3 or b == 7 else list_style[2])

    sheet.write(rows+ 3, 5, '记录人签字: ', list_style[3])
    # # sheet2.write(10, 6, '钏兴炳', set_style_1('宋体', 205, False))
    sheet.write(rows+ 3, 7, '日期: ', list_style[3])
    # # sheet2.write(10, 8, date_i, set_style_1('Times New Roman', 205, False))
    #
    sheet.write(rows+ 5, 5, '审核人签字: ', list_style[3])
    # # sheet2.write(11, 6, '刘丰恺', set_style_1('宋体', 205, False))
    sheet.write(rows + 5, 7, '日期: ', list_style[3])
    for i in range(0, 9):
        if i == 8:
            first_col = sheet.col(i)  # xlwt中是行和列都是从0开始计算的
            first_col.width = 256 * 24
        elif i == 6:
            first_col = sheet.col(i)  # xlwt中是行和列都是从0开始计算的
            first_col.width = 256 * 15
        else:
            first_col = sheet.col(i)  # xlwt中是行和列都是从0开始计算的
            first_col.width = 256 * 13
    return book



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


# TODO 设置表格样式
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

    align.horz = 0x02  # 设置水平居中
    align.vert = 0x01  # 设置垂直居中
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    style.alignment = align
    style.borders = borders
    return style


# deal_excel()

if __name__ == '__main__':

    src_path = "/media/tx-eva-data/Data1/CE-DR/数据清洗记录/数据清洗记录.xlsx"
    book = xlwt.Workbook()  # 每次写的时候创建一个新的xlwt的对象

    style_1 = set_style_1('宋体', 225, True)
    style_2 = set_style_1('Time New Roman', 205,False)
    style_3 = set_style_1( '宋体', 205, False)
    style_4 = set_style_3('宋体', 205, False)
    list_style =[style_1, style_2, style_3, style_4]
    for index, file in enumerate(os.listdir(src_path)):
        #
        file_path = os.path.join(src_path, file)
        deal_excel(index, file, file_path, book, list_style)
        # print(index)
    book.save("/media/tx-eva-data/Data1/CE-DR/数据清洗记录/split_file/3.xls")