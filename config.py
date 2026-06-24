import numpy as np

from Food import *

from Objective import Objective
from Constraint import Constraint

from utils import extend_coeffs, create_daily_food_coeffs, create_period_food_coeffs

DAYS_IN_PERIOD  = 7
WEEKS_IN_PERIOD = DAYS_IN_PERIOD / 7

MINIMUM_DAILY_PROTEIN  = 160.0
MINIMUM_DAILY_CARBS    = 165.0
MINIMUM_DAILY_FAT      = 60.0

# *************************** Objective ***************************
min_calorie_objective = Objective(
    type="min",
    coeffs=extend_coeffs(
        coeffs=calorie_coeffs,
        days_in_period=DAYS_IN_PERIOD
    )
)

constraints = []
# *************************** Macro Constraints ***************************
    
# Minimum daily protein constraint
for i in range(DAYS_IN_PERIOD):
    day_coeffs = np.zeros(num_foods * DAYS_IN_PERIOD)
    day_coeffs[i * num_foods: (i * num_foods) + num_foods] = protein_coeffs.copy()
    day_constraint = Constraint(
        coeffs=day_coeffs,
        type=">=",
        rhs=MINIMUM_DAILY_PROTEIN
    )
    constraints.append(day_constraint)
    
# Minimum daily carb constraint
for i in range(DAYS_IN_PERIOD):
    day_coeffs = np.zeros(num_foods * DAYS_IN_PERIOD)
    day_coeffs[i * num_foods: (i * num_foods) + num_foods] = carbs_coeffs.copy()
    day_constraint = Constraint(
        coeffs=day_coeffs,
        type=">=",
        rhs=MINIMUM_DAILY_CARBS
    )
    constraints.append(day_constraint)
    
# Minimum daily fat constraint
for i in range(DAYS_IN_PERIOD):
    day_coeffs = np.zeros(num_foods * DAYS_IN_PERIOD)
    day_coeffs[i * num_foods: (i * num_foods) + num_foods] = fat_coeffs.copy()
    day_constraint = Constraint(
        coeffs=day_coeffs,
        type=">=",
        rhs=MINIMUM_DAILY_FAT
    )
    constraints.append(day_constraint)
    
# *************************** Peanut Butter Constraints ***************************
if "Peanut Butter" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Peanut Butter",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=25
        )
        constraints.append(c)
    
# *************************** Protein Powder Constraints ***************************
if "Protein Powder" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Protein Powder",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=1
        )
        constraints.append(c)
    
# *************************** Egg Constraints ***************************
if "Egg" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Egg",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=5
        )
        constraints.append(c)
    
# *************************** Butter Constraints ***************************
if "Butter" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Butter",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=1
        )
        constraints.append(c)
    
# *************************** Beef Constraints ***************************
if "Beef" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Beef",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=300
        )
        constraints.append(c)
    # --------------------------- Periodic Constraints ---------------------------
    constraints.append(
        Constraint(
            coeffs=create_period_food_coeffs(
                food_name="Beef",
                food_keys=food_keys,
                days_in_period=DAYS_IN_PERIOD
            ),
            type=">=",
            rhs=400 * WEEKS_IN_PERIOD
        )
    )
    constraints.append(
        Constraint(
            coeffs=create_period_food_coeffs(
                food_name="Beef",
                food_keys=food_keys,
                days_in_period=DAYS_IN_PERIOD
            ),
            type="<=",
            rhs=800 * WEEKS_IN_PERIOD
        )
    )
    
# *************************** Organic Super Smoothie Mix Constraints ***************************
if "Organic Super Smoothie Mix" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Organic Super Smoothie Mix",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=1
        )
        constraints.append(c)
    
# *************************** Blueberry Constraints ***************************
if "Blueberries" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Blueberries",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type=">=",
            rhs=100
        )
        constraints.append(c)
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Blueberries",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=150
        )
        constraints.append(c)
    
# *************************** Salmon Constraints ***************************
# --------------------------- Daily Constraints ---------------------------
for i in range(DAYS_IN_PERIOD):
    c = Constraint(
        coeffs=create_daily_food_coeffs(
            food_name="Salmon",
            food_keys=food_keys,
            day=i,
            days_in_period=DAYS_IN_PERIOD
            ),
        type="<=",
        rhs=200
    )
    constraints.append(c)
# --------------------------- Periodic Constraints ---------------------------
constraints.append(
    Constraint(
        coeffs=create_period_food_coeffs(
            food_name="Salmon",
            food_keys=food_keys,
            days_in_period=DAYS_IN_PERIOD
        ),
        type="<=",
        rhs=420 * WEEKS_IN_PERIOD
    )
)
constraints.append(
    Constraint(
        coeffs=create_period_food_coeffs(
            food_name="Salmon",
            food_keys=food_keys,
            days_in_period=DAYS_IN_PERIOD
        ),
        type="<=",
        rhs=0
    )
)

