# Alexandra Excell  PSID: 1595971

class FoodItem:
    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + ((self.carbs + self.protein) * 4)) * num_servings
        print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,calories))
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    input_name = input()

    input_fat = float(input())
    input_carb = float(input())
    input_protein = float(input())
    input_servings = float(input())

    food1 = FoodItem()
    food1.print_info()
    food1.get_calories(input_servings)
    print('')

    food2 = FoodItem(input_name,input_fat,input_carb,input_protein)
    food2.print_info()
    food2.get_calories(input_servings)





