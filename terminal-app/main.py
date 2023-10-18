from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self):
        self.name = name
        self.description = description
        hasNorthDoor = False
        hasEastDoor = False
        hasSouthDoor = False
        hasWestDoor = False

    @abstractmethod
    def what_doors(self, name):
        
        


    @abstractmethod
    def go(self, direction):
        pass
    
class Entrance(Room):
    def __init__(self):
        self.description = "You are at the entrance of the house."
        hasEastDoor = True

        

class Library(Room):
    def __init__(self):
        self.description = "You are in the library"

class Study(Room):
    def __init__(self):
        self.description = "You are in the study."

class Statue(Room):
    def __init__(self):
        self.description = "You are in a room full of statues."

class Bedroom(Room):
    def __init__(self):
        self.description = "You are in the bedroom."

class Kitchen(Room):
    def __init__(self):
        self.description = "You are in the kitchen."

class DininigRoom(Room):
    def __init__(self):
        self.description = "You are in the kitchen ."

        def doorway(direction, room):
            print(f"The {room} is to the {direction}")


print("You wake in a spooky scary house! Uh oh!")

