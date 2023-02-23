#!/usr/bin/env python
# coding: utf-8

############################### 모듈 import #####################################

import pyupbit
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


############################### 프로그램 상수 #####################################
access_key = ""          # 본인 값으로 변경
secret_key = ""          # 본인 값으로 변경
myToken = ""               # 본인 값으로 변경
 

#투자금액
invest_money = 30000

#거래할 코인
krw_tickers = ['KRW-BTC', 'KRW-ETH', 'KRW-NEO', 'KRW-MTL', 'KRW-XRP', 'KRW-ETC', 'KRW-OMG', 'KRW-SNT', 'KRW-WAVES',
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


#익절,손절 퍼센트
goodsell_percent = 1.05
deadsell_percent = 0.93
buydown_percent = 0.988
aftergoodsell_percent = 0.985 #goodsell각 이후 1.5% 떨어지면 매도

################################# 함수 ####################################
upbit = pyupbit.Upbit(access_key, secret_key) # pyupbit 사용하기 위함


#슬랙 message
def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )


#스토캐스틱rsi 1week (반환값 매수조건만족시 True 나머지는 False)
def stockrsiweeks(symbol):
    url = "https://api.upbit.com/v1/candles/weeks"

    querystring = {"market":symbol,"count":"200"}

    response = requests.request("GET", url, params=querystring)

    data = response.json()

    df = pd.DataFrame(data)

    series=df['trade_price'].iloc[::-1]

    df = pd.Series(df['trade_price'].values)

    period=9
    smoothK=3
    smoothD=3

    delta = series.diff().dropna()
    ups = delta * 0
    downs = ups.copy()
    ups[delta > 0] = delta[delta > 0]
    downs[delta < 0] = -delta[delta < 0]
    ups[ups.index[period-1]] = np.mean( ups[:period] )
    ups = ups.drop(ups.index[:(period-1)])
    downs[downs.index[period-1]] = np.mean( downs[:period] )
    downs = downs.drop(downs.index[:(period-1)])
    rs = ups.ewm(com=period-1,min_periods=0,adjust=False,ignore_na=False).mean() /          downs.ewm(com=period-1,min_periods=0,adjust=False,ignore_na=False).mean() 
    rsi = 100 - 100 / (1 + rs)

    stochrsi  = (rsi - rsi.rolling(period).min()) / (rsi.rolling(period).max() - rsi.rolling(period).min())
    stochrsi_K = stochrsi.rolling(smoothK).mean()
    stochrsi_D = stochrsi_K.rolling(smoothD).mean()

    
    

    condition = False;
    yyester_K=stochrsi_K.iloc[-3]*100
    yyester_D=stochrsi_D.iloc[-3]*100
    yester_K=stochrsi_K.iloc[-2]*100
    yester_D=stochrsi_D.iloc[-2]*100
    today_K=stochrsi_K.iloc[-1]*100
    today_D=stochrsi_D.iloc[-1]*100
    if(yester_K < today_K and today_D < 75):
        condition=True
    return condition


#스토캐스틱 1day (반환값 매수조건만족시 True 나머지는 False)
def stockrsidays(symbol):
    url = "https://api.upbit.com/v1/candles/days"

    querystring = {"market":symbol,"count":"200"}

    response = requests.request("GET", url, params=querystring)

    data = response.json()

    df = pd.DataFrame(data)

    series=df['trade_price'].iloc[::-1]

    df = pd.Series(df['trade_price'].values)

    period=10
    smoothK=3
    smoothD=3

    delta = series.diff().dropna()
    ups = delta * 0
    downs = ups.copy()
    ups[delta > 0] = delta[delta > 0]
    downs[delta < 0] = -delta[delta < 0]
    ups[ups.index[period-1]] = np.mean( ups[:period] )
    ups = ups.drop(ups.index[:(period-1)])
    downs[downs.index[period-1]] = np.mean( downs[:period] )
    downs = downs.drop(downs.index[:(period-1)])
    rs = ups.ewm(com=period-1,min_periods=0,adjust=False,ignore_na=False).mean() /          downs.ewm(com=period-1,min_periods=0,adjust=False,ignore_na=False).mean() 
    rsi = 100 - 100 / (1 + rs)

    stochrsi  = (rsi - rsi.rolling(period).min()) / (rsi.rolling(period).max() - rsi.rolling(period).min())
    stochrsi_K = stochrsi.rolling(smoothK).mean()
    stochrsi_D = stochrsi_K.rolling(smoothD).mean()

    
    condition = False;
    yyester_K=stochrsi_K.iloc[-3]*100
    yyester_D=stochrsi_D.iloc[-3]*100
    yester_K=stochrsi_K.iloc[-2]*100
    yester_D=stochrsi_D.iloc[-2]*100
    today_K=stochrsi_K.iloc[-1]*100
    today_D=stochrsi_D.iloc[-1]*100
    if(yester_K < today_K and today_D < today_K and today_D < 60):
        condition=True
    return condition

