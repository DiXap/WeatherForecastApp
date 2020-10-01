from state import State
from builtins import object

class States(object):
    """ Inicialmente una clase para almacenar los objetos State
    >Status: Deprecated
    """
    def __init__(self):
        self.states = {}
        
        
    def __iter__(self):
        return iter(self.states)

    def set_dict(self, dict):
        self.states = dict

    def add(self, state: State):
        self.__setitem__(state, state.cities)

    def __setitem__(self, item, value):
        self.states[item] = value

    def __getitem__(self, item):
        return self.states[item]

    
    def __repr__(self):
        return str(self.states)

    def keys(self):
        return self.states.keys()

    def items(self):
        return self.states.items()

    def values(self):
        return self.states.values()
    