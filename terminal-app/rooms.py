from abc import ABC, abstractmethod
import time
import sys
import characters


# General code
def quitcheck(input):
    if input == 'quit':
        sys.exit()

# Items
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def inspect(self):
        print(f'{self.description}')

    @abstractmethod
    def interact(self):
        pass

class Book(Item):
    def __init__(self, name, description, excerpt):
        self.excerpt = excerpt
    def interact():
        print('You flip to a random page and begin to read ...')
        time.sleep(2)
        print(f'{self.excerpt}')
        time.sleep(3)
        print('Hmm... a lot to think about.')

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
        quitcheck(door)
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
    
    def scene(self):
        print('You see a bookshelf groaning under the weight of ')
    
odyssey = characters.Book('The Odyssey', 'The Odyssey by Homer', '“But the great leveler, Death: not even the gods can defend a man, not even one they love, that day when fate takes hold and lays him out at last.”')
carson = characters.Book('Autobiography of Red', 'Autobiography of Red by Anne Carson', 'XIII. HERAKLES\' KILLING CLUB\nLittle red dog did not see it he felt it\nAll events carry but one')
riddle = characters.Book('Anglo-Saxon Riddles', 'A book about Anglo-Saxon riddles.', '...although contentious, most scholars agree the answer to the riddle \'I saw a...(There\'s a stain on the page here.) ...alone is a mirror.')

        

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
    
    def scene(self, player_inventory):
        print('It\'s too dark to see...')
        if 'candle' in player_inventory and 'matches' not in player_inventory:
            print('You have a candle, but nothing to light it with! \nYou should probably leave.')
        if 'matches' in player_inventory and 'candle' not in player_inventory:
            print('You try to light some matches...')
            time.sleep(1)
            print('You get a second of light! You see briefly what look\'s to be a bedroom, it\'s very pink and- wait.')
            time.sleep(2)
            print('Did something just move?')
            time.sleep(1)
            print('The match burns out, leaving you with nothing but burnt fingertips and a stone of dread rising in your throat. \n Best come back when you have something to light the candle with.')
        if 'candle' in player_inventory and 'matches' in player_inventory:
            print('You see a spooky ghost girl!')
            ghost.conversation()
            



class Kitchen(Room):
     def __init__(self, name, north, south, east, west, doors):
         self.name = name
         self.east = 'statue'
         self.north = 'dining'
         self.doors = doors
        
     def scene(self):
        print('Kitchen time baby. Time to make a pie... of PEOPLE!!! SPOOKY SCARY')

        


class Dining(Room):
     def __init__(self, name, north, south, east, west, doors):
         self.name = name
         self.south = 'kitchen'
         self.east = 'entrance'
         self.doors = doors
         self.has_scene_played = False
         self.inv = characters.Inventory(['candle'])

     def scene(self, user):
        if self.has_scene_played == False:
            print('There\'s a table set with what looks like to have been roast chicken once.\n It looks like it might have been out for a while.')
            time.sleep(2)
            print('... It smells like it\'s been out for a while. \n There\'s a beautiful long white tallow candle illuminating the screen.' ) 
            time.sleep(2)
            answer =(input('Blow out candle?  '))
            quitcheck(answer)  
            if answer == 'yes':
                self.has_scene_played = True
                print('You blow out the candle. As soon as you do, the food resting on the dinner plates errupts into a cacouphanous swirl of flies and cocharoaches.')
                time.sleep(1)
                print('They fly thick and fast at your face; some get tangled in your hair, some get into your mouth.\n When they finally disapate enough that you can see again, you notice the plates are empty.')
                time.sleep(3)
                print('The smell remains.')
                self.inv.add_from(self.inv, user)
            if answer == 'no':
                print('You leave it be. The skin of the roast chicken ripples slightly as something moves from underneath it.')
        if self.has_scene_played == True:
            print('There\'s a table set for two, the bone-whiteplates are empty. The smell of rot is intense.')



# Inventory
class Inventory:
    def __init__(self, items):
        self.items = items
    
    def add_from(self, from_inv):
        self.items.extend(from_inv)
        from_inv = []
    


# Charater 
class Charater:
    def __init__(self, name, things):
        self.things = things
        self.inv = Inventory([self.things])
    
    def conversation(self):
        print('The ghost says \'No... please don\'t go... I don\'t want you to go...\'')
        print('I\'ll give you the key if you can answer my riddle; I saw a woman sit alone.')
        answer = input('What am I?')
        if answer == 'a mirror' or 'mirror':
            print('That\'s exactly right.')
        else:
            print('The ghost shrieks \'WRONG!\' A red cloud covers the mirror and when it disappates the ghost is gone.')


ghost = Charater('Ghost', ['key'])

