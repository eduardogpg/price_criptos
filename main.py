import time
import requests

from app import User
from app import UserCripto
from app import CriptoCurrency

from app import create_app

app = create_app()

def insert_currencies():
    CriptoCurrency.create(name='Bitcoin', symbol='BTC', coingecko_id='bitcoin')
    CriptoCurrency.create(name='Terra', symbol='Luna', coingecko_id='terra-luna')


def send_notification(email, symbol, price):
    print(f'Una noficiación será enviada a {email} por que el precio de la cripto {symbol} esta en {price}')


def get_current_price(symbol, vs_currencies='usd'):
    
    response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies={vs_currencies}')
    
    if response.status_code == 200:
        payload = response.json()
        return payload
    
    else:
        return None

if __name__ == '__main__':

    while True:
        ids = [ cripto.coingecko_id for cripto in CriptoCurrency.select(CriptoCurrency.coingecko_id).execute() ]
        ids = ','.join(ids)

        if (prices := get_current_price(ids)):
            
            for name, price in prices.items():

                user_criptos = ( UserCripto.select()
                .join(CriptoCurrency)
                .where(CriptoCurrency.name==name)
                .where(UserCripto.stop_limit < price['usd']))
                
                for user_cripto in user_criptos.execute():

                    send_notification(user_cripto.user.email,
                                    user_cripto.criptocurrency.symbol,
                                    price['usd'])

                    

        time.sleep(5)

            

    
    