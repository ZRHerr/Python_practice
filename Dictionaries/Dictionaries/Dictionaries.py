# A dictionary is an unordered, changeable and indexed collection 
# that doesnt allow for duplicate members

# KeyValue pair Key- has to be string Value- can be anything
states = {'NY': 'New York', 'PA': 'Pennsylvania', 'IA': 'Iowa', 'CA': 'California', 'CO': 'Colorado'}
# can be accessed using the key
print(states['IA'])
print(states.keys())
print(states.values())

# Set the values
states['FL'] = 'Florida'
print(states)

#dictionaries are typically used to store values of objects
#ie...
user = {'name': 'Zach', 'height': '65in', 'shoe-size': '10.5', 'hair': 'black'}
# can turn dictionaries into lists
usertwo = {'name': 'Mike', 'height': '70in', 'shoe-size': '10', 'hair': 'black'}
people = [user, usertwo]

print(people)
