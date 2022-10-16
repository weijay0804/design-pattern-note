'''
Author: weijay
Date: 2022-10-16 15:04:07
LastEditors: weijay
LastEditTime: 2022-10-16 16:43:59
FilePath: /design-pattern2/Chapter2-Observer/src/displayItem.py
Description: 建立顯示元素
'''

from dataclasses import dataclass, field

from interface import DisplayElementInterface, ObserverInterface
from weatherData import WeatherData

@dataclass
class CurrentConditionsDisplay(DisplayElementInterface, ObserverInterface):
    ''' 目前天氣狀況 '''

    weatherData: WeatherData
    humidity: float = field(init=False)
    temperature: float = field(init=False)

    def __post_init__(self):
        self.weatherData.registerObserver(self)

    def update(self):
        self.temperature = self.weatherData.getTemperature()
        self.humidity = self.weatherData.getHumidity()

        self.display()

    def display(self):
        print(f"目前天氣: 溫度: {self.temperature} 濕度: {self.humidity}")

@dataclass
class StatisticsDisplay(ObserverInterface, DisplayElementInterface):
    ''' 顯示氣溫統計 '''

    weatherData: WeatherData
    _maxTemp: float = field(init=False, default=0.0)
    _minTemp: float = field(init=False, default=200)
    _tempSum: float = field(init=False, default=0)
    _numReadings: int = field(init=False, default=0)

    def __post_init__(self):
        self.weatherData.registerObserver(self)

    def update(self):
        temp = self.weatherData.getTemperature()

        self._tempSum += temp
        self._numReadings += 1

        if temp > self._maxTemp:
            self._maxTemp = temp
        
        if temp < self._minTemp:
            self._minTemp = temp

        self.display()

    def display(self):
        print(f"平均溫度: {self._tempSum / self._numReadings} 最高溫度: {self._maxTemp} 最低溫度: {self._minTemp}")

@dataclass
class ForecastDisplay(ObserverInterface, DisplayElementInterface):
    ''' 顯示天氣預報 '''

    _currentPressure: float = field(init=False, default=29.92)
    _lastPressure: float = field(init=False, default=0)
    _weather_date: WeatherData

    def __post_init__(self):
        self._weather_date.registerObserver(self)

    def update(self):

        self._lastPressure = self._currentPressure
        self._currentPressure = self._weather_date.getPressure()

        self.display()

    def display(self):
        print("天氣預測: ")

        if self._currentPressure > self._lastPressure:
            print("天氣會持續變好")

        elif self._currentPressure == self._lastPressure:
            print("看樣子天氣會一樣")

        else:
            print("天氣會越來越糟")
