dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


# looping throught a tuple
for dimension in dimensions:
    print(dimension)

# rewrite a tuple
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)


# Exemples

# 4.13 Buffet
foods = ('hot dog', 'barbecue', 'pastel', 'feijoada')
for food in foods:
    print(food)
foods = ('hot dog', 'hamburguer', 'pastel', 'alface')
for food in foods:
    print(food)
