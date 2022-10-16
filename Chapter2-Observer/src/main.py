'''
Author: weijay
Date: 2022-10-16 15:17:30
LastEditors: weijay
LastEditTime: 2022-10-16 16:44:29
FilePath: /design-pattern2/Chapter2-Observer/src/main.py
Description: 建立氣象站
'''

from weatherData import WeatherData
from displayItem import CurrentConditionsDisplay, StatisticsDisplay, ForecastDisplay

if __name__ == "__main__":

    weather_data = WeatherData()

    current_condition_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    # 模擬天氣數值更新
    weather_data.setMeasurements(
        25, 65, 30.4
    )

    print("-" * 20)

    weather_data.setMeasurements(
        27, 60, 30
    )

