############################### 모듈 import #####################################
import json
import pyupbit
import talib
import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import pandas as pd
import time
import webbrowser
import numpy as np
import time
import requests
import datetime 

krw_tickers1 = ["BTC", "ETH", "NEO", "MTL", "XRP", "ETC", "OMG", "SNT", "WAVES",
            "XEM", "QTUM", "LSK", "STEEM", "XLM", "ARDR", "ARK", "STORJ", "GRS",
            "REP", "ADA", "SBD", "POWR", "BTG", "ICX", "EOS", "TRX", "SC",
            "ONT", "ZIL", "POLYX", "ZRX", "LOOM", "BCH", "BAT", "IOST", "RFR",
            "CVC", "IQ", "IOTA", "ONG", "GAS", "UPP", "ELF", "KNC",
            "BSV", "THETA", "QKC", "AVAX", "MOC", "ENJ", "TFUEL", "MANA",
            "ANKR", "AERGO", "ATOM", "TT", "CRE", "MBL", "WAXP", "HBAR", "MED",
            "MLK", "STPT", "ORBS", "VET", "CHZ", "STMX", "DKA", "HIVE", "KAVA",
            "AHT", "LINK", "XTZ", "BORA", "JST", "CRO", "TON", "SXP", "HUNT",
            "PLA", "DOT", "SRM", "MVL", "STRAX", "AQT", "GLM", "SSX", "META",
            "FCT2", "CBK", "SAND", "HUM", "DOGE", "STRK", "PUNDIX", "FLOW",
            "DAWN", "AXS", "STX", "XEC"]

# Define constants
COIN_LIST = ["BTC", "ETH", "DOGE", "HIVE", "EOS", "ADA", "NEO", "BORA"]
BUYDOWN_PERCENT = 0.988
INVEST_MONEY = 30000
HOUR = 60 * 60

BUY_WAITING_LIST = {}

# Slack Bot Settings
myToken = "XXXXXXXXXXXXXXXXXXXXXXX" # your slack bot token
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel, "text": text}
    )
    print(response)

def main():
    while True:
        try:
            # Get the current time
            now = datetime.datetime.now()

            # Step 1: Get the list of coins to trade
            coins_to_trade = [coin for coin in COIN_LIST if coin in pyupbit.get_tickers("KRW")]
        
        except Exception as e:
         print(e)
        # Send an error message to Slack or other notification service
import json
import pyupbit
import jwt
import talib
import uuid
import hashlib
from urllib.parse import urlencode
import pandas as pd
import time
import webbrowser
import numpy as np
import time
import requests
import datetime 
import time
import talib.abstract as ta


############################### 프로그램 상수 #####################################
access_key = "YOUR ACCESS KEY"
secret_key = "YOUR SECRET KEY"
myToken = "YOUR SLACK BOT TOKEN"


################################# 함수 ####################################
upbit = pyupbit.Upbit(access_key, secret_key) # upbit 사용하기 위함

# Set the target coins

# Define constants
COIN_LIST = ["BTC", "ETH", "DOGE", "HIVE", "EOS", "ADA", "NEO", "BORA"]
BUYDOWN_PERCENT = 0.988
INVEST_MONEY = 30000
HOUR = 60 * 60

BUY_WAITING_LIST = {}
###################################


# Set the minimum balance of KRW to continue trading
MIN_KRW_BALANCE = 100000

# Set the percentage threshold for price decrease to buy
BUYDOWN_PERCENT = 0.016

# Set the amount of KRW to invest in each coin
INVEST_KRW = 30000

# Define the time constants in seconds
HOUR = 3600
THREE_HOURS = HOUR * 3
# Define the coins subject to automatic trading
COINS = ["BTC", "ETH", "DOGE", "HIVE", "EOS", "ADA", "NEO", "BORA"]

# Initialize empty lists to temporarily store coins
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
list_6 = []
list_7 = []
list_8 = []

# Define the threshold values for the indicators
D_THRESHOLD = 75
K_THRESHOLD = 60
        for coin in list_8:
            if (coin in list_1) and (coin in list_2) and (coin in list_3) and (coin in list_4) and (coin in list_5) and (coin in list_6) and ((coin in list_7) or (coin in list_1)):

# Define the buy waiting list to store coins that satisfy all conditions
BUY_WAITING_LIST = {}

# Define the function to send messages to Slack
def post_message(token, channel, text):
    """Send a Slack message"""
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + token},
        data={"channel": channel, "text": text},
    )

# define the function to get the stochastic slow weekly indicator value
def get_stochastic_slow_weekly_indicator(coin):
    # make API call to get the stochastic slow weekly indicator value for the coin
    url = f'https://api.example.com/stochastic-slow-weekly?coin={coin}'
    response = requests.get(url)
    value = response.json()['value']
    return value

# define the function to get the stochastic slow daily indicator value
def get_stochastic_slow_daily_indicator(coin):
    # make API call to get the stochastic slow daily indicator value for the coin
    url = f'https://api.example.com/stochastic-slow-daily?coin={coin}'
    response = requests.get(url)
    value_k = response.json()['value_k']
    value_d = response.json()['value_d']
    return (value_k, value_d)

# define the function to get the stochastic slow 240-minute indicator value
def get_stochastic_slow_240_indicator(coin):
    # make API call to get the stochastic slow 240-minute indicator value for the coin
    url = f'https://api.example.com/stochastic-slow-240?coin={coin}'
    response = requests.get(url)
    value_k = response.json()['value_k']
    value_d = response.json()['value_d']
    return (value_k, value_d)

# define the function to get the stochastic slow 60-minute indicator value
def get_stochastic_slow_60_indicator(coin):
    # make API call to get the stochastic slow 60-minute indicator value for the coin
    url = f'https://api.example.com/stochastic-slow-60?coin={coin}'
    response = requests.get(url)
    value_k = response.json()['value_k']
    value_d = response.json()['value_d']
    return (value_k, value_d)

# define the function to get the MACD daily indicator value
def get_macd_daily_indicator(coin):
    # make API call to get the MACD daily indicator value for the coin
    url = f'https://api.example.com/macd-daily?coin={coin}'
    response = requests.get(url)
    value_macd = response.json()['value_macd']
    value_signal = response.json()['value_signal']
    return (value_macd, value_signal)

# define the function to get the MACD 60-minute indicator value
def get_macd_60_indicator(coin):
    # make API call to get the MACD 60-minute indicator value for the coin
    url = f'https://api.example.com/macd-60?coin={coin}'
    response = requests.get(url)
    value_macd = response.json()['value_macd']
    value_signal = response.json()['value_signal']
    return (value_macd, value_signal)
coins = []

