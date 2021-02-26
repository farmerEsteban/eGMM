import time
import requests
import hmac
import hashlib

from apikeys import keysB


symbolB = 'BUSDUSDT'
sideB = 'BUY'
typeB = 'LIMIT'
timeInForceB = 'GTC'
quantityB = str(10719.28)

precision = 8
priceB = 0.9998
priceB_str = '{:0.0{}f}'.format(priceB, precision)
recvWindowB = str(50000)


#########
timestampB = str(int(time.time()*1000))

requestBody = bytes('symbol='+symbolB+'&side='+sideB+'&type='+typeB+'&timeInForce='+timeInForceB+'&quantity='+quantityB+'&price='+priceB_str+'&recvWindow='+recvWindowB+'&timestamp='+timestampB, 'utf-8')

signature = hmac.new(
    keysB()[1],
    msg=requestBody,
    digestmod=hashlib.sha256
).hexdigest().lower()

header =  {'X-MBX-APIKEY':keysB()[0]}
query_string = str('https://api.binance.com/api/v3/order?symbol='+symbolB+'&side='+sideB+'&type='+typeB+'&timeInForce='+timeInForceB+'&quantity='+quantityB+'&price='+priceB_str+'&recvWindow='+recvWindowB+'&timestamp='+timestampB+'&signature='+signature)

res = requests.post(query_string, headers=header)
print(res.text)
print(res.status_code)
#############################


def sign_and_stamp(requestBody):
    timestamp = str(int(time.time()*1000))

    signature = hmac.new(
        secretKeyB,
        msg=requestBody,
        digestmod=hashlib.sha256
        ).hexdigest().lower()

    return(signature, timestamp)

def get_market_price(pair):
    return()

def get_volatility(pair, volatility_range_days):
    volatility = 1
    mean = 1
    return(volatility, mean)

def place_order(pair, price, amount):
    return()

def generate_grid(variance):
    return()

def check_connectivity():
    return()
