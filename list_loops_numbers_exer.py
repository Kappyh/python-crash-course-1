# 4.3 Counting to twenty
for value in range(1, 21):
    print(value)

#  4.4 One Million Count
for value in range(1, 1000001):
    print(value)

# 4.5 Summing a million
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4.6 Odd Numbers
for value in range(1, 21, 3):
    print(value)

# 4.7 Threes
for value in range(3, 31, 3):
    print(value)

# 4.8 Cubes
for value in range(1, 11):
    print(value ** 3)

# 4.9 Cubes comprehension
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)