def get_coins(my_coins):
    upbit_tickers = pyupbit.get_tickers()
    for coin in my_coins:
        if coin in upbit_tickers:
            coins.append(coin)
    return coins
upbit_tradable_coins = get_coins(my_coins)
print(coins)



###################################
# 11. Buy coins
def buy_coins(coins_to_buy):
    for coin in coins_to_buy:
        # Check if the current price has fallen by 1.6% or less
        current_price = get_current_price(coin)
        if current_price <= coin['price'] * 0.984:
            # Check if the MACD value has risen and exceeded the signal value
            if is_macd_rising(coin['symbol'], '5m'):
                # Buy the coin at the market price with 30,000 won
                order_result = market_buy(coin['symbol'], 30000 / current_price)
                if order_result['status'] == 'FILLED':
                    # Delete the coin from the temporary storage list and the coin waiting list
                    delete_coin_from_list(coin, coin_1)
                    print(f"Bought {coin['symbol']} at {current_price} KRW")

# 12. Delete a coin from the temporary storage list and the coin waiting list
def delete_coin_from_list(coin, coin_list):
    for i in range(len(coin_list)):
        if coin_list[i]['symbol'] == coin['symbol']:
            del coin_list[i]
            break

# 13. Delete coins stored for more than 3 hours in the temporary storage list and the coin waiting list
def delete_old_coins():
    current_time = datetime.now()
    for coin_list in [list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8]:
        for i in range(len(coin_list)):
            coin_time = coin_list[i]['time']
            if (current_time - coin_time).total_seconds() / 3600 > 3:
                del coin_list[i]
                break
