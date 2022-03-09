from secret import current_investment, annual_inflation_rate
import datetime


DAYS_IN_YEAR = 365

def calc_pos(total_balance : float, initial_pos : float = current_investment) -> float:
    return total_balance - initial_pos

def calc_pos_w_inflation( total_balance : float, initial_pos : float = current_investment, inflation_rate : float = annual_inflation_rate) -> float:
    curr_date = datetime.date.today()
    day_of_year = curr_date.timetuple().tm_yday

    applicable_inf_rate = (day_of_year/DAYS_IN_YEAR) * annual_inflation_rate
    inflated_investment = (initial_pos * applicable_inf_rate) + initial_pos

    return total_balance - inflated_investment
