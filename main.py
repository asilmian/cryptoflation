#Written by Asil Mian

import fire
import requests
import time
from cryptoflation.inflation_calculator import calc_pos, calc_pos_w_inflation
from secret import annual_inflation_rate
from coinspot import get_coin_spot_data
import inflation_calculator

def total_profit_w_inflation(rate : float = annual_inflation_rate):
    """
    Returns position of crypto holdings adjusted for previous years' inflation
    Assumes inflation is linear across the year 
    :param: rate: yearly inflation rate, passed from secret by default
    :return: position of cryptocurrency holding in coinspot adjusted for inflation
    """

    coin_data = get_coin_spot_data()
    curr_pos = calc_pos(coin_data['total_balance'])
    print("Your current position is {:+.2f}".format(curr_pos))
    curr_pos = calc_pos_w_inflation(coin_data['total_balance'])
    print("Your current position with inflation is {:+.2f}".format(curr_pos))

    return






if __name__=="__main__":
    fire.Fire({
        "calc_position" : total_profit_w_inflation
    })