#############################
# Define function to get Stochastic Slow values
def get_stoch_values(ticker, interval):
    df = pyupbit.get_ohlcv(ticker, interval=interval, count=14)
    slowk, slowd = talib.STOCH(df['high'], df['low'], df['close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    return slowk[-1], slowd[-1]

# Define function to get MACD values
def get_macd_values(ticker, interval):
    df = pyupbit.get_ohlcv(ticker, interval=interval)
    macd, macdsignal, macdhist = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return macd[-1], macdsignal[-1]

# Define function to get OBV values
def get_obv_value(ticker, interval):
    df = pyupbit.get_ohlcv(ticker, interval=interval)
    obv = talib.OBV(df['close'], df['volume'])
    return obv[-1]

##########################################            #####################################
            import json
import pyupbit
import jwt
import talib
import uuid
import hashlib
from urllib.parse import urlencode
import pandas as pd
import time
import webbrowser
import numpy as np
import time
import requests
import datetime 
import time
import talib.abstract as ta


############################### 프로그램 상수 #####################################
access_key = "YOUR ACCESS KEY"
secret_key = "YOUR SECRET KEY"
myToken = "YOUR SLACK BOT TOKEN"


################################# 함수 ####################################
upbit = pyupbit.Upbit(access_key, secret_key) # upbit 사용하기 위함

# Set the target coins

# Define constants
coins = ["BTC", "ETH", "DOGE", "HIVE", "EOS", "ADA", "NEO", "BORA"]
BUYDOWN_PERCENT = 0.988
INVEST_MONEY = 30000
HOUR = 60 * 60

BUY_WAITING_LIST = {}

# Set the minimum balance of KRW to continue trading
MIN_KRW_BALANCE = 100000

# Set the percentage threshold for price decrease to buy
BUYDOWN_PERCENT = 0.016

# Set the amount of KRW to invest in each coin
INVEST_KRW = 30000

# Define the time constants in seconds
HOUR = 3600
THREE_HOURS = HOUR * 3
# Define the coins subject to automatic trading
import pyupbit
import talib
import time
import requests

# Step 1: Define the coins to trade
COINS = ["BTC", "ETH", "DOGE", "HIVE", "EOS", "ADA", "NEO", "BORA"]

# Step 2: Define the list to store coins from Stochastic Slow weekly index
list_1 = []

# Step 3: Define the list to store coins from Stochastic Slow daily index
list_2 = []

# Step 4: Define the list to store coins from Stochastic Slow 240 minute index
list_3 = []

# Step 5: Define the list to store coins from Stochastic Slow 60 minute index
list_4 = []

# Step 6: Define the list to store coins from MACD daily index
list_5 = []

# Step 7: Define the list to store coins from MACD 60 minute index
list_6 = []

# Step 8: Define the list to store coins from MACD 30 minute index
list_7 = []

# Step 9: Define the list to store coins from OBV 60 minute index
list_8 = []

# Step 10: Define the list to store coins satisfying all conditions for trading
Coin_1 = []

# Define API keys and slack webhook url
access_key = "your-access-key"
secret_key = "your-secret-key"
slack_url = "https://hooks.slack.com/services/your-webhook-url"

# Define Upbit object using API keys
upbit = pyupbit.Upbit(access_key, secret_key)

# Step 10: Find coins that meet all conditions and add to Coin-1 waiting for purchase
for coin in coins:
    if coin in list_1 and coin in list_2 and coin in list_3 and coin in list_4 and coin in list_5 and coin in list_6 and coin in list_7 and coin in list_8:
        Coin_1.append({"coin": coin, "price": get_current_price(coin), "time": datetime.now()})
        print(coin, " meets all conditions")
        send_slack_message(coin + " meets all conditions")

# Print coins in Coin-1 waiting for purchase
print("Coins in Coin-1 waiting for purchase: ")
for coin in Coin_1:
    print(coin["coin"], " ", coin["price"], " ", coin["time"])
    send_slack_message(coin["coin"] + " " + str(coin["price"]) + " " + str(coin["time"]))


##############################################################################
                      
# Step 2: Get coins with k value rising and D value less than 75 in weekly Stochastic Slow
list_1 = []
for coin in coins:
    data = pyupbit.get_ohlcv(coin, interval="week")
    slow_k, slow_d = ta.STOCH(data['high'], data['low'], data['close'])
    if slow_k[-1] > slow_k[-2] and slow_d[-1] > slow_d[-2] and slow_d[-1] < 75:
        list_1.append(coin)
print(f"List-1: {list_1}")

# Step 3: Get coins with k value rising, k value greater than D value, and D value less than 60 in daily Stochastic Slow
list_2 = []
for coin in coins:
    data = pyupbit.get_ohlcv(coin)
    slow_k, slow_d = ta.STOCH(data['high'], data['low'], data['close'])
    if slow_k[-1] > slow_k[-2] and slow_d[-1] > slow_d[-2] and slow_k[-1] > slow_d[-1] and slow_d[-1] < 60:
        list_2.append(coin)
print(f"List-2: {list_2}")

# Step 4: Get coins with k value rising and k value larger than D value in 240-minute Stochastic Slow
list_3 = []
for coin in coins:
    data = pyupbit.get_ohlcv(coin, interval="minute240")
    slow_k, slow_d = ta.STOCH(data['high'], data['low'], data['close'])
    if slow_k[-1] > slow_k[-2] and slow_k[-1] > slow_d[-1]:
        list_3.append(coin)
print(f"List-3: {list_3}")

# Step 5: Get coins with k value rising and k value greater than D value in 60-minute Stochastic Slow
list_4 = []
for coin in coins:
    data = pyupbit.get_ohlcv(coin, interval="minute60")
    slow_k, slow_d = ta.STOCH(data['high'], data['low'], data['close'])
    if slow_k[-1] > slow_k[-2] and slow_k[-1] > slow_d[-1]:
        list_4.append(coin)
print(f"List-4: {list_4}")

# Step 6: Get coins with rising signal value and macd value greater than signal value in daily MACD
list_5 = []
for coin in coins:
    data = pyupbit.get_ohlcv(coin)
    macd, macd_signal, _ = ta.MACD(data['close'])
    if macd[-1] > macd_signal[-1] and macd[-1] > macd[-2] and macd_signal[-1] > macd_signal[-2]:
        list_5.append(coin)
print(f"List-5: {list_5}")

# Step 7: Get coins with rising signal value in 60-minute MACD
list_6 = []
for coin in coins:
    data = pyupbit.get_ohlcv(coin, interval="minute60")
    macd, macd_signal, _ = ta.MACD(data['close'])
    if macd[-1] > macd_signal[-1] and macd_signal[-1] > macd_signal[-2]:
        list_6.append(coin)
print(f"List-6: {list_6}")

# Step 8: MACD 30-minute indicator
# Temporary storage list for coins with rising MACD value and breakout of signal value
list_7 = []
for coin in coins:
    data = pyupbit.get_ohlcv(coin, interval="minute30")
    macd, macd_signal, _ = ta.MACD(data['close'])
    if macd[-1] > macd[-2] and macd_signal[-1] < macd_signal[-2] and macd[-1] > macd_signal[-1]:
        list_7.append(coin)
print(f"List-7: {list_7}")

# Step 9: OBV 60-minute index
# Temporary storage list for coins with OBV value greater than signal value
list_8 = []
for coin in coins:
    data = pyupbit.get_ohlcv(coin, interval="minute60")
    obv = talib.OBV(data['close'])
    if obv[-1] > talib.SMA(obv, timeperiod=10)[-1]:
        list_8.append(coin)
print(f"List-8: {list_8}")

# Step 10: Store information for coins satisfying all conditions
Coin_1 = []
for coin in list_1:
    if (coin in list_2) and (coin in list_3) and (coin in list_4) and (coin in list_5) and (coin in list_6) and (coin in list_7) and (coin in list_8):
        price = pyupbit.get_current_price(coin)
        Coin_1.append((coin, price))
        print(coin, price)
        post_message(myToken,"#upbit1", coin+" buy at : " +str(price))

import time

watchlist = ['BTC', 'ETH', 'DOGE', 'HIVE', 'EOS', 'ADA', 'NEO', 'BORA']
buy_waitlist = []
sell_waitlist = []

def check_buy_conditions(ticker):
    # Check Condition 1: Stochastic Slow Daily
    df = pyupbit.get_ohlcv(ticker, interval="day", count=28)
    df_ta = talib.abstract.Stoch(df, 5, 3, 3)
    if df_ta['slowk'][-1] > df_ta['slowk'][-2] and df_ta['slowk'][-2] > df_ta['slowk'][-3] and df_ta['slowd'][-1] < 75:
        # Check Condition 2: MACD 30-minute
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=60)
        df_ta = talib.abstract.MACD(df)
        if df_ta['macdhist'][-1] > 0 and df_ta['macdhist'][-2] < 0:
            price = pyupbit.get_current_price(ticker)
            buy_waitlist.append({'ticker': ticker, 'price': price, 'time': time.time()})
            print(f"{ticker} added to buy_waitlist")
        
def check_sell_conditions(ticker, bought_price):
    # Check for sell conditions
    curr_price = pyupbit.get_current_price(ticker)
    if curr_price <= bought_price * 0.93:
        print(f"Selling {ticker} at market price {curr_price}")
        pyupbit.sell_market_order(ticker, 30000)
        sell_waitlist.remove({'ticker': ticker, 'price': bought_price})
    elif curr_price >= bought_price * 1.07:
        print(f"Selling {ticker} at market price {curr_price}")
        pyupbit.sell_market_order(ticker, 30000)
        sell_waitlist.remove({'ticker': ticker, 'price': bought_price})

while True:
    for ticker in watchlist:
        if ticker not in [x['ticker'] for x in buy_waitlist]:
            check_buy_conditions(ticker)

    for item in buy_waitlist:
        ticker = item['ticker']
        bought_price = item['price']
        curr_price = pyupbit.get_current_price(ticker)
        if curr_price <= bought_price * 0.984:
            df = pyupbit.get_ohlcv(ticker, interval="minute5", count=12)
            df_ta = talib.abstract.MACD(df)
            if df_ta['macdhist'][-1] > 0 and df_ta['macdhist'][-2] < 0:
                print(f"Buying {ticker} at market price {curr_price}")
                pyupbit.buy_market_order(ticker, 30000)
                sell_waitlist.append({'ticker': ticker, 'price': curr_price})
                buy_waitlist.remove(item)
                time.sleep(1800)
        elif time.time() - item['time'] > 10800:
            buy_waitlist.remove(item)

    for item in sell_waitlist:
        ticker = item['ticker']
        bought_price = item['price']
        check_sell_conditions(ticker, bought_price)

    time.sleep(180)
   # Check purchase list at 3-minute intervals
    time.sleep(180)
    for i, item in enumerate(purchase_list):
        current_price = pyupbit.get_current_price(f"KRW-{item['coin']}")
        if current_price < item['price'] * 0.984:
            # Check MACD 5-minute indicator
            df = pyupbit.get_ohlcv(f"KRW-{item['coin']}", "minute5", count=100)
            macd, macdsignal, macdhist = pyupbit.ta.macd(df['close'])
            if (macdhist[-1] > 0) and (macdhist[-2] < 0):
                # Place buy order
                krw_balance = pyupbit.get_balance("KRW")
                order_size = min(30000, int(krw_balance / current_price))
                if order_size > 0:
                    upbit.buy_market_order(f"KRW-{item['coin']}", order_size)
                    purchase_list.pop(i)
                    
        # Remove item from purchase list after 60 minutes
        elif time.time() - item['time'] > 3600:
            purchase_list.pop(i)
            
        # Sell coin when purchase price drops below 7%
        elif current_price < item['price'] * 0.93:
            coin_balance = pyupbit.get_balance(f"{item['coin']}")
            if coin_balance > 0:
                upbit.sell_market_order(f"KRW-{item['coin']}", coin_balance)

def buy_wait_coins(coin):
    upbit_tickers = pyupbit.get_tickers()
    for coin in coins:
        if coin in list_1:
            if coin in list_2:
                if coin in list_3:
                    buy_waitlist.append(coin)
    return buy_waitlist
try:
    # Get the list of tradable coins
    tickers = pyupbit.get_tickers()
    
    # Iterate over the list of tradable coins in buy_waitlist1
    for coin in buy_waitlist1:
        # Get the temporarily stored price and time     
        ticker = coin['ticker']  # Access the 'ticker' key from the dictionary
        current_price = pyupbit.get_current_price(ticker)
        
        if always_true():
            print(f"{coin['ticker']} Buy Waiting List {current_price} {now}")
            # Append a dictionary with 'ticker', 'price', and 'time' keys to buy_waitlist
            buy_waitlist.append({'ticker': ticker, 'price': current_price, 'time': time.time()})
            post_message(myToken, "#upbit1", coin['ticker'] + " buy waiting list at: " + str(current_price))
            
            # Access the 'price' and 'time' keys from the dictionary
            temp_price = coin['price']
            temp_time = coin['time']
            
            # Check if the current price is below 1.2% from the temporarily stored price
            if macd_min5(ticker):
                if current_price < temp_price * buydown_percent:
                    # Place a market buy order for the coin with 30,000 won
                    krw_balance = upbit.get_balance("KRW")
                    if krw_balance > invest_money * 1.01:
                        order = upbit.buy_market_order(ticker, invest_money)
                        print(f"{ticker} bought at {current_price}")
                        # Remove the coin from both buy_waitlist and buy_waitlist1
                        buy_waitlist1.remove(coin)
                        buy_waitlist.remove(coin)
            # Check if the coin has been on the buy waiting list continuously for more than 6 hours
            elif time.time() - temp_time > 10800:
                buy_waitlist1.remove(coin)
                buy_waitlist.remove(coin)
                print(f"{ticker} removed from the buy waiting list")
                
    print("Coins in Buy waiting-1:", buy_waitlist1)
    #print("Coins in Buy waiting:", buy_waitlist)

    # Wait for 10 seconds before checking again
    time.sleep(10)

except Exception as e:
    print(f"Error_B: {e}")
#######################

import pyupbit
import time

# Define the coins to be traded
coins = ['BTC', 'ETH', 'DOGE', 'HIVE', 'EOS', 'ADA', 'NEO', 'BORA']

# Define the waiting list for coins to be bought
buy_waiting_list = {}

# Define the function to check the envelope 30-minute indicator
def check_envelope(coin):
    df = pyupbit.get_ohlcv(coin, interval='minute30', count=2)
    prev_close = df.iloc[0]['close']
    curr_close = df.iloc[1]['close']
    ma = df['close'].rolling(window=20).mean()
    std = df['close'].rolling(window=20).std()
    lower = ma - (2 * std)
    if prev_close < lower[0] and curr_close > lower[1]:
        return True
    else:
        return False

# Define the function to place a buy order
def place_buy_order(coin):
    orderbook = pyupbit.get_orderbook(coin)
    sell_price = orderbook['asks'][0]['price']
    buy_price = sell_price * 0.985
    resp = upbit.buy_market_order(coin, buy_price, 30000)
    return resp

# Define the function to place a sell order
def place_sell_order(coin):
    balance = upbit.get_balance(coin)
    resp = upbit.sell_market_order(coin, balance)
    return resp

# Connect to the Upbit API
access_key = 'your-access-key'
secret_key = 'your-secret-key'
upbit = pyupbit.Upbit(access_key, secret_key)

while True:
    for coin in coins:
        # Check if the coin satisfies the condition
        if check_envelope(coin):
            # Save the coin to the waiting list
            if coin not in buy_waiting_list:
                buy_waiting_list[coin] = {'price': pyupbit.get_current_price(coin), 'time': time.time()}
        
        # Check if the buy order can be executed
        if coin in buy_waiting_list:
            current_price = pyupbit.get_current_price(coin)
            if current_price <= buy_waiting_list[coin]['price'] * 0.985:
                place_buy_order(coin)
                del buy_waiting_list[coin]
            elif time.time() - buy_waiting_list[coin]['time'] > 1800:
                del buy_waiting_list[coin]
        
        # Check if the sell order can be executed
        balance = upbit.get_balance(coin)
        avg_buy_price = upbit.get_avg_buy_price(coin)
        if balance > 0 and (pyupbit.get_current_price(coin) <= avg_buy_price * 0.93 or pyupbit.get_current_price(coin) >= avg_buy_price * 1.07):
            place_sell_order(coin)
    
    # Wait for 10 seconds before checking again
    time.sleep(10)
##################
try:
    # Iterate over the list of tradable coins
    for coin in coin_list:
        if coin in buy_waitlist:
            current_price = pyupbit.get_current_price(coin)
            buy_price = buy_waitlist[coin]['price']
            # Check if the buy order can be executed
            if current_price <= buy_price * 0.985:
                if macd_min5:
                    place_buy_order(coin)
                    del buy_waitlist[coin]
            elif current_price >= buy_price * 1.07:
                place_sell_order(coin)
                del buy_waitlist[coin]
        else:
            if macd_min30:
                price = pyupbit.get_current_price(coin)
                if price <= envelope_min30[coin]:
                    buy_waitlist[coin] = {'price': price, 'time': time.time()}
                    buy_waitlist1[coin] = {'price': price, 'time': time.time()}

    # Remove coins that have been in the buy waitlist for more than 30 minutes
    for coin in buy_waitlist.copy().keys():
        if time.time() - buy_waitlist[coin]['time'] > 1800:
            del buy_waitlist[coin]
            del buy_waitlist1[coin]

    # Wait for 1 minute before checking again
    time.sleep(60)
except Exception as e:
    print(f"Error_B: {e}")

        # Step 10: Check envel min240
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if envelope_min240(coin):
               list_11.append(coin)

def check_buy_conditions(ticker):
    # Get 240-minute envelope indicator
    df_240 = pyupbit.get_ohlcv(ticker, interval='minute240')
    ma_240 = df_240['close'].rolling(window=20).mean()
    std_240 = df_240['close'].rolling(window=20).std()
    upper_240 = ma_240 + 2 * std_240
    lower_240 = ma_240 - 2 * std_240

    # Get current price and indicators
    df = pyupbit.get_ohlcv(ticker, interval='minute60')
    close = df['close']
    low = df['low'].rolling(14).min()
    high = df['high'].rolling(14).max()
    fast_k = (close - low) / (high - low) * 100
    slow_k = fast_k.rolling(3).mean()
    slow_d = slow_k.rolling(3).mean()
    ma_60 = close.rolling(window=20).mean()
    std_60 = close.rolling(window=20).std()
    upper_60 = ma_60 + 2 * std_60
    lower_60 = ma_60 - 2 * std_60

    # Check buy conditions
    if (close[-2] < lower_240[-2] and close[-1] > lower_240[-1]) or (slow_k[-1] > slow_d[-1] and slow_k[-2] > slow_d[-2] and slow_k[-3] > slow_d[-3]):
        return True
    else:
        return False
    # Define the function to check the envelope indicator
envelope_periods = 240
envelope_deviation = 0.03

def envelope_min240(coin):
    df = pyupbit.get_ohlcv(f"{coin}", interval='minute240')
    if df is None:
        return
    close = df['close']
    ma = close.rolling(envelope_periods).mean()
    std = close.rolling(envelope_periods).std()
    upper_band = ma + envelope_deviation * std
    lower_band = ma - envelope_deviation * std
    if (((close[-2] < lower_band[-2] or close[-3] < lower_band[-3]) and (close[-1] > lower_band[-1])) or
    ((close[-2] < ma[-2] or close[-3] > ma[-3]) and (close[-1] > ma[-1]))) or ma[-2] <= ma[-1] :
        return True
    return False
import time
import pyupbit

# Define the list of coins subject to automatic trading
coins = ['BTC', 'ETH', 'DOGE', 'HIVE', 'EOS', 'ADA', 'NEO', 'BORA']

# Define the investing parameters
invest_money = 30000  # KRW
profit_rate = 0.07  # Sell the coin when the profit rate drops below this value

# Define the envelope 240-minute indicator parameters
envelope_period = 240  # minutes
envelope_ma_period = 20  # minutes
envelope_upper_shift = 0.05
envelope_lower_shift = 0.05

# Define the buy waiting list and the sell waiting list
buy_waitlist = []
sell_waitlist = []

# Define the Upbit API access key and secret key
access_key = "your-access-key"
secret_key = "your-secret-key"
upbit = pyupbit.Upbit(access_key, secret_key)


def check_envelope_indicator(ticker):
    # Get the candle data of the coin for the envelope 240-minute indicator
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=envelope_period)

    # Calculate the moving averages for the upper and lower envelopes
    ma_upper = df['close'].rolling(envelope_ma_period).mean() * (1 + envelope_upper_shift)
    ma_lower = df['close'].rolling(envelope_ma_period).mean() * (1 - envelope_lower_shift)

    # Check if the current value of the coin is above the lower envelope or if the middle envelope is rising 3 times
    current_price = pyupbit.get_current_price(ticker)
    if current_price > ma_lower.iloc[-1]:
        return True
    elif ma_lower[-3] < ma_lower[-2] < ma_lower[-1] and ma_lower[-1] < current_price < ma_upper[-1]:
        return True
    else:
        return False


