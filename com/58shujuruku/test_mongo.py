# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/27 下午5:20
Author: ybx
"""
import pymongo


import time

start = time.time()

myclient = pymongo.MongoClient("mongodb://forModel:ForOrigion123@localhost/PatientReport")
mydb = myclient["PatientReport"]

'''
用mongodb来保存病人的报告信息的时候 我们 需要给字段添加文本索引 这样的话是可以提高检索的效率的
其中文本索引还是可以添加权重的
关于 文本索引的限制 一个集合最多可以有一个文本索引
mongodb text search 自动对于大段的文本进行粉分词处理, 模糊匹配, 同义词匹配, 来解决文本的搜索问题

mongodb 对于创建了文本索引的 字段支持全文检索的操作
简单的全文检索
db.report.find({$text: {$search: "纵隔居中"}}).limit(3).pretty();
查询包含某一个字段或者另一字段 相当于是或的操作


'''

# 集合
mycol = mydb['report']

# TODO 插入一条数据

# mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
#

# mydict = {'patientid': 1290095, 'accessionnumber': 1873512, 'ReportTime': '2019-08-26 13:08:42', 'PatientSex': '男', 'PatientAge': '45岁', 'ExamineBodyPart': '胸部平扫+HRCT(高分辨CT)', 'imagesight': '    双侧胸廓对称。双肺纹理走行、段、前段、下叶前基底段见散在实性结节影，大小约3mm～9mm，余肺内未见明显异常密度影。两肺门结构尚清。纵隔居中。纵隔内及两肺门未见明显肿大淋巴结。气管、支气管通畅，未见明显狭窄、阻塞。心影大小、形态如常，大血管未见明显异常。所见'  }
# res = mycol.insert_one(mydict)
# print(res.acknowledged)
# TODO 插入多条数据操作

# mylist = [
#     {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
#     {"_id": 2, "name": "Google", "address": "Google 搜索"},
#     {"_id": 3, "name": "Facebook", "address": "脸书"},
#     {"_id": 4, "name": "Taobao", "address": "淘宝"},
#     {"_id": 5, "name": "Zhihu", "address": "知乎"}
# ]
#
# x = mycol.insert_many(mylist)
# print(x.inserted_ids)


# todo 查询一条数据

# x = mycol.find_one() # 查询集合里面的第一条数据
# print(x)

# todo 查询所有的数据

# all = mycol.find()


# todo 根据指定条件 查询数据 类似于 sql 里面的where操作
#
# myquery = {"name": "RUNOOB"}
# myquery1 = {"name": {"$gt": "H"}}  # 第一个字母的ASCII码的值 大于"H" 的数据
# myquery2 = {"name": {"$regex": "^R"}}  # 正则表达式来检索数据的操作
#
#
# mydoc = mycol.find(myquery).limit(1) # limit 来限制指定返回的数据
# for x in mydoc:
#     print(x)

# dblist = myclient.list_database_names()
#
# if 'runoobdb' in dblist:
#     print('数据库已经存在了')

# 接下来是创建集合的操作 集合类似于mysql里面的表

import json
import csv
import json

keyword1 = '结节'
keyword2 = 'CT_Chest'
keyword3 = 'CT_Head'


param1 = 'DESCRIPTION'
param2 = 'IMPRESSION'
param3 = '报告类型'


myQuery = '{"%s": "%s"}' % (param1, keyword1)



myQuery1 = '{"$or": [{"%s": {"$regex": ".%s.+"}},{"%s": {"$regex": ".%s.+"}}]}' \
           % ( param1, keyword1, param2, keyword1)

# 进行条件插查询 其中or 可以利用起来
# python里面的eval函数

result = mycol.find(eval(myQuery1), {param1:1, param2:1, "_id": 0})


# fout = open('/media/tx-eva-data/Data1/pycharmproject/mysite/blog/test/a.csv', 'wb+')
fout = open('./bingli.txt', 'a+')

for res in result:
    # res['_id'] = str(res['_id'])
    fout.write(res['DESCRIPTION'] + '\n')
    fout.write(res['IMPRESSION'] + '\n')

fout.close()

print('程序利用的时间:', float(time.time()-start))
# str_json = json.dumps(result)
# res_dict = eval(str_json)
# print(type(result))
# print(result)
# print(result.get('影像号', None))
# print(result.get('卡号', None))

# with open('/media/tx-eva-data/Data1/pycharmproject/mysite/blog/test/a.csv', 'w+', encoding='utf8') as a:
#     writer = csv.writer(a)
#     writer.writerow(
#         res_dict.keys()
#     )
#
#
# with open('/media/tx-eva-data/Data1/pycharmproject/mysite/blog/test/a.csv', 'a', encoding='utf8') as a:
#     writer = csv.writer(a)
#     writer.writerow(res_dict.values())


