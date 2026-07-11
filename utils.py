import numpy as np

def get_days_elements(quantities: np.ndarray, num_foods: int, day: int) -> np.ndarray:
    return quantities[day * num_foods: (day * num_foods) + num_foods].copy()

def extend_coeffs(coeffs: np.ndarray, days_in_period: int) -> np.ndarray:
    as_list = list(coeffs)
    
    extended_coeffs = as_list * days_in_period
    
    return np.array(extended_coeffs)

# Returns the full coefficient vector pertaining to a particular food on a particular day
def create_daily_food_coeffs(food_name: str, food_keys: dict, day: int, days_in_period: int) -> np.ndarray:
    num_foods = len(food_keys)
    food_idx = food_keys.index(food_name)
    coeffs = np.zeros(num_foods * days_in_period)
    coeffs[(day * num_foods) + food_idx] = 1.0
    return coeffs

# Returns the full coefficient vector pertaining to a particular food for the entire period
def create_period_food_coeffs(food_name: str, food_keys: dict, days_in_period: int) -> np.ndarray:
    num_foods = len(food_keys)
    food_idx = food_keys.index(food_name)
    coeffs = np.zeros(num_foods * days_in_period)
    for i in range(days_in_period):
        coeffs[(i * num_foods) + food_idx] = 1.0
    return coeffs
