# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/22 下午2:41
Author: ybx
"""
import os
import xlwt
import random

def generate_tuoluo():
    path = '/media/tx-eva-data/Data4/CE_DATA/基础数据库'
    list_dcoter = ['丁雷', '付德利', '周玉荣', '张晓玮'] # 医生列表
    list_a = []
    for file in os.listdir(path):
        hosp_folder = os.path.join(path, file)
        for sfile in os.listdir(hosp_folder):
            if sfile == 'dcm':
                s_folder_path = os.path.join(hosp_folder, sfile)
                for tfile in os.listdir(s_folder_path):
                    if tfile.endswith('T500'):
                        continue
                    list_a.append(tfile)
    # print(len(list_a))
    list_id_test = read_test_id()
    # 保存不是test的数据pi
    list_diff = []
    for a in list_a:
        if a not in list_id_test:
            list_diff.append(a)
    print(len(list_diff))
    i = 0
    #脱落记录生成四分
    random.shuffle(list_diff)
    random.shuffle(list_id_test) # 挑选出来的test的数据pid
    while i < 4:
        boot = xlwt.Workbook()
        boot.footer_str = b''
        boot.header_str = b''
        sheet = boot.add_sheet('sheet', cell_overwrite_ok=True)
        new_clo = ['日期', 'PID', '检查医生', '检查结果']  # 新表格的列的title
        for col_name in range(len(new_clo)):
            sheet.write(0, col_name, new_clo[col_name], set_style_2('宋体', 230, True))  # 写进表格里面去
        list_row_data = []  # 用来保存每行数据 在xieru excel 的时候是按照行来写数据的
        for value in list_id_test[i * 40: (i + 1) * 40]:
            list_row_data.append(['2019-04-03', value, list_dcoter[i], '图像清晰,比较适合作为测试集'])

        for value in list_diff[i*85:(i+1)* 85]:
            list_row_data.append(['2019-04-03', value,list_dcoter[i],' '])

        for a in range(0, len(list_row_data)):
            for b in range(0, len(list_row_data[a])):
                sheet.write(a + 1, b, list_row_data[a][b],
                             set_style_2('Times New Roman', 205, False) if b == 1 else set_style_2('宋体', 205, False))

        file_name = list_dcoter[i] + '_' +str(i)  # file
        boot.save(
            "/media/tx-eva-data/Data4/CE_DATA/CE_三四级文件/数据脱落记录/%s.xls" % file_name)
        i += 1

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
    # alignment.horz = xlwt.Alignment.HORZ_RIGHT
    # 0x00(上端对齐)、 0x01(垂直方向上居中对齐)、0x02(底端对齐)
    # alignment.vert = xlwt.Alignment.
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    style.alignment = align
    style.borders = borders
    return style


def read_test_id():
    list_a = []
    path = '/media/tx-eva-data/Data4/CE_DATA/标注数据库/detection/dcm'
    count = 0
    for file in os.listdir(path):
        list_a.append(file)
        count += 1
    print('标记量: %d' % count)
    return list_a



if __name__ == '__main__':
    generate_tuoluo()
    # read_test_id()