#스토캐스틱 240min (반환값 매수조건만족시 True 나머지는 False)
def stockrsi240(symbol):
    url = "https://api.upbit.com/v1/candles/minutes/240"

    querystring = {"market":symbol,"count":"200"}

    response = requests.request("GET", url, params=querystring)

    data = response.json()

    df = pd.DataFrame(data)

    series=df['trade_price'].iloc[::-1]

    df = pd.Series(df['trade_price'].values)

    period=14
    smoothK=3
    smoothD=3

    delta = series.diff().dropna()
    ups = delta * 0
    downs = ups.copy()
    ups[delta > 0] = delta[delta > 0]
    downs[delta < 0] = -delta[delta < 0]
    ups[ups.index[period-1]] = np.mean( ups[:period] )
    ups = ups.drop(ups.index[:(period-1)])
    downs[downs.index[period-1]] = np.mean( downs[:period] )
    downs = downs.drop(downs.index[:(period-1)])
    rs = ups.ewm(com=period-1,min_periods=0,adjust=False,ignore_na=False).mean() /          downs.ewm(com=period-1,min_periods=0,adjust=False,ignore_na=False).mean() 
    rsi = 100 - 100 / (1 + rs)

    stochrsi  = (rsi - rsi.rolling(period).min()) / (rsi.rolling(period).max() - rsi.rolling(period).min())
    stochrsi_K = stochrsi.rolling(smoothK).mean()
    stochrsi_D = stochrsi_K.rolling(smoothD).mean()


    condition = False;
    yyester_K=stochrsi_K.iloc[-3]*100
    yyester_D=stochrsi_D.iloc[-3]*100
    yester_K=stochrsi_K.iloc[-2]*100
    yester_D=stochrsi_D.iloc[-2]*100
    today_K=stochrsi_K.iloc[-1]*100
    today_D=stochrsi_D.iloc[-1]*100
    if(yester_K < today_K and today_D < today_K):
        condition=True
    return condition

#스토캐스틱 60min (반환값 매수조건만족시 True 나머지는 False)
def stockrsi60(symbol):
    url = "https://api.upbit.com/v1/candles/minutes/60"

    querystring = {"market":symbol,"count":"200"}

    response = requests.request("GET", url, params=querystring)

    data = response.json()

    df = pd.DataFrame(data)

    series=df['trade_price'].iloc[::-1]

    df = pd.Series(df['trade_price'].values)

    period=14
    smoothK=3
    smoothD=3

    delta = series.diff().dropna()
    ups = delta * 0
    downs = ups.copy()
    ups[delta > 0] = delta[delta > 0]
    downs[delta < 0] = -delta[delta < 0]
    ups[ups.index[period-1]] = np.mean( ups[:period] )
    ups = ups.drop(ups.index[:(period-1)])
    downs[downs.index[period-1]] = np.mean( downs[:period] )
    downs = downs.drop(downs.index[:(period-1)])
    rs = ups.ewm(com=period-1,min_periods=0,adjust=False,ignore_na=False).mean() /          downs.ewm(com=period-1,min_periods=0,adjust=False,ignore_na=False).mean() 
    rsi = 100 - 100 / (1 + rs)

    stochrsi  = (rsi - rsi.rolling(period).min()) / (rsi.rolling(period).max() - rsi.rolling(period).min())
    stochrsi_K = stochrsi.rolling(smoothK).mean()
    stochrsi_D = stochrsi_K.rolling(smoothD).mean()


    condition = False;
    yyester_K=stochrsi_K.iloc[-3]*100
    yyester_D=stochrsi_D.iloc[-3]*100
    yester_K=stochrsi_K.iloc[-2]*100
    yester_D=stochrsi_D.iloc[-2]*100
    today_K=stochrsi_K.iloc[-1]*100
    today_D=stochrsi_D.iloc[-1]*100
    if(yester_K < today_K and today_D < today_K):
        condition=True
    return condition

#macd 1day (반환값 매수조건만족시 True 나머지는 False)
def macddays(symbol):

    url = "https://api.upbit.com/v1/candles/days"


    querystring = {"market":symbol,"count":"200"}

    response = requests.request("GET", url, params=querystring)

    data = response.json()

    df = pd.DataFrame(data)

    df=df.iloc[::-1]

    df=df['trade_price']

    exp1 = df.ewm(span=12, adjust=False).mean() 
    exp2 = df.ewm(span=26, adjust=False).mean()
    macd = exp1-exp2
    exp3 = macd.ewm(span=9, adjust=False).mean()  #signal

    condition = False
    if(((macd[1]-exp3[1] < macd[0]-exp3[0]) and (macd[0]-exp3[0] >= 0)) or (macd[2]-exp3[2] < macd[1]-exp3[1] < macd[0]-exp3[0])):
        condition = True

    return condition

