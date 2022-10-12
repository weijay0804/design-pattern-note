'''
Author: weijay
Date: 2022-10-12 21:03:10
LastEditors: weijay
LastEditTime: 2022-10-12 22:40:26
FilePath: /design-pattern2/Chapter1-Strategy/src/duck.py
Description: Duck 類別
'''

from abc import ABC, abstractmethod

from flyBehavior import FlyInterface, FlyWithWings, FlyNoWay
from quackBehavior import QuackInterface, Quack, MuteQuack

class Duck(ABC):
    ''' duck 抽象類別 '''

    def __init__(self, flyBehavior: FlyInterface, quackBehavior: QuackInterface):
        self._flyBehavior = flyBehavior
        self._quackBehavior = quackBehavior

    @abstractmethod
    def display(self):
        ''' 顯示鴨鴨 '''
        pass

    def performFly(self):
        self._flyBehavior.fly()

    def setFly(self, fb: FlyInterface):
        self._flyBehavior = fb

    def performQuack(self):
        self._quackBehavior.quack()

    def setQuack(self, qu: QuackInterface):
        self._quackBehavior = qu

    def swim(self):
        print("所有的鴨子都飄在水上")

class MallardDuck(Duck):

    def __init__(self):
        super().__init__(flyBehavior=FlyWithWings(), quackBehavior=Quack())

    def display(self):
        print("我是 mallar duck")

class ModelDuck(Duck):

    def __init__(self):
        super().__init__(flyBehavior=FlyNoWay(), quackBehavior=Quack())

    def display(self):
        print("我是 modle 鴨")