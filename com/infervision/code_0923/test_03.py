# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/24 下午6:21
Author: ybx
"""
# import xlwt
#
# workbook = xlwt.Workbook()  # Create workbook
# worksheet = workbook.add_sheet('My sheet')  # Create worksheet
# borders = xlwt.Borders()  # Create borders
#
# borders.left = xlwt.Borders.MEDIUM  # 添加边框-虚线边框
# borders.right = xlwt.Borders.MEDIUM  # 添加边框-虚线边框
# borders.top = xlwt.Borders.MEDIUM  # 添加边框-虚线边框
# borders.bottom = xlwt.Borders.MEDIUM  # 添加边框-虚线边框
# '''
# May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE,
# HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED,
# THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED,
# or 0x00 through 0x0D.
# '''
# borders.left_colour = 0x90  # 边框上色
# borders.right_colour = 0x90
# borders.top_colour = 0x90
# borders.bottom_colour = 0x90
#
# style = xlwt.XFStyle()  # Create style
# style.borders = borders  # Add borders to style
# worksheet.write(2, 3, 'Content', style)  # row, col, content
# workbook.save('a.xls')

import os
import shutil
path = "/home/tx-eva-data/Downloads/tmp_01/数据调研表"

for file in os.listdir(path):
    new_file = file[:-5]
    print(new_file)
    os.rename(os.path.join(path, file), os.path.join(path, new_file +".xls"))