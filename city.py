from os import name, sendfile


class City:
    """
    docstring
    """
    def __init__(self, name: str, dt=0) -> None:
        self.dt = dt
        self.name = name

    def __str__(self) -> str:
        info = self.name + ': ' + self.dt
        return info 

    def __repr__(self) -> str:
        return '{' + "'" + self.name + "' :" + str(self.dt) + '}'


    def set_dt(self, dt):
        if dt == None:
            self.set_dt(0)
        self.dt = dt

    @property
    def compare(self):
        return self.name
        
    def __lt__(self, other):
        return self.compare < other.compare
    
    def __eq__(self, other: object) -> bool:
       if (isinstance(other, City)):
           return self.name == other.name
       return False

    
    