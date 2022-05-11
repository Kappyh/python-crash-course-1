# Basic list
small_dogs_breeds = ['poodle', 'schipperke', 'pug', 'pischer']
print(small_dogs_breeds)

# Accessing one element of the collection
print(small_dogs_breeds[1].title())

# Accessing the last element of the list
print(small_dogs_breeds[-1].upper())

# Using with f-strings
print(f'My first dog was from the breed {small_dogs_breeds[0].title()}, '
      f'and my actual is from the breed {small_dogs_breeds[1].upper()}')
