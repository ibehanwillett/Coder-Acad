from abc import ABC, abstractmethod

# Room base class
class Room(ABC):
    def __init__(self, name):
        self.name = name
        self.north = 'wall'
        self.east = 'wall'
        self.south = 'wall'
        self.west = 'wall'
    
    def __str__(self):
        return f'You are in the {self.name}'

    def doorpick(self):
        door = str(input('Where do you want to go?  '))
        if door == 'north':
            return f'{self.north}'
        if door == 'south':
            return f'{self.south}'
        if door == 'east':
            return f'{self.east}'
        if door == 'west':
            return f'{self.west}'

# Doors
# class Door():
#     def __init__(self, name):
#         self.name = name

#     def move(name):
#         print('The door creaks as you move into the other room')
#         return name


            


    
# Rooms themselves definition
class Entrance(Room):
    def __init__(self, name):
        super.__init__(self)
        self.name = name
        self.north = 'locked'
        self.east = 'library'
        self.south = 'statue'
        self.west = 'dining'

    def description(self):
       print('The entrance is a room. Placeholder description. There is a door on the east wall, west wall and south wall.')
    


class Library(Room):
    def __init__(self, name):
        super.__init__(self.east, self.east)
        self.name = name
        self.south = 'study'
        self.west = 'entrance'
        
    def description(self):
       print('You\'re in a library. Placeholder description. There is a door on south wall and west wall.')

class Study(Room):
     def __init__(self, name):
         self.west = 'statue'
         self.north = 'library'
    
     def description(self):
        print('You\'re in the study. There is a door on the west wall and the north wall.')
        

class Statue(Room):
     def __init__(self, name):
        self.north = 'entrance'
        self.east = 'study'
        self.south = 'bedroom'
        self.west = 'kitchen'

     def description(self):
        print('You\'re in a room full of statutes. Doors surround you on all all four cardinal directions.')

class Bedroom(Room):
    def __init__(self, name):
         self.description = "You are in the bedroom."
         self.north = 'statue'

    def description(self):
        print('You are in the bedroom. There is only one door to the north.')

class Kitchen(Room):
     def __init__(self, name):
         self.east = 'statue'
         self.north = 'dining'
        
     def description(self):
        print('You\'re in the kitchen. There is a door on the east wall and north wall.')

class Dining(Room):
     def __init__(self, name):
         self.south = 'kitchen'
         self.east = 'entrance'

     def description(self):
        print('You\'re in the dining room. There\'s a door on the south wall and east wall.')





## Rooms set-up
entrance = Entrance('Entrance')
library = Library('Library')
study = Study('Study')
statue = Statue('Statue')
bedroom = Bedroom('Bedroom')
kitchen = Kitchen('Kitchen')
dining = Dining('Dining Room')


# Items
class Item(ABC):
    def __init__(self, name, description):
        self.name = name
        self.definition = description

    @abstractmethod
    def inspect(self):
        pass

class Book(Item):
    def __init__(self, name, description, excerpt):
        super.__init__(name, description)
        self.excerpt = excerpt
    def inspect()
        print(excerpt)

# Inventory
class Inventory:
    



