import numpy as np
from Constraint import Constraint
from Objective import Objective
from config import METRIC, OBJECTIVE, NUM_DAYS, NUM_FOODS
from foods import foods, food_keys
from utils import get_var_idx, create_daily_nutrient_coefs, create_single_food_coefs

# Total decision variables: NUM_FOODS * NUM_DAYS
# Variables ordered as: [food1_day1, food1_day2, ..., food1_day7, food2_day1, ..., foodN_day7]

calorie_coefs = np.zeros(NUM_FOODS * NUM_DAYS)
for food_name in food_keys:
    for day in range(NUM_DAYS):
        calorie_coefs[get_var_idx(food_name, day)] = foods[food_name].calories
        
cost_coefs = np.zeros(NUM_FOODS * NUM_DAYS)
for food_name in food_keys:
    for day in range(NUM_DAYS):
        cost_coefs[get_var_idx(food_name, day)] = foods[food_name].price
    
diet_constraints = []

obj = None

if METRIC == "CALORIES":
    if OBJECTIVE == "MIN":
        obj = Objective(
            coefficients=calorie_coefs,
            obj="min"
        )
    elif OBJECTIVE == "MAX":
        obj = Objective(
            coefficients=calorie_coefs,
            obj="max"
        )
    diet_constraints.append(Constraint(
        coefficients=cost_coefs,
        type="<=",
        rhs=100.0
    ))
elif METRIC == "COST":
    if OBJECTIVE == "MIN":
        obj = Objective(
            coefficients=cost_coefs,
            obj="min"
        )
    elif OBJECTIVE == "MAX":
        obj = Objective(
            coefficients=cost_coefs,
            obj="min"
        )
    diet_constraints.append(Constraint(
        coefficients=calorie_coefs,
        type="<=",
        rhs=(2000.0 * 7)
    ))

############################## DAILY MACRONUTRIENT CONSTRAINTS ##############################
for day in range(NUM_DAYS):
    # Daily carb constraint
    carb_coefs = create_daily_nutrient_coefs(day, 'carbs')
    diet_constraints.append(Constraint(
        coefficients=carb_coefs,
        type=">=",
        rhs=150.0
    ))
    
    # Daily fat constraint
    fat_coefs = create_daily_nutrient_coefs(day, 'fat')
    diet_constraints.append(Constraint(
        coefficients=fat_coefs,
        type=">=",
        rhs=75.0
    ))
    
    # Daily protein constraint
    protein_coefs = create_daily_nutrient_coefs(day, 'protein')
    diet_constraints.append(Constraint(
        coefficients=protein_coefs,
        type=">=",
        rhs=170.0
    ))
############################## DAILY MACRONUTRIENT CONSTRAINTS ##############################


################################## DAILY LIMITS ##################################
for day in range(NUM_DAYS):
    # Max 2 bananas per day
    banana_daily_coefs = np.zeros(NUM_FOODS * NUM_DAYS)
    banana_daily_coefs[get_var_idx("Banana", day)] = 1
    diet_constraints.append(Constraint(
        coefficients=banana_daily_coefs,
        type="<=",
        rhs=2.0
    ))
    
    # Max 1 protein powder per day
    protein_powder_daily_coefs = np.zeros(NUM_FOODS * NUM_DAYS)
    protein_powder_daily_coefs[get_var_idx("Protein Powder", day)] = 1
    diet_constraints.append(Constraint(
        coefficients=protein_powder_daily_coefs,
        type="<=",
        rhs=1.0
    ))
    
    # Max 1 smoothie pouch per day
    smoothie_pouch_daily_coefs = np.zeros(NUM_FOODS * NUM_DAYS)
    smoothie_pouch_daily_coefs[get_var_idx("Organic Super Smoothie Mix", day)] = 1
    diet_constraints.append(Constraint(
        coefficients=smoothie_pouch_daily_coefs,
        type="<=",
        rhs=1.0
    ))
    
    # Max 200 g beef per day
    beef_daily_coefs = np.zeros(NUM_FOODS * NUM_DAYS)
    beef_daily_coefs[get_var_idx("Beef", day)] = 1
    diet_constraints.append(Constraint(
        coefficients=beef_daily_coefs,
        type="<=",
        rhs=200.0
    ))
################################## DAILY LIMITS ##################################

################################## WEEKLY LIMITS ##################################
# Max 1 serving of Mahi Mahi per week
mahi_mahi_weekly_coefs = create_single_food_coefs("Mahi Mahi")
diet_constraints.append(Constraint(
    coefficients=mahi_mahi_weekly_coefs,
    type="<=",
    rhs=150
))

# Max 3 servings of Cod per week
cod_weekly_coefs = create_single_food_coefs("Cod")
diet_constraints.append(Constraint(
    coefficients=cod_weekly_coefs,
    type="<=",
    rhs=115 * 3
))

# Max 3 servings of Salmon per week
salmon_weekly_coefs = create_single_food_coefs("Salmon")
diet_constraints.append(Constraint(
    coefficients=salmon_weekly_coefs,
    type="<=",
    rhs=140 * 3
))
################################## WEEKLY LIMITS ##################################

################################## WEEKLY MINIMUMS ##################################
# Min 400 g beef per week
beef_coefs = create_single_food_coefs("Beef")
diet_constraints.append(Constraint(
    coefficients=beef_coefs,
    type=">=",
    rhs=400
))