import json


def get_world() -> dict:
    """ Obtains iformation from the local cache
    - Returns:
      - `dict`: with all cache info
    """
    data = {}
    try:
        with open('./Data/World.json', 'r', encoding='utf-8') as target:
            data = json.load(target)
    except:
        create_world(data)
        get_world()
    return data


def save_world(data: dict):
    ''' Saves current data into the cache as `json` file
    - Args:
      - data (`dict`): data to be stored
    '''
    world = get_world()
    world.update(data)
    with open('./Data/World.json', 'w', encoding='utf-8') as outfile:
        json.dump(world, outfile, indent=2)


def create_world():
    """ Creates a new cache
    """
    world = {}
    with open('./Data/World.json', 'w', encoding='utf-8') as outfile:
        json.dump(world, outfile, indent=2)