def buy_coin(ticker, current_price):
    # Place a buy order for the coin with the given amount of money
    upbit.buy_market_order(ticker, invest_money)
    print(f"Bought {ticker} at {current_price} KRW")
    post_message(myToken, "#upbit1", f"Bought {ticker} at {current_price} KRW")


def sell_coin(ticker, buy_price, current_price):
    # Calculate the profit rate and sell the coin if it drops below the target
    profit_rate = (current_price / buy_price) - 1
    if profit_rate < -0.07:
        upbit.sell_market_order(ticker, upbit.get_balance(ticker))
        print(f"Sold {ticker} at {current_price} KRW with {profit_rate * 100:.2f}% loss")
        post_message(myToken, "#upbit1", f"Sold {ticker} at {current_price} KRW with {profit_rate * 100:.2f}% loss")
    else:
        print(f"Profit rate of {ticker} is {profit_rate * 100:.2f}%")

        
def monitor_buy_waitlist():
    # Check the market price of the coins on the buy waiting list every 3 minutes and buy if the price drops below 1.5%
    while buy_waitlist:
        for i in range(len(buy_waitlist)):
            coin = buy_waitlist[i]
            current_price = pyupbit.get_current_price(coin['ticker'])
            if current_price <= coin['price'] * 0.985:
               