#macd 30분 (반환값 매수조건만족시 True 나머지는 False)
def macd30m(symbol):

    url = "https://api.upbit.com/v1/candles/minutes/30"

    
    querystring = {"market":symbol,"count":"200"}

    response = requests.request("GET", url, params=querystring)

    data = response.json()

    df = pd.DataFrame(data)

    df=df.iloc[::-1]

    df=df['trade_price']

    exp1 = df.ewm(span=12, adjust=False).mean() 
    exp2 = df.ewm(span=26, adjust=False).mean()
    macd = exp1-exp2
    exp3 = macd.ewm(span=9, adjust=False).mean()  #signal

    condition = False
    if(((macd[2]-exp3[2] < 0) and (macd[1]-exp3[1] >= 0)) or ((macd[1]-exp3[1] < 0) and (macd[0]-exp3[0] >= 0))):
        condition = True

    return condition

#MACD 60분 (반환값 매수조건만족시 True 나머지는 False)
def macd60m(symbol):

    url = "https://api.upbit.com/v1/candles/minutes/60"


    querystring = {"market":symbol,"count":"200"}
    
    response = requests.request("GET", url, params=querystring)

    data = response.json()

    df = pd.DataFrame(data)

    df=df.iloc[::-1]

    df=df['trade_price']

    exp1 = df.ewm(span=12, adjust=False).mean() 
    exp2 = df.ewm(span=26, adjust=False).mean()
    macd = exp1-exp2
    exp3 = macd.ewm(span=9, adjust=False).mean()  #signal
    condition = False
    if((macd[1]-exp3[1]) < (macd[0]-exp3[0])):
        condition = True
        
    return condition

#OBV 값 구하는 함수
def OBV(tradePrice, volume):
    obv = pd.Series(index=tradePrice.index)
    obv.iloc[0] = volume.iloc[0]
    
    for i in range(1,len(tradePrice)):
        if tradePrice.iloc[i] > tradePrice.iloc[i-1] : 
            obv.iloc[i] = obv.iloc[i-1] + volume[i]
            
        elif tradePrice.iloc[i] < tradePrice.iloc[i-1] :
            obv.iloc[i] = obv.iloc[i-1] - volume[i]
            
        else:
            obv.iloc[i] = obv.iloc[i-1]
            
    return obv

#코인의 OBV 매수조건 테스트 (반환값 매수조건만족시 True 나머지는 False)
def obv60m(symbol):
    
    url = "https://api.upbit.com/v1/candles/minutes/60"
    querystring = {"market":symbol,"count":"200"}

    response = requests.request("GET", url, params=querystring)

    data = response.json()

    df = pd.DataFrame(data)
    df=df.iloc[::-1]

    obv = OBV(df['trade_price'],df['candle_acc_trade_volume'])
    condition= False
    if(((obv[2]*1.08 < obv[0]) or (obv[1]*1.04 < obv[0])) and (obv[0] > 0)):
        condition = True
    
    return condition    

#코인의 OBV 매수조건 테스트 (반환값 매수조건만족시 True 나머지는 False)
def obv30m(symbol):
    
    url = "https://api.upbit.com/v1/candles/minutes/30"
    querystring = {"market":symbol,"count":"200"}

    response = requests.request("GET", url, params=querystring)

    data = response.json()

    df = pd.DataFrame(data)
    df=df.iloc[::-1]

    obv = OBV(df['trade_price'],df['candle_acc_trade_volume'])
    condition= False
    if(((obv[2]*1.10 < obv[0]) or (obv[1]*1.06 < obv[0])) and (obv[0] > 0)):
        condition = True
    
    return condition    



#내 KRW 자산 조회
def get_my_KRW_Balance():
    return upbit.get_balance("KRW")



# 모든 매수조건 만족 테스트
def buy_test (symbol):
    test = False
    if(macd60m(symbol) and macd30m(symbol) and stockrsiweeks(symbol) and stockrsidays(symbol) 
       and (obv60m(symbol) or obv30m(symbol)) and stockrsi60(symbol) and stockrsi240(symbol) and macddays(symbol)):
        test = True
    return test



########### 메인 로직 ##############################################

# Define variables
BUY_WAITING_LIST = {}
MINUTE = 60
HOUR = 60 * MINUTE


# Function to check if the order is completed
def check_order(order_id):
    result = upbit.get_order(order_id)
    state = result['state']
    if state == 'done':
        return True
    else:
        return False

############# 매수 ##################

# Buy & Sell Main loop

