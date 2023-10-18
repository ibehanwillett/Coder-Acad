from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self):
        self.name = name

    @abstractmethod
    def go(self, direction):
        pass
    
class Entrance(Room):
    def __init__(self):
        self.description = "You are at the entrance of the house."

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
        self.description = "You are in the kitchen."