'''
Author: weijay
Date: 2022-10-15 23:15:05
LastEditors: weijay
LastEditTime: 2022-10-16 15:48:19
FilePath: /design-pattern2/Chapter2-Observer/src/interface.py
Description: 定義 interface
'''

from abc import ABC, abstractmethod

class ObserverInterface(ABC):
    ''' observer interface '''

    @abstractmethod
    def update(self):
        ''' 更新資料 '''
        pass

class SubjectInterface(ABC):
    ''' subject interface '''

    @abstractmethod
    def registerObserver(self, o: ObserverInterface):
        '''註冊觀察者

        Args:
            o (Observer): 觀察者
        '''
        pass

    @abstractmethod
    def removeObserver(self, o: ObserverInterface):
        '''移除觀察者

        Args:
            o (Observer): 觀察者
        '''
        pass

    @abstractmethod
    def notifyObservers(self):
        ''' 當資料更新時，通知觀察者們 '''
        pass

class DisplayElementInterface(ABC):
    ''' 顯示元素 interface '''

    @abstractmethod
    def display(self):
        ''' 顯示元素 '''
        pass



