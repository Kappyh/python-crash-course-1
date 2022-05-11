# Changing itens from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding elements with a native list function
# The new item always go for the end of the list
motorcycles.append('BMW')
print(motorcycles)

# Adding a element in a certain order of the list
motorcycles.insert(1, 'Harley Davidson')
print(motorcycles)

# Removing a item from the list
# Using del statement

del motorcycles[0]
print(motorcycles)

# Removing using the pop() method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Using pop() to remove from a specific position on the list
first_owned = motorcycles.pop(0)
print(f'My first owned motorcycle was {first_owned.upper()}')

# Removing a item by value
# Using the remove() method, remove only one occurrency for method call
# Beware if the value appears more than once on the list

small_dogs_breeds = ['poodle', 'schipperke', 'pug', 'bulldog']
print(small_dogs_breeds)
small_dogs_breeds.remove('pug')
print(small_dogs_breeds)
uggly_breed = 'bulldog'
small_dogs_breeds.remove(uggly_breed)
print(f"I don't like the {uggly_breed} breed")
