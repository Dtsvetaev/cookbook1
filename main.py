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
print(cook_book)
