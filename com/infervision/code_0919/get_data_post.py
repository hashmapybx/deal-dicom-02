# # -*- coding: utf-8 -*-
# """
# Create Time: 2019/9/19 上午11:00
# Author: ybx
# """
# # coding=utf-8
#
# import os
# import sys
# import boto3
# import requests
# import json
# import private_config
# import shutil
# import random
# from multiprocessing import cpu_count, Process, JoinableQueue
#
#
#
# def test_connection(endPointUrl, verify, access_key, secret_key):
#     s3 = boto.resource(service_name='s3', aws_access_key_id=access_key,
#                         aws_secret_access_key=secret_key, endpoint_url=endPointUrl,
#                         verify=verify)
#
#     dcm_bucket = s3.Bucket('dicom')
#     label_bucket = s3.Bucket('label')
#     return dcm_bucket, label_bucket
#
#
# def post_map(Seqlen):
#     headers = {"Content-Type": "application/json"}
#     data = {"batchInformations": private_config.batchInformations, "seqlen": Seqlen,
#             "standName": private_config.standName, }
#     r = requests.post(private_config.url, data=json.dumps(data), headers=headers)
#     post_dict = json.loads(r.text)
#     return post_dict
#
#
# def bridge_get_map(post_dict, Seqlen, q):
#     headers = {"Content-Type": "application/json"}
#     if isinstance(post_dict, dict):
#         version_keys = post_dict.keys()
#         for version_key in version_keys:
#             version_values = post_dict[version_key]
#             vo_keys = version_values.keys()
#             for vo_key in vo_keys:
#                 vo_values = version_values[vo_key]
#                 for vo_value in vo_values:
#                     dicomId = vo_value["dicomId"]
#                     labelId = vo_value["labelId"]
#                     Url = private_config.url + str(dicomId) + "/" + str(labelId) + "/" + str(Seqlen) + "/"
#                     data = {"dicomId": dicomId, "labelId": labelId, "seqlen": Seqlen, "url": Url}
#                     r = requests.get(Url, data=json.dumps(data), headers=headers)
#                     data_dict = json.loads(r.text)
#                     q.put([version_key, data_dict])
#                     print
#                     dicomId
#     return q
#
#     q.join()
#
#
# def download_list_all_dict(version_key, data_dict, dcm_bucket, label_bucket, out_path):
#     if isinstance(data_dict, dict):
#         folder_keys = data_dict.keys()
#         for folder_key in folder_keys:
#             if folder_key == "dicoms":
#                 dicoms_value = data_dict[folder_key]
#                 target_folder_keys = dicoms_value.keys()
#                 for target_folder_key in target_folder_keys:
#                     target_folder_values = dicoms_value[target_folder_key]
#                     dcm_out_path = os.path.join(out_path, version_key, "dicom", target_folder_key)
#                     if not os.path.exists(dcm_out_path):
#                         os.makedirs(dcm_out_path)
#                     for target_folder_value in target_folder_values:
#                         dcm_name = target_folder_value.split("/")[1]
#                         dcm_bucket.download_file(target_folder_value, os.path.join(dcm_out_path, dcm_name))
#             if folder_key == "xmls":
#                 labels_value = data_dict[folder_key]
#                 target_folder_keys = labels_value.keys()
#                 for target_folder_key in target_folder_keys:
#                     target_folder_values = labels_value[target_folder_key]
#                     label_out_path = os.path.join(out_path, version_key, "label", target_folder_key)
#                     if not os.path.exists(label_out_path):
#                         os.makedirs(label_out_path)
#                     for target_folder_value in target_folder_values:
#                         label_name = target_folder_value.split("/")[1]
#                         label_bucket.download_file(target_folder_value, os.path.join(label_out_path, label_name))
#
#
# def Worker(dcm_bucket, label_bucket, out_path):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         download_list_all_dict(item[0], item[1], dcm_bucket, label_bucket, out_path)
#         q.task_done()
#
#
# if __name__ == '__main__':
#     cpuCount = int(cpu_count())
#     access_key = private_config.access_key
#     secret_key = private_config.secret_key
#     endPointUrl = private_config.endPointUrl
#     out_path = private_config.out_path
#     verify = False
#     Seqlen = private_config.connect_Seqlen
#     multiprocessing_list = []
#     q = JoinableQueue()
#     all_data_list = []
#     dcm_bucket, label_bucket = test_connection(endPointUrl, verify, access_key, secret_key)
#     post_dict = post_map(Seqlen)
#     q = bridge_get_map(post_dict, Seqlen, q)
#     for i in range(0, cpuCount):
#         p = Process(target=Worker, args=(dcm_bucket, label_bucket, out_path,))
#         p.daemon = True
#         p.start()
#         multiprocessing_list.append(p)
#
#     for i in range(0, cpuCount):
#         q.put(None)
#     for p in multiprocessing_list:
#         p.join()
#     print
#     "all work done"