# Create a function to check if a coin satisfies the buying condition
def check_buy_condition(ticker):
    # Get data for the last 240 minutes
    df = pyupbit.get_ohlcv(ticker, interval='minute240')
    # Calculate the envelope indicator
    ma = df['close'].rolling(20).mean()
    std = df['close'].rolling(20).std()
    upper = ma + 2 * std
    lower = ma - 2 * std
    # Check if the current price is above the lower band
    current_price = pyupbit.get_current_price(ticker)
    if current_price > lower[-1]:
        return True
    # Check if the middle band has risen 3 times in a row
    if (ma[-1] > ma[-2]) and (ma[-2] > ma[-3]):
        return True
    # Check if the value before the indicator was below the indicator and the current value is above the lower band
    if (df['close'][-2] < lower[-2]) and (current_price > lower[-1]):
        return True
    return False
################################################################
import time
import pyupbit
import pandas as pd

# Define the coins for automatic trading
coins = ['BTC', 'ETH', 'DOGE', 'HIVE', 'EOS', 'ADA', 'NEO', 'BORA']

# Define the Stochastic Slow Weekly Indicator function
def stoch_slow_weekly(ticker):
    df = pyupbit.get_ohlcv(ticker, interval='week')
    high_14 = df['high'].rolling(window=14).max()
    low_14 = df['low'].rolling(window=14).min()
    df['fast_k'] = (df['close'] - low_14) / (high_14 - low_14) * 100
    df['slow_k'] = df['fast_k'].rolling(window=3).mean()
    df['slow_d'] = df['slow_k'].rolling(window=3).mean()
    return df

# Define the Envelope 240-minute Indicator function
def envelope_240min(ticker):
    df = pyupbit.get_ohlcv(ticker, interval='minute240')
    ma20 = df['close'].rolling(window=20).mean()
    std20 = df['close'].rolling(window=20).std()
    upper = ma20 + std20*2
    lower = ma20 - std20*2
    middle = ma20
    return upper, middle, lower

