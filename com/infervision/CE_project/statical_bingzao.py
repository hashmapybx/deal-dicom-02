# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/4 下午6:27
Author: ybx
"""

import os
import xml.etree.cElementTree as ET
import xlwt



def method():
    path = '/media/tx-eva-data/Data4/songxiaoyuan/2019_11_01_ShenZhenSanYuan_DR'
    boot = xlwt.Workbook()
    sheet = boot.add_sheet('sheet1', cell_overwrite_ok=True)
    # 下面的list记录的是标签的值为有结合
    list_bingzao = ["ObsoletePulmonaryTuberculosis", "ActiveTuberculosis", "Tb", "tb",
                    "PrimaryPulmonaryTuberculosis", "HematogenousPulmonaryTuberculosis",
                    "SecondaryPulmonaryTuberculosis", "BronchialTuberculosis", "TuberculousPleurisy"]
    list_row_data = []
    count = 0
    list_pid = []
    list_dicom = []
    doctor = 'LuoChaoFeng'
    for sfile in os.listdir(path):
        if sfile == 'anno':
            anno_folder = os.path.join(path, sfile)
            for xml_file in os.listdir(anno_folder):
                pid = xml_file[:-4]
                list_pid.append(pid)
                xml_path = os.path.join(anno_folder, xml_file)
                root = ET.parse(xml_path)
                objects = root.findall('object')
                for obj in objects:
                    if str(obj.find('name').text) in list_bingzao:
                        list_row_data.append([pid, '有结合', doctor])
                    else:
                        print('其他病灶')
                        list_row_data.append([pid, '无' , '其他病灶%s' % str(obj.find('name').text), doctor])

        if sfile == 'dcm':
            dcm_folder = os.path.join(path, sfile)
            for dcm in os.listdir(dcm_folder):
                pid = dcm[:-4]
                list_dicom.append(pid)

    for id in list_dicom:
        if id not in list_pid:
            list_row_data.append([id, '没有anno', doctor])

    list_new = {}
    for d in list_row_data:
        if d[0] not in list_new:
            list_new[d[0]] = d
        else:
            aa = list_new[d[0]]
            aa.append(d[2])
            list_new[d[0]] = aa


    list_bb = []
    for key, value in list_new.items():
        list_bb.append(value)

    for a in range(0, len(list_bb)):
        for b in range(0, len(list_bb[a])):
            sheet.write(a, b, list_bb[a][b], set_style_1('Time New Roman', 205,
                                                                   False) if b == 0 or b == 2 or b == 7 else set_style_1(
                '宋体', 205, False))
    boot.save('/media/tx-eva-data/Data4/songxiaoyuan/2019_11_01_ShenZhenSanYuan_DR/info_1.xls')
    # print(count)





def set_style_1(name, height, bold=False):
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
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    style.alignment = align
    style.borders = borders
    return style






if __name__ == '__main__':
    method()

