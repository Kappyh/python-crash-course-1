# 5.1 conditional test

car = 'toyota'
print("Is car == 'toyota' ? I predicted True")
print(car == 'toyota')

print("\nIs car == 'bmw' ? I predicted False")
print(car == 'bmw')

car = 'bmw'
print("\nIs car == 'bmw' ? I predicted True")
print(car == 'bmw')
print("\nIs car == 'toyota' ? I predicted False")
print(car == 'toyota')

car = 'subaru'
print("\nIs car == 'subaru' ? I predicted True")
print(car == 'subaru')
print("\nIs car == 'mercedez' ? I predicted False")
print(car == 'mercedez')

car = 'mercedez'
print("\nIs car == 'mercedez' ? I predicted True")
print(car == 'mercedez')
print("\nIs car == 'honda' ? I predicted False")
print(car == 'honda')

car = 'honda'
print("\nIs car == 'honda' ? I predicted True")
print(car == 'honda')
print("\nIs car == 'subaru' ? I predicted False")
print(car == 'subaru')

car = 'subaru'
print("\nIs car == 'subaru' ? I predicted True")
print(car == 'subaru')
print("\nIs car == 'honda' ? I predicted False")
print(car == 'honda')

# 5.2 more conditional tests
print('\nEquality on strings:\n')
fruit = 'banana'
print(fruit == 'banana')

fruit = 'Banana'
print(fruit == 'banana')
print(fruit.lower() == 'banana')

print('\nNumeric tests, operators and or:\n')

number_1 = 2
number_2 = 3
print(number_2 == number_2)
print(number_1 < number_2)
print(number_2 > number_1)
print(number_2 >= 3 and number_1 <= 2)
print(number_2 < number_1)
print(number_2 >= 3 or number_1 >= 4)
print(number_2 > 4 and number_1 < 2)

print('\nList tests:\n')

#element on a list
dogs_breeds = ['poodle', 'pinscher', 'doberman', 'schipperke']
print('poodle' in dogs_breeds)

dog_breed = 'yorkshire'
if dog_breed not in dogs_breeds:
    print(f"{dog_breed.title()} is not my dog breed")