while True:
    try:
        # Loop through the coins for automatic trading
        for coin in coins:
            # Check if the k value is on the rise and the D value is less than 75 in the Stochastic Slow Weekly Indicator
            df_stoch = stoch_slow_weekly(f'KRW-{coin}')
            latest_k, latest_d = df_stoch['slow_k'][-1], df_stoch['slow_d'][-1]
            prev_k, prev_d = df_stoch['slow_k'][-2], df_stoch['slow_d'][-2]
            if latest_k > prev_k and latest_d < 75:
                # Check if the coin meets the Envelope 240-minute Indicator condition
                upper, middle, lower = envelope_240min(f'KRW-{coin}')
                latest_price = pyupbit.get_current_price(f'KRW-{coin}')
                prev_price = pyupbit.get_ohlcv(f'KRW-{coin}', interval='minute240')['close'][-2]
                if prev_price < lower[-2] and latest_price > lower[-1]:
                    # Buy the coin at the market price
                    krw_balance = pyupbit.get_balance('KRW')
                    buy_amount = 30000
                    if krw_balance >= buy_amount:
                        order = pyupbit.buy_market_order(f'KRW-{coin}', buy_amount)
                        print(f"Buy {coin} at {order['price']} KRW")

        # Wait for 10 seconds before checking again
        time.sleep(10)

    except Exception as e:
        print(f"Error: {e}")

        # define the function to check if the coin meets the envelope 240-minute indicator condition
def check_envelope_240(ticker):
    url = "https://api.upbit.com/v1/candles/minutes/240"
    querystring = {"market": ticker, "count": "30"}
    response = requests.request("GET", url, params=querystring)
    data = response.json()
    df = pd.DataFrame(data)
    df = df.iloc[::-1]
    upper, middle, lower = ta.ENVELOPE(df['trade_price'], 20, 0.05)
    if (df['trade_price'].iloc[-2] < lower.iloc[-2] and df['trade_price'].iloc[-1] > lower.iloc[-1]) or \
    (middle.iloc[-3] < middle.iloc[-2] < middle.iloc[-1]):
        return True
    else:
        return False

