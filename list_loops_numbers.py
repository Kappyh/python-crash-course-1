# List loops with numbers
# Using range function

for value in range(0, 41):
    print(value)

# Making a list using range() function
numbers = list(range(10))
print(numbers)

# Skipping number with a third argument
numbers_2 = list(range(2,11,2))
print(numbers_2)

# Creating square numbers
squares = []
numbers_3 = list(range(1, 11))
for number in numbers_3:
    squares.append(number ** 2)

print(squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits))
print(max(digits))
print(sum(digits))

