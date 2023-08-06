from typing import List, Dict, Any

with open('Recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recipes_name = i.strip()
        ingredient_count = file.readline()
        ingredient = []
        for p in range(int(ingredient_count)):
            recipes = file.readline().strip().split(' | ')
            product, quantity, word = recipes
            ingredient.append({'product': product, 'quantity': quantity, 'measure': word})
        file.readline()
        cook_book[recipes_name] = ingredient


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                product = ingredient['product']
                quantity_per_person = int(ingredient['quantity']) * person_count
                measure = ingredient['measure']

                if product in shop_list:
                    shop_list[product]['quantity'] += quantity_per_person
                else:
                    shop_list[product] = {'quantity': quantity_per_person, 'measure': measure}

    return shop_list


if __name__ == "__main__":

    dishes_to_cook = ['Запеченный картофель', 'Омлет']
    person_count = 2
    shop_list = get_shop_list_by_dishes(dishes_to_cook, person_count, cook_book)


    for ingredient, details in shop_list.items():
        print(f"{ingredient}: {details['quantity']} {details['measure']}")

