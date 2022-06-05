alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# adding more elements to a dictionary

alien_0['x_position']= 0
alien_0['y_position']= 25

print(alien_0)

# start a empty dictionary
bird = {}
bird['color'] = 'blue'
bird['specie'] = 'macaw'
print(bird)

# modify a value in a dictionary
bird['color']= 'red'
print(bird)

# removing key-value in a dictionary
bird['name']= 'jade'
print(bird)
del bird['name']
print(bird)