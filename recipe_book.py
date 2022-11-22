from pprint import pprint

class Cook_book:
    def __init__(self, document):
        self.document = document
        self.cook_book = {}

    def open_file(self):
        data = open(self.document, 'r', encoding='utf-8')
        return data.readlines()

    def make_cook_book_keys(self):
        for info in self.open_file():
        return self.cook_book



def get_shop_list_by_dishes(name, count):
    pass


recipe = Cook_book('recipe.txt')
# recipe.make_cook_book()
recipe.open_file()
print(recipe.open_file())
recipe.make_cook_book_keys()
print(recipe.make_cook_book_keys())
# get_shop_list_by_dishes(dishes, person_count)

cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ]
}