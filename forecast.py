import json, os, requests
from city import City

api = 'API KEY goes here'
states = {}
#data = {}
cities = []

def update(cities):
    
    pass

def consult(city, state, cities):
    """
    docstring
    """
    ct = City(city)
      
    
    ow_url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}&units=metric'.format(ct.name, state, api)
    
    #try:
    response = requests.get(ow_url)    
    #except requests.exceptions.RequestException:
    #    return

    data = json.loads(response.text)
    with open('./Data/' + city + '.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

    #try:
    ct.set_dt(data['dt'])
    #except:
    #    pass

    cities.append(ct)
    cities.sort()
    #cities.update({ct.name : ct.dt})
    #states[state] = cities;
    return cities;
    

print(consult('Tokyo', 'JP', cities))
consult('Sapporo', 'JP', cities)
consult('Okinawa', 'JP', cities)
#consult('Cancun', 'MX')

#print(d)

#c = City('Tokyo')
#c1 = City('Mom')
#d = [c, c1]
print(cities)

print(
    states
)


print()