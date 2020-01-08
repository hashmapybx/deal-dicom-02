# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/26 下午6:41
Author: ybx
"""

import pymysql

config = {
    'host': '192.168.130.81',
    'port': 4000,
    'user': 'root',
    'password': 'dicom@infervision',
    'db': 'db_infervision',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}



'''
数据上传检查  数据是否在数据库 中已经存在
'''
def conn():
    # 创建连接 （2）
    conn = pymysql.connect(**config)
    # 创建游标
    cursor = conn.cursor()
    # result = cursor.execute("select count(DISTINCT substring(substring(remote_path, -20), 1, 12))  from t_dicom_information WHERE remote_path like %s", ['%CT190%.dcm'])
    # print('this is 执行查询的结果是: %s ' % result)
    try:
        cursor.execute('SELECT label_path from t_label_information limit %s;', [12] )

        results = cursor.fetchall()
        for ll in results:
             print(ll)
    except:
        import traceback
        traceback.print_exc()
    # conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

if __name__ == '__main__':

    conn()



