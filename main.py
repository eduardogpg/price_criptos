import time
import requests

from app import UserCripto
from app import create_app

STOP_LIMIT = 50000
app = create_app()

def send_notification():
    print('El correo se envío')


def get_current_price(symbol, vs_currencies='usd'):
    
    response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies={vs_currencies}')
    
    if response.status_code == 200:
        payload = response.json()
        return payload[symbol][vs_currencies]


if __name__ == '__main__':
    
    # En cada iteración se va a hacer una petición al API

    while:
        
        # Iterar sobre los precios de las criptos
        price = get_current_price('bitcoin')

        for limit in UserCripto.select().where( UserCripto.stop_limit < price ):
            send_notification()

            UserCripto.update(stop_limit=None).where(UserCripto.id == limit.id).execute()

        time.sleep(20)

    