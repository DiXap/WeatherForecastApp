import pandas as pd

class D1Origin:
    """#### 
    Clase que crea los atributos para las petciones (origen)
    """
def __init__(self, origen: str):
    """    Constructor
        - Args:
          - origen (str): Origen del vuelo
        """
    self.origen = origen

def set_origen(self, origen: str):
    if origen == None:
        self.origen = 'MEX'
    self.origen = origen

def __str__(self) -> str:
    ori = self.origen + ': ' + str(self.dt)
    return ori

class D1Destination:
    """#### 
    Clase que crea los atributos para las petciones (destino)
    """
def __init__(self, destino: str):
    """    Constructor
        - Args:
          - destino (str): Destino del vuelo
        """
    self.destino = destino

def set_destino(self, destino: str):
    if destino == None:
        self.destino = 'MEX'
    self.destino = destino

def __str__(self) -> str:
    dest = self.destino + ': ' + str(self.dt)
    return dest

d1 = pd.read_csv("dataset1.csv")
print(d1['origin'])

oridata = {d: {'origin': set()} for d in d1['origin']}
for k in oridata.items():
    print("Origin Airport code:", k[0])
    D1Origin.origen = k[0]
    print(str(D1Origin.origen))
else:
    print('Error 404: Origin was not found')

desdata = {d: {'destination': set()} for d in d1['destination']}
for k in desdata.items():
    print("Destination Airport code:", k[0])
    D1Destination.destino = k[0]
    print(str(D1Destination.destino))
else:
    print('Error 404: Destination was not found')

data = {c: {'lat': set(), 'lon': set()} for c in d1['origin']}
for k, v in data.items():
    data[k]['lat'] |= set(d1[d1['origin'] == k] ['origin_latitude'])
    data[k]['lon'] |= set(d1[d1['origin'] == k]['origin_longitude'])
    data[k]['lat'] |= set(d1[d1['destination'] == k] ['destination_latitude'])
    data[k]['lon'] |= set(d1[d1['destination'] == k]['destination_latitude'])

for k, v in data.items():
    if len(v['lat']) != 1 or len (v['lon']) != 1:
        print("Ariport code:", k)
        print("\tLatitudes found:", v['lat'])
        print("\tLongitudes found:", v['lon'])
    else:
            print('Nothing was found')
