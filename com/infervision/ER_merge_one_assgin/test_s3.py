# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/12 下午8:50
Author: ybx
"""
import boto3

access_key = "Y37DCO4238IH7VFLQSGW"
secret_key = "NJXRbEX2lFXoP5IB15TrykRZQnvg8KR3qz9AgbBc"

'''连接到数据库接口和Ｓ3地址'''

endPointUrl = "http://192.168.130.82:7480"
s3 = boto3.resource(service_name='s3', aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key, endpoint_url=endPointUrl,
                        verify=False)


# for bucket in s3.buckets.all():
#     print(bucket.name)

dicom = s3.Bucket('dicom').download_file('49cef87d-4c92-4f91-aa3d-f3595557c3c4/CS755003-528358-T125_461.dcm', './CS755003-528358-T125_461.dcm')



print(dicom)








