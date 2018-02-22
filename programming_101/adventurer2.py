# a class encapsulates behavior and state -- they are like a template

class Hat:
    def __init__(self, style: str):
        self.style = style

    def a_method(self):
        pass

    def __str__(self):
        return self.style

def a_funtion():
    pass

hat1 = Hat('beanie')
hat2 = Hat('sports cap')
hat3 = Hat('fedora')

hats = [hat1, hat2, hat3]

for hat in hats:
    print(hat)

class Adventurer:

    def __init__(self, name: str, equipment:dict):
        self.name = name
        self.hat = equipment['hat']
        self.shoes = equipment['shoes']

    def __str__(self):
        print(f'I am {self.name}. I wear {self.hat} hat and {self.shoes} shoes')

default_equipment = {
    'hat': Hat('peasant hat'),
    'shoes': None
}

sara = Adventurer('sara', default_equipment)

print(sara)

x = 5
y = 4

for x_count in range(x):
    grid.append([])
    for y count in range(y):
        grid[x].append('x')

print(grid)