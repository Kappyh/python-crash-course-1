# 3.1 create and print a list of my friends names
friends = ['sky', 'Lella', 'Lucas', 'Rodolpho', 'Lídia']
print(friends[0].title())
print(friends[1])
print(friends[2])
print(friends[-1])
print(friends[-2].upper())

# 3.2 show a message with the each friend name

print(f'Hello my crazy friend {friends[0].upper()}')
print(f'Hello my crazy friend {friends[1]}')
print(f'Hello my crazy friend {friends[2]}')
print(f'Hello my crazy friend {friends[-2]}')
print(f'Hello my crazy friend {friends[-1].lower()}')

# 3.3 make my own list of transportation vehicles

transportation = ['car', 'motorcyle', 'bicycle']
print(f'Once a ride a Honda {transportation[1]}')
print(f'I own a Ford {transportation[0].upper()} with a engine of 138 HP')
print(f'My old {transportation[-1]} was hit by a car from my aunt')
