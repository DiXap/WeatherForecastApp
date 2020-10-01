# -*- coding: utf-8 -*-
""" ### WeatherApp
Funciones principales de la aplicacion
    - Obtener informacion existente
    - Decidir si lo obtenido satisface los requerimientos
        - Si no -> Consumir API
    - Actualizar estructuras
    - Devolver informacion al usuario

Todo:
    * Tratar de mandar metodos especificos a sus clases
    * Manejar excepciones
        * Validar entradas para mitigar
    * Cambiar los EventHandler (temporal)
"""

import json, requests
from data import create_world, get_world
from state import State
from city import City

api = 'YOUR_APIKEY_GOES_HERE'
states = get_world()


def access(city: object) -> dict:
    """Accesa al archivo de una ciudad.    
    - Args:
      - city (City): Objeto City a consultar.
    
    - Returns:
      - Diccionario: Populado con la informacion obtenida. 
    """
    with open('./Data/' + city.name + '.json') as target:
        data = json.load(target)
    return data


def consult(city: City, state: State, states: dict): # TODO Cambios
    """#### Obtiene la informacion de una ciudad. 
    Consume el API si es una consulta nueva, obtiene la informacion de la base de datos local en otro caso.
    - Args:
      -                                                                                                                                                                                                                      city (City): Objeto City de donde obtendremos la informacion para la consulta.
      - state (State): Objeto City de donde obtendremos la informacion para la consulta.
      - states (dict): Diccionario donde almacenaremos los cambios hechos a la base de datos.
    
    - Returns:
      - Diccionario: Populado con la informacion obtenida.
    """
    ow_url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}&units=metric'.format(city.name, state.name, api)
    
    # consulta la estructura de datos para verificar la existencia de yuna ciudad
    try:
        if city.name in states[state.name]:
            print('no') # TODO Event handler
            return access(city)
    except:
        pass
    
    # consume la API
    try:
        response = requests.get(ow_url)  
    except requests.exceptions.RequestException:
        return

    # TODO Pasar a func independiente
    # crea un diccionario con la informacion obtenida
    data = json.loads(response.text)
    with open('./Data/' + city.name + '.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

    # cambia el atributo de City
    try:
        city.set_dt(data['dt'])
    except:
        pass

    # actualiza la informacion de las edd
    state.add(city)
    insert = {state.name : state.cities}
    states.update(insert)

    print('yes') #TODO Event handler
    # actualiza la info de la edd de la base de datos
    create_world(states)

    return data;
    


tokyo = City('Tokyo')
jp = State('JP')


print(consult(tokyo, jp, states))
consult(tokyo, jp, states)
consult(City('Sapporo'), jp, states)
consult(City('Okinawa'), jp, states)

consult(City('Cancun'), State('MX'), states)

c = City('Tokyo')

if jp in states:
    print(tokyo)


print(
    states
)

