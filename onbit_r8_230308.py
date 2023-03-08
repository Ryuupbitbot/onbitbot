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

#투자금액
invest_money = 30000

# Define the time constants in seconds
HOUR = 3600
THREE_HOURS = HOUR * 3

# Step 1: Define the coins to trade
my_coins = ['KRW-BTC', 'KRW-ETH', "KRW-NEO", 'KRW-MTL', 'KRW-XRP', 'KRW-ETC', 'KRW-OMG', 'KRW-SNT', 'KRW-WAVES',
              'KRW-XEM', 'KRW-QTUM', 'KRW-LSK', 'KRW-STEEM', 'KRW-XLM', 'KRW-ARDR', 'KRW-ARK', 'KRW-STORJ', 'KRW-GRS',
               'KRW-REP', 'KRW-ADA', 'KRW-SBD', 'KRW-POWR', 'KRW-BTG', 'KRW-ICX', 'KRW-EOS', 'KRW-TRX', 'KRW-SC',
               'KRW-ONT', 'KRW-ZIL', 'KRW-POLYX', 'KRW-ZRX', 'KRW-LOOM', 'KRW-BCH', 'KRW-BAT', 'KRW-IOST', 'KRW-RFR',
               'KRW-CVC', 'KRW-IQ', 'KRW-IOTA', 'KRW-ONG', 'KRW-GAS', 'KRW-UPP', 'KRW-ELF', 'KRW-KNC',
               'KRW-BSV', 'KRW-THETA', 'KRW-QKC', 'KRW-AVAX', 'KRW-MOC', 'KRW-ENJ', 'KRW-TFUEL', 'KRW-MANA',
               'KRW-ANKR', 'KRW-AERGO', 'KRW-ATOM', 'KRW-TT', 'KRW-CRE', 'KRW-MBL', 'KRW-WAXP', 'KRW-HBAR', 'KRW-MED',
               'KRW-MLK', 'KRW-STPT', 'KRW-ORBS', 'KRW-VET', 'KRW-CHZ', 'KRW-STMX', 'KRW-DKA', 'KRW-HIVE', 'KRW-KAVA',
               'KRW-AHT', 'KRW-LINK', 'KRW-XTZ', 'KRW-BORA', 'KRW-JST', 'KRW-CRO', 'KRW-TON', 'KRW-SXP', 'KRW-HUNT',
               'KRW-PLA', 'KRW-DOT', 'KRW-SRM', 'KRW-MVL', 'KRW-STRAX', 'KRW-AQT', 'KRW-GLM', 'KRW-SSX', 'KRW-META',
               'KRW-FCT2', 'KRW-CBK', 'KRW-SAND', 'KRW-HUM', 'KRW-DOGE', 'KRW-STRK', 'KRW-PUNDIX', 'KRW-FLOW',
               'KRW-DAWN', 'KRW-AXS', 'KRW-STX', 'KRW-XEC']

coins = []
def get_coins(my_coins):
    upbit_tickers = pyupbit.get_tickers()
    for coin in my_coins:
        if coin in upbit_tickers:
            coins.append(coin)
    return coins
upbit_tradable_coins = get_coins(my_coins)

#익절,손절 퍼센트
goodsell_percent = 1.05
deadsell_percent = 0.93
buydown_percent = 0.985
aftergoodsell_percent = 0.985 #goodsell각 이후 1.5% 떨어지면 매도


now = datetime.datetime.now()

buy_waitlist1 = [] # Condtion 1 ~ 9 : test 용

buy_waitlist = {} # Condtion 1 ~ 9 : OK

# Initialize temporary storage lists
list_1 = [] # Weekly Stochastic Slow (k rising, D < 75)
list_2 = [] # Daily Stochastic Slow (k rising, k > D, D < 60)
list_3 = [] # 240 min Stochastic Slow (k rising, k > D)
list_4 = [] # 60 min Stochastic Slow (k rising, k > D)
list_5 = [] # Daily MACD (signal rising, macd > signal)
list_6 = [] # 60 min MACD (signal rising)
list_7 = [] # 30 min MACD (macd rising, macd breaks above signal)
list_8 = [] # 240 min OBV (obv > signal)
list_9 = [] # 30 min OBV (obv > signal)
list_10 = [] # 5 min MACD (signal cross)
list_11 = [] # day envelope (signal cross)
list_12 = [] # 240min envelope (signal cross)

################################# 함수 ####################################
upbit = pyupbit.Upbit(access_key, secret_key) # pyupbit 사용하기 위함

######################################################################################

# 슬랙 message
def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + token},
        data={"channel": channel, "text": text},
    )

##############  Main Function #######################################################################

# Step 1: Stochastic Slow Weekly Indicator
def stoch_week(coin):
    df = pyupbit.get_ohlcv(coin, interval="week")
    if df is None:
        return
    slowk, slowd = talib.STOCH(df['high'], df['low'], df['close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    if slowk[-1] > slowk[-2] and slowd[-1] < 75:
                list_1.append(coin)
                return True
    return False

# Step 2: Stochastic Slow Daily Indicator
def stoch_day(coin):
    df = pyupbit.get_ohlcv(coin, interval="day")
    if df is None:
        return
    slowk, slowd = talib.STOCH(df['high'], df['low'], df['close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    if slowk[-1] > slowd[-1] and slowk[-1] > slowk[-2] and slowd[-1] < 60:
                list_2.append(coin)
                return True
    return False

# Step 3: Stochastic Slow 240min Indicator
def stoch_min240(coin):
    df = pyupbit.get_ohlcv(coin, interval="minute240")
    if df is None:
        return
    slowk, slowd = talib.STOCH(df['high'], df['low'], df['close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    if slowk[-1] > slowd[-1] and slowk[-1] > slowk[-2]:
                list_3.append(coin)
                return True
    return False

# Step 4: Stochastic Slow 60min Indicator
def stoch_min60(coin):
    df = pyupbit.get_ohlcv(coin, interval="minute60")
    if df is None:
        return
    slowk, slowd = talib.STOCH(df['high'], df['low'], df['close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    if slowk[-1] > slowd[-1] and slowk[-1] > slowk[-2]:
                list_4.append(coin)
                return True
    return False

# Step 5: Get the day OHLCV data for the given coin
def macd_day(coin):
    df = pyupbit.get_ohlcv(coin, interval="day")
    if df is None:
        return

    macd, signal, hist = ta.MACD(df["close"], fastperiod=12, slowperiod=26, signalperiod=9)
    if (macd[-1] >= signal[-1] and hist[-1] > hist[-2]) or (hist[-1] > hist[-2] and hist[-2] > hist[-3]):
        list_5.append(coin)

# Step 6: Get the 60 minute OHLCV data for the given coin
def macd_min60(coin):
    df = pyupbit.get_ohlcv(coin, interval="minute60")
    if df is None:
        return

    macd, signal, hist = ta.MACD(df["close"], fastperiod=12, slowperiod=26, signalperiod=9)
    if macd[-1] > macd[-2]:
        list_6.append(coin)

# Step 7: Get the macd 30minute OHLCV data for the given coin
def macd_min30(coin):
    df = pyupbit.get_ohlcv(coin, interval="minute30")
    if df is None:
        return

    macd, signal, hist = ta.MACD(df["close"], fastperiod=12, slowperiod=26, signalperiod=9)
    if hist[-1] > hist[-2] and ((hist[-2] < 0 and hist[-1] > 0) or (hist[-3] < 0 and hist[-2] > 0) or (hist[-4] < 0 and hist[-3] > 0)):
        list_7.append(coin)

#Step 8 : Define a function to check the OBV 240-minute indicator
def obv_min240(coin):
    df = pyupbit.get_ohlcv(coin, interval="minute240")
    if df is None:
        return

    obv = talib.OBV(df['close'], df['volume'])
    obv_signal = talib.SMA(obv, timeperiod=10)
    if obv_signal[-1] > obv_signal[-2]:
        list_8.append(coin)

# Step 9 : Define a function to check the OBV 30-minute indicator
def obv_min30(coin):
    df = pyupbit.get_ohlcv(coin, interval="minute30")
    if df is None:
        return

    obv = talib.OBV(df['close'], df['volume'])
    obv_signal = talib.SMA(obv, timeperiod=10)
    if obv_signal[-1] > obv_signal[-2] and obv[-1] > obv[-2]*1.15:
        list_9.append(coin)

def macd_min5(coin):
# Step 10 : Get the macd 5minute OHLCV data for the given coin
    df = pyupbit.get_ohlcv(coin, interval="minute5")
    if df is None:
        return
    macd, signal, hist = ta.MACD(df["close"], fastperiod=12, slowperiod=26, signalperiod=9)
    if (hist[-2] < 0 and hist[-1] > 0) or (hist[-3] < 0 and hist[-2] > 0):
        list_10.append(coin)

# Define the function to check the envelope day indicator
def envelope_day(coin):
    df = pyupbit.get_ohlcv(coin, count=25, interval="day")
    if df is None:
        return False
    upper, middle, lower = talib.BBANDS(df['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    if (df['close'][-2] < lower[-2] and df['close'][-1] > lower[-1]) or (df['close'][-3] < lower[-3] and df['close'][-2] > lower[-2]):
        if df['close'][-3] < df['close'][-2] < df['close'][-1]:
            return True
    return False
# Define the function to check the envelope 240min indicator
def envelope_min240(coin):
    df = pyupbit.get_ohlcv(coin, count=25, interval="minute240")
    if df is None:
        return False
    upper, middle, lower = talib.BBANDS(df['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    if (df['close'][-2] < lower[-2] and df['close'][-1] > lower[-1]) or (df['close'][-3] < lower[-3] and df['close'][-2] > lower[-2]):
        if df['close'][-3] < df['close'][-2] < df['close'][-1]:
            return True
    return False


# always true
def always_true():
    if True:
        return True
    
# 시작 메세지 슬랙 전송
post_message(myToken,"#upbit1", "autotrade start")
    
print("autotrade start")
    
########## list append function ############################################################################

while True:
    try:
        # Step 1: Check stoch week
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if stoch_week(coin):
               list_1.append(coin)

        # Step 2: Check stoch day
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if stoch_day(coin):
               list_2.append(coin)
       
        # Step 3: Check stoch min240
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if stoch_min240(coin):
               list_3.append(coin)

        # Step 4: Check stoch min60
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if stoch_min60(coin):
               list_4.append(coin)

        # Step 5: Check MACD day
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if macd_day(coin):
               list_5.append(coin)

        # Step 6: Check MACD min60
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if macd_min60(coin):
               list_6.append(coin)

        # Step 7: Check MACD 30min
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if macd_min30(coin):
               list_7.append(coin)

        #Step 8: Check obv min240
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if obv_min240(coin):
              list_8.append(coin)

        # Step 9: Check obv 30min
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if obv_min30(coin):
               list_9.append(coin)

        # Step 10: Check macd 5min
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if macd_min5(coin):
               list_10.append(coin)
             
             # Step 11: Check envelope day
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if envelope_day(coin):
               list_11.append(coin)

             # Step 12: Check envelope 240min
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if envelope_min240(coin):
               list_12.append(coin)
   
   
        #12 Test Buy condition.
        for coin in list_1 or list_11 or list_12:
            if coin in list_2:
                if coin in list_3:
                    if coin in list_4:
                        if coin in list_5 or list_11 or list_12:
                            if coin in list_6:
                                if coin in list_8 or list_9:
                                    buy_waitlist1.append(coin)
                                    print(f"{coin} added to buy_waitlist1")
                                    post_message(myToken,"#upbit1", coin+" buy waiting list-11 at : " +str(current_price))

        print("Coins in Buy waiting :", buy_waitlist)

        time.sleep(300)
    except Exception as e:
        print(f"Error while-1 {e}")
        time.sleep(10)

###############################################################################
    try:
        # Iterate over the list of tradable coins
        for coin in buy_waitlist1:
            if macd_min30(coin):
                    buy_waitlist[coin] = {'price': pyupbit.get_current_price(coin), 'time': time.time()}
                    # Save the coin to the waiting list
                    if coin not in buy_waitlist:
                                buy_waitlist[coin] = {'price': pyupbit.get_current_price(coin), 'time': time.time()}
                                post_message(myToken,"#upbit1", coin+" buy waiting list at : " +str(current_price))

                    # Check if the buy order can be executed
                    if coin in buy_waitlist:
                        current_price = pyupbit.get_current_price(coin)
                        if current_price <= buy_waitlist[coin]['price'] * buydown_percent:
                            if macd_min5(coin):
                                krw_balance = upbit.get_balance("KRW")
                                if krw_balance is not None and krw_balance > invest_money*1.01:
                                    order = upbit.buy_market_order(coin, invest_money)
                                    print(f"{coin} bought at {current_price}")
                                    post_message(myToken,"#upbit1", coin+" buy at : " +str(current_price))
                                    del buy_waitlist[coin]
                                    del buy_waitlist1[coin]
                        
                        elif time.time() - buy_waitlist[coin]['time'] > 7200:
                                del buy_waitlist[coin]
                                del buy_waitlist1[coin]

        # Wait for 1 minute before checking again
        time.sleep(30)
    except Exception as e:
        print(f"Error_B: {e}")

################################################################################
    ######### Sell #########
    # 1) Load the coin name, balance amount, and average purchase price from Upbit
    try:
        coin_balance = upbit.get_balances()
        for coin in coin_balance:
            if isinstance(coin, dict) and coin.get('currency') != 'KRW':
                coin_name = coin.get('currency')
                balance = float(coin.get('balance'))
                avg_price = float(coin.get('avg_buy_price'))
                print(f"Coin: {coin_name}, Balance: {balance}, Average Purchase Price: {avg_price}")

        time.sleep(30)
    except Exception as e:
        print(f"Error_S1: {e}")

    # 2) Load the number of coins available for sell order from Upbit
    try:
        sellable_coins = upbit.get_balances()
        for coin in sellable_coins:
            if isinstance(coin, dict) and coin.get('currency') != 'KRW':
                coin_name = coin.get('currency')
                sellable_amount = float(coin.get('balance', 0)) - float(coin.get('locked', 0))
                print(f"Sellable Coins for {coin_name}: {sellable_amount}")       

    # 3) If the current price of an available coin rises by more than goodsell percent(5%) from the average purchase price 
    # and falls more than aftergoodsell_percent(1.5%) from the highest price, sell at the market price
                ticker = f"{coin}"
                current_price = pyupbit.get_current_price(ticker)
                if current_price is None:
                    continue
                avg_price = float(coin.get('avg_buy_price', 0))
                ohlcv = pyupbit.get_ohlcv(ticker, interval="day", count=3)
                highest_price = ohlcv['high'].max()
                if current_price > avg_price * goodsell_percent and current_price < highest_price * aftergoodsell_percent:
                    sell_price = pyupbit.get_orderbook(ticker)['asks'][0]['price']
                    upbit.sell_market_order(ticker, sellable_amount, price=sell_price)
                    buy_waitlist.pop(coin)
                    print(f"{coin_name} good sell {current_price}")
                    post_message(myToken,"#upbit1", f"{coin_name} good sell {current_price}")
        
        time.sleep(30)

    except Exception as e:
        print(f"Error_S3: {e}")

    # 4) If the condition in 3) is not satisfied and the current price falls by more than deadsell percent(7%) of the average purchase price, sell at the market price
    try:
        sellable_coins = upbit.get_balances()
        for coin in sellable_coins:
            if isinstance(coin, dict) and coin.get('currency') != 'KRW':
                coin_name = coin.get('currency')
                sellable_amount = float(coin.get('balance', 0)) - float(coin.get('locked', 0))
                ticker = f"{coin}"
                current_price = pyupbit.get_current_price(ticker)
                if current_price is None:
                    continue
                avg_price = float(coin.get('avg_buy_price', 0))
                if current_price < avg_price * deadsell_percent:
                    orderbook = pyupbit.get_orderbook(ticker)
                    if orderbook:
                        sell_price = orderbook[0]['orderbook_units'][0]['ask_price']
                        upbit.sell_market_order(ticker, sellable_amount, price=sell_price)
                        buy_waitlist.pop(coin)
                        print(f"{coin_name} dead sell {current_price}")
                        post_message(myToken, "#upbit1", coin_name + "coin dead sell : " + str(current_price))
                    else:
                        print(f"Error: No orderbook data for {ticker}")
        # Wait for 1 minute before checking again
        time.sleep(30)
    except Exception as e:
        print(f"Error4: {e}")
        time.sleep(2)

    except KeyboardInterrupt:
        print("Program stopped by the user")

