# encoding = utf-8

import os
import pydicom
import copy
import argparse


def addColorOnPixelArray(pixel_array, pos0, pos1, line_color):
    '''
    在指定像素矩阵中填充灰度值
    :param pixel_array: 指定像素矩阵
    :param pos0: 框的最小顶点
    :param pos1: 框的最大顶点
    :param line_color: 颜色 int 值域参考hu值 （dicom文件值域）
    :return: 没有return
    '''
    for x in range(pos0[0], pos1[0]):
        for y in range(pos0[1], pos1[1]):
            pixel_array[y][x] = line_color


def recur_open(path, key, pid_dic):
    '''
    递归打开文件夹，功能基本同os.walk
    :param path: 根目录
    :param key: 文件关键字
    :param pid_dic: .dcm文件及路径信息 字典的key是dcm文件名 dcm的路径
    :return:
    '''
    for folders_path, folders, files in os.walk(path):
        for dcm_file in files:
            dcm_file_path = os.path.join(folders_path, dcm_file)
            if dcm_file.endswith(key):
                pid_dic[dcm_file] = dcm_file_path
    return pid_dic


def main(root_path):
    ### 全局变量
    # 填充亮度，default=3000
    LINE_COLOR = 0
    # 指定输出目录
    output_dir = os.path.join(root_path, "DCM")

    # print(output_dir)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pid_dic = {}
    # ### end 全局变量
    # # 遍历所有dcm文件
    recur_open(root_path, ".dcm", pid_dic)
    # 试图读取dcm数据
    for key in pid_dic:
        dcm_path = pid_dic[key]
        info = pydicom.read_file(dcm_path, force=True)
        Rows = info.Rows
        Columns = info.Columns
        # 脱敏区域[xmin,ymin,xmax,ymax]
        target_list = [[0, 0, 400, 200], [int(Columns) - 600, 0, Columns, 200]]
        # info.file_meta.MediaStorageSOPClassUID = info.SOPClassUID
        # info.file_meta.MediaStorageSOPInstanceUID = info.SOPInstanceUID
        # info.file_meta.ImplementationClassUID = info.SOPClassUID
        # info.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
        img = copy.deepcopy(info)

        # 在dicom图片的pixel_array上填充灰度值，覆盖敏感信息
        for target_value in target_list:
            addColorOnPixelArray(img.pixel_array,
                                 [target_value[0], target_value[1]],
                                 [target_value[2], target_value[3]],
                                 LINE_COLOR)
        # 必须把pixel_array映射到PixelData上（int64编码），dicom图片才会被修改
        img.PixelData = img.pixel_array.tostring()
        a = dcm_path.replace(root_path, output_dir)
        # print(a)

        out_path = a.replace("/" + key, "")
        print(out_path)
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        output_path = os.path.join(out_path, key)
        # print(output_path)
        img.save_as(output_path)







if __name__ == "__main__":




    root_path = "/media/tx-eva-data/Data4/大连中山肺不张/save"

    main(root_path)



