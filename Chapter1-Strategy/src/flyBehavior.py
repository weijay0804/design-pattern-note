'''
Author: weijay
Date: 2022-10-12 21:04:14
LastEditors: weijay
LastEditTime: 2022-10-12 22:41:21
FilePath: /design-pattern2/Chapter1-Strategy/src/flyBehavior.py
Description: 定義 fly 行為
'''

from abc import ABC, abstractmethod

class FlyInterface(ABC):
    ''' fly 行為的 interface '''

    @abstractmethod
    def fly(self):
        ''' 飛 '''
        pass

class FlyWithWings(FlyInterface):
    ''' 用翅膀飛 '''

    def fly(self):
        print("我在用翅膀飛")

class FlyNoWay(FlyInterface):
    ''' 不會飛 '''

    def fly(self):
        print("我不會飛")

class FlyWithRocket(FlyInterface):
    ''' 用火箭飛 '''

    def fly(self):
        print("我在用火箭飛")