#Prabhu Roka
#1986444
import math
print("Enter wall height (feet):")
height = float(input())
print("Enter wall width (feet):")
width = float(input())
area = int(height * width)
print("Wall area: " + str(area) + " square feet")
gallon_paint = area / 350
print("Paint needed: " + '{:.2f}'.format(gallon_paint) + " gallons")
cans_paint = math.ceil(gallon_paint)
print("Cans needed: " + str(cans_paint) + " can(s)")
print("")
print("Choose a color to paint the wall:")
color = str(input())
if color == "red":
    price = 35 * cans_paint
    print("Cost of purchasing red paint: $" + str(price))
elif color == "green":
    price = 23 * cans_paint
    print("Cost of purchasing green paint: $" + str(price))
elif color == "blue":
    price = 25 * cans_paint
    print("Cost of purchasing blue paint: $" + str(price))
else:
    print("Invalid color")
