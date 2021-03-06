# a class encapsulates behavior and state

class Hat:
    def __init__(self):
        pass

hat = Hat()

print(hat)
print(hat.__name__)
print(hat.__class__)

import random

class Adventurer:
    def __init__(self, map, name, strength):
        self.map = map
        self.name = name
        self.strength = strength


    def receive_map(self, other_adventurer):
        other_map = other_adventurer.map
        self.map = other_map

def generate_character(map):
    strength = random.randit(1, 18)
    adventurer = Adventurer(map, name, strength)
    return adventurer

good_map = 'good map'
bad_map = 'bad map'

justin = generate_character(bad_map, 'justin')
alex = generate_character(good_map, 'alex')
sara = generate_character(bad_map, 'sara')
grande = generate_character(good_map, 'grande')

adventurers = [justin, alex, sara, grande]

for adventurers in party:
    print(adventurers.map + ':' + str(adventurer.strength))
print(justin.map)
print(alex.map)
print(sara.map)
print(grande.map)

sara.receive_map(grande)
sara.map = good_map

print('sara' + sara.map)