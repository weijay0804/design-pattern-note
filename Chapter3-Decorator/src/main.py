'''
Author: weijay
Date: 2022-10-16 20:57:13
LastEditors: weijay
LastEditTime: 2022-10-17 22:33:16
FilePath: /design-pattern/Chapter3-Decorator/src/main.py
Description: 實作飲料
'''

from condiment import Whip, Mocha, Soy
from beverage import Espresso, HouseBlend, DarkRoast

if __name__ == "__main__":

    beverage = Espresso()

    print(beverage.getDescription(), "cost: ", beverage.cost())

    beverage2 = HouseBlend()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)

    print(beverage2.getDescription(), "cost: ", beverage2.cost())

    beverage3 = DarkRoast()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)

    print(beverage3.getDescription(), "cost: ", beverage3.cost())

