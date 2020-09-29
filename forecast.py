import json, os, requests
from city import City

api = '1192a5270a138f03ee3e5add35415f3e'
states = {}
#data = {}
cities = []

def update(cities):
    
    pass

def consult(city: object, state, cities, states):
    """
    docstring
    """
    #ct = City(city)
    
    
    ow_url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}&units=metric'.format(city.name, state, api)
    
    try:
        response = requests.get(ow_url)    
    except requests.exceptions.RequestException:
        return

    data = json.loads(response.text)
    with open('./Data/' + city.name + '.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

    try:
        city.set_dt(data['dt'])
    except:
        pass

    cities.append(city)
    cities.sort()
    #cities.update({ct.name : ct.dt})
    states[state] = cities;
    return data;
    

tokyo = City('Tokyo')
print(consult(tokyo, 'JP', cities, states))
consult(City('Sapporo'), 'JP', cities, states)
consult(City('Okinawa'), 'JP', cities, states)

aux = []
consult(City('Cancun'), 'MX', aux, states)

#print(d)

c = City('Tokyo')
#c1 = City('Mom')
#d = [c, c1]

if tokyo in states['JP']:
    print(tokyo)

print(
    states
)


print()