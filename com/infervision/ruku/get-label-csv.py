# -*- coding: utf-8 -*-
"""
Create Time: 2019/8/30 下午4:15
Author: ybx
"""
import os
import re
import pandas as pd
import time
import datetime
import pydicom
import csv
"""
this is user to generation csv file of label
"""


def get_csv(src_path, csv_path, lists):
    counter = 0
    for filename in os.listdir(src_path):
        if filename.endswith('.csv'):
            continue
        for xml in os.listdir(os.path.join(src_path, filename)):
            xml_path = os.path.join(os.path.join(src_path, filename), xml)
            collectPath = '/' + '/'.join(os.path.split(xml_path)[0].split('/')[-4:])
            with open(csv_path, 'a+') as b:
                writer = csv.writer(b)
                writer.writerow(
                    [lists[0], '', '', '', '', '', '', lists[1], lists[2], lists[3], collectPath, lists[4], lists[5],
                     lists[6]]
                )
            # t = pd.concat([pd.DataFrame(
            #     [lists[0], '', '', '', '', '', '', lists[1], lists[2], lists[3], collectPath, lists[4], lists[5],
            #      lists[6]]).T])
            # t.columns = df.columns
            # df = pd.concat([df, t], ignore_index=True)
            counter += 1
            break
    print("this total of %s dicom data" % counter)
    # df.to_csv(src_path + '/source.csv', index=0)  # index = 0表示不保存索引


if __name__ == '__main__':
    start = time.time()
    src_path = "/media/tx-eva-data/Data1/tmp/2019-12-13_hainanyiyuan_71/tmp/label/CT/2019-12-14_DATA-1109"
    # 先创建一个空的dataframe
    csv_path = src_path + '/source.csv'
    with open(csv_path, 'w+') as a:
        writer = csv.writer(a)
        writer.writerow(
            ["version", "doctor", "label_date", "first_auditor", "first_audit_date", "second_auditor",
             "second_audit_date", "device", "project", "mark_rule", "collect_path", "data_type", "model_name",
             "check_time"
             ]
        )
    # df = pd.DataFrame(
    #     columns=
    #     ["version", "doctor", "label_date", "first_auditor", "first_audit_date", "second_auditor",
    #              "second_audit_date", "device", "project", "mark_rule", "collect_path", "data_type", "model_name",
    #              "check_time"
    #              ])
    version = "2019-12-14_DATA-1109"  # version的值是等于jira的创建时间_task编号 (这里的task编号是数据标注的jira的task 编号)
    device = "CT"
    project = "CT_Chest"
    mark_rule = "CT_Chest_Test_1.0"  # 这个是标注的规则
    data_type = "test"
    model_name = "smm"  # 关于这个参数有值的话 前面的参数docter-second_audit_date 五个参数都是不用写值的
    check_time = str(datetime.datetime.now()).split(' ')[0]
    lists = [version, device, project, mark_rule, data_type, model_name, check_time]
    get_csv(src_path, csv_path, lists)

    end = time.time() - start

    print(end)










