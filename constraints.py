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

############################## OBJECTIVES ##############################
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
        rhs=500.0 # This value is your weekly budget
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
        rhs=(2000.0 * 7) # Number of total calories per week
    ))
############################## OBJECTIVES ##############################

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


################################## DAILY LIMITS/REQUIREMENTS ##################################
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
    
    # Max of 2 filets of salmon per day
    salmon_daily_coefs = np.zeros(NUM_FOODS * NUM_DAYS)
    salmon_daily_coefs[get_var_idx("Salmon", day)] = 1
    diet_constraints.append(Constraint(
        coefficients=salmon_daily_coefs,
        type="<=",
        rhs=140.0 
    ))
    
    # Max of 2 cups of vegetables per day
    veggies_daily_coefs = np.zeros(NUM_FOODS * NUM_DAYS)
    veggies_daily_coefs[get_var_idx("Normandy Vegetables", day)] = 1
    diet_constraints.append(Constraint(
        coefficients=veggies_daily_coefs,
        type="<=",
        rhs=100.0 * 2 # roughly 100 g per cup
    ))
    
    # 100 g blueberries per day
    blueberries_daily_coefs = np.zeros(NUM_FOODS * NUM_DAYS)
    blueberries_daily_coefs[get_var_idx("Blueberries", day)] = 1
    diet_constraints.append(Constraint(
        coefficients=blueberries_daily_coefs,
        type="=",
        rhs=100.0
    ))
    
    # Max of 200 g greek yogurt per day
    greek_yogurt_daily_coefs = np.zeros(NUM_FOODS * NUM_DAYS)
    greek_yogurt_daily_coefs[get_var_idx("Greek Yogurt (Nonfat)", day)] = 1
    diet_constraints.append(Constraint(
        coefficients=greek_yogurt_daily_coefs,
        type="<=",
        rhs=200.0
    ))
    
    # Max of 100 g spinach per day
    spinach_daily_coefs = np.zeros(NUM_FOODS * NUM_DAYS)
    spinach_daily_coefs[get_var_idx("Spinach (Frozen)", day)] = 1
    diet_constraints.append(Constraint(
        coefficients=spinach_daily_coefs,
        type="<=",
        rhs=100.0
    ))
    
    # Max of 100 g peanut butter per day
    peanut_butter_daily_coefs = np.zeros(NUM_FOODS * NUM_DAYS)
    peanut_butter_daily_coefs[get_var_idx("Peanut Butter", day)] = 1
    diet_constraints.append(Constraint(
        coefficients=peanut_butter_daily_coefs,
        type="<=",
        rhs=100.0
    ))
    
    # Max of 40 g smoked salmon per day
    smoked_salmon_daily_coefs = np.zeros(NUM_FOODS * NUM_DAYS)
    smoked_salmon_daily_coefs[get_var_idx("Smoked Salmon", day)] = 1
    diet_constraints.append(Constraint(
        coefficients=smoked_salmon_daily_coefs,
        type="<=",
        rhs=40.0
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

# Max 700 g spinach per week
spinach_weekly_coefs = create_single_food_coefs("Spinach (Frozen)")
diet_constraints.append(Constraint(
    coefficients=spinach_weekly_coefs,
    type="<=",
    rhs=700
))

# Max 1400 g greek yogurt per week
greek_yogurt_weekly_coefs = create_single_food_coefs("Greek Yogurt (Nonfat)")
diet_constraints.append(Constraint(
    coefficients=greek_yogurt_weekly_coefs,
    type="<=",
    rhs= 200.0 * 7
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
################################## WEEKLY MINIMUMS ##################################

################################## WEEKLY REQUIREMENTS ##################################
# 3 servings salmon per week
salmon_coefs = create_single_food_coefs("Salmon")
diet_constraints.append(Constraint(
    coefficients=salmon_coefs,
    type="=",
    rhs=140.0*3
))