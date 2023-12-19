
cook_book = {}
with (open('recipes.txt', 'r', encoding='UTF-8') as f):
    data = f.read().split('\n\n')
    for food in data:
        key = food.split('\n')[0]
        ingredients = food.split('\n')[2:]

        ingredients_value = []
        for value in ingredients:
            value = value.split('|')
            ingredients_value.append({'ingredient_name': value[0], 'quantity': value[1], 'measure': value[2]})
        cook_book[key] = ingredients_value


def get_shop_list_by_dishes(dishes, person_count):
    cook_dishes = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            dish_cook = ingredient['ingredient_name']
            quantity = int(ingredient['quantity']) * person_count
            measure = ingredient['measure']
            if dish_cook not in cook_dishes:
                cook_dishes[dish_cook] = {
                    "quantity": quantity,
                    "measure": measure
                }
            else:
                cook_dishes[dish_cook]['quantity'] += quantity

    return cook_dishes

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 1))









