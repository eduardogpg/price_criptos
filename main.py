import time
import requests

from app import db

# TODO
# Consultar el precio
# Envíar un correo si y solo si se llega a un stop limit
# Leer de una base de datos para saber los usuarios y las criptos relacionadas!

STOP_LIMIT = 50000

def send_notification():
    print('El correo se envío')


def get_current_price(symbol, vs_currencies='usd'):
    
    response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies={vs_currencies}')
    
    if response.status_code == 200:
        payload = response.json()
        return payload[symbol][vs_currencies]


if __name__ == '__main__':
    while True:
        price = get_current_price('bitcoin')
        
        if price >= STOP_LIMIT:
            send_notification()

        time.sleep(15)