'''
This module contains API request function
'''

import requests
from json import dump

#Request weather data from OpenWeatherMap
def request(city, API):
    '''
    API call, stores json from current weather and from forecast in seperate files
    '''
    url_current = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}'
    response_current = requests.get(url_current)

    if response_current.status_code == 200:
        data_current = response_current.json()
        lat, lon = data_current['coord']['lat'], data_current['coord']['lon']
        current_file = open('./storage/current.json', 'w')
        dump(data_current, current_file)
        current_file.close()
        #Build url for forecast and send request
        url_forecast = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API}'
        response_forecast = requests.get(url_forecast)
        if response_forecast.status_code == 200:
            data_forecast = response_forecast.json()
            forecast_file = open('./storage/forecast.json', 'w')
            dump(data_forecast, forecast_file)
            forecast_file.close()
    else:
        print('Error fetching weather data')



