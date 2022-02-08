#Written by Asil Mian
#for Kogan coding challenge

import fire
import requests
import time
from secret import annual_inflation_rate
from coinspot import get_coin_spot_data

def total_profit_w_inflation(rate : float = annual_inflation_rate) -> float:
    """
    Returns position of crypto holdings adjusted for previous years' inflation
    Assumes inflation is linear across the year 
    :param: rate: yearly inflation rate, passed from secret by default
    :return: position of cryptocurrency holding in coinspot adjusted for inflation
    """
    
    """ Plan:
        1- Get all coins held and calculate curr value in AUD: 
        - sum AUD value of all coins (cvh)
        2- Calulate current postion in AUD:
        -use deposit - withdrawl history
        3- Calculate current position overall: 
        - cvh - AUD put in
        4- Calculate current inflation: 
        - get todays date
        - calculate how many days into the year are we
        - (days dvi 365) * inflation rate = curr inflation rate (cir)
        5- Calculate current value held in AUD with inflation rate: 
        -  (totalAUD^2) div (totalAUD + (totalAUD * cir) = deflated money
        - calculate position with deflated money: 
        - cvh - deflated money
    """


    get_coin_spot_data()

    return 1.0
    # curr_value_AUD = calc_current_crypto_value(coin_spot_data)

    # total_AUD_invested = calc_total_AUD(coin_spot_data)

    # curr_pos = curr_value_AUD - total_AUD_invested

    # est_inflation = estmiate_inflation()

    # inflated_val = total_AUD_invested * (1+ est_inflation)

    # curr_pos_w_inflation = curr_value_AUD - inflated_val






if __name__=="__main__":
    fire.Fire({
        "test" : total_profit_w_inflation
    })