# Standard library imports
import json, requests
from requests.sessions import session

# Third party imports
import unidecode

# Local app imports
from .airports import IATA_handler as iata



def access(coordinates, dir='./Data') -> dict:
   try:
       with open(dir + '/' + str(coordinates) + '.json') as target:
           data = json.load(target)
       return data
   except:
      print('Info not accesible')
      return

def save(response, coordinates: str , dir='./Data'):
   data = json.loads(response.text)
   with open(dir + '/' + coordinates +'.json', 'w', encoding='utf-8') as outfile:
       json.dump(data, outfile, ensure_ascii=False, indent=4)
   return data

def get_full_forecast(coordinates, time= 'current'):
    raw = None
    try:
        raw = access(coordinates)
    except:
        return
    weather = raw[time]['weather'][0]['main'] 
    weather_desc = raw[time]['weather'][0]['description']
    temp = str(raw[time]['temp'])
    feels_temp = str(raw[time]['feels_like'])
    uvi = str(raw[time]['uvi'])
    humidity =  str(raw[time]['humidity'])
    pressure = str(raw[time]['pressure'])
    info = 'Weather: {} as {} \nCurrent temp: {}°C \n\tbut feels like: {}°C \nUVI: {} \nHumidity: {}%  Pressure: {}Pa'
    report = info.format(weather, weather_desc, temp, feels_temp, uvi, humidity, pressure)
    return report


def get_todays_forecast(place):
    raw = None
    try:
        raw = access(place, dir='./Data/set2')
    except:
        return
    weather = raw['weather'][0]['main'] 
    weather_desc = raw['weather'][0]['description']
    temp = str(raw['main']['temp'])
    feels_temp = str(raw['main']['feels_like'])
    max_temp = str(raw['main']['temp_max'])
    min_temp = str(raw['main']['temp_min'])
    humidity =  str(raw['main']['humidity'])
    pressure = str(raw['main']['pressure'])
    info = 'Weather: {} as {} \nCurrent temp: {}°C \n\tbut feels like: {}°C \n\tMax temp: {}°C  Min temp: {}°C \nHumidity: {}%  Pressure: {}Pa'
    report = info.format(weather, weather_desc, temp, feels_temp, max_temp, min_temp, humidity, pressure)
    return report



class Forecast():
    def __init__(self, api_key) :
        self.__api = api_key
        self._iata = iata()

    
    def call_coordinates(self, session, place, states: dict):
        ow_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly&appid={}&units=metric'
        
        coordinates = self._iata.coordinates(place)
        response = None
        t = str(coordinates[0]) + '_' + str(coordinates[1])
        
        if t in states:
            print(self._iata.place(place) + '\n' + get_full_forecast(t) + '\n') 
            return 

        with session.get(ow_url.format(coordinates[0], coordinates[1], self.__api)) as response:
            if response.status_code != 200:
                return
        
        try:
            to_save = save(response, t)
            more = {t: to_save['current']['dt']}
            states.update(more)
            print(self._iata.place(place) + '\n' + get_full_forecast(t) + '\n')
        except:
            print('Cant request a forecast for ' + self._iata.place(place) + '\n' + get_todays_forecast('Tokyo') + '\n')


    
    def call_place(self, session, place, states: dict):
        ow_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&exclude=minutely,hourly&appid={}&units=metric'
        
        response = None
        pl = unidecode.unidecode(place)
        
        if pl in states:
            print(place + '\n' + get_todays_forecast(pl) + '\n') 
            return 

        with session.get(ow_url.format(place, self.__api)) as response:
            if response.status_code != 200:
                return
        
        try:
            to_save = save(response, pl, dir='./Data/set2')
            more = {pl: to_save['dt']}
            states.update(more)
            print(place + '\n' + get_todays_forecast(pl) + '\n')
        except:
            print('Cant request a forecast for ' + place + '\n' + get_todays_forecast('Tokyo') + '\n')
        


    