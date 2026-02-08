from Food import Food

beef = Food(
    name="Beef",
    units="g",
    price=(24.99 / 2268), # ~$5.00/lb ground beef (5lb pack)
    calories=1.5, 
    carbs=0, 
    fat=0.0706, 
    protein=0.2028
    )
egg = Food(
    name="Egg",
    units="Eggs",
    price=(14.99 / 60), # 5-dozen pack
    calories=60, 
    carbs=0, 
    fat=0.15, 
    protein=6
    )
milk = Food(
    name="Milk",
    units="ml",
    price=(6.49 / 7570), # 2-gallon pack (~7570ml)
    calories=0.634, 
    carbs=0.0338, 
    fat=0.0338,
    protein=0.0338,
    )
chicken = Food(
    name="Chicken",
    units="g",
    price=0.0075, # $3.39/lb conversion we calculated
    calories=1.76,
    carbs=0.0,
    fat=0.0545,
    protein=0.296
)
butter = Food(
    name="Butter",
    units="tbsp",
    price=(13.99 / 128), # 4lb pack has 128 tbsp
    calories=100, 
    carbs=0.0, 
    fat=11,
    protein=0.0,
    )
creamer = Food(
    name="Creamer",
    units="ml",
    price=(5.99 / 1890), # 1.89L Half & Half
    calories=2.367, 
    carbs=0.3381, 
    fat=0.1014,
    protein=0.0,
    )
smoked_salmon = Food(
    name="Smoked Salmon",
    units="g",
    price=(22.99 / 680), # 24oz (680g) twin pack
    calories=1.17, 
    carbs=0.0, 
    fat=0.0432,
    protein=0.183,
    )
white_rice = Food(
    name="White Rice",
    units="g",
    price=(19.99 / 11340), # 25lb bag (11,340g)
    calories=1.3,
    carbs=0.28,
    fat=0.003,
    protein=0.027
)
lamb = Food(
    name="Lamb",
    units="g",
    price=(28.50 / 2267), # Leg of lamb ~$5.69/lb
    calories=1.852,
    carbs=0.0,
    fat=0.1146,
    protein=0.194
)
protein_powder = Food(
    name="Protein Powder",
    units="scoops",
    price=(59.99 / 80), # Whey Isolate 5.4lb (~80 servings)
    calories=120.0,
    carbs=3.0,
    fat=2.0,
    protein=24.0
)
peanut_butter = Food(
    name="Peanut Butter",
    units="g",
    price=(12.49 / 2260), # 2-pack 40oz jars
    calories=5.625,
    carbs=0.2188,
    fat=0.4688,
    protein=0.25
)
banana = Food(
    name="Banana",
    units="Bananas",
    price=(1.99 / 7), # ~3lb bunch (approx 7 bananas)
    calories=114,
    carbs=26.8,
    fat=0.3,
    protein=0.9
)
organic_super_smoothie = Food(
    name="Organic Super Smoothie Mix",
    units="pouches",
    price=(12.99 / 6), # Frozen 6-pack
    calories=100.0,
    carbs=24.0,
    fat=1.0,
    protein=3.0
)
salmon = Food(
    name="Salmon",
    units="g",
    price=(45.39 / 1360.78), # 3lb bag
    calories=1.31,
    carbs=0.0,
    fat=0.0476,
    protein=0.2202
)
mahi_mahi = Food(
    name="Mahi Mahi",
    units="g",
    price=(24.99 / 1360), # 3lb bag
    calories=0.838,
    carbs=0.0,
    fat=0.0088,
    protein=0.1852
)
cod = Food(
    name="Cod",
    units="g",
    price=(21.99 / 907), # 2lb bag
    calories=0.823,
    carbs=0.0,
    fat=0.0,
    protein=0.194
)
apple = Food(
    name="Apple",
    units="Apples",
    price=(10.99 / 12), # Organic 12-count bag
    calories=95.0,
    carbs=25.0,
    fat=0.3,
    protein=0.5
)


foods = {
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
    "Cod" : cod
}

food_keys = list(foods.keys())