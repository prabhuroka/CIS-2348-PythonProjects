# Prabhu Roka
# 1986444
class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, x):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * x
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":

    item_name = input()
    if item_name.lower() == 'water':
        food_item = FoodItem()
        food_item.print_info()
        print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')

    else:
        amount_fat = float(input())
        amount_carbs = float(input())
        amount_protein = float(input())
        num_servings = float(input())

        food_item_default = FoodItem()
        food_item_default.print_info()
        print(f'Number of calories for {num_servings:.2f} serving(s):'
              f' {food_item_default.get_calories(num_servings):.2f}')
        print()

        food_item = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
        food_item.print_info()
        print(f'Number of calories for {num_servings:.2f} serving(s):'
              f' {food_item.get_calories(num_servings):.2f}')
