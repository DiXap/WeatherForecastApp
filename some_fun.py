import json
from airports import from_iata

def iata_coords(code: str):
    data = from_iata(code)
    lat = data['latitude']
    long = data['longitude']
    return [lat, long]


class IATA_handler():

    def __init__(self):
        #self._coords = iata_coords(iata_code)
        with open('./Data/IATA_base/airports.json') as target:
            self.__data = json.load(target)
        #self.__coords = self.__data[iata_code]

    def place(self, iata_code: str):
        place = self.__data[iata_code]
        info = '\n' + place['name'] + '\n '
        info += place['city'] + ', ' + place['country']
        return info

    def coordinates(self, iata_code: str):
        iata_info = self.__data[iata_code]
        coords = [iata_info['latitude'], iata_info['longitude']]
        return coords

    #def latitude(self):
    #    return self.__coords['latitude']
    #
    #def longitude(self):
    #    return self.__coords['longitude']
        
    #def __str__(self) -> str:
    #    info = self.__coords['name'] + '\n '
    #    info += self.__coords['city'] + ', ' + self.__coords['country']
    #    return info