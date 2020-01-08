# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/15 下午2:42
Author: ybx
"""

'''
识别图片中的文字
'''
from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open('/home/tx-eva-data/Pictures/a1.png'), lang='chi_sim')
print(text)