from abc import ABC
import time
import sys
import characters
import items


# General code
def quitcheck(input):
    if input == 'quit':
        sys.exit()



# Room base class
class Room:


    def __init__(self, name, north, south, east, west, doors):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.doors = doors
        self.inv = items.Inventory([])

    def door_pick(self):
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
    
    def print_item_list(self, room_inv):
        answer = input('Do you want to look around?')
        quitcheck(answer)
        if answer == 'yes' or answer == 'y':
            print('Here\'s what jumps out at you as you look around the room')
            for item in range(len(room_inv)):
                print(room_inv[item])
        if answer == 'no' or answer == 'n':
            return

    
# Rooms themselves definition
class Entrance(Room):


    def __init__(self, name, north, south, east, west, doors):
        self.name = name
        self.north = 'locked'
        self.east = 'library'
        self.south = 'statue'
        self.west = 'dining'
        self.doors = doors
        self.inv = items.Inventory([])

    


class Library(Room):


    def __init__(self, name, north, south, east, west, doors):
        self.name = name
        self.south = 'study'
        self.west = 'entrance'
        self.doors = doors
        self.inv = items.Inventory([items.odyssey, items.carson, items.riddle])
    
    def scene(self, user):
        print('You see a bookshelf groaning under the combined weight of many large tomes.\n The smell of rot and mildew is overwhelming- What first looked like a pattern on the wallpaper is revealed to be black mold winding over the walls.\nMost of the books have become swollen with water like a well fed tick and can\'t be moved from their place on the shelf.\nThree books look like they\'re not too water damaged.')
        answer = input('')
    


        

class Study(Room):


     def __init__(self, name, north, south, east, west, doors):
         self.name = name
         self.west = 'statue'
         self.north = 'library'
         self.doors = doors
         self.inv = characters.Inventory([])

        
class Statue(Room):


     def __init__(self, name, north, south, east, west, doors):
        self.name = name
        self.north = 'entrance'
        self.east = 'study'
        self.south = 'bedroom'
        self.west = 'kitchen'
        self.doors = doors
        self.inv = characters.Inventory([])


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
        if ('candle' in player_inventory and 'matches' in player_inventory) or 'lit candle' in player_inventory:
            print('You see a spooky ghost girl!')
            ghost.conversation()
            



class Kitchen(Room):


     def __init__(self, name, north, south, east, west, doors):
         self.name = name
         self.east = 'statue'
         self.north = 'dining'
         self.doors = doors
         self.inv = characters.Inventory([])
        
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

     def flavourtext(self):
        if self.has_scene_played == False:
            print('There\'s a table set with what looks like to have been roast chicken once.\nIt looks like it might have been out for a while.')
            time.sleep(2)
            print('... It smells like it\'s been out for a while.') 
            time.sleep(2)
            print('There\'s a beautiful long white tallow candle illuminating the screen.')
        if self.has_scene_played == True:
            print('There\'s a table set for two, the bone-whiteplates are empty. The smell of rot is intense.')

     def scene(self, user):
        answer = input('What would you like to interact with?  ')
        quitcheck(answer)
        if answer == 'candle' or 'the candle':
            extinguish_candle =(input('Blow out candle?  '))
            quitcheck(extinguish_candle)  
            if extinguish_candle == 'yes':
                self.has_scene_played = True
                print('You blow out the candle.\n As soon as you do, the food resting on the dinner plates errupts into a cacophonous swirl of flies and cockroaches.')
                time.sleep(1)
                print('They fly thick and fast at your face; some get tangled in your hair, some get into your mouth.\n When they finally disapate enough that you can see again, you notice the plates are empty.')
                time.sleep(3)
                print('The smell remains.')
                self.inv.add_from(self.inv, user)
                time.sleep(3)
                print('You pick up the candle and put it in your pocket.')
            if extinguish_candle == 'no':
                print('You leave it be. The skin of the roast chicken ripples slightly as something moves from underneath it.')

        
