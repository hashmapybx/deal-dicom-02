# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/11 下午3:30
Author: ybx
"""

import xlwt
import xlrd

path = "/home/tx-eva-data/Downloads/print_file/a/2017-11-18-CT肺-结节检出训练集王旭4.xls"

workboot = xlrd.open_workbook(path)
tables = workboot.sheets()[0]
boot = xlwt.Workbook()

a = boot.add_sheet('sheet1', cell_overwrite_ok=True )
a.show_headers = False
a.header_str = b''
a.footer_str = b''
a.write(1,1,'李四')
print(a.show_headers)
boot.save('a.xls')


# print(tables.show_header)

