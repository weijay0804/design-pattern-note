'''
Author: weijay
Date: 2022-10-16 20:28:37
LastEditors: weijay
LastEditTime: 2022-10-17 22:33:04
FilePath: /design-pattern/Chapter3-Decorator/src/beverage.py
Description: Beverage 抽象類別
'''

from abc import ABC, abstractmethod

class Beverage(ABC):
    ''' beverage 抽象類別 '''

    description: str = "未知的飲品"

    def getDescription(self) -> str:
        """ 取得飲品描述 """

        return self.description

    @abstractmethod
    def cost(self) -> int:
        ''' 計算價格 '''
        pass

class Espresso(Beverage):
    ''' 濃縮咖啡 '''

    def __init__(self) -> None:
        self.description = "濃縮咖啡"

    def cost(self) -> int:
        return 60

class HouseBlend(Beverage):
    ''' 家常咖啡 '''

    def __init__(self) -> None:
        self.description = "家常咖啡"

    def cost(self) -> int:
        return 30

class DarkRoast(Beverage):
    ''' 深度烘焙 '''

    def __init__(self) -> None:
        self.description = "深度烘焙"

    def cost(self) -> int:
        return 40
