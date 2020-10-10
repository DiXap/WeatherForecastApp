import  time
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
    f = Forecast(API)
    sess = Session()
    states = {}
    response = f.call_place(sess, ' ', states)
    if response == None:
        return 1
    return 0


def handle_bad_api_key():
    f = Forecast(' ')
    sess = Session()
    states = {}
    response = f.call_coordinates(sess, 'ACA', states)
    if response == None:
        return 1
    return 0

def handle_non_existing_local_data():
    response = access(' ')
    if response == None:
        return 1
    return 0
    
def handling_non_existin_dir():
    response = access('Tokyo.json', dir='unexpected')
    if response == None:
        return 1
    return 0

def handle_bad_iata_code():
    ia = iata()
    coords = ia.coordinates('')
    place = ia.place(' ')
    if place != None and coords != None:
        return 1
    return 0

def fetch_csv_data():
    d = D1_Handler(' ')
    if d != None:
        return 1
    return 0

def fetch_csv_data2():
    d = D2_Handler(' ')
    if d != None:
        return 1
    return 0


def everythings_wrong():
    f = Forecast(API)
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
    print('Getting a bad API Key ...')
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