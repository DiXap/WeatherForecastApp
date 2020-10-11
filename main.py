# Standard library imports
import time
from asyncio import tasks
import asyncio, requests
from concurrent.futures import ThreadPoolExecutor
from requests.sessions import Session, session

# Local library imports
from core.data import  get_world, save_world
from core.forecast import Forecast
from core.info_processor import D1_Handler as data_1
from core.info_processor import D2_Handler as data_2
from core.airports import IATA_handler as iata

start_time = time.time()

API = 'ENTER_YOUR_API_KEY'

f = Forecast(API)

iata_decode = iata()

states = get_world()

async def get_data_iata(places_to_fetch: list, states):
    ''' This asyncronous func handles the multiple requests called by `Forecast.call_coordinates()`
     - Args:
        - places_to_fetch (`list`): A `list` containing IATA codes for the function to retrieve its Weather Forecast.
        - states: A python `dict` that contains the cache. 
    '''
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            loop = asyncio.get_event_loop()
            tasks = [
                loop.run_in_executor(
                    executor,
                    f.call_coordinates,
                    *(session, coords, states)
                )
                for coords in places_to_fetch
            ]
            for response in await asyncio.gather(*tasks):
                pass

async def get_data_place(places_to_fetch: list, states):
    ''' This asyncronous func handles the multiple requests called by `Forecast.call_place()`
     - Args:
        - places_to_fetch (`list`): A `list` containing city names for the function to retrieve its Weather Forecast.
        - states: A python `dict` that contains the cache. 
    '''
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            loop = asyncio.get_event_loop()
            tasks = [
                loop.run_in_executor(
                    executor,
                    f.call_place,
                    *(session, coords, states)
                )
                for coords in places_to_fetch
            ]
            for response in await asyncio.gather(*tasks):
                pass

def main():
    d1 = data_1('./resources/dataset1.csv')
    d1_list = d1.fetch()
    d1_coords = d1_list[:20:-1]

    d2 = data_2('./resources/dataset2.csv')
    d2_list = d2.fetch()
    call = d2_list[200:210]
    
   
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_data_iata(d1_coords, states))
    loop.run_until_complete(future)

    #save_world(states)
    
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_data_place(call, states))
    loop.run_until_complete(future)
    
    save_world(states)



if __name__ == '__main__':
    main()

print('--- Completed in %s seconds ---'% (round(time.time() - start_time, 3)))