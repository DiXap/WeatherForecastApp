import pandas as pnd
from some_fun import IATA_handler as iata
from geopy.geocoders import Nominatim as geo

class Origin():
    
    def __init__(self, place: str):
        self.origin = place

    def set_origin(self, new_place: str):
        if new_place == None:
            self.origin = 'MEX'
        self.origin = new_place
    
    def __str__(self) -> str:
        return 'Coming from {}.'.format(self.origin)

class Destination():
    
    def __init__(self, place: str):
        self.destination = place

    def set_destination(self, new_place: str):
        if new_place == None:
            self.destination = 'MEX'
        self.destination = new_place
    
    def __str__(self) -> str:
        return 'Arriving to {}.'.format(self.origin)

class D1_Handler():
    
    def __init__(self, csv: str):
        self.__data = pnd.read_csv(csv)
        self.__set = set()
        self._iata_decode = iata()
        
    def __fetch_departures(self):
        departures = {d: {'origin': set()} for d in self.__data['origin']}
        for item in departures.items():
            origin = Origin(item[0])
            self.__set.add(origin.origin)

    def __fetch_arrivals(self):
        arrivals = {d: {'destination': set()} for d in self.__data['destination']}
        for item in arrivals.items():
            destination = Destination(item[0])
            self.__set.add(destination.destination)

    def fetch(self) -> list:
        self.__fetch_arrivals()
        self.__fetch_departures()
        list = sorted(self.__set)
        return list

    def _fetch_coordinates(self) -> list:
        list = self.fetch()
        coords = []
        for iata in list:
            aux = self._iata_decode.coordinates(iata)
            coords.append(aux)
        return coords


class D2_Handler():
    
    def __init__(self, csv: str):
        self.__data = pnd.read_csv(csv, encoding='utf8')
        self.__list = list()
        self._iata_decode = iata()
        
    def __fetch_arrivals(self):
        arrivals = {d: {'destino': list()} for d in self.__data['destino']}
        for item in arrivals.items():
            destination = Destination(item[0])
            self.__list.append(destination.destination)

    def fetch(self) -> list:
        self.__fetch_arrivals()
        self.__list.sort()
        return self.__list
