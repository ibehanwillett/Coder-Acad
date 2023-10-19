from abc import ABC, abstractmethod

# Room base class
class Room(ABC):
    def __init__(self):
        self.name = name
        NorthDoor = False
        EastDoor = False
        SouthDoor = False
        WestDoor = False
    
    def __str__(self):
        return f'You are in the {self.name}'
    
    # @abstractmethod
    # def what_doors(self, name):
    #     pass
        

    # @abstractmethod
    # def go(self, direction):
    #     pass
    
# Rooms themselves
class Entrance(Room):
    def __init__(self, name):
        self.name = name
        EastDoor = True
        SouthDoor = True
        WestDoor = True


class Library(Room):
    def __init__(self, name):
        self.name = name

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

# MOVEMENT
def doorways():
    if  EastDoor = True
        SouthDoor = True
        WestDoor = True

#START OF GAME
print("You wake in a spooky scary house! Uh oh!")

# ENTRANCE 
entrance = Entrance("Entrance")
print(entrance)