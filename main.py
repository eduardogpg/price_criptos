import time
import requests

from app import User
from app import UserCripto
from app import CriptoCurrency

from app import create_app

STOP_LIMIT = 50000
app = create_app()

def insert_currencies():
    # CriptoCurrency.create(name='Bitcoin', symbol='BTC')
    CriptoCurrency.create(name='Terra', symbol='Luna')


def send_notification():
    print('El correo se envío!!!')


def get_current_price(symbol, vs_currencies='usd'):
    
    response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies={vs_currencies}')
    
    if response.status_code == 200:
        payload = response.json()
        return payload
    
    else:
        return None

if __name__ == '__main__':
    ids = [ cripto.name for cripto in CriptoCurrency.select(CriptoCurrency.name).execute() ]
    ids = ','.join(ids)

    if (prices := get_current_price(ids)):
        
        for cripto in prices.items():
            print(cripto)

    
    