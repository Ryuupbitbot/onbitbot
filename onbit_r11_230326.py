#!/usr/bin/env python
# coding: utf-8

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
import talib.abstract as ta


############################### 프로그램 상수 #####################################
access_key = "??"
secret_key = "??"
myToken = "??"
################################# 함수 ####################################
upbit = pyupbit.Upbit(access_key, secret_key) # upbit 사용하기 위함

#투자금액
invest_money1 = 7000
invest_money2 = 23000

# Step 1: Define the coins to trade
my_coins = ['KRW-BTC', 'KRW-ETH', 'KRW-NEO', 'KRW-MTL', 'KRW-XRP', 'KRW-ETC', 'KRW-OMG', 'KRW-SNT', 'KRW-WAVES',
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

# Step 1: Define the coins for 거래량 많음
my_coins2 = ['KRW-BTC', 'KRW-ETH', 'KRW-NEO', 'KRW-MTL', 'KRW-XRP', 'KRW-ETC', 'KRW-OMG', 'KRW-ADA', 'KRW-EOS', 'KRW-TRX',
               'KRW-LOOM', 'KRW-BCH', 'KRW-IQ', 'KRW-ONG', 'KRW-GAS', 'KRW-KNC', 'KRW-BSV', 'KRW-AVAX', 'KRW-MANA',
               'KRW-ANKR', 'KRW-ATOM', 'KRW-CRE', 'KRW-HBAR', 'KRW-STPT', 'KRW-ORBS', 'KRW-STMX', 'KRW-DKA', 'KRW-HIVE',
               'KRW-LINK', 'KRW-CRO', 'KRW-HUNT', 'KRW-PLA', 'KRW-DOT', 'KRW-SRM', 'KRW-MVL', 'KRW-STRAX', 'KRW-META',
               'KRW-FCT2', 'KRW-SAND', 'KRW-DOGE', 'KRW-STRK', 'KRW-FLOW', 'KRW-AXS', 'KRW-STX']

coins = []
def get_coins(my_coins):
    upbit_tickers = pyupbit.get_tickers()
    for coin in my_coins:
        if coin in upbit_tickers:
            coins.append(coin)
    return coins
upbit_tradable_coins = get_coins(my_coins)

#익절,손절 퍼센트
goodsell_percent = 1.032
deadsell_percent = 0.93
buydown_percent = 0.986
aftergoodsell_percent = 0.986 #goodsell각 이후 1.5% 떨어지면 매도
buy_waiting_time = 21600 #조건만족후 구매대기 최대 시간(초)
now = datetime.datetime.now()

buy_waitlist1 = [] # Condtion 1 ~ 9 : test 용
buy_waitlist2 = [] # Condtion 1 ~ 9 : test 용
buy_waitlist3 = [] # Condtion 10, 13 : test 용


buy_waitlist = {} # Condtion 1 ~ 9 : OK
sell_waitlist = {} # sell wait list

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
list_13 = [] # 1min macd (signal cross)


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
    if slowk[-1] > slowk[-2] and slowd[-1] < 76:
        if coin not in list_1:
            list_1.append(coin)
            return True
    return False

# Step 2: Stochastic Slow Daily Indicator
def stoch_day(coin):
    df = pyupbit.get_ohlcv(coin, interval="day")
    if df is None:
        return
    slowk, slowd = talib.STOCH(df['high'], df['low'], df['close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    if slowk[-1] > slowd[-1] and slowk[-1] > slowk[-2] and slowd[-1] < 72:
        if coin not in list_2:
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
        if coin not in list_3:
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
        if coin not in list_4:
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
        if coin not in list_5:
            list_5.append(coin)
            return True
    return False

# Step 6: Get the 60 minute OHLCV data for the given coin
def macd_min60(coin):
    df = pyupbit.get_ohlcv(coin, interval="minute60")
    if df is None:
        return

    macd, signal, hist = ta.MACD(df["close"], fastperiod=12, slowperiod=26, signalperiod=9)
    if macd[-1] > macd[-2]:
        if coin not in list_6:
            list_6.append(coin)
            return True
    return False

# Step 7: Get the macd 30minute OHLCV data for the given coin
def macd_min30(coin):
    df = pyupbit.get_ohlcv(coin, interval="minute30")
    if df is None:
        return

    macd, signal, hist = ta.MACD(df["close"], fastperiod=12, slowperiod=26, signalperiod=9)
    if hist[-1] > hist[-2] and hist[-1] > 0 and (hist[-2] < 0  or hist[-3] < 0  or hist[-4] < 0 ):
        if coin not in list_7:
            list_7.append(coin)
            return True
    return False

#Step 8 : Define a function to check the OBV 240-minute indicator
def obv_min240(coin):
    df = pyupbit.get_ohlcv(coin, interval="minute240")
    if df is None:
        return

    obv = talib.OBV(df['close'], df['volume'])
    obv_signal = talib.SMA(obv, timeperiod=10)
    if obv_signal[-1] > obv_signal[-2]:
        if coin not in list_8:
            list_8.append(coin)
            return True
    return False

# Step 9 : Define a function to check the OBV 30-minute indicator
def obv_min30(coin):
    df = pyupbit.get_ohlcv(coin, interval="minute30")
    if df is None:
        return

    obv = talib.OBV(df['close'], df['volume'])
    obv_signal = talib.SMA(obv, timeperiod=10)
    if obv_signal[-1] > obv_signal[-2] and obv[-1] > obv[-2]*1.15:
        if coin not in list_9:
            list_9.append(coin)
            return True
    return False

def macd_min5(coin):
# Step 10 : Get the macd 5minute OHLCV data for the given coin
    df = pyupbit.get_ohlcv(coin, interval="minute5")
    if df is None:
        return
    macd, signal, hist = ta.MACD(df["close"], fastperiod=12, slowperiod=26, signalperiod=9)
    if hist[-1] > hist[-2] and hist[-1] > 0 and (hist[-2] < 0 or hist[-3] < 0):
        if coin not in list_10:
            list_10.append(coin)
            return True
    return False

# step 11: Define the function to check the envelope day indicator
def envelope_day(coin):
    df = pyupbit.get_ohlcv(coin, count=25, interval="day")
    if df is None:
        return False
    upper, middle, lower = talib.BBANDS(df['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    if (df['close'][-2] < lower[-2] and df['close'][-1] > lower[-1]) or (df['close'][-3] < lower[-3] and df['close'][-2] > lower[-2]):
        if df['close'][-3] < df['close'][-2] < df['close'][-1]:
            if coin not in list_11:
                list_11.append(coin)
                return True
    return False
# step 12: Define the function to check the envelope 240min indicator
def envelope_min240(coin):
    df = pyupbit.get_ohlcv(coin, count=25, interval="minute240")
    if df is None:
        return False
    upper, middle, lower = talib.BBANDS(df['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    if (df['close'][-2] < lower[-2] and df['close'][-1] > lower[-1]) or (df['close'][-3] < lower[-3] and df['close'][-2] > lower[-2]):
        if df['close'][-3] < df['close'][-2] < df['close'][-1]:
            if coin not in list_12:
                list_12.append(coin)
                return True
    return False

# step 13: Get the historical candlestick 1-min data
candle_period = 120
def macd_min1(coin):
    df = pyupbit.get_ohlcv(coin, interval="minute3", count=candle_period)
    if df is None:
        return False
    # Calculate the moving averages
    ma60 = df['close'].rolling(window=60).mean()
    ma30 = df['close'].rolling(window=30).mean()
    ma15 = df['close'].rolling(window=15).mean()
    # Get the previous and before-previous values
    prev_close = df['close'][-2]
    prev2_close = df['close'][-3]
    prev3_close = df['close'][-4]
    # Check if the trading condition is met
    if (prev_close < ma60[-2] or prev2_close < ma60[-3] or prev3_close < ma60[-4]) and df['close'][-1] > ma60[-1] and ma30[-1] > ma30[-2] and ma15[-1] > ma30[-1]:
        if coin not in list_13:
            list_13.append(coin)
            return True
    return False

# My KRW account
def get_my_KRW_Balance():
    return upbit.get_balance("KRW")

# Test Buy condition.
def buy_test1(coin):
        for coin in coins:
            if (coin in list_1) or (coin in list_11) or (coin in list_12):
                    if coin in list_2:
                        if coin in list_3:
                            if coin in list_4:
                                if coin in list_5:
                                    if coin in list_6:
                                        if (coin in list_8) or (coin in list_9):
                                            if coin in list_7:
                                                if (coin in list_10) or (coin in list_13):
                                                    if coin not in buy_waitlist1:
                                                        buy_waitlist1.append(coin)
                                                        return True

def buy_test2(coin):
        for coin in coins:
            if stoch_week(coin) or envelope_day(coin) or envelope_min240(coin):
                if stoch_day(coin):
                    if stoch_min240(coin):
                        if stoch_min60(coin):
                            if macd_day(coin):
                                if macd_min60(coin):
                                    if obv_min240(coin) or obv_min30(coin):
                                        if coin not in buy_waitlist2:
                                            buy_waitlist2.append(coin)
                                            return True

def buy_test3(coin):
        for coin in coins:
            if coin in list_1 and coin in list_5 and coin in list_10 and coin in list_13:
               if coin not in buy_waitlist3:
                    buy_waitlist3.append(coin)
                    return True

######################################################
# 시작 메세지 슬랙 전송
post_message(myToken,"#upbit1", "autotrade start")
    
print("autotrade start")

###############################################################################

########## list append function #################
   
while True:
    try:
        # Step 1: Check stoch week
        for coin in coins:
            ticker = f"{coin}"
            current_price = pyupbit.get_current_price(ticker)
            if stoch_week(coin):
                condition = True
               #print(f"{coin} stoch_week_ok {current_price} {now}")

        # Step 2: Check stoch day
            if stoch_day(coin):
                condition = True
               #print(f"{coin} stoch_day_ok {current_price} {now}")
       
        # Step 3: Check stoch min240
            if stoch_min240(coin):
                condition = True
               #print(f"{coin} stoch_min240_ok {current_price} {now}")

        # Step 4: Check stoch min60
            if stoch_min60(coin):
                condition = True
               #print(f"{coin} stoch_min60_ok {current_price} {now}")

        # Step 5: Check MACD day
            if macd_day(coin):
                condition = True
               #print(f"{coin} macd_day_ok {current_price} {now}")

        # Step 6: Check MACD min60
            if macd_min60(coin):
                condition = True
               #print(f"{coin} macd_min60_ok {current_price} {now}")
        
        #Step 8: Check obv min240
            if obv_min240(coin):
                condition = True
              #print(f"{coin} obv_min240_ok {current_price} {now}")

        # Step 9: Check obv 30min
            if obv_min30(coin):
                condition = True
               #print(f"{coin} obv_min30_ok {current_price} {now}")

        # Step 11: Check envelope day
            if envelope_day(coin):
                condition = True
                #print(f"{coin} envelop_day_ok {current_price} {now}")

        # Step 12: Check envelope 240min
            if envelope_min240(coin):
                condition = True
               #print(f"{coin} envelope_min240_ok {current_price} {now}")

        # Step 7: Check MACD 30min
            if macd_min30(coin):
                condition = True
               #print(f"{coin} macd_min30_ok {current_price} {now}")

        # Step 10: Check macd 5min
            if macd_min5(coin):
                condition = True
               #print(f"{coin} macd_min5_ok {current_price} {now}")

        # Step 13: Check macd min1
            if macd_min1(coin):
                condition = True
               #print(f"{coin} mac min1_ok {current_price} {now}")
        
        # Step 14: Buy condtion Test
            if buy_test1(coin):
                condition = True
               #print(f"{coin} buy coin list1_ok {current_price} {now}")

        # Step 15: Buy condtion Test
            #if buy_test2(coin):
               #print(f"{coin} buy_coin_list2_ok {current_price} {now}")

        # Step 16: Buy condtion Test
            if buy_test3(coin):
                condition = True
               #print(f"{coin} buy_coin_list3_ok {current_price} {now}")

        
        time.sleep(2)
    except Exception as e:
        print(f"Buy condition-1 {e}")
        time.sleep(1)
        post_message(myToken,"#upbit1", "Error while-1" + str(e))
 
    ########################### Buy####################################

    try:
        # Iterate over the list of tradable coins
        for coin in list(buy_waitlist1):
            # Save the coin to the waiting list
            current_price = pyupbit.get_current_price(coin)
            if coin not in buy_waitlist:
                buy_waitlist[coin] = {'price': current_price, 'time': time.time()}
                post_message(myToken,"#upbit1", coin+" buy waiting list-1: " +str(current_price))
                krw_balance = upbit.get_balance("KRW")
                if krw_balance is not None and krw_balance > invest_money1*1.01:
                    order = upbit.buy_market_order(coin, invest_money1)
                    sell_waitlist[coin] = {'price': current_price, 'time': time.time()}
                    post_message(myToken,"#upbit1", coin+" buy at-30min : " +str(current_price))
        
        for coin in list(buy_waitlist3):
            # Save the coin to the waiting list
            current_price = pyupbit.get_current_price(coin)
            if coin not in buy_waitlist:
                buy_waitlist[coin] = {'price': current_price, 'time': time.time()}
                post_message(myToken,"#upbit1", coin+" buy waiting list-3 : " +str(current_price))
                krw_balance = upbit.get_balance("KRW")
                if krw_balance is not None and krw_balance > invest_money1*1.01:
                    order = upbit.buy_market_order(coin, invest_money1)
                    sell_waitlist[coin] = {'price': current_price, 'time': time.time()}
                    post_message(myToken,"#upbit1", coin+" buy at-5,3min : " +str(current_price))


        # Check if the buy order can be executed
        for coin in list(buy_waitlist):
            temp_price = buy_waitlist[coin]['price']
            temp_time = buy_waitlist[coin]['time']
            elapsed_time = time.time() - temp_time
            current_price = pyupbit.get_current_price(coin)
            if current_price <= temp_price * buydown_percent:
                if macd_min5(coin):
                    krw_balance = upbit.get_balance("KRW")
                    if krw_balance is not None and krw_balance > invest_money2*1.01:
                        order = upbit.buy_market_order(coin, invest_money2)
                        post_message(myToken,"#upbit1", coin+" buy at-5min : " +str(current_price))
                        del buy_waitlist[coin]

                elif macd_min1(coin):
                    krw_balance = upbit.get_balance("KRW")
                    if krw_balance is not None and krw_balance > invest_money2*1.01:
                        order = upbit.buy_market_order(coin, invest_money2)
                        post_message(myToken,"#upbit1", coin+" buy at-3min : " +str(current_price))
                        del buy_waitlist[coin]

            elif elapsed_time > buy_waiting_time:
                del buy_waitlist[coin]

        # Remove the reference to coin, as it will not be defined outside the loop
        print("Coins in Buy waiting :", buy_waitlist)

        # Wait for 10 seconds before checking again
        time.sleep(2)
    except Exception as e:
        print(f"Error_Buy : {e}")
        post_message(myToken,"#upbit1", "Error Buy : " + str(e))
        time.sleep(1)

    ########################### Sell ####################################
    try:
        # Get the available balance and average purchase price for each coin
        for coin in sell_waitlist:
            temp_price1 = sell_waitlist[coin]['price']
            coin_name = coin.split('-')[1]
            balance = upbit.get_balance(coin_name)
            current_price = pyupbit.get_current_price(coin)
            if current_price is None:
                continue
            high_prices = pyupbit.get_ohlcv(coin, interval='day', count=3)['high']
            three_day_high = high_prices.max()
            if balance is not None and temp_price1 is not None:
                if balance > 0:
                    if (current_price >= goodsell_percent * temp_price1 and current_price <= aftergoodsell_percent * three_day_high):
                        upbit.sell_market_order(coin, balance)
                        del sell_waitlist[coin]
                        post_message(myToken,"#upbit1", f"{coin} good sell {current_price}")
                    
                    elif (current_price <= deadsell_percent * temp_price1):
                        upbit.sell_market_order(coin, balance)
                        del sell_waitlist[coin]
                        post_message(myToken, "#upbit1", coin + " coin dead sell : " + str(current_price))

        time.sleep(1)

    except Exception as e:
        print(f"Error sell: {e}")
        post_message(myToken,"#upbit1", "Error Sell: " + str(e))
        time.sleep(1)