while True:
    try:
        # Get the list of tradable coins
        # tickers = pyupbit.get_tickers(fiat="KRW")
        # Iterate over the list of tradable coins
        for symbol in krw_tickers:
            # Get the current price and yesterday's closing price
            current_price = pyupbit.get_current_price(symbol)
            #yesterday_price = pyupbit.get_yesterday_price(symbol)
            # Calculate the price difference
            #price_diff = (current_price - yesterday_price) / yesterday_price * 100
            # Check if the price difference is greater than 2% and the coin is not in the buy waiting list
            if buy_test and symbol not in BUY_WAITING_LIST:
                # Add the coin to the buy waiting list with the current price and time
                BUY_WAITING_LIST[symbol] = {'price': current_price, 'time': time.time()}
                print(f"{symbol} added to the buy waiting list at {current_price}")
            # Check if the coin is in the buy waiting list
            elif symbol in BUY_WAITING_LIST:
                # Get the temporarily stored price and time
                temp_price = BUY_WAITING_LIST[symbol]['price']
                temp_time = BUY_WAITING_LIST[symbol]['time']
                # Check if the current price is below 1.2% from the temporarily stored price
                if current_price < temp_price * buydown_percent:
                    # Place a market buy order for the coin with 30,000 won
                    krw_balance = upbit.get_balance("KRW")
                    if krw_balance > invest_money*1.01:
                        order = upbit.buy_market_order(symbol, invest_money)
                        print(f"{symbol} bought at {current_price}")
                        BUY_WAITING_LIST.pop(symbol)
                # Check if the coin has been on the buy waiting list continuously for more than 12 hours
                elif time.time() - temp_time > 12 * HOUR:
                    BUY_WAITING_LIST.pop(symbol)
                    print(f"{symbol} removed from the buy waiting list")
        
        # Wait for 1 minute before checking again
        time.sleep(60)
    except Exception as e:
        print(e)
        time.sleep(10)


################# 매 도 ######################
    # 1) Load the coin name, balance amount, and average purchase price from Upbit
    try:
        coin_balance = upbit.get_balances()
        for coin in coin_balance:
            if coin.get('currency') != 'KRW':
                coin_name = coin['currency']
                balance = float(coin['balance'])
                avg_price = float(coin['avg_buy_price'])
                print(f"Coin: {coin_name}, Balance: {balance}, Average Purchase Price: {avg_price}")
    except Exception as e:
        print(f"Error: {e}")

    # 2) Load the number of coins available for sell order from Upbit
    try:
        sellable_coins = upbit.get_balances()
        for coin in sellable_coins:
            if float(coin['locked']) > 0:
                coin_name = coin['currency']
                sellable_amount = float(coin['balance']) - float(coin['locked'])
                print(f"Sellable Coins for {coin_name}: {sellable_amount}")
    except Exception as e:
        print(f"Error: {e}")

    # 3) If the current price of an available coin rises by more than goodsell percent(5%) from the average purchase price 
    # and falls more than aftergoodsell_percent(1.5%) from the highest price, sell at the market price
    try:
        for coin in sellable_coins:
            if coin.get('currency') != 'KRW':
                coin_name = coin['currency']
                ticker = f"KRW-{coin_name}"
                current_price = pyupbit.get_current_price(ticker)
                if current_price is None:
                    continue
                avg_price = float(coin['avg_buy_price'])
                if current_price > avg_price * goodsell_percent:
                    highest_price = pyupbit.get_ohlcv(ticker, interval="day", count=1)['high'][0]
                    if current_price < highest_price * aftergoodsell_percent:
                        sell_price = pyupbit.get_orderbook(ticker)[0]['orderbook_units'][0]['ask_price']
                        upbit.sell_market_order(ticker, sellable_amount, price=sell_price)
                        print(f"{coin_name} good sell {current_price}")
    except Exception as e:
        print(f"Error: {e}")

    # 4) If the condition in 3) is not satisfied and the current price falls by more than deadsell percent(7%) of the average purchase price, sell at the market price
    try:
        for coin in sellable_coins:
            if coin.get('currency') != 'KRW':
                coin_name = coin['currency']
                ticker = f"KRW-{coin_name}"
                current_price = pyupbit.get_current_price(ticker)
                if current_price is None:
                    continue
                avg_price = float(coin['avg_buy_price'])
                sellable_amount = float(coin['balance']) - float(coin['locked'])
                if current_price < avg_price * deadsell_percent:
                    sell_price = pyupbit.get_orderbook(ticker)[0]['orderbook_units'][0]['ask_price']
                    upbit.sell_market_order(ticker, sellable_amount, price=sell_price)
                    print(f"{coin_name} dead sell {current_price}")

    # Wait for 1 minute before checking again
        time.sleep(60)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)

    print("Program ran successfully.")
