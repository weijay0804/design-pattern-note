'''
Author: weijay
Date: 2022-10-15 21:27:37
LastEditors: weijay
LastEditTime: 2022-10-16 16:01:09
FilePath: /design-pattern2/Chapter2-Observer/src/weatherData.py
Description: 實作 weather data
'''

from dataclasses import dataclass, field
from typing import List

from interface import SubjectInterface, ObserverInterface

@dataclass
class WeatherData(SubjectInterface):
    ''' 實作 subject '''

    observers: List[ObserverInterface] = field(default_factory=list)
    temperature: float = field(init=False)
    humidity: float = field(init=False)
    pressure: float = field(init=False)

    def registerObserver(self, o: ObserverInterface):
        self.observers.append(o)

    def removeObserver(self, o: ObserverInterface):
        self.observers.remove(o)

    def notifyObservers(self):

        for i in self.observers:
            i.update()
    
    def measurementsChanged(self):
        ''' 當氣象站資料更新 '''

        self.notifyObservers()

    def setMeasurements(self, temp: float, humidity: float, pressure: float):
        ''' 模擬從氣象站取得氣象資料 '''

        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()

    def getTemperature(self):
        ''' 取得氣溫 '''

        return self.temperature

    def getHumidity(self):
        ''' 取得濕度 '''

        return self.humidity

    def getPressure(self):
        ''' 取得氣壓 '''

        return self.pressure