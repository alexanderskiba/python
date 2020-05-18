# класс будет принимать на вход название города и будет иметь метод,
# который будет возвращать прогноз погоды в этом городе
import pprint
import requests
from dateutil.parser import parse

class YahooWeatherForecast:
    def get(self, city): # Запросы на сайт Yahoo
        url = f"https://query.yahooapis.com/v1/public/yql?" \
              f"q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20" \
              f"(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{city}" \
              f"%22)%20and%20u%3D%27c%27&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
        data = requests.get(url).json()
        forecast_data = data["query"]["results"]["channel"]["item"]["forecast"] #query - Это словарь, который  находится на верхнем уровне, results внутри query
        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date": day_data[date],
                "high_temp": day_data["high"]
            })
        return forecast

class CityInfo:


    def __init__(self, city, weather_forecast = None): # Принимает название города
        self.city = city
        self._weather_forecast = weather_forecast or YahooWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)


def _main():
    city_info = CityInfo("Moscow")
    forecast = city_info.weather_forecast() # Данный метод вернет нам список погоды на несколько дней вперед
    pprint.pprint(forecast) #pretty-print


if __name__ == "__main__":
    _main()  # _ - значит приватная функция