def check_list_2(coin):
    df = pyupbit.get_ohlcv(coin, count=25, interval='minute240')
    upper, middle, lower = talib.BBANDS(df['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    if (df['close'][-2] < lower[-2] and df['close'][-1] > lower[-1]) or (df['close'][-3] < middle[-3] and df['close'][-2] < lower[-2] and df['close'][-1] > lower[-1]):
        if df['close'][-3] < df['close'][-2] < df['close'][-1]:
            return True
    return False


# Set the 120-minute moving average window size
ma_window = 120

# Authenticate API access keys
access_key = "YOUR_ACCESS_KEY"
secret_key = "YOUR_SECRET_KEY"
upbit = pyupbit.Upbit(access_key, secret_key)

# Loop through each coin ticker
for ticker in tickers:
    interval = "minute1"

    # Set initial 120-minute moving average value and upward trend indicator
    ma120 = None
    ma120_trend = None

    # Enter the continuous buy loop for the current coin ticker
    while True:
        try:
            # Get the current market price
            current_price = pyupbit.get_current_price(ticker)

            # Get the 120-minute moving average
            ma = pyupbit.get_ohlcv(ticker, interval=interval, count=ma_window)["close"].rolling(ma_window).mean().iloc[-1]

            # Update the moving average upward trend indicator
            if ma120 is None:
                ma120 = ma
            elif ma > ma120:
                ma120_trend = "up"
            else:
                ma120_trend = "down"

            # Check if conditions are met for a buy order
            if ma120_trend == "up" and current_price > ma and current_price < upbit.get_balance("KRW"):
                # Place a buy order for the current coin ticker at the market price
                krw_balance = upbit.get_balance("KRW")
                upbit.buy_market_order(ticker, krw_balance)

            # Sleep for 1 minute before checking conditions again
            time.sleep(60)

        except Exception as e:
            print(e)
            time.sleep(1)


# define the function to check the trading conditions
def macd_min1(coin):
    # get the current price and the historical prices
    current_price = pyupbit.get_current_price(coin)
    hist_prices = pyupbit.get_ohlcv(coin, interval="minute1")

    # calculate the moving average
    moving_average = hist_prices['close'].rolling(window=120).mean()

    # check the trading conditions
    pre_ma = moving_average[-2]
    cur_ma = moving_average[-1]
    up_trend = all(moving_average[i] < moving_average[i+1] for i in range(-10, -1))

    return pre_ma < cur_ma and current_price >= cur_ma and up_trend
3 / 3

Sure, here's a possible implementation of the coin automatic trading buying strategy using the Upbit API in Python:

python
Copy code
import pyupbit

# set the coins to trade
coins = ['KRW-BTC', 'KRW-ETH', 'KRW-NEO', 'KRW-MTL', 'KRW-XRP']

# define the sub-indicator period in minutes
sub_indicator_period = 1

# define the moving average period in minutes
moving_average_period = 120

# initialize the Upbit API client
access_key = 'your-access-key'
secret_key = 'your-secret-key'
upbit = pyupbit.Upbit(access_key, secret_key)

# define the function to check the trading conditions
def should_buy(coin):
    # get the current price and the historical prices
    current_price = pyupbit.get_current_price(coin)
    historical_prices = pyupbit.get_ohlcv(coin, interval=f"{sub_indicator_period}m")

    # calculate the moving average
    moving_average = historical_prices['close'].rolling(window=moving_average_period).mean()




# Set the timeframe for the daily bar indicator (1 day)
timeframe = 'minute1'

# Set the period for the moving average
ma_period = 120

# Get the current price and previous day's closing price for each coin
def macd_min1(coin):
# Set the timeframe for the daily bar indicator (1 day)
    timeframe = 'minute1'

    # Set the period for the moving average
    ma_period = 120


    for coin in coins:
        df = pyupbit.get_ohlcv(coin, interval=timeframe)
        current_price = pyupbit.get_current_price(coin)
        yesterday_close = df.iloc[-2]['close']
        ma = df['close'].rolling(window=ma_period).mean()

        # Check if the current price is greater than the 120-day moving average
        if current_price > ma.iloc[-1]:
            # Check if the previous day's closing price is less than the 120-day moving average
            if yesterday_close < ma.iloc[-2]:
                # Check if the 120-day moving average is in an upward trend
                if ma.iloc[-1] > ma.iloc[-2]:
                    # Buy the coin at the market price
                    # Replace this with your own code for executing the buy order
                    print(f"Buy {coin} at market price")
                    return True
        return False

#############################

 

# function to check if 120-minute average line is on uptrend

def check_uptrend(df):
    ma120 = df['close'].rolling(window=120).mean()
    if ma120[-1] > ma120[0] and all(ma120[i] <= ma120[i+1] for i in range(len(ma120)-1)):
        return True
    else:
        return False

# main function to buy coins based on strategy

def buy_coins():
    ohlcv = pyupbit.get_ohlcv("KRW-BTC", interval="minute30")
    for coin in coins:
        ma120 = df['close'].rolling(window=120).mean()
        if ma120[-1] > ma120[0] and all(ma120[i] <= ma120[i+1] for i in range(len(ma120)-1)):
            return True
            df = pyupbit.get_ohlcv(coin, interval="minute30")
            if df is None:
                continue
            if df["close"][-1] > df['close'].rolling(window=120).mean()[-1] and \
            (df["close"][-2] < df['close'].rolling(window=120).mean()[-2] or df["close"][-3] < df['close'].rolling(window=120).mean()[-3]) and \
            check_uptrend(df):
                list_13.append(coin)
        else:
            return False




 

    # buy coins that meet the strategy conditions

    for coin in buy_coins:

        krw_balance = pyupbit.get_balance("KRW")

        if krw_balance > 5000: # minimum order amount is 5,000 KRW

            buy_price = pyupbit.get_current_price(coin)

            if buy_price is None:

                continue

            order_size = krw_balance / buy_price

            pyupbit.buy_market_order(coin, order_size)

            print(f"Bought {coin} at {buy_price} KRW")

        time.sleep(1) # sleep for 1 second between orders


 

# run the buy_coins function every 5 minutes

while True:

    buy_coins()

    time.sleep(60*5)

# set the target time interval to 1 day
interval = 'minute1'

# set the moving average window to 120
window = 120

# retrieve historical data for each coin
data = {}
for coin in coins:
    df = pyupbit.get_ohlcv(coin, interval=interval)
    data[coin] = df

# check if the current value is greater than the 120 average and the 120 average is in an upward trend
for coin in coins:
    df = data[coin]
    ma = df['close'].rolling(window=window).mean()
    ma_slope = (ma[-1] - ma[0]) / window
    yesterday_value = df.iloc[-2]['close']
    current_value = df.iloc[-1]['close']
    if yesterday_value < ma[-2] and current_value > ma[-1] and ma_slope > 0:
        # buy the coin at the market price



        ##################


# function to check if 120-minute average line is on uptrend

def check_uptrend(df):

    ma120 = df['close'].rolling(window=120).mean()

    if ma120[-1] > ma120[0] and all(ma120[i] <= ma120[i+1] for i in range(len(ma120)-1)):

        return True

    else:

        return False


 

# main function to buy coins based on strategy

def buy_coins():

    # get 30-minute OHLCV data for each coin

    ohlcv = pyupbit.get_ohlcv("KRW-BTC", interval="minute30")


 

    # check strategy conditions for each coin

    buy_coins = []

    for coin in coins:

        df = pyupbit.get_ohlcv(coin, interval="minute30")

        if df is None:

            continue

        if df["close"][-1] > df['close'].rolling(window=120).mean()[-1] and \

        (df["close"][-2] < df['close'].rolling(window=120).mean()[-2] or df["close"][-3] < df['close'].rolling(window=120).mean()[-3]) and \

        check_uptrend(df):

            buy_coins.append(coin)


 

    # buy coins that meet the strategy conditions

    for coin in buy_coins:

        krw_balance = pyupbit.get_balance("KRW")

        if krw_balance > 5000: # minimum order amount is 5,000 KRW

            buy_price = pyupbit.get_current_price(coin)

            if buy_price is None:

                continue

            order_size = krw_balance / buy_price

            pyupbit.buy_market_order(coin, order_size)

            print(f"Bought {coin} at {buy_price} KRW")

        time.sleep(1) # sleep for 1 second between orders


 

# run the buy_coins function every 5 minutes

while True:

    buy_coins()

    time.sleep(60*5)        

    ###############################
    import pyupbit
import numpy as np

# Define the coins to be traded
coins = ['BTC', 'ETH', 'DOGE', 'HIVE', 'EOS', 'ADA', 'NEO', 'BORA']

# Define the moving average periods
ma120_period = 120
ma60_period = 60


# Get the current prices and candlestick data for each coin
prices = {}
candle_data = {}
for coin in coins:
    ticker = f'KRW-{coin}'
    prices[coin] = pyupbit.get_current_price(ticker)
    candle_data[coin] = pyupbit.get_ohlcv(ticker, interval='minute1')

# Define a function to check if a coin meets the trading conditions
def is_trade_candidate(coin):
    # Calculate the moving averages for the coin's candlestick data
    ma120 = np.mean(candle_data[coin]['close'].iloc[-ma120_period:])
    ma60 = np.mean(candle_data[coin]['close'].iloc[-ma60_period:])
 
    # Check if the trading conditions are met
    if ((candle_data[coin]['close'].iloc[-3] < ma120) or (candle_data[coin]['close'].iloc[-2] < ma120)) and (candle_data[coin]['close'].iloc[-1] > ma120) and (ma60 > ma120):
        else:
        return False

# Create a list of coins that meet the trading conditions
trade_candidates = [coin for coin in coins if is_trade_candidate(coin)]

# Buy the coins that meet the trading conditions at the market price
for coin in trade_candidates:
    ticker = f'KRW-{coin}'
    orderbook = pyupbit.get_orderbook(ticker)
    bids = orderbook[0]['orderbook_units'][0]['bid_price']
    bid_price = bids * prices[coin]
    resp = upbit.buy_market_order(ticker, bid_price)
    print(resp)

####################
# 
import pyupbit
import numpy as np
import pandas as pd
import time

# Define the target coins
coins = ["BTC", "ETH", "DOGE", "HIVE", "EOS", "ADA", "NEO", "BORA"]

# Set the interval and time period for candlesticks and Stochastic Slow
interval = "minute1"
candle_period = 120

# Define the function to check the trading condition
def check_buy_signal(coin):
    # Get the historical candlestick data
    df = pyupbit.get_ohlcv(coin, interval=interval, count=candle_period)
    # Calculate the moving averages
    ma120 = df['close'].rolling(window=120).mean()
    ma60 = df['close'].rolling(window=60).mean()
    # Get the previous and before-previous values
    prev_close = df['close'][-2]
    prev2_close = df['close'][-3]
    # Check if the trading condition is met
    if (prev_close < ma120[-2] or prev2_close < ma120[-3]) and df['close'][-1] > ma120[-1] and ma60[-1] > ma60[-2]:
        # Get the Stochastic Slow data
        df_stoch = pyupbit.get_ohlcv(ticker, interval="week", count=stoch_period*stoch_smooth)
        stoch_k, stoch_d = ta.STOCH(df_stoch['high'], df_stoch['low'], df_stoch['close'], fastk_period=stoch_period, slowk_matype=1, slowd_period=stoch_smooth, slowd_matype=1)
        # Check if the Stochastic Slow condition is met
        if stoch_k[-1] > stoch_k[-2] and stoch_d[-1] < 75:
            return True
    return False

# Create a list to store the coins that meet the condition
buy_list = []

while True:
    try:
        for coin in coins:
            # Check the trading condition for each coin
            if check_buy_signal("KRW-" + coin):
                buy_list.append(coin)
        # Buy the coins in the buy list at the market price
        for buy_coin in buy_list:
            krw_balance = pyupbit.get_balance("KRW")
            if krw_balance > 5000:
                # Buy the coin at the market price
                order = pyupbit.buy_market_order("KRW-" + buy_coin, krw_balance)
                print("Bought", buy_coin, "at", order["avg_price"])
                buy_list.remove(buy_coin)
        # Wait for the next iteration
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
    

# Define a list of functions to check for each coin
indicators = [stoch_week, stoch_day, stoch_min240, stoch_min60, 
              macd_day, macd_min60, macd_min30, obv_min240, obv_min30, 
              macd_min5, envelope_day, envelope_min240, macd_min1]

# Define empty lists to store the coins that meet each condition
lists = [[] for _ in range(len(indicators))]

# Loop through each coin and check all indicators
for coin in coins:
    ticker = f"{coin}"
    current_price = pyupbit.get_current_price(ticker)
    for i, func in enumerate(indicators):
        if func(coin):
            print(f"{coin} {func.__name__}_ok {current_price} {now}")
            lists[i].append(coin)

###############################

try:
    # Iterate over the list of tradable coins
    for coin in coins:
        if stoch_min240(coin):
            # Save the coin to the waiting list
            current_price = pyupbit.get_current_price(coin)
            if coin not in buy_waitlist:
                buy_waitlist.append({"coin": coin, "price": pyupbit.get_current_price(coin), 'time': time.time()})
                print(f"{coin} Buy Waitng List in {current_price}")
                post_message(myToken,"#upbit1", coin+" buy waiting list at : " +str(current_price))

            # Check if the buy order can be executed
            if coin in buy_waitlist:
                current_price = pyupbit.get_current_price(coin)
                df_time=time.time() - buy_waitlist[coin]['time']
                if current_price <= buy_waitlist[coin]['price'] * buydown_percent:
                    if macd_min5(coin):
                        print(f"{coin} min5_ok {current_price} {now}")
                      
                    if macd_min1(coin):
                        print(f"{coin} min1_ok {current_price} {now}")
                        
                        krw_balance = upbit.get_balance("KRW")
                        if krw_balance is not None and krw_balance > invest_money*1.01:
                            order = upbit.buy_market_order(coin, invest_money)
                            print(f"{coin} bought at {current_price}")
                            post_message(myToken,"#upbit1", coin+" buy at : " +str(current_price))
                            del buy_waitlist[coin]
                            del buy_waitlist1[coin]
                
                df_time=time.time() - buy_waitlist[coin]['time']
                if df_time > 10800:
                    del buy_waitlist[coin]
                    del buy_waitlist1[coin]

        print("Coins in Buy waiting :", buy_waitlist)

    # Wait for 1 minute before checking again
    time.sleep(3)
except Exception as e:
    print(f"Error_B: {e}")
    post_message(myToken,"#upbit1", "Error Buy" +str(e))
    time.sleep(2)


#Step 8 : Define a function to check the OBV 240-minute indicator
def obv_min240(coin):
    df = pyupbit.get_ohlcv(coin, interval="minute240")
    if df is None:
        return

    obv = talib.OBV(df['close'], df['volume'])
    obv_signal = talib.SMA(obv, timeperiod=10)
    if obv_signal[-1] > obv_signal[-2]:
              list_8.append({"coin": coin, "price": pyupbit.get_current_price(coin), "time": time.time()})
        # Step 14: Buy condtion Test
            if buy_test(coin):
               print(f"{coin} buy condtion_ok {current_price} {now}")

### 매도 관련 #########################
try:
    sellable_coins = upbit.get_balances()
    for coin in sellable_coins:
        if isinstance(coin, dict) and coin.get('currency') != 'KRW':
            coin_name = coin.get('currency')
            sellable_amount = float(coin.get('balance', 0)) - float(coin.get('locked', 0))
            ticker = f"{coin_name}-KRW"
            current_price = pyupbit.get_current_price(ticker)
            if current_price is None:
                continue
            avg_price = float(coin.get('avg_buy_price', 0))
            if current_price < avg_price * deadsell_percent:
                orderbook = pyupbit.get_orderbook(ticker)
                if orderbook:
                    sell_price = orderbook[0]['orderbook_units'][0]['ask_price']
                    upbit.sell_market_order(ticker, sellable_amount, price=sell_price)
                    print(f"{coin_name} dead sell {current_price}")
                    post_message(myToken, "#upbit1", coin_name + " coin dead sell : " + str(current_price))
                else:
                    print(f"Error: No orderbook data for {ticker}")
                    post_message(myToken, "#upbit1", "Error Sell: No orderbook data for " + str(ticker))
        # Wait for 10 seconds before checking again
        time.sleep(10)
except Exception as e:
    print(f"Error: {e}")
    post_message(myToken,"#upbit1", "Error Sell: " + str(e))

try:
    sellable_coins = upbit.get_balances()
    for coin in sellable_coins:
        if isinstance(coin, dict) and coin.get('currency') != 'KRW':
            coin_name = coin.get('currency')
            sellable_amount = float(coin.get('balance', 0)) - float(coin.get('locked', 0))
            ticker = f"{coin_name}-KRW"
            current_price = pyupbit.get_current_price(ticker)
            if current_price is None:
                continue
            avg_price = float(coin.get('avg_buy_price', 0))
            if current_price < avg_price * deadsell_percent:
                orderbook = pyupbit.get_orderbook(ticker)
                if orderbook:
                    sell_price = orderbook[0]['orderbook_units'][0]['ask_price']
                    upbit.sell_market_order(ticker, sellable_amount, price=sell_price)
                    print(f"{coin_name} dead sell {current_price}")
                    post_message(myToken, "#upbit1", coin_name + " coin dead sell : " + str(current_price))
                else:
                    print(f"Error: No orderbook data for {ticker}")
        # Wait for 10 seconds before checking again
        time.sleep(10)
except Exception as e:
    print(f"Error: {e}")
    post_message(myToken,"#upbit1", "Error Sell: " + str(e))
