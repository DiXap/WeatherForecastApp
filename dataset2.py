# -*- coding: utf-8 -*-
import pandas as pd

class D2Destination:
    """#### 
    Clase que crea los atributos para las petciones (origen)
    """
def __init__(self, destino: str):
    """    Constructor
        - Args:
          - origen (str): Origen del vuelo
        """
    self.destino = destino

def set_destino(self, destino: str):
    if destino == None:
        self.destino = 'MEX'
    self.destino = destino

def __str__(self) -> str:
    des = self.destino + ': ' + str(self.dt)
    return des


d1 = pd.read_csv("dataset2.csv", encoding='utf8')
print(d1['destino'])

desdata = {d: {'destino': set()} for d in d1['destino']}
for k in desdata.items():
    print("Origin Airport code:", k[0])
    D2Destination.destino = k[0]
    print(str(D2Destination.destino))
else:
    print('Error 404: Destination was not found')

data = {c: {'sal': set(), 'lle': set()} for c in d1['destino']}
for k, v in data.items():
    data[k]['sal'] |= set(d1[d1['destino'] == k] ['salida'])
    data[k]['lle'] |= set(d1[d1['destino'] == k] ['llegada'])

for k, v in data.items():
    if len(v['sal']) != 1 or len (v['lle']) != 1:
        print("Ariport code:", k)
        print("\tSalida:", v['sal'])
        print("\tLlegada:", v['lle'])
    else:
            print('Nothing was found')
