"""
Module to get data from coinSpot ReadOnly API
"""

import json
from typing import Dict
from secret import api_key, api_secret
import aiohttp
import asyncio
import hashlib
import hmac
import time
from itertools import count

BASE_URL = 'https://www.coinspot.com.au/api/ro'
BALANCE_URL = '/my/balances'
TRANSACTION_HIST_URL = '/my/transactions/'


class CoinSpotReq:

    NONCE = count(int(time.time()*1000))
    
    def __init__(self, url : str, post_processor = None, payload = {}):
        payload['nonce'] = next(self.NONCE)
        payload = json.dumps(payload, separators=(',',':'))
        self.payload = payload
        self.url = url
        self.sign = hmac.new(api_secret, self.payload.encode('utf-8'), hashlib.sha512).hexdigest()
        self.headers = {'key' : api_key, 'sign' : self.sign, 'Content-type' : 'application/json'}
        self.post_processor = (post_processor if post_processor != None else no_process)

def process_balance(data : Dict, result : Dict) -> Dict:
    total_balance = 0
    coins_held = {}
    for crypto_coin in data['balances'] :
        coin = list(crypto_coin.keys())[0]
        coin_balance = crypto_coin[coin]['audbalance']
        total_balance += coin_balance
        coin_held = crypto_coin[coin]['balance']
        coins_held[coin] = coin_held
    
    result['total_balance'] = total_balance
    result['coins_held'] = coins_held

    return result

def process_transaction_hist(data : Dict, result: Dict) -> Dict: 
    """
    Figure out initial investment for each coin held today
    """

    pass

def no_process(data, result):
    print(data)
    pass

def generate_coin_spot_reqs() -> list:
    return [CoinSpotReq(BASE_URL + BALANCE_URL, process_balance), CoinSpotReq(BASE_URL + TRANSACTION_HIST_URL, process_transaction_hist)]

async def main() -> dict:

    coin_spot_reqs = generate_coin_spot_reqs()
    result = {}

    async with aiohttp.ClientSession() as session:
        for coin_spot_req in coin_spot_reqs:
            async with session.post(coin_spot_req.url, data=coin_spot_req.payload, headers=coin_spot_req.headers) as response:
                data = await response.json()
                coin_spot_req.post_processor(data, result)

    return result

def get_coin_spot_data():
    result = asyncio.get_event_loop().run_until_complete(main())
    return result



