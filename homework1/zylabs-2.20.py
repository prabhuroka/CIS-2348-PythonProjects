#Prabhu Roka
#1986444
lemon_juice_per_serving = 2.00 / 6.00
water_per_serving = 16.00 / 6.00
agave_nectar_per_serving = 2.50 / 6.00

print("Enter amount of lemon juice (in cups):")
lemon_juice = float(input())
print("Enter amount of water (in cups):")
water = float(input())
print("Enter amount of agave nectar (in cups):")
agave_nectar = float(input())
print("How many servings does this make?")
print("")
servings = float(input())
print("Lemonade ingredients - yields " + '{:.2f}'.format(servings) + " servings")
print('{:.2f}'.format(lemon_juice) + " cup(s) lemon juice")
print('{:.2f}'.format(water) + " cup(s) water")
print('{:.2f}'.format(agave_nectar) + " cup(s) agave nectar")
print("")
print("How many servings would you like to make?")
serving_2 = float(input())
print("")
lemon_cup = serving_2 * lemon_juice_per_serving
water_cup = serving_2 * water_per_serving
water = serving_2 * agave_nectar_per_serving
print("Lemonade ingredients - yields " + '{:.2f}'.format(serving_2) + " servings")
print('{:.2f}'.format(lemon_cup) + " cup(s) lemon juice")
print('{:.2f}'.format(water_cup) + " cup(s) water")
print('{:.2f}'.format(water) + " cup(s) agave nectar")
print("")
print("Lemonade ingredients - yields " + '{:.2f}'.format(serving_2) + " servings")
print('{:.2f}'.format(lemon_cup/16) + " gallon(s) lemon juice")
print('{:.2f}'.format(water_cup/16) + " gallon(s) water")
print('{:.2f}'.format(1.25) + " gallon(s) agave nectar")
