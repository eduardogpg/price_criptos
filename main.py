import requests

# TODO
# Consultar el precio
# Envíar un correo
# Leer de una base de datos para saber los usuarios y las criptos relacionadas!

def get_current_price(symbol, vs_currencies='usd'):
    
    response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies={vs_currencies}')
    
    if response.status_code == 200:
        payload = response.json()
        return payload[symbol][vs_currencies]


if __name__ == '__main__':
    print(
        get_current_price('bitcoin')
    )
    