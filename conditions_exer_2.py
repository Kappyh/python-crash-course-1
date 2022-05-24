# 5.3 alien colors
alien_color = 'green'
if alien_color == 'green':
    print('player won 5 points')

alien_color = 'red'
if alien_color == 'green':
    print('player won 5 points')

# 5.4 aliens colors part II
alien_color_2 = 'blue'
if alien_color_2 == 'green':
    print('player won 5 points')
if alien_color_2 == 'blue':
    print('player won 10 points')

# aproach 2 with else
if alien_color_2 == 'green':
    print('player won 5 points')
else:
    print('player won 10 points')

# 5.5 aliens colors part III if-elif-else
alien_color_3 = 'yellow'
if alien_color_3 == 'green':
    print('player won 5 points')
elif alien_color_3 == 'yellow':
    print('player won 10 points')
elif alien_color_3 == 'red':
    print('player won 15 points')

# 5.6 st
# ages of life
age = 12

if age < 2:
    print('baby')
elif age <=2 and age <4:
    print('toddler')
elif age  >=4 and age < 13:
    print('kid')
elif age >= 13 and age < 20:
    print('teenager')
elif age >= 20 and age < 65:
    print('adult')
elif age >= 65:
    print('elder')

# 5.7
favorite_fruits = ['apple', 'orange', 'lemon']

if 'apple' in favorite_fruits:
    print('get a apple')
if 'lemon' in favorite_fruits:
    print('get a lemon')
if 'tangerin' in favorite_fruits:
    print('get a tangerin')