# *************************** Chicken Constraints ***************************
if "Chicken" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Chicken",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=250
        )
        constraints.append(c)
    
# *************************** Normandy Vegetables Constraints ***************************
if "Normandy Vegetables" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Normandy Vegetables",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=200
        )
        constraints.append(c)
    # --------------------------- Periodic Constraints ---------------------------
    constraints.append(
        Constraint(
            coeffs=create_period_food_coeffs(
                food_name="Normandy Vegetables",
                food_keys=food_keys,
                days_in_period=DAYS_IN_PERIOD
            ),
            type=">=",
            rhs=200 * DAYS_IN_PERIOD
        )
    )
    
# *************************** Raw Spinach Constraints ***************************
if "Raw Spinach" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Raw Spinach",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=50
        )
        constraints.append(c)
    # --------------------------- Periodic Constraints ---------------------------
    constraints.append(
        Constraint(
            coeffs=create_period_food_coeffs(
                food_name="Raw Spinach",
                food_keys=food_keys,
                days_in_period=DAYS_IN_PERIOD
            ),
            type=">=",
            rhs=200 * WEEKS_IN_PERIOD
        )
    )

# *************************** Lamb Constraints ***************************
if "Lamb" in foods:
    # --------------------------- Periodic Constraints ---------------------------
    constraints.append(
        Constraint(
            coeffs=create_period_food_coeffs(
                food_name="Lamb",
                food_keys=food_keys,
                days_in_period=DAYS_IN_PERIOD
            ),
            type="<=",
            rhs=400 * WEEKS_IN_PERIOD
        )
    )

# *************************** Banana Constraints ***************************
if "Banana" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Banana",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=200
        )
        constraints.append(c)

# *************************** Cod Constraints ***************************
if "Cod" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Cod",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=250
        )
        constraints.append(c)
    # --------------------------- Periodic Constraints ---------------------------
    constraints.append(
        Constraint(
            coeffs=create_period_food_coeffs(
                food_name="Cod",
                food_keys=food_keys,
                days_in_period=DAYS_IN_PERIOD
            ),
            type="<=",
            rhs=420 * WEEKS_IN_PERIOD
        )
    )

# *************************** Greek Yogurt (Nonfat) Constraints ***************************
if "Greek Yogurt (Nonfat)" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Greek Yogurt (Nonfat)",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type=">=",
            rhs=100
        )
        constraints.append(c)
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Greek Yogurt (Nonfat)",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=200
        )
        constraints.append(c)

# *************************** Olive Oil Constraints ***************************
if "Olive Oil" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Olive Oil",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type=">=",
            rhs=14.7
        )
        constraints.append(c)
    
# *************************** Apple Constraints ***************************
if "Apple" in foods:
    # --------------------------- Daily Constraints ---------------------------
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Apple",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type=">=",
            rhs=175.0
        )
        constraints.append(c)
    for i in range(DAYS_IN_PERIOD):
        c = Constraint(
            coeffs=create_daily_food_coeffs(
                food_name="Apple",
                food_keys=food_keys,
                day=i,
                days_in_period=DAYS_IN_PERIOD
                ),
            type="<=",
            rhs=250.0
        )
        constraints.append(c)
    
# *************************** Salmon + Normandy Vegetables Constraints ***************************
# --------------------------- Periodic Constraints ---------------------------
constraints.append(
    Constraint(
        coeffs=create_period_food_coeffs(
            food_name="Salmon + Normandy Vegetables",
            food_keys=food_keys,
            days_in_period=DAYS_IN_PERIOD
        ),
        type="<=",
        rhs=2 * WEEKS_IN_PERIOD
    )
)
    
# *************************** Salmon + White Rice Constraints ***************************
# --------------------------- Periodic Constraints ---------------------------
constraints.append(
    Constraint(
        coeffs=create_period_food_coeffs(
            food_name="Salmon + White Rice",
            food_keys=food_keys,
            days_in_period=DAYS_IN_PERIOD
        ),
        type="<=",
        rhs=2 * WEEKS_IN_PERIOD
    )
)

# *************************** Mahi Mahi Constraints ***************************
# --------------------------- Periodic Constraints ---------------------------
constraints.append(
    Constraint(
        coeffs=create_period_food_coeffs(
            food_name="Mahi Mahi",
            food_keys=food_keys,
            days_in_period=DAYS_IN_PERIOD
        ),
        type="<=",
        rhs=0
    )
)