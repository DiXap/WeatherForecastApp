import json


def get_data(city: object):
    """
    Obtenemos la informacion de un serializable JSON
    """
    data = {}
    
    with open('./Data/' + city.name + '.json') as target:
        data = json.load(target)
    return data


def get_world() -> dict:
    """ Obtiene informacion del contenido de la base de datos
    """
    data = {}
    try:
        with open('./Data/World.json', 'r', encoding='utf-8') as target:
            data = json.load(target)
    except:
        create_world(data)
        get_world()
    return data


def save_world(data: dict): #TODO Deprecar
    world = get_world()
    world.update(data)
    with open('./Data/World.json', 'w', encoding='utf-8') as outfile:
        json.dump(world, outfile, indent=2)


def create_world(): # TODO Testeo. Ver si no rompe codigo
    """ Sobre-escribe el Diccionario donde se almacenan los State
    """
    world = {}
    with open('./Data/World.json', 'w', encoding='utf-8') as outfile:
        json.dump(world, outfile, indent=2)
