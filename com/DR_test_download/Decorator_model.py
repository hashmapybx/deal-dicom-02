# -*- coding: utf-8 -*-
"""
Create Time: 2020/1/3 下午9:21
Author: ybx
"""

import logging
logging.basicConfig(level=logging.INFO)

def loggingDecorator(func):
    '''记录日志的装饰器'''

    def wrapperLogging(*args, **kwargs):
        logging.info('开始执行 %s() ...' % func.__name__)
        func(*args, **kwargs)
        logging.info("%s() 执行完成！", args, kwargs)

    return wrapperLogging



def showInfo(*args, **kwargs):
    print('这是一个测试logging装饰器的方法', args, kwargs)



decorator = loggingDecorator(showInfo)
decorator('args1', 'arg2', kwarg1 =1, kwarg2 = 2)
