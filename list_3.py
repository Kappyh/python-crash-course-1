# Sort list permanently with sort() method
# note: the sort() method works better with lower case strings
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# reverse sort
cars.sort(reverse=True)
print(cars)

# temporarily sort, doesnt change the original list

cars_2 = ['bmw', 'audi', 'toyota', 'subaru']
print('original list')
print(cars_2)
print('\n thats the sorted list')
print(sorted(cars_2))
print('\n original list again')
print(cars_2)

# print the list on reverse order, but not alphabetic
# this change is permanent, but you can do another reverse to change the list again
cars_2.reverse()
print(cars_2)

# Finding the length of a list

print(len(cars_2))
