# coding=utf-8
import os
'''连接S3用户名及密钥'''
access_key = "Y37DCO4238IH7VFLQSGW"
secret_key = "NJXRbEX2lFXoP5IB15TrykRZQnvg8KR3qz9AgbBc"

'''连接到数据库接口和Ｓ3地址'''
endPointUrl = "http://192.168.130.82:7480"

url = "http://192.168.130.81:8096/acquire/"
#batchInformations：需要下载的task名称
batchInformations = [ "2019-12-31_DATA-1587" ]
connect_Seqlen = 0
#standName：标记标准
standName = "DR_Chest_2.0"
#out_path：数据下载保存地址
out_path = "/media/tx-eva-data/Data1/download_data_from_S3/data"

''''''
#seqlen:设置用于训练的序列长度
seqlen=3
#root_path:用于保存rec文件的地方，生成的rec文件用于训练
root_path='/media/tx-eva-data/Data1/download_data_from_S3/data/rec'
#CT_set:当其为空列表的时候，选择data_path下所有目录下面的数据进行训练，如果列表不为空，那么就会选择列表中的目录训练
CT_set = ['nanchang2fu']
#image_set:rec文件名字的前缀，一般用于区别你不同的训练任务或者数据使用的情况
image_set = '5mmtrain_seg_20181108_small'
fp_file = ''
fp_file = ''
valid_image_set=''
valid_data_path=''
valid_CT_set=['']
model_dir='./'
classes = ['__background__', '0-3nodule', 'solid nodule', 'calcific nodule', 'pleural nodule', 'mass', 'GGN']
CLASSES=classes

CLASS_DICT = {
    'calcific nodule': 'calcific nodule',
    '3-6nodule': 'solid nodule',
    '6-10nodule': 'solid nodule',
    'pleural nodule': 'pleural nodule',
    'pleural calcific nodule':'calcific nodule',
    '10-30nodule': 'solid nodule',
    '0-3nodule': '0-3nodule',
    'mass': 'mass',
    '0-5GGN': 'GGN',
    '0-5pGGN': 'GGN',
    '0-5mGGN': 'GGN',
    '5pGGN': 'GGN',
    '5mGGN': 'GGN',
    '5GGN': 'GGN',
    'suspect nodule': '0-3nodule',
    'suspect GGN': 'GGN',
    # 'similar nodule': 'suspect',
    # 'similar GGN': 'suspect',
}
temp_seg_dir='./temp_seg'

detailed_class = ['calcific nodule',
                  '3-6nodule',
                  '6-10nodule',
                  'pleural calcific nodule',
                  'pleural nodule',
                  '10-30nodule',
                  '0-3nodule',
                  'mass',
                  '0-5GGN',
                  '5GGN',
                  '5pGGN',
                  '0-5pGGN',
                  '5mGGN',
                  '0-5mGGN',
                  'suspect nodule',
                  'suspect GGN']

has_crop=True
data_shape=512
crop_scale=0.5
fg_thresh=0.7
bg_thresh=0.1
soft_degree=0
enable_soft_mining=False
enable_aspp=False
batch_size=18
num_gpus=3
gpu_id=['1']
lr=5e-4
train_samples_count=30040
exclude_dirs=[]
# thresh_list=[0.95,0.95,0.95,0.4,0.4]
# test_CLASSES=['__background__','nodule']
# test_CLASS_DICT=dict(zip(detailed_class,['nodule']*len(detailed_class)))

