# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/17 下午8:04
Author: ybx
"""
import os
import csv
import logging
import xlrd
import datetime
from xlrd import xldate_as_tuple


def data_desensition_log():
    root_path = "/media/tx-eva-data/yushiyan/基础数据库"
    # save_path = "/media/tx-eva-data/yushiyan/四级文件/给执行的日志"
    hosp_dict = get_tuomin_date()
    for h_folder in os.listdir(root_path):
        a_folder = os.path.join(root_path, h_folder)
        list_date = sorted(hosp_dict[h_folder])
        for bfile in os.listdir(a_folder):
            try:
                h_folder_path = os.path.join(a_folder, bfile)
                if bfile == 'dcm':
                    for b_folder in os.listdir(h_folder_path):
                        if b_folder.endswith('.log'):
                            continue
                        b_folder_path = os.path.join(h_folder_path, b_folder)
                        new_path = os.path.join(root_path, h_folder)
                        if not os.path.exists(new_path):
                            os.makedirs(new_path)
                        desensitization_path = os.path.join(new_path,  list_date[0] + "_data_clean.log")
                        date = "[ " + list_date[0] + " ]"
                        # date = "[ " + (b_folder[:10]).replace("_", "-") + " ]"
                        os.system('touch %s' % desensitization_path)
                        for folders_path, folders, files in os.walk(b_folder_path):
                            for dcm_file in files:
                                dcm_file_path = os.path.join(folders_path, dcm_file)
                                # filepath = dcm_file_path.replace(b_folder_path, "")
                                filepath = '/'.join(dcm_file_path.split('/')[7:])
                                with open(desensitization_path, 'a+') as b:
                                    writer = csv.writer(b)
                                    writer.writerow(['%s %s\n%s\n%s\n' % (
                                        date, dcm_file, filepath, "dirty data has been cleaned ")])
                        print(b_folder)
            except:
                print(h_folder_path)
                pass
                # else:
                #     try:
                #         for b_folder in os.listdir(h_folder_path):
                #             if b_folder.endswith('.log'):
                #                 continue
                #
                #             b_folder_path = os.path.join(h_folder_path, b_folder)
                #             new_path = os.path.join(save_path, bfile, b_folder)
                #             if not os.path.exists(new_path):
                #                 os.makedirs(new_path)
                #             desensitization_path = os.path.join(new_path,  list_date[0] + "_desensitization.log")
                #             date = "[ " + list_date[0] + " ]"
                #             # date = "[ " + (b_folder[:10]).replace("_", "-") + " ]"
                #             os.system('touch %s' % desensitization_path)
                #             for folders_path, folders, files in os.walk(b_folder_path):
                #                 for dcm_file in files:
                #                     dcm_file_path = os.path.join(folders_path, dcm_file)
                #                     filepath = dcm_file_path.replace(b_folder_path, "")
                #                     with open(desensitization_path, 'a+') as b:
                #                         writer = csv.writer(b)
                #                         writer.writerow(['%s %s\n%s\n%s\n' % (
                #                             date, dcm_file, filepath, "Sensitive information has been removed ")])
                #             print(b_folder)



def get_tuomin_date():
    path = "/home/tx-eva-data/Downloads/预实验时间点+医院情况.xlsx"
    workboot = xlrd.open_workbook(path)
    table = workboot.sheets()[0]
    dict_pici_date = {}
    rows = table.nrows
    for row in range(0, rows):
        if row == 0:
            continue
        hosp_name = str(table.row_values(row)[1]).strip()
        collection_date = table.row_values(row)[9].replace('.', '-')
        # date = datetime.datetime(*xldate_as_tuple(collection_date, 0))
        # collection_date = date.strftime('%Y-%m-%d')
        if hosp_name not in dict_pici_date:
            list_date = []
            list_date.append(collection_date)
            dict_pici_date[hosp_name] = list_date
        else:
            list_b = dict_pici_date[hosp_name]
            list_b.append(collection_date)
            dict_pici_date[hosp_name] = list_b
    return dict_pici_date


if __name__ == "__main__":
    data_desensition_log()
