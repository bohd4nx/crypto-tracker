import time
import configparser
from api import *
from bot import send_message

config = configparser.ConfigParser()
config.read('config/config.ini')
tracked_coins = config['Cryptocurrencies']['cryptocurrency']
sleep_interval = int(config['Settings']['sleep_interval'])
exchanges_config = config['Exchanges']

previous_prices = {}


#     Here you can find a list of cryptocurrencies you can use. (The list is incomplete.)
#        ↘️                                                                    ↙️
#          https://github.com/7GitGuru/crypto-tracker/blob/main/coin-names.json

def main():
    while True:
        for coin in tracked_coins.split(','):
            try:
                prices = {}
                message = f"{coin.capitalize()} prices:\n"
                if exchanges_config.getboolean('binance'):
                    try:
                        price_binance = Binance(coin)
                        prices["Binance"] = price_binance
                    except Exception as e:
                        print(f"Binance error: {e}")
                if exchanges_config.getboolean('bybit'):
                    try:
                        price_bybit = Bybit(coin)
                        prices["Bybit"] = price_bybit
                    except Exception as e:
                        print(f"Bybit error: {e}")
                if exchanges_config.getboolean('bitfinex'):
                    try:
                        price_bitfinex = Bitfinex(coin)
                        prices["Bitfinex"] = price_bitfinex
                    except Exception as e:
                        print(f"Bitfinex error: {e}")
                if exchanges_config.getboolean('coinbase'):
                    try:
                        price_coinbase = Coinbase(coin)
                        prices["Coinbase"] = price_coinbase
                    except Exception as e:
                        print(f"Coinbase error: {e}")

                if len(prices) > 0:
                    for exchange, price in prices.items():
                        previous_price = previous_prices.get(coin, {}).get(exchange)
                        if previous_price is None:
                            emoji = "💲"
                        elif previous_price < price:
                            emoji = "📈"
                        elif previous_price > price:
                            emoji = "📉"
                        else:
                            emoji = "💲"
                        message += f"{emoji}{exchange}: ${price}\n"
                        previous_prices.setdefault(coin, {})[exchange] = price
                    send_message(message)
                else:
                    print(f"No exchanges available for {coin}")
            except Exception as e:
                print(f"Error: {e}")
        time.sleep(sleep_interval)


if __name__ == "__main__":
    main()
