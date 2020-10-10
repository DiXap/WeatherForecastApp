# Standard library imports
import json, requests
from numpy.lib.function_base import place
from requests.sessions import session

# Third party imports
import unidecode

# Local app imports
from .airports import IATA_handler as iata



def access(place, dir='./Data') -> dict:
    '''  Retieves all weather information stored in a `.json` file of a place after the  call 
         - Args:
            - place (`str`): place to consult
            - dir= : directory where the function should look for your `.json` file
         - Returns:
            - `dict` containing all weather data
    '''
    try:
        with open(dir + '/' + str(place) + '.json') as target:
            data = json.load(target)
        return data
    except:
       return 

def save(response, place: str , dir='./Data'):
    '''  Saves all weather information in a `.json` file of a place after the `requests` call 
         - Args:
            - response: the `requests` response
            - place (`str`): place to be saved
            - dir= : directory where the function should store your `.json` file
         - Returns:
            - `dict` containing all weather data
    '''
    data = json.loads(response.text)
    with open(dir + '/' + place +'.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
    return data

def get_full_forecast(place, time= 'current'): # TODO time arg still under development
    ''' Fetches and formats all weather data from a place already stored
      - Args:
        - place: place to consult
        - time= : what day of the week you want the weather forecast of. 
      - Returns:
         - `str` containing:
           - `weather` and `description`
           - `current temperature` and `thermal sensation`
           - `uv index`, `humidity` and `pressure`
    '''
    raw = None
    try:
        raw = access(place)
        if raw == None:
            return
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
    ''' Fetches and formats all current weather data from a place already stored
      - Args:
        - place: place to consult
      - Returns:
         - `str` containing:
           - `weather` and `description`
           - `current temperature`, `thermal sensation`, `max temperature` and `min temperature`
           - `uv index`, `humidity` and `pressure`
    '''
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
    '''### Forecast
    Creates an object that is able to manage `OpenWeather` API calls through `requests` library
      * `request`, `stores` and `retrives`  
      Weather forescast data
    '''
    def __init__(self, api_key) :
        ''' Args:
         - api_key (`str`): insert yor `OpenWeather` API Key here 
        '''
        self.__api = api_key
        self._iata = iata()

    
    def call_coordinates(self, session, place, states: dict):
        ''' Makes an API call with the coordinates of the IATA place provided
          - Args:
            - place: IATA code to consult
            - session: from `requests.session`, allows it to run inside an async function
            - states (`dict`): cointaining the cache
          - Prints:
             - Weather forecast data
        '''
        ow_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly&appid={}&units=metric'
        
        coordinates = self._iata.coordinates(place)
        response = None
        t = str(coordinates[0]) + '_' + str(coordinates[1])
        
        if t in states:
            print(self._iata.place(place) + '\n' + get_full_forecast(t) + '\n') 
            return get_full_forecast(t)

        with session.get(ow_url.format(coordinates[0], coordinates[1], self.__api)) as response:
            if response.status_code != 200:
                return None
        
        try:
            to_save = save(response, t)
            more = {t: to_save['current']['dt']}
            states.update(more)
            print(self._iata.place(place) + '\n' + get_full_forecast(t) + '\n')
            return get_full_forecast(t)
        except:
            print('Cant request a forecast for ' + self._iata.place(place) + '\n')
            return None


    
    def call_place(self, session, place, states: dict):
        ''' Makes an API call with the name of a place provided
          - Args:
            - place: name to consult
            - session: from `requests.session`, allows it to run inside an async function
            - states (`dict`): cointaining the cache
          - Prints:
             - Today's weather forecast data
        '''
        ow_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&exclude=minutely,hourly&appid={}&units=metric'
        
        response = None
        pl = unidecode.unidecode(place)
        
        if pl in states:
            print(place + '\n' + get_todays_forecast(pl) + '\n') 
            return get_todays_forecast(pl)

        with session.get(ow_url.format(place, self.__api)) as response:
            if response.status_code != 200:
                return None
        
        try:
            to_save = save(response, pl, dir='./Data/set2')
            more = {pl: to_save['dt']}
            states.update(more)
            print(place + '\n' + get_todays_forecast(pl) + '\n')
            return get_todays_forecast(pl)
        except:
            print('Cant request a forecast for ' + place + '\n')
            return None
        


    