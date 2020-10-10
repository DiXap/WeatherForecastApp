# Third party imports
import pandas as pnd

# Local app imports
from .airports import IATA_handler as iata

class Origin():
    '''### Origin
    Generates an object which stores a place as `origin`
    '''
    def __init__(self, place: str):
        '''     Constructor
         - Args:
            - place (`str`): Name of the place you want to create as an `origin` object
        '''
        self.origin = place

    def set_origin(self, new_place: str):
        '''     Changes the current origin attribute of the object
         - Args:
            - new_place (`str`): Name of the place you want to set as new atribute for the `origin` object
        '''
        if new_place == None:
            self.origin = 'MEX'
        self.origin = new_place
    
    def __str__(self) -> str:
        return 'Coming from {}.'.format(self.origin)

class Destination():
    '''### Destination
    Generates an object which stores a place as `destination`
    '''
    
    def __init__(self, place: str):
        '''     Constructor
         - Args:
            - place (`str`): Name of the place you want to create as an `destination` object
        '''
        self.destination = place

    def set_destination(self, new_place: str):
        '''     Changes the current origin attribute of the object
         - Args:
            - new_place (`str`): Name of the place you want to set as new atribute for the `destination` object
        '''
        if new_place == None:
            self.destination = 'MEX'
        self.destination = new_place
    
    def __str__(self) -> str:
        return 'Arriving to {}.'.format(self.origin)

class D1_Handler():
    ''' Using `pandas` library reads and formats all the info fetched from a `.csv` file
    '''
    def __init__(self, csv: str):
        ''' Args:
         - csv (`str`): complete path to your `.csv` file 
        '''
        try:
            self.__data = pnd.read_csv(csv)
            self.__set = set()
            self._iata_decode = iata()
        except:
            self.__data = pnd.read_csv('./resources/dataset1.csv')
        
    def __fetch_departures(self):
        '''Fetches the departures column from a `.csv` file  
        - Creates `Origin` objects on the go and stores them inside a `set` to ensure there aren't duplicates
        '''
        departures = {d: {'origin': set()} for d in self.__data['origin']}
        for item in departures.items():
            origin = Origin(item[0])
            self.__set.add(origin.origin)

    def __fetch_arrivals(self):
        '''Fetches the arrivals column from a `.csv` file  
        - Creates `Destination` objects on the go and stores them inside a `set` to ensure there aren't duplicates
        '''
        arrivals = {d: {'destination': set()} for d in self.__data['destination']}
        for item in arrivals.items():
            destination = Destination(item[0])
            self.__set.add(destination.destination)

    def fetch(self) -> list:
        '''Fetches the all data from a `.csv` file  
        - Uses `self.__fetch_departures` and `self.__fetch_arrivals` to gather all information inside a `set`.
            Therefore, moves all data into a `list` and then sorts it.
        
        - Returns:
          - A sorted `list` with all departures an arrivals info
        '''
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
    ''' Using `pandas` library reads and formats all the info fetched from a `.csv` file
    '''
    def __init__(self, csv: str):
        ''' Args:
         - csv (`str`): complete path to your `.csv` file 
        '''
        try:
            self.__data = pnd.read_csv(csv, encoding='utf8')
            self.__set = set()
            self._iata_decode = iata()
        except:
            self.__data = None#pnd.read_csv('./resources/dataset2.csv')
        
    def __fetch_arrivals(self):
        '''Fetches the arrivals column from a `.csv` file  
        - Creates `Destination` objects on the go and stores them inside a `set` to ensure there aren't duplicates
        '''
        arrivals = {d: {'destino': set()} for d in self.__data['destino']}
        for item in arrivals.items():
            destination = Destination(item[0])
            self.__set.add(destination.destination)

    def fetch(self) -> list:
        '''Fetches the all data from a `.csv` file  
        - Uses `self.__fetch_arrivals` to gather all information inside a `set`.
            Therefore, moves all data into a `list` and then sorts it.
        
        - Returns:
          - A sorted `list` with all arrivals info
        '''
        self.__fetch_arrivals()
        list = sorted(self.__set) 
        return list
