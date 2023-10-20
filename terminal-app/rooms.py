from abc import ABC, abstractmethod

# Room base class
class Room(ABC):
    def __init__(self):
        self.name = name
        self.north = 'locked'
        self.east = 'locked'
        self.south = 'locked'
        self.west = 'locked'
    
    def __str__(self):
        return f'You are in the {self.name}'


# Doors
class Door():
    def __init__(self, name):
        self.name = name

    def move(name):
        print('The door creaks as you move into the other room')
        return global position
        position = name


            
         


    
# Rooms themselves definition
class Entrance(Room):
    def __init__(self, name):
        self.name = name
        self.east = Door(library)
        self.south = Door(statue)
        self.west = Door(dining)
        

    def description(self):
       print('The entrance is a room. Placeholder description. There is a door on the east wall, west wall and south wall.')
    


class Library(Room):
    def __init__(self, name):
        self.name = name
        self.south = Door(study)
        self.west = Door(entrance)
        
    def description(self):
       print('You\'re in a library. Placeholder description. There is a door on south wall and west wall.')

class Study(Room):
     def __init__(self, name):
         self.description = "You are in the study. There is a door to the west and to the north."
         self.west = Door(statue)
         self.north = Door(library)
        

class Statue(Room):
     def __init__(self):
        self.description = "You are in a room full of statues."
        self.north = 

class Bedroom(Room):
    def __init__(self):
         self.description = "You are in the bedroom."

 class Kitchen(Room):
     def __init__(self):
         self.description = "You are in the kitchen."

 class DininigRoom(Room):
     def __init__(self):
         self.description = "You are in the kitchen ."

        # def doorway(direction, room):
        #                  print(f"The {room} is to the {direction}")


## Doors set-up
library_door = Door('library')
entrance_door = Door('entrance')

## Rooms set-up
entrance = Entrance('Entrance')
library = Library('Library')
