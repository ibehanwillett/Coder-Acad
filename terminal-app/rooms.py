from abc import ABC, abstractmethod
import time

# Room base class
class Room:
    def __init__(self, name, north, south, east, west, doors):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.doors = doors
    

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

    def description(self):
        print(f'You are in the {self.name}')
        print(self.doors)
    
    



    
# Rooms themselves definition
class Entrance(Room):
    def __init__(self, name, north, south, east, west, doors):
        self.name = name
        self.north = 'locked'
        self.east = 'library'
        self.south = 'statue'
        self.west = 'dining'
        self.doors = doors

    


class Library(Room):
    def __init__(self, name, north, south, east, west, doors):
        self.name = name
        self.south = 'study'
        self.west = 'entrance'
        self.doors = doors
        

class Study(Room):
     def __init__(self, name, north, south, east, west, doors):
         self.name = name
         self.west = 'statue'
         self.north = 'library'
         self.doors = doors

        

class Statue(Room):
     def __init__(self, name, north, south, east, west, doors):
        self.name = name
        self.north = 'entrance'
        self.east = 'study'
        self.south = 'bedroom'
        self.west = 'kitchen'
        self.doors = doors


class Bedroom(Room):
    def __init__(self, name, north, south, east, west, doors):
         self.name = name
         self.north = 'statue'
         self.doors = doors



class Kitchen(Room):
     def __init__(self, name, north, south, east, west, doors):
         self.name = name
         self.east = 'statue'
         self.north = 'dining'
         self.doors = doors
        


class Dining(Room):
     def __init__(self, name, north, south, east, west, doors):
         self.name = name
         self.south = 'kitchen'
         self.east = 'entrance'
         self.doors = doors
         self.candle = True
        


     def scene(self):
        if self.candle == True:
            print('There\'s a table set with a beautiful roast chicken. It looks like it might have been out for a while.')
            time.sleep(1)
            print('... It smells like it\'s been out for a while. \n There\'s a beautiful long white tallow candle illuminating the screen.' ) 
            answer = str(input('Blow out candle?'  ))  
            if answer == 'yes':
                self.candle == False
                print('You blow out the candle. As soon as you do, the food resting on the dinner plates errupts into a cacouphanous swirl of flies and cocharoaches.\n They fly thick and fast at your face; some get tangled in your hair, some get into your mouth.\n When they finally disapate enough that you can see again, you notice the plates are empty.')
                time.sleep(1)
                print('The smell remains.)')
                return complete
            if answer == 'no':
                print('You leave it be. The skin of the roast chicken ripples slightly as something moves from underneath it.')
        if self.candle == False:
            print('There\'s a table set for two, the bone-whiteplates are empty. The smell of rot is intense.')









## Rooms set-up
# entrance = Entrance('entrance', 'locked', 'statue','library','dining','The entrance is a room. Placeholder description. There is a door on the east wall, west wall and south wall.')
# library = Library('library', 'wall', 'study', 'wall', 'entrance', 'You\'re in a library. There\'s a door on south wall and west wall.')
# study = Study('study', 'library', 'wall', 'wall', 'statue', 'You\'re in the study. There is a door on the west wall and the north wall.')
# statue = Statue('statue', 'entrance', 'bedroom', 'study', 'kitchen','You\'re in a room full of statutes. Doors surround you on all all four cardinal directions.' )
# bedroom = Bedroom('Bedroom','statue', 'wall', 'wall', 'wall', 'You are in the bedroom. There is only one door to the north.' )
# kitchen = Kitchen('Kitchen', 'dining', 'wall', 'statue', 'wall','You\'re in the kitchen. There is a door on the east wall and north wall.')
# dining = Dining('Dining Room', 'wall', 'kitchen', 'entrance', 'wall', 'You\'re in the dining room. There\'s a door on the south wall and east wall.')


# Items
class Item:
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
    def inspect():
        print(excerpt)

# Inventory
class Inventory:
    def __init__(self, items, hasKey):
        self.items = items
        self.hasKey = hasKey
    


# Charater 
class Charater:
    def __init__(self, name):
        inv = Inventory([], False)




