# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/23 下午6:19
Author: ybx
"""
# -*- coding: utf-8 -*-
import os
import xml.etree.cElementTree as ET
import sys

json_path ='/media/tx-eva-data/Data3/DATA-159/20190820_ct_lung_delete/ct_lung_delete.json'
dcm_path = '/media/tx-eva-data/Data3/DATA-159/20190820_ct_lung_delete/CT_Lung_save/CT'


def create_studyid2patientid(dcm_path):
    p2s_dict = {}
    for slicethickness in os.listdir(dcm_path):
        thicknessPath = os.path.join(dcm_path,slicethickness)
        for pid in os.listdir(thicknessPath):
            pidPath = os.path.join(thicknessPath,pid)
            for study_id in os.listdir(pidPath):
                p2s_dict[study_id] = pid
    return p2s_dict

def xml_creator(save_path,bndboxs):
    xml_name = bndboxs[5] + '_' + bndboxs[6] + '.xml'
    if not os.path.exists(os.path.join(save_path, xml_name)):
        root = ET.Element('annotation')
        folder = ET.SubElement(root, 'folder')
        filename = ET.SubElement(root, 'filename')
        path = ET.SubElement(root, 'path')
        source = ET.SubElement(root, 'source')
        size = ET.SubElement(root, 'size')
        segmented = ET.SubElement(root, 'segmented')
        objects = ET.SubElement(root, 'object')
        database = ET.SubElement(source, 'database')
        width = ET.SubElement(size, 'width')
        height = ET.SubElement(size, 'height')
        depth = ET.SubElement(size, 'depth')
        name = ET.SubElement(objects, 'name')
        lob_pos = ET.SubElement(objects, 'lob_pos')
        truncated = ET.SubElement(objects, 'truncated')
        difficult = ET.SubElement(objects, 'difficult')
        bndbox = ET.SubElement(objects, 'bndbox')
        xmin = ET.SubElement(bndbox, 'xmin')
        ymin = ET.SubElement(bndbox, 'ymin')
        xmax = ET.SubElement(bndbox, 'xmax')
        ymax = ET.SubElement(bndbox, 'ymax')
        folder.text = 'anno'
        database.text = 'Unknown'
        width.text = '0'
        height.text = '0'
        depth.text = '3'
        segmented.text = '0'
        try:
            lob_pos.text = bndboxs[7]
        except:
            lob_pos.text = 'None'
        truncated.text = '0'
        difficult.text = '0'
        name.text = bndboxs[0]
        xmin.text = str(int(float(bndboxs[1])))
        ymin.text = str(int(float(bndboxs[2])))
        xmax.text = str(int(float(bndboxs[3])))
        ymax.text = str(int(float(bndboxs[4])))
        print(xml_name)
        tree = ET.ElementTree(root)
        tree.write(os.path.join(save_path,xml_name), encoding='utf-8')
    else:
        tree = ET.parse(os.path.join(save_path, xml_name))
        root = tree.getroot()
        new_object = ET.SubElement(root,'object')
        new_name = ET.SubElement(new_object, 'name')
        new_pose = ET.SubElement(new_object, 'pose')
        new_truncated = ET.SubElement(new_object, 'truncated')
        new_dif = ET.SubElement(new_object, 'difficult')
        new_bndbox = ET.SubElement(new_object, 'bndbox')
        new_xmin = ET.SubElement(new_bndbox, 'xmin')
        new_ymin = ET.SubElement(new_bndbox, 'ymin')
        new_xmax = ET.SubElement(new_bndbox, 'xmax')
        new_ymax = ET.SubElement(new_bndbox, 'ymax')
        new_pose.text = 'Unspecified'
        new_truncated.text = '0'
        new_dif.text = '0'
        new_name.text = bndboxs[0]
        new_xmin.text = str(bndboxs[1])
        new_ymin.text = str(bndboxs[2])
        new_xmax.text = str(bndboxs[3])
        new_ymax.text = str(bndboxs[4])
        tree.write(save_path, encoding='utf-8')
        print('more times')


def create_bndbox_detection(json_path,dcm_path):
    save_path = dcm_path.replace(dcm_path.split('/')[-1],'anno')
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    p2s_dict = create_studyid2patientid(dcm_path)
    with open(json_path,'r') as f:
        lines = f.readlines()
        study_id = ''
        for line in lines:
            if len(line) < 100 and line != '\n':

                study_id = line.replace('\n','')
            if len(line) > 100:
                line = line.replace('\n','')
                info = eval(line)
                print(info)
                try:
                    # 这里需要注意的 处理的数据是 add 的话要给到type  如果是change   delete 的话  给fp 也行
                    name = info['type']
                except:
                    name = 'fp'
                # name = 'fp'
                boxes = info['boxes']
                for box in boxes:
                    slices = format(box['sliceId'], '03d')
                    xmin = box['left']
                    xmax = box['right']
                    ymin = box['top']
                    ymax = box['bottom']
                    try:
                        pid = p2s_dict[study_id]
                        bndbox = [name,str(xmin),str(ymin),str(xmax),str(ymax),pid,str(slices)]
                        print(bndbox)
                        xml_creator(save_path,bndbox)

                    except:
                        pass

def create_bndbox_position(json_path,dcm_path):
    save_path = dcm_path.replace(dcm_path.split('/')[-1],'anno')
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    p2s_dict = create_studyid2patientid(dcm_path)
    with open(json_path,'r') as f:
        lines = f.readlines()
        study_id = ''
        for line in lines:
            if len(line) <120:
                pass
            elif len(line) < 180:
                infos = eval(line)
                study_id = infos['series_uid']
                change = infos['change']
            else:
                line = line.replace('\n','')
                info = eval(line)
                name = info['type']
                boxes = info['boxes']
                slices = format(info['keySliceId'], '03d')
                xmin = boxes[0]['left']
                xmax = boxes[0]['right']
                ymin = boxes[0]['top']
                ymax = boxes[0]['bottom']
                try:
                    pid = p2s_dict[study_id]
                    bndbox = [name,str(xmin),str(ymin),str(xmax),str(ymax),pid,str(slices),change]
                    print(bndbox)
                    xml_creator(save_path,bndbox)

                except:
                    pass

create_bndbox_detection(json_path,dcm_path)
# create_bndbox_position(json_path,dcm_path)