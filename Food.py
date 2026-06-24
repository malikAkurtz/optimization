import numpy as np

class Ingredient():
    def __init__(self, name: str, units: str, price: float, calories: float, carbs: float, fat: float, protein: float):
        self.name       = name
        self.units      = units
        self.price      = price
        self.calories   = calories
        self.carbs      = carbs
        self.fat        = fat
        self.protein    = protein
        
    def get_units(self):
        return self.units
        
    def get_calories(self):
        return self.calories
    
    def get_carbs(self):
        return self.carbs
    
    def get_fat(self):
        return self.fat
    
    def get_protein(self):
        return self.protein
        
# *************************** Ingredients ***************************
beef = Ingredient(
    name="Beef",
    units="g",
    price=(24.99 / 2268), # ~$5.00/lb ground beef (5lb pack)
    calories=1.5, 
    carbs=0, 
    fat=0.0706, 
    protein=0.2028
)
egg = Ingredient(
    name="Egg",
    units="Eggs",
    price=(14.99 / 60), # 5-dozen pack
    calories=60, 
    carbs=0.0, 
    fat=4, 
    protein=6
)
milk = Ingredient(
    name="Milk",
    units="ml",
    price=(6.49 / 7570), # 2-gallon pack (~7570ml)
    calories=0.634, 
    carbs=0.0338, 
    fat=0.0338,
    protein=0.0338,
)
chicken = Ingredient(
    name="Chicken",
    units="g",
    price=0.0075, # $3.39/lb conversion we calculated
    calories=1.76,
    carbs=0.0,
    fat=0.0545,
    protein=0.296
)
butter = Ingredient(
    name="Butter",
    units="tbsp",
    price=(13.99 / 128), # 4lb pack has 128 tbsp
    calories=100, 
    carbs=0.0, 
    fat=11,
    protein=0.0,
)
creamer = Ingredient(
    name="Creamer",
    units="ml",
    price=(5.99 / 1890), # 1.89L Half & Half
    calories=2.367, 
    carbs=0.3381, 
    fat=0.1014,
    protein=0.0,
)
smoked_salmon = Ingredient(
    name="Smoked Salmon",
    units="g",
    price=(22.99 / 680), # 24oz (680g) twin pack
    calories=1.17, 
    carbs=0.0, 
    fat=0.0432,
    protein=0.183,
)
white_rice = Ingredient(
    name="White Rice",
    units="g",
    price=(19.99 / 11340), # 25lb bag (11,340g)
    calories=1.3,
    carbs=0.28,
    fat=0.003,
    protein=0.027
)
lamb = Ingredient(
    name="Lamb",
    units="g",
    price=(28.50 / 2267), # Leg of lamb ~$5.69/lb
    calories=1.852,
    carbs=0.0,
    fat=0.1146,
    protein=0.194
)
protein_powder = Ingredient(
    name="Protein Powder",
    units="scoops",
    price=(59.99 / 80), # Whey Isolate 5.4lb (~80 servings)
    calories=120.0,
    carbs=3.0,
    fat=2.0,
    protein=24.0
)
peanut_butter = Ingredient(
    name="Peanut Butter",
    units="g",
    price=(12.49 / 2260), # 2-pack 40oz jars
    calories=5.625,
    carbs=0.2188,
    fat=0.4688,
    protein=0.25
)
banana = Ingredient(
    name="Banana",
    units="g",
    price=(7 * 121) / 1.69, # ~3lb bunch (approx 7 bananas)
    calories=(970 / 1000),
    carbs=(227 / 1000),
    fat=(2.8 / 1000),
    protein=(7.4 / 1000)
)
organic_super_smoothie = Ingredient(
    name="Organic Super Smoothie Mix",
    units="pouches",
    price=(12.99 / 6), # Frozen 6-pack
    calories=100.0,
    carbs=24.0,
    fat=1.0,
    protein=3.0
)
salmon = Ingredient(
    name="Salmon",
    units="g",
    price=(45.39 / 1360.78), # 3lb bag
    calories=1.31,
    carbs=0.0,
    fat=0.0476,
    protein=0.2202
)
mahi_mahi = Ingredient(
    name="Mahi Mahi",
    units="g",
    price=(24.99 / 1360), # 3lb bag
    calories=0.838,
    carbs=0.0,
    fat=0.0088,
    protein=0.1852
)
cod = Ingredient(
    name="Cod",
    units="g",
    price=(21.99 / 907), # 2lb bag
    calories=0.823,
    carbs=0.0,
    fat=0.0,
    protein=0.194
)
apple = Ingredient(
    name="Apple",
    units="g",
    price=None, # Organic 12-count bag
    calories=(520.0 / 1000),
    carbs=(138.1 / 1000),
    fat=(1.7 / 1000),
    protein=(2.6 / 1000)
)
normandy_veggies = Ingredient(
    name="Normandy Vegetables",
    units="g",
    price=0.0040, 
    calories=0.328,
    carbs=0.057,
    fat=0.003,
    protein=0.024
)
blueberries = Ingredient(
    name="Blueberries",
    units="g",
    price=0.0117,      # $5.99 / 510g = $0.0117 per gram
    calories=0.57,     # 57 kcal per 100g → 0.57 per gram
    carbs=0.144,       # 14.4g per 100g → 0.144 per gram
    fat=0.003,         # 0.3g per 100g → 0.003 per gram
    protein=0.007      # 0.7g per 100g → 0.007 per gram
)
raw_spinach = Ingredient(
    name="Raw Spinach",
    units="g",
    price=0.0044,
    calories=(230 / 1000),  
    carbs=(36.3 / 1000),  
    fat=(3.9 / 1000),
    protein=(28.6 / 1000) 
)
greek_yogurt = Ingredient(
    name="Greek Yogurt (Nonfat)",
    units="g",
    price=0.0037,      # $4.99 / 1361g = $0.0037 per gram
    calories=0.59,     # 59 kcal per 100g → 0.59 per gram
    carbs=0.038,       # 3.8g per 100g → 0.038 per gram
    fat=0.0,           # 0g per 100g (nonfat)
    protein=0.10       # 10g per 100g → 0.10 per gram
)
olive_oil = Ingredient(
    name="Olive Oil",
    units="ml",
    price=None,
    calories=(8115.0 / 1000),  
    carbs=(0.0 / 1000),  
    fat=(913.0 / 1000),
    protein=(0.0 / 1000) 
)

ingredients = {
    "Beef" : beef,
    "Egg" : egg,
    "Milk" : milk,
    "Chicken" : chicken,
    "Butter" : butter,
    "Creamer" :creamer,
    "Smoked Salmon" : smoked_salmon,
    "White Rice": white_rice,
    "Lamb" : lamb,
    "Protein Powder": protein_powder,
    "Peanut Butter" : peanut_butter,
    "Banana" : banana,
    "Organic Super Smoothie Mix" : organic_super_smoothie,
    "Salmon" : salmon,
    "Mahi Mahi" : mahi_mahi,
    "Cod" : cod,
    "Apple": apple,
    "Normandy Vegetables" : normandy_veggies,
    "Blueberries" : blueberries,
    "Raw Spinach" : raw_spinach,
    "Greek Yogurt (Nonfat)" : greek_yogurt,
    "Olive Oil" : olive_oil
}

class Recipe():
    def __init__(self, name: str, ingredients: dict[str, float]):
        self.name        = name
        self.ingredients = ingredients
        
    def get_units(self):
        return "servings"
    
    def get_calories(self):
        total_calories = 0
        for ingredient_name, num_units in self.ingredients.items():
            total_calories += (ingredients[ingredient_name].get_calories() * num_units)
        return total_calories
    
    def get_carbs(self):
        total_carbs = 0
        for ingredient_name, num_units in self.ingredients.items():
            total_carbs += (ingredients[ingredient_name].get_carbs() * num_units)
        return total_carbs
    
    def get_fat(self):
        total_fat = 0
        for ingredient_name, num_units in self.ingredients.items():
            total_fat += (ingredients[ingredient_name].get_fat() * num_units)
        return total_fat
    
    def get_protein(self):
        total_protein = 0
        for ingredient_name, num_units in self.ingredients.items():
            total_protein += (ingredients[ingredient_name].get_protein() * num_units)
        return total_protein
    
# *************************** Recipes ***************************
beef_normandy_veggies = Recipe(
    name="Beef + Normandy Vegetables",
    ingredients={
        "Beef": 200,
        "Normandy Vegetables": 100
    }
)
beef_white_rice = Recipe(
    name="Beef + White Rice",
    ingredients={
        "Beef": 200,
        "White Rice": 100
    }
)
chicken_normandy_veggies = Recipe(
    name="Chicken + Normandy Vegetables",
    ingredients={
        "Chicken": 200,
        "Normandy Vegetables": 100
    }
)
chicken_white_rice = Recipe(
    name="Chicken + White Rice",
    ingredients={
        "Chicken": 200,
        "White Rice": 100
    }
)
salmon_normandy_veggies = Recipe(
    name="Salmon + Normandy Vegetables",
    ingredients={
        "Salmon": 200,
        "Normandy Vegetables": 100
    }
)
salmon_white_rice = Recipe(
    name="Salmon + White Rice",
    ingredients={
        "Salmon": 200,
        "White Rice": 100
    }
)
cod_normandy_veggies = Recipe(
    name="Cod + Normandy Vegetables",
    ingredients={
        "Cod": 200,
        "Normandy Vegetables": 100
    }
)
cod_white_rice = Recipe(
    name="Cod + White Rice",
    ingredients={
        "Cod": 200,
        "White Rice": 100
    }
)

recipes = {
    "Beef + Normandy Vegetables": beef_normandy_veggies,
    "Beef + White Rice": beef_white_rice,
    chicken_normandy_veggies.name: chicken_normandy_veggies,
    chicken_white_rice.name: chicken_white_rice,
    salmon_normandy_veggies.name: salmon_normandy_veggies,
    salmon_white_rice.name: salmon_white_rice,
    cod_normandy_veggies.name: cod_normandy_veggies,
    cod_white_rice.name: cod_white_rice
}

foods = ingredients | recipes

food_keys = list(foods.keys())
num_foods = len(food_keys)

calorie_coeffs = np.array([f.get_calories() for f in foods.values()])
protein_coeffs = np.array([f.get_protein() for f in foods.values()])
carbs_coeffs   = np.array([f.get_carbs() for f in foods.values()])
fat_coeffs     = np.array([f.get_fat() for f in foods.values()])


