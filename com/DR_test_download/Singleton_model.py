# -*- coding: utf-8 -*-
"""
Create Time: 2020/1/3 下午9:42
Author: ybx
"""

class Singleton1(object):

    __instance = None  #　类的初始化空对象
    __isFirstInit = False # 标识符

    def __new__(cls, name):
        '''
        这个是一个类方法负责对象的创建
        :param name:
        :return:
        '''
        if not cls.__instance:
            Singleton1.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, name):
        '''
        这个是一个对象的方法 负责对象的初始化
        :param name:
        '''
        if not self.__isFirstInit:
            self.__name = name
            Singleton1.__isFirstInit = True

    def getName(self):
        return self.__name



tony = Singleton1('TOny')
kerry = Singleton1('Kerry')
print(tony == kerry)
print(id(tony), id(kerry))





