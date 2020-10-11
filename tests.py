import  time
import requests
from requests.sessions import Session

from core.info_processor import D1_Handler
from core.info_processor import D2_Handler
from core.forecast import Forecast, access, get_full_forecast
import core.forecast 
from core.airports import IATA_handler as iata

API = 'ENTER_YOUR_API_KEY'

aproved = 0
total = 7

start_time = time.time()

def handle_non_existing_place():
    ''' Function to test if error handling is working for `Forecast.call_places()`.
    - It's expected for `Forecast.call_places()` to return `None` if something goes wrong within its excecution, in this case we're requesting
    forecast information from an empty string i.e. an nonexistent place.
     - Returns:
       - `1` : If the error is handled as expected
       - `0` : In other case
    '''
    f = Forecast(API)
    sess = Session()
    states = {}
    response = f.call_place(sess, ' ', states)
    if response == None:
        return 1
    return 0


def handle_bad_api_key():
    ''' Function to test if error handling is working for all `Forecast` function that requires an API Key to make a request.
    - It's expected for `Forecast` functions to return `None` if `requests.status_code` differs from `200` i.e. it couldn't complete the request 
    because we're requesting forecast information with an invalid or nonexistent URL. In this case we're using a bad API Key.
     - Returns:
       - `1` : If the error is handled as expected
       - `0` : In other case
    '''
    f = Forecast(' ')
    sess = Session()
    states = {}
    response = f.call_coordinates(sess, 'ACA', states)
    if response == None:
        return 1
    return 0

def handle_non_existing_local_data():
    ''' Function to test if error handling is working for `core.forecast` function `access()`.
    - It's expected for `access()` to return `None` if it couldn't reach target file. In this case we're tryng to `access()` a nonexistent file.
     - Returns:
       - `1` : If the error is handled as expected
       - `0` : In other case
    '''
    response = access(' ')
    if response == None:
        return 1
    return 0
    
def handling_non_existin_dir():
    ''' Function to test if error handling is working for `core.forecast` function `access()`.
    - It's expected for `access()` to return `None` if it couldn't reach target file. In this case we're tryng to `access()` a nonexistent file inside
     a nonexistent directory.
     - Returns:
       - `1` : If the error is handled as expected
       - `0` : In other case
    '''
    response = access('Tokyo.json', dir='unexpected')
    if response == None:
        return 1
    return 0

def handle_bad_iata_code():
    ''' Function to test if error handling is working for `IATA_Handler` functions.
    - It's expected for both of its methods `coordinates()` and `place()` to return a default value if they couldn't access the requested `dict` key. 
     - Returns:
       - `1` : If the error is handled as expected
       - `0` : In other case
    '''
    ia = iata()
    coords = ia.coordinates('')
    place = ia.place(' ')
    if place != None and coords != None:
        return 1
    return 0

def fetch_csv_data():
    ''' Function to test if error handling is working for `D1_Handler.__init__()`.
    - It's expected to initaliza a `D1_Handler` `object` with default value if it couldn't reach the specified `.csv` file. 
     - Returns:
       - `1` : If the error is handled as expected
       - `0` : In other case
    '''
    d = D1_Handler(' ')
    if d != None:
        return 1
    return 0

def fetch_csv_data2():
    ''' Function to test if error handling is working for `D2_Handler.__init__()`.
    - It's expected to initaliza a `D2_Handler` `object` with default value if it couldn't reach the specified `.csv` file. 
     - Returns:
       - `1` : If the error is handled as expected
       - `0` : In other case
    '''
    d = D2_Handler(' ')
    if d != None:
        return 1
    return 0


def everythings_wrong():
    ''' Just a small test to check if everything behaves when more than one thing fails at the same time.
    Here we try to request forecast information of a nonexistent place from `IATA_Handler` with a bad API Key.
    - Returns:
      - `1` : If the error is handled as expected
      - `0` : If it's not
    '''
    f = Forecast(' ')
    sess = Session()
    states = {}
    ia = iata()
    place = ia.place(' ')
    response = f.call_place(sess, place, states)
    if response == None:
        return 1
    return 0



if __name__ == '__main__':
    print('Testing ... ')
    print('***'*20)
    print('Fetching info from a bad .csv ... ')
    aproved += fetch_csv_data()
    aproved += fetch_csv_data2()
    print('Requesting a non existant place ...')
    aproved += handle_non_existing_place()
    print('When you get a bad API Key ...')
    aproved += handle_bad_api_key()
    print('Accessing a non existing file ...')
    aproved += handle_non_existing_local_data()
    print('Fetching information from a bad IATA code...')
    aproved += handle_bad_iata_code()
    print('When everything goes wrong ...')
    aproved += everythings_wrong()
    print()

total_time = round(time.time() - start_time, 3)
print('***'*20)
sum_up = 'Completed {} tests in {} seconds'.format(total, total_time)

results = '\n --- {} tets passed, {} failed ---'.format(aproved, total - aproved)
print(sum_up, results)