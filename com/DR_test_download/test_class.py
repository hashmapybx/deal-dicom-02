# -*- coding: utf-8 -*-
"""
Create Time: 2020/1/3 下午8:45
Author: ybx
"""

from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name  # protected 只有该类和子类可以放问的

    @abstractmethod
    def wear(self):
        print('着装：')


class Engineer(Person):

    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill  # 私有的字段 只有该类的内部可以访问的

    def getSkill(self):
        return self.__skill

    def wear(self):
        print('我是' + self.getSkill() + '工程师' + self._name)
        super().wear()


class Teacher(Person):

    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    def getTtile(self):
        return self.__title

    def wear(self):
        print('我司：' + self._name + self.getTtile())
        super().wear()


class ClothingDecorator(Person):

    def __init__(self, person):
        self._decorated = person


    def wear(self):
        self._decorated.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class CasualPantDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)


    def decorate(self):
        print('一条卡其色的裤子')




class DeltDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print('一条皮带')


def testCode():
    tony = Engineer('Tony', '客户端')
    pant = CasualPantDecorator(tony)
    belt = DeltDecorator(pant)
    belt.wear()
    print()


testCode()