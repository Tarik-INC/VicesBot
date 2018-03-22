import requests

BASE_URL = "https://api.coinmarketcap.com/v1/ticker/"

def get_btc_price(**kwargs):

    try:
        r = requests.get(BASE_URL, params=kwargs)
    except r.raise_for_status():
        print(r.status_code)

    data = r.json()

    result = f"{data[0]['symbol']} price: 1 BTC ={float(data[0]['price_brl']):0.2f} BRL "

    return result
 


def main():
    get_btc_price(ULR="https://api.coinmarketcap.com/v1/ticker/", convert="BRL", limit=10)


if __name__ == '__main__':
    main()
