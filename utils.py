import numpy as np
from foods import foods, food_keys
from config import NUM_DAYS, NUM_FOODS

# Helper function to get variable index for a specific food on a specific day
def get_var_idx(food_name: str, day: int) -> int:
    """
    Get the variable index for a food on a specific day.
    day: 0-6 (Monday-Sunday)
    """
    food_idx = food_keys.index(food_name)
    return food_idx * NUM_DAYS + day

# Helper function to create coefs for e.g. monday_carbs
def create_daily_nutrient_coefs(day: int, nutrient: str):
    """
    Create the coefficients corresponding to a particular nutrient for a particular day
    day: 0-6 (Monday-Sunday)
    """
    # Create coefficient vector
    coefs = np.zeros(NUM_FOODS * NUM_DAYS)
    
    # Iterate through each food
    for food in food_keys:
        # Get its nutrient content
        nutrient_value = getattr(foods[food], nutrient)
        # Set the correct coef to nutrient_value
        coefs[get_var_idx(food, day)] = nutrient_value
        
    return coefs

# Helper function to create coefs for a single food across the entire week
def create_single_food_coefs(food_name: str):
    """
    Create the coefficients corresponding to a particular food across all days
    food: str
    """
    # Create coefficient vector
    coefs = np.zeros(NUM_FOODS * NUM_DAYS)
    
    # For each day
    for day in range(NUM_DAYS):
        # Put a 1 at the index corresponding to food_day
        coefs[get_var_idx(food_name, day)] = 1.0
        
    return coefs