# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/18 上午11:48
Author: ybx
"""

'''
产生损坏数据的pid
'''
import os
import xlwt

def method():
    path = '/media/tx-eva-data/NAS/原始数据库/中国医科大学附属第一医院/error_error'
    list_a = []
    for file in os.listdir(path):
        list_a.append(file)

    boot = xlwt.Workbook()
    sheet1 = boot.add_sheet('sheet1', cell_overwrite_ok=True)

    new_col = ['id', 'reason']
    for a in range(len(new_col)):
        sheet1.write(0, a, new_col[a], set_style_1('宋体', 205, True))  # 写进表格里面去

    for index, value in enumerate(list_a):
        sheet1.write(index+1, 0, value,  set_style_1('宋体', 205, True))
        sheet1.write(index+1, 1, '损坏',  set_style_1('宋体', 205, True))

    boot.save('/media/tx-eva-data/NAS/原始数据库/中国医科大学附属第一医院/28例损坏数据.xls')



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


def delete_log():
    path = '/media/tx-eva-data/NAS/原始数据库'
    for file in os.listdir(path):
        a_folder = os.path.join(path, file)
        for sfile in os.listdir(a_folder):
            if sfile.endswith('.log'):
                print(os.path.join(a_folder, sfile))
                os.system('rm -rf %s' % os.path.join(a_folder, sfile))



if __name__ == '__main__':
    # method()
    delete_log()