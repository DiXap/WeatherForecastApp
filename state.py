from json import JSONEncoder
import json
from city import City

class State:
    """#### State
    Clase para adecuar la infromacion recibida segun los requerimientos para consumir la API
    """
    def __init__(self, name: str): 
        #TODO Modificar name antes de asignarlo:
        # - convertir a ISO-3. Usar librieria 'country_converter'
        """     Constructor
        - Args:
          - name (str): Nombre del pais
        """   
        self.name = name
        self.cities = {}


    def __repr__(self) -> str:
        return self.name 

    
    def __str__(self) -> str:
        return self.name + ': ' + str(self.cities)

    def set_name(self, name: str):
        if name == None:
            self.name = 'Germany'
        self.name = name

    def add(self, city: City):
        insert = {city.name : city.dt}
        self.cities.update(insert)


    def __key(self):
        return (self.name)

    def __hash__(self) -> int:
        return hash(self.__key())
    
    def __eq__(self, other) -> bool:
        if isinstance(other, State):
            return self.__key() == other.__key()
        return False
        

