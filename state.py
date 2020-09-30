from json import JSONEncoder
import json

class State(object):

    def __init__(self, name: str):    
        self.name = name
        self.cities = []

    def __str__(self) -> str:
       info = self.name + ': ' + str(self.cities)
       return info 

    def __repr__(self) -> str:
        return "'" + self.name + "'"


    def set_name(self, name: str):
        if name == None:
            self.name = 'Germany'
        self.name = name


    #def __hash__(self):
    #    return hash((self.name))

    def __key(self):
        return (self.name)

    def __hash__(self) -> int:
        return hash(self.__key())
    
    def __eq__(self, other) -> bool:
        if isinstance(other, State):
            return self.__key() == other.__key()
        return NotImplemented
        


#class StateEncoder(JSONEncoder):
#    """
#    docstring
#    """
#    def default(self, object):
#        if isinstance(object, State):
#            return object.__dict__
#        else:
#            return json.JSONEncoder.default(self, object)