# basic if

cars = ['bmw', 'toyota', 'subaru', 'mitsubish']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# case sensitive fix in equality

car = 'Subaru'
print(car.lower() == 'subaru')

# checking inequality
request_topping = 'mushrooms'
if request_topping != 'anchovies':
    print('hold the anchovies')

# Multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >=21 and age_1 >= 21)


# Cheking value in a list
request_toppings = ['chocolate', 'strawberries', 'banana']
print('banana' in request_toppings)

# Cheking if a value is not in a list

banned_users = ['andrew', 'mara', 'tony']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")

# Boolean expression
game_active = True
can_edit = False

# if-else
age = 17
if age >=18:
    print('You can vote')
else:
    print('You can not vote')

# if-elif-else
age = 12
if age < 4:
    print('Your admission cost is $10')
elif age < 18:
    print('Your admission cost is $25.')
else:
    print('Your admission cost is $40')

# testing multiple coonditions

request_topping_2 = ['mushrooms', 'extra cheese']
if 'mushrooms' in request_topping_2:
    print('Adding mushrooms.')
if 'pepperoni' in request_topping_2:
    print('Adding pepperoni.')
if 'extra cheese' in request_topping_2:
    print('Adding extra cheese.')
