from pprint import pprint


class Cookbook:
    def __init__(self, document):
        self.document = document
        self.cook_book = {}

    def make_cook_book(self):
        with open(self.document, encoding='utf-8') as file:
            for lines in file:
                item = lines.strip()
                amount = int(file.readline())
                food_list = []
                for i in range(amount):
                    ingr = file.readline().split(' | ')
                    ingredients = {'ingredient_name': ingr[0], 'quantity': ingr[1], 'measure': ingr[2].strip()}
                    food_list.append(ingredients)
                self.cook_book[item] = food_list
                file.readline()
        book = open('recipe_dict.txt', 'w', encoding='utf-8')
        book.write(f'{self.cook_book}')
        book.close()
        return self.cook_book


def get_shop_list_by_dishes(dishes: list, res, person_count=2):
    cook_book = res.make_cook_book()
    shop_list = {}
    for dish_name in dishes:
        for ingredient in cook_book.get(dish_name, []):
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
            else:
                shop_list[ingredient['ingredient_name']] = {'quantity': int(ingredient['quantity']) * person_count, 'measure': ingredient['measure']}
    shop_list_file = open('shopping_list.txt', 'w', encoding='utf-8')
    shop_list_file.write(f'{shop_list}')
    shop_list_file.close()
    return shop_list


recipe = Cookbook('recipe.txt')
pprint(recipe.make_cook_book(), width=70, sort_dicts=False)
print()
dish_list = ['Омлет', 'Фахитос']
recipe_dict = open('recipe_dict.txt', 'r', encoding='utf-8')
pprint(get_shop_list_by_dishes(dish_list, recipe), width=70)
