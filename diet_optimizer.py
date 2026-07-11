import numpy as np

from LinearProgram import LinearProgram

from config import *
from utils import get_days_elements

def main():
    LP = LinearProgram(
        objective=min_calorie_objective,
        constraints=constraints
    )
    
    LP.optimize()
    
    quantities = np.array(LP.solution[:LP.num_decision_vars])
     
    for i in range(DAYS_IN_PERIOD):
        print("*" * 20 + f" Day {i} Diet " + "*" * 20)
        
        days_quantities = get_days_elements(
            quantities=quantities,
            num_foods=num_foods,
            day=i
        )
        
        for j, (name, food) in enumerate(foods.items()):
            name_length = len(name)
            shift = 50 - name_length
            if not np.isclose(days_quantities[j], 0.0):
                print(f"{name}: {days_quantities[j]:>{shift}.2f} {food.get_units()}")
            
        print("-" * 20 + f" Day {i} Totals " + "-" * 20)
        
        days_total_calories = np.dot(days_quantities, calorie_coeffs)
        days_total_protein  = np.dot(days_quantities, protein_coeffs)
        days_total_carbs    = np.dot(days_quantities, carbs_coeffs)
        days_total_fat      = np.dot(days_quantities, fat_coeffs)
        
        print(f"Total Calories: {days_total_calories:>{50 - len("Total Calories")}.0f}")
        print(f"Protein: {days_total_protein:>{50 - len("Protein")}.0f} g")
        print(f"Carbs: {days_total_carbs:>{50 - len("Carbs")}.0f} g")
        print(f"Fat: {days_total_fat:>{50 - len("Fat")}.0f} g")
        
    units_required_dict = {}
    for j, (name, food) in enumerate(foods.items()):
        units_required = 0
        
        for i in range(DAYS_IN_PERIOD):
            days_quantities = get_days_elements(
                quantities=quantities,
                num_foods=num_foods,
                day=i
            )
            units_required += days_quantities[j]
            
        units_required_dict[name] = units_required
                
    print("=" * 20 + f" Required Inventory " + "=" * 20)
    
    required_inventory = {}
    
    for i, (food_name, units_required) in enumerate(units_required_dict.items()):
        food = foods[food_name]
        if not np.isclose(units_required, 0.0):
            if isinstance(food, Ingredient):
                required_inventory[food_name] = required_inventory.get(food_name, 0.0) + units_required
            elif isinstance(food, Recipe):
                for ingredient_name, num_units in food.ingredients.items():
                    required_inventory[ingredient_name] = required_inventory.get(ingredient_name, 0.0) + (num_units * units_required)
                
            
    for ingredient_name, required_quantity in required_inventory.items():
        name_length = len(ingredient_name)
        shift = 50 - name_length
        print(f"{ingredient_name}: {required_quantity:>{shift}.2f} {foods[ingredient_name].get_units()}")
        
        
    print("=" * 20 + f" To Prep " + "=" * 20)
    for food_name, units_required in units_required_dict.items():
        food = foods[food_name]
        name_length = len(food_name)
        shift = 50 - name_length
        if not np.isclose(units_required, 0.0) and isinstance(food, Recipe):
            print(f"{food_name}: {units_required:>{shift}.2f} {foods[food_name].get_units()}")
    
    
if __name__=="__main__":
    main()
