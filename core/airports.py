# Standard library imports
import json


class IATA_handler():
    '''### IATA_Handler
    Retrieves info from a local data base that contains all IATA codes and its relevant information.  
      * Refer to https://github.com/ram-nadella/airport-codes
    '''
    def __init__(self):
        with open('./Data/IATA_base/airports.json') as target:
            self.__data = json.load(target)

    def place(self, iata_code: str):
        '''  Retieves basic information based on a IATA code 
         - Args:
            - iata_code (`str`): IATA code to consult
         - Returns:
            - `str` containing:
              - `name` of the airport
              - `city` and `country` where it's located
        '''
        try:
          place = self.__data[iata_code]
          info = '\n' + place['name'] + '\n '
          info += place['city'] + ', ' + place['country']
          return info
        except:
          return self.place('NRT')

    def coordinates(self, iata_code: str):
        '''  Retieves coordinate information based on a IATA code 
         - Args:
            - iata_code (`str`): IATA code to consult
         - Returns:
            - `list` containing:
              - `latitude` and `longitude` where it's located
        '''
        try:
          iata_info = self.__data[iata_code]
          coords = [iata_info['latitude'], iata_info['longitude']]
          return coords
        except:
          return self.coordinates('NRT')
