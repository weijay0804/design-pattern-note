'''
Author: weijay
Date: 2022-10-12 21:16:59
LastEditors: weijay
LastEditTime: 2022-10-12 21:19:26
FilePath: /design-pattern2/Chapter1-Strategy/src/quackBehavior.py
Description: 定義 quack 行為
'''

from abc import ABC, abstractmethod

class QuackInterface(ABC):
    ''' 鴨子叫 '''

    def quack(self):
        ''' 叫 '''

        pass

class Quack(QuackInterface):
    ''' 普通鴨子叫 '''

    def quack(self):
        print("呱呱")

class MuteQuack(QuackInterface):
    ''' 不會叫 '''

    def quack(self):
        print("我不會叫")

class Squeak(QuackInterface):
    ''' 唧唧叫 '''

    def quack(self):
        print("唧唧唧")
