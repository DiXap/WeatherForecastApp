from json.encoder import JSONEncoder
import json
import jsonpickle


class City:
    """#### City
    Clase para adecuar la infromacion recibida segun los requerimientos para consumir la API
    """
    def __init__(self, name: str, dt=0): 
        #TODO Entrada 
        # Modificar los parametros antes de asignarlos al objeto: pasar name a lower case
        """    Constructor
        - Args:
          - name (str): Nombre de la ciudad
          - dt (int): Hora en que se hizo la consulta a la API (en UTC)
        """
        self.dt = dt 
        self.name = name

    def __str__(self) -> str:
        info = self.name + ': ' + str(self.dt)
        return info 

    def __repr__(self) -> str:
        return self.name

    def set_dt(self, dt):
        if dt == None:
            self.set_dt(0)
        self.dt = dt

    def set_name(self, name: str):
        if name == None:
            self.name = 'Tokyo'
        self.name = name


    @property
    def compare(self):
        return self.name
        
    def __lt__(self, other):
        return self.compare < other.compare
    
    def __eq__(self, other: object) -> bool:
       if (isinstance(other, City)):
           return self.__key() == other.__key()
       return False

    def __key(self):
        return (self.name)

    def __hash__(self) -> int:
        return hash(self.__key())


class CityHandler(jsonpickle.handlers.BaseHandler): #TODO Ver si el codificadore aun nos sirve (tentativamente deprecar)
    """
    Auxiliar para codificar un objeto City
    """
    def flatten(self, obj, data):
        """
        docstring
        """
        return [self.context.flatten(x,reset=False) for x in obj.contents]
