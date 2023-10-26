from abc import ABC
import time
import characters
import items
from general import quitcheck
from general import get_a_yes_no


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
        while True:
            door = (input('Where do you want to go?  '))
            quitcheck(door)
            if door == 'north':
                return f'{self.north}'
            if door == 'south':
                return f'{self.south}'
            if door == 'east':
                return f'{self.east}'
            if door == 'west':
                return f'{self.west}'
            else: 
                print('Sorry, I don\'t understand. Please try again.')
                continue

    def description(self):
        print(f'You are in the {self.name}')
        print(self.doors)
    
    def print_item_list(self, room_inv):
        answer = get_a_yes_no('Do you want to look around?  ')
        if answer == True:
            print('Here\'s what jumps out at you as you look around the room')
            for item in range(len(room_inv)):
                print(room_inv[item])
        if answer == False:
            pass

    
# Rooms themselves definition
class Entrance(Room):
    def __init__(self, name, north, south, east, west, doors):
        self.name = name
        self.north = 'locked'
        self.east = 'library'
        self.south = 'statue'
        self.west = 'dining'
        self.doors = doors
        self.inv = items.Inventory(['locked door'])
    
    def flavourtext(self, player_inv):
        print('You find yourself in a ruined entrance of a grand old manor house.')
        print('The black and white parquet is cracked and ruined. ')
        print('Sometimes, something hot and wet oozes from underneath the tile as you step on it.')

    def scene(self, player_inventory):
        answer = get_a_yes_no('Do you try and open the locked door?')
        if answer == True:
            if 'key' in player_inventory.items:
                

    


class Library(Room):
    def __init__(self, name, north, south, east, west, doors):
        self.name = name
        self.south = 'study'
        self.west = 'entrance'
        self.doors = doors
        self.inv = items.Inventory([items.odyssey, items.carson, items.riddle])
    
    def flavourtext(self):
        print('You see a bookshelf groaning under the weight of many large tomes.\n The smell of rot and mildew is overwhelming-  you realise what you first took to be a pattern on the wallpaper is actually black mold growing in spirals over everything.\nMost of the books have become swollen with water and can\'t be moved from their place on the shelf.\nThree books look like they\'re not too water damaged.')

    def scene(self):
        answer = get_a_yes_no('Do you want to read any of the books?  ')
        if answer == True:
            while True:
                book_pick = input('Which book do you want to read?  ')
                quitcheck(book_pick)
                if book_pick == 'book with a blue spine' or book_pick == 'blue book':
                    items.odyssey.interact()
                    break
                if book_pick == 'book with a red spine' or book_pick == 'red book':
                    items.carson.interact()
                    break
                if book_pick == 'book with a black spine' or book_pick == 'black book':
                    items.riddle.interact()
                    break
                if book_pick == 'none':
                    break
                else:
                    print('I can\'t find that book; try again or write \'exit\' to leave.')
        if answer == False:
            print('You leave the books alone to their somber, sodden rest.')


        

class Study(Room):


     def __init__(self, name, north, south, east, west, doors):
         self.name = name
         self.west = 'statue'
         self.north = 'library'
         self.doors = doors
         self.inv = items.Inventory(['matches'])
         self.has_scene_played = False

     def flavourtext(self, player_inv):
        print('The study\'s wall are covered in writing. The words spiral out from the writing desk like someone starting writing and couldn\'t stop.\nThe writing starts out neat and carefully penned in black ink and gets wilder and more erratic as it goes on.\nEventually the ink runs out and the words are scratched into the wall instead.\n ...then the writer found a new kind of ink.')
        if 'knife' in player_inv.items:
            print('You can make the words out now. In fact you can\'t believe they ever gave you difficulty.\nIt reads \"MEAT MEAT MEAT MEAT MEAT\" They\'re lyrics and you know the song.')

     def scene(self, player_inv):
        if self.has_scene_played == False:
            answer = input('What do you want to interact with?  ')
            quitcheck(answer)
            if answer == 'matches':
                print('You see some matches scattered across the table.\nMost of them have been ruined by the... ink... but some are still good.')
                get_matches = get_a_yes_no('Pick them up?')
                if get_matches == True:
                    self.inv.add_from(self.inv, player_inv)
                    self.has_scene_played = True
                    print('You pick the matches up.')
                if get_matches == False:
                    print('You leave them alone.')
            else: 
                print('I don\'t know what you mean.')
        if self.has_scene_played == True:
            print('God... why does some of the ink still look wet?')


class Statue(Room):


     def __init__(self, name, north, south, east, west, doors):
        self.name = name
        self.north = 'entrance'
        self.east = 'study'
        self.south = 'bedroom'
        self.west = 'kitchen'
        self.doors = doors
        self.inv = items.Inventory([])


class Bedroom(Room):


    def __init__(self, name, north, south, east, west, doors):
         self.name = name
         self.north = 'statue'
         self.doors = doors
         
    def scene(self, player_inventory, ghost_inventory, username):
        print('It\'s so dark...')
        if ('candle' in player_inventory.items and 'matches' not in player_inventory.items):
            print('It\'s too dark to see. You have a candle, but nothing to light it with! \nYou should probably leave.')
        elif ('matches' in player_inventory.items and 'candle' not in player_inventory.items):
            print('You try to light some matches...')
            time.sleep(1)
            print('You get a second of light! You see briefly what look\'s to be a bedroom, it\'s very pink and- wait.')
            time.sleep(2)
            print('Did something just move?')
            time.sleep(1)
            print('The match burns out, leaving you with nothing but burnt fingertips and a stone of dread rising in your throat. \n Best come back when you have something to light the candle with.')
        elif ('candle' in player_inventory.items and 'matches' in player_inventory.items) or ('lit candle' in player_inventory.items):
            print('You see a spooky ghost girl!')
            characters.ghost.conversation(player_inventory, ghost_inventory, username)
        else:
            print('It\'s too dark to see! You get a bad feeling; you should leave.')  



class Kitchen(Room):


     def __init__(self, name, north, south, east, west, doors):
         self.name = name
         self.east = 'statue'
         self.north = 'dining'
         self.doors = doors
         self.inv = items.Inventory(['knife'])
        
     def scene(self):
        print('Kitchen time baby. Time to make a pie... of PEOPLE!!! SPOOKY SCARY')

        


class Dining(Room):

    
     def __init__(self, name, north, south, east, west, doors):
         self.name = name
         self.south = 'kitchen'
         self.east = 'entrance'
         self.doors = doors
         self.has_scene_played = False
         self.inv = items.Inventory(['candle'])

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
        if answer == 'nothing':
            print('You leave it be.')
            return
        if answer == 'candle' or 'the candle':
            if self.has_scene_played == False:
                extinguish_candle = (get_a_yes_no('Blow out candle?  '))
                if extinguish_candle == True:
                    self.has_scene_played = True
                    print('You blow out the candle.\n As soon as you do, the food resting on the dinner plates errupts into a cacophonous swirl of flies and cockroaches.')
                    time.sleep(1)
                    print('They fly thick and fast at your face; some get tangled in your hair, some get into your mouth.\n When they finally disapate enough that you can see again, you notice the plates are empty.')
                    time.sleep(3)
                    print('The smell remains.')
                    self.inv.add_from(self.inv, user)
                    time.sleep(3)
                    print('You pick up the candle and put it in your pocket.')
                if extinguish_candle == False:
                    print('You leave it be. The skin of the roast chicken ripples slightly as something moves from underneath it.')
    
        
