"""
Module to get data from coinSpot ReadOnly API
"""
import json
from operator import ne
from pickle import DICT
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
DEPOSIT_HIST_URL = '/my/deposits'
WITHDRAW_HIST_URL = '/my/withdrawals'


class CoinSpotReq:

    NONCE = count(int(time.time()*1000))
    
    def __init__(self, url : str, payload = {}) -> None:
        payload['nonce'] = next(self.NONCE)
        payload = json.dumps(payload, separators=(',',':'))
        self.payload = payload
        self.url = url
        self.sign = hmac.new(api_secret, self.payload.encode('utf-8'), hashlib.sha512).hexdigest()
        self.headers = {'key' : api_key, 'sign' : self.sign, 'Content-type' : 'application/json'}

async def access_coin_spot() -> Dict:

    async with aiohttp.ClientSession() as session:

        req_model = CoinSpotReq(url=BASE_URL + BALANCE_URL)
        async with session.post(req_model.url, data=req_model.payload, headers=req_model.headers) as response:
            data = await response.json()
            print(data)

        req_model = CoinSpotReq(url=BASE_URL + DEPOSIT_HIST_URL)
        async with session.post(req_model.url, data=req_model.payload, headers=req_model.headers) as response:
            data = await response.json()
            print(data)

        req_model = CoinSpotReq(url=BASE_URL + WITHDRAW_HIST_URL)
        async with session.post(req_model.url, data=req_model.payload, headers=req_model.headers) as response:
            data = await response.text()
            print(data)

def get_coin_spot_data():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(access_coin_spot())



