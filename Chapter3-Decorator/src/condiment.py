'''
Author: weijay
Date: 2022-10-16 20:32:17
LastEditors: weijay
LastEditTime: 2022-10-16 21:05:57
FilePath: /design-pattern2/Chapter3-Decorator/src/condiment.py
Description: condiment (decorator) 抽象類別
'''

from abc import ABC

from beverage import Beverage

class CondimentDecorator(Beverage, ABC):
    ''' condiment 抽象類別 '''

    beverage: Beverage

    def getDescription(self) -> str:
        pass

class Mocha(CondimentDecorator):
    ''' 摩卡 '''

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    def getDescription(self) -> str:

        return self.beverage.getDescription() + ", 摩卡"

    def cost(self) -> int:
        return self.beverage.cost() + 10

class Soy(CondimentDecorator):
    ''' 豆漿 '''

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    def getDescription(self) -> str:

        return self.beverage.getDescription() + ", 豆漿"

    def cost(self) -> int:

        return self.beverage.cost() + 5

class Whip(CondimentDecorator):
    ''' 奶泡 '''

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    def getDescription(self) -> str:

        return self.beverage.getDescription() + ", 奶泡"

    def cost(self) -> int:

        return self.beverage.cost() + 3
