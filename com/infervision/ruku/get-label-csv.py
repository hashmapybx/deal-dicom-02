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

"""
this is user to generation csv file of label
"""
def get_csv(src_path, df, lists):
    counter = 0
    for filename in os.listdir(src_path):
        for xml in os.listdir(os.path.join(src_path, filename)):
            xml_path = os.path.join(os.path.join(src_path, filename), xml)
            collectPath = '/' + '/'.join(os.path.split(xml_path)[0].split('/')[6:])
            t = pd.concat([pd.DataFrame(
                [lists[0], '','','','','','',lists[1], lists[2], lists[3], collectPath, lists[4], lists[5],lists[6]]).T])
            t.columns = df.columns
            df = pd.concat([df, t], ignore_index=True)
            counter += 1
            break
    print("this total of %s dicom data" % counter)
    df.to_csv(src_path + '/source.csv', index=0)  # index = 0表示不保存索引

if __name__ == '__main__':
    start = time.time()
    src_path = "/media/tx-eva-data/Data1/tmp/CN319002/label/CT/2019.08.27_DATA-93"
    # 先创建一个空的dataframe
    df = pd.DataFrame(
        columns=["version","doctor","label_date","first_auditor","first_audit_date","second_auditor","second_audit_date","device","project","mark_rule","collect_path",	"data_type","model_name","check_time"
])
    version = "2019.08.27_DATA-93" # version的值是等于jira的创建时间_task编号
    device = "CT"
    project = "CT_Detection"
    mark_rule = "CT_Chest_Test_1.0"
    data_type = "test"
    model_name = "smm" # 关于这个参数有值的话 前面的参数docter-second_audit_date 五个参数都是不用写值的
    check_time = str(datetime.datetime.now()).split(' ')[0]
    lists = [version, device, project, mark_rule,data_type, model_name, check_time]
    get_csv(src_path, df, lists)


    end = time.time() - start
    print(end)
