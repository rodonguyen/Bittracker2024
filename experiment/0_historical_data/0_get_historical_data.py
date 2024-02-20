import sys
sys.path.insert(0, '.')
import config
import requests



def get_and_save(API, coin, period, savefilename, custom_url=False):
    # url = f"https://rest.coinapi.io/v1/ohlcv/BITFINEX_SPOT_{coin}_USD/history?"+\
    # url = f"https://rest.coinapi.io/v1/ohlcv/KRAKEN_SPOT_{coin}_USDT/history?"+\
    # url = f"https://rest.coinapi.io/v1/ohlcv/BINANCE_SPOT_{coin}_USDT/history?" + \
    # url = f"https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_{coin}_USD/history?"+\
    
    url = f"https://rest.coinapi.io/v1/ohlcv/BINANCE_SPOT_{coin}_USDT/history?"+\
        f"period_id={period}&"+\
        f"limit=100000&output_format=csv&apiKey={API}"
    # Timeframe param: HRS, MIN

    download = requests.get(url)
    decoded_content = download.content.decode('utf-8')
    file = open(f"experiment/historical_data/{savefilename}_original.csv", 'w')
    file.write(decoded_content)
    file.close()
    print(f'Done: {coin} {period}')

# get_and_save(config.API_COINAPI1, 'BNB', '4HRS', 'bnb_4h')
# get_and_save(config.API_COINAPI2, 'BNB', '1HRS', 'bnb_1h')
# get_and_save(config.API_COINAPI3, 'XRP', '4HRS', 'xrp_4h')
# get_and_save(config.API_COINAPI4, 'XRP', '1HRS', 'xrp_1h')
# get_and_save(config.API_COINAPI5, 'SOL', '4HRS', 'sol_4h')
# get_and_save(config.API_COINAPI6, 'SOL', '1HRS', 'sol_1h')
# get_and_save(config.API_COINAPI5, 'BTC', '4HRS', 'btc_4h')
get_and_save(config.API_COINAPI6, 'ETH', '4HRS', 'eth_4h')
