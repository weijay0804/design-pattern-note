'''
Author: weijay
Date: 2022-10-12 21:24:43
LastEditors: weijay
LastEditTime: 2022-10-12 22:45:01
FilePath: /design-pattern2/Chapter1-Strategy/src/main.py
Description: 測試鴨鴨
'''

from duck import MallardDuck, ModelDuck
from flyBehavior import FlyWithRocket

if __name__ == '__main__':

    mallar = MallardDuck()

    mallar.performFly()
    mallar.performQuack()
    mallar.display()
    mallar.swim()

    model = ModelDuck()

    model.performFly()

    model.setFly(FlyWithRocket())

    model.performFly()