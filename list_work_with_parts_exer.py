# 4.10 Slices
pets_list = ['Kira', 'Dolly', 'Kaká', 'Billie', 'King']
print(pets_list[:3])
print(pets_list[1:4])
print(pets_list[2:5])

# 4.11 Pizzas

list_of_pizzas = ['mozzarela', 'peperoni', 'vegeterian']
friend_pizzas = list_of_pizzas[:]

list_of_pizzas.append('Bacon')
friend_pizzas.append('Garlic')

print('My favorite pizzas are:')
for pizza in list_of_pizzas:
    print(pizza)

print('\nMy friend favorite pizzas:')
for friend_pizza in friend_pizzas:
    print(friend_pizza)
