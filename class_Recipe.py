class Recipe:
    def __init__(self, b, i):
        self.bludo = b
        self.ingredients = i

    def print_ingredients(self):
        for ingredient in self.ingredients:
            print("- {}".format(ingredient))    # или print(f"- {ingredient}")

    def cook(self):
        print("Готовим {}".format(self.bludo))    # или f-string
        print("Блюдо {} готово".format(self.bludo))