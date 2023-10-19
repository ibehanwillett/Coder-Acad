from abc import ABC, abstractmethod

# GENERAL SCRIPT
howto_move = print('To move to another room, input the direction you want to move)')
position = 'entrance'

# Room base class
class Room(ABC):
    def __init__(self):
        self.name = name
        NorthDoor = 'locked'
        EastDoor = 'locked'
        SouthDoor = 'locked'
        WestDoor = 'locked'
    
    def __str__(self):
        return f'You are in the {self.name}'


# Doors
class Door():
    def __init__(self, name):
        self.name: name

    def move(name):
        # global position = name
        print(f'You move into the {name}')
            
         


    
# Rooms themselves definition
class Entrance(Room):
    def __init__(self, name):
        self.name = name
        

    def description(self):
       print('The entrance is a room. Placeholder description. There is a door on the east wall, west wall and south wall.')
    


class Library(Room):
    def __init__(self, name):
        self.name = name
        

    def description(self):
       print('You\'re in a libray. Placeholder description. There is a door on south wall and west wall.')

# class Study(Room):
#     def __init__(self, name):
#         self.description = "You are in the study."

# class Statue(Room):
#     def __init__(self):
#         self.description = "You are in a room full of statues."

# class Bedroom(Room):
#     def __init__(self):
#         self.description = "You are in the bedroom."

# class Kitchen(Room):
#     def __init__(self):
#         self.description = "You are in the kitchen."

# class DininigRoom(Room):
#     def __init__(self):
#         self.description = "You are in the kitchen ."

#         def doorway(direction, room):
#             print(f"The {room} is to the {direction}")





def whereto():
    direction = str(input("What direction would you like to go?"))
    return direction





#SET UP
## Rooms set-up
entrance = Entrance('Entrance')
entrance.east_door = Door('library')
library = Library('Library')
library.west_door = Door('entrance')

## Doors set-up

#START OF GAME
print('You wake in a spooky scary house! Uh oh!')

# ENTRANCE 
entrance.description()
print(howto_move)
move_choice = whereto()
if move_choice == 'east':
    library.move()
else:
    print('I have\'t coded that yet, sorry!')

    
    


    

