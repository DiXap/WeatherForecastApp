import json
import airporttime


def from_iata(code: str):
    apt = airporttime.AirportTime(iata_code=code)
    d = apt.airport.__dict__
    return d


def iata_coords(code: str):
    data = from_iata(code)
    lat = data['latitude']
    long = data['longitude']
    return [lat, long]


class IATA_handler():

    def __init__(self):
        with open('./Data/IATA_base/airports.json') as target:
            self.__data = json.load(target)

    def place(self, iata_code: str):
        place = self.__data[iata_code]
        info = '\n' + place['name'] + '\n '
        info += place['city'] + ', ' + place['country']
        return info

    def coordinates(self, iata_code: str):
        iata_info = self.__data[iata_code]
        coords = [iata_info['latitude'], iata_info['longitude']]
        return coords
