from data import get_world, save_world
from forecst import Forecast
from info_processor import D1_Handler as data_1
from info_processor import D2_Handler as data_2
from some_fun import IATA_handler as iata

from asyncio import tasks
import asyncio, requests
from concurrent.futures import ThreadPoolExecutor

from requests.sessions import session

import time

start_time = time.time()

api = '1192a5270a138f03ee3e5add35415f3e'

f = Forecast(api)

iata_decode = iata()

states = get_world()

async def get_data(places_to_fetch: list, states):
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
    d1_coords = []

    d2 = data_2('./resources/dataset2.csv')
    d2_list = d2.fetch()
    #d2_coords = []
    call = d2_list[:70]
    print(call)

    #d2_coords = d2.fetch_coordinates()
    #print(d2_coords)
    

    #for iata in d1_list:
    #    d1_coords.append(iata)
    
    print(d1_list)
#
#
    #loop = asyncio.get_event_loop()
    #future = asyncio.ensure_future(get_data(d1_list, states))
    #loop.run_until_complete(future)
#
    #save_world(states)
    
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_data_place(call, states))
    loop.run_until_complete(future)
    
    save_world(states)


main()

print('--- %s seconds ---'% (time.time() - start_time))