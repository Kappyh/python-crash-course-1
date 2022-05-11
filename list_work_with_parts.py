# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# Ommiting the first index in a slice
print(players[:4])

# Ommiting the second index of a slice
print(players[2:])

# Slicing with negative index
print(players[-3:])

# Slicing with range steps
print(players[0:4:2])


# Looping through a slice
for player in players[:3]:
    print(player)

# copying a list with slice
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)

print("\n Also my friend's favorite food:")
print(friend_foods)

# this doenst work: friend_foods = my_foods, because will create a dependencie between the lists
# if I add a new member in my_foods, will appear in friend_foods
