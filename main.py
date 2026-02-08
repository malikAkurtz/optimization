from Simplex import System
from constraints import NUM_FOODS, NUM_DAYS, diet_constraints, obj
from foods import foods, food_keys
from utils import get_var_idx

def main():
    
    system = System(
        num_decision_vars=NUM_FOODS * NUM_DAYS,
        constraints=diet_constraints,
        objective=obj
    )
    
    # 1) Make sure we are maximizing an objective, transform if necessary
    system._verify_objective()
    # 2) Ensure the RHS >= 0
    system._ensure_positve_rhs()
    # 3) Put system in standard form
    system._standardize()
    # 4) Run Phase 1
    system._phase_1()
    # 5) Run Phase 2
    optimal_vals, optimal_z = system._phase_2()
    
    if optimal_vals is None:
        print("No optimal solution found!")
        return
    
    # Display daily meal plan
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    print("\n" + "="*70)
    print("WEEKLY MEAL PLAN")
    print("="*70)
    
    for day_idx, day_name in enumerate(days):
        print(f"\n{day_name.upper()}:")
        print("-" * 70)
        
        day_calories = 0
        day_carbs = 0
        day_fat = 0
        day_protein = 0
        
        for food_name in food_keys:
            var_idx = get_var_idx(food_name, day_idx)
            amount = optimal_vals[var_idx]
            
            if amount > 0.01:  # Only show foods with meaningful amounts
                food = foods[food_name]
                print(f"  {food_name:30s} {amount:8.2f} {food.units}")
                
                day_calories += amount * food.calories
                day_carbs += amount * food.carbs
                day_fat += amount * food.fat
                day_protein += amount * food.protein
        
        print(f"\n  Daily Totals:")
        print(f"    Calories: {day_calories:8.2f} kcal")
        print(f"    Carbs:    {day_carbs:8.2f} g")
        print(f"    Fat:      {day_fat:8.2f} g")
        print(f"    Protein:  {day_protein:8.2f} g")
    
    print("\n" + "="*70)
    print(f"TOTAL WEEKLY CALORIES: {optimal_z:.2f} kcal")
    print("="*70)

if __name__ == "__main__":
    main()