from abc import ABC
import time
import characters
import items
import random
from doors import Doors
from general import quitcheck
from general import get_a_yes_no
from general import win_condition_met


# Room base class
class Room:
    def __init__(self, name):
        self.name = name
        self.inv = items.Inventory([])

    def description(self):
        print(f'You are in the {self.name}')
        random.seed()
        num = random.randint(1,10)
        match num:
            case 1:
                print('You can hear the wind moaning outside.')
            case 2:
                print('You feel watched.')
            case 3:
                print('The reflections are wrong here.')
            case 4:
                print('Suddenly, you\'re struck by a ravenous hunger.')
            case 5:
                print('Your teeth feel wrong in your mouth.')
            case 6:
                print('The floorboards creak underneath your feet.')
            case 7:
                print('Suddenly, your heart starts beating faster.')
            case 8:
                print('You feel sick.')
            case 9:
                print('Somewhere else, a door slams.')
            case 10:
                print('You hear a scream from somewhere else in the house.')
        time.sleep(1)
    
    def print_item_list(self, room_inv):
        answer = get_a_yes_no('Do you want to look around?  ')
        if answer == True:
            if room_inv == []:
                print('There\'s nothing interesting here.')
            else:
                print('Here\'s what jumps out at you as you look around the room')
                for item in range(len(room_inv)):
                    print(room_inv[item])
        if answer == False:
            pass

    
# Rooms themselves definition
class Entrance(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('locked', 'statue','library','dining')
        self.inv = items.Inventory(['locked door'])
    
    def flavourtext(self, player_inv):
        print('You find yourself in a ruined entrance of a grand old manor house.')
        print('The black and white parquet is cracked and ruined. ')
        print('Sometimes, something hot and wet oozes from underneath the tile as you step on it.')

    def scene(self, player_inventory, username):
        answer = get_a_yes_no('Do you try and open the locked door?  ')
        if answer == True:
            if 'key' in player_inventory.items:
                win_condition_met(username)
            else: 
                print('You really try to pry the door open but it\'s locked fast.')
        else: 
            print('The wind howls outside.')

                
class Library(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('wall', 'study', 'wall', 'entrance')
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
    def __init__(self, name):
         self.name = name
         self.doors = Doors('library', 'wall', 'wall', 'statue')
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
                    self.inv.transfer_item(player_inv, 'matches')
                    self.has_scene_played = True
                    print('You pick the matches up.')
                if get_matches == False:
                    print('You leave them alone.')
            else: 
                print('I don\'t know what you mean.')
        if self.has_scene_played == True:
            print('God... why does some of the ink still look wet?')


class Statue(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('entrance', 'bedroom', 'study', 'kitchen')
        self.inv = items.Inventory([])
    
    def flavourtext(self):
        random.seed()
        num = random.randint(1,5)
        match num:
            case 1:
                print('The statues are all gasping in horror.')
            case 2:
                print('All the statues are facing you. Have they always faced this direction? Did they always look this angry?')
            case 3:
                print('There\'s only one statue in the room.')
                print('It\'s of a young women. She\'s looking into a handmirror and crying.')
                time.sleep(1)
                print('She looks... familiar.')
            case 4:
                print('The room is filled with horse statues.')
                print('The horses are bitng and tearing each other\'s skin.')
                print('Eurgh!')
            case 5:
                print('There\'s a statue of... you?')
                print('You\'re looking into a handmirror and crying.')


class Bedroom(Room):


    def __init__(self, name):
         self.name = name
         self.doors = Doors('statue', 'wall', 'wall', 'wall')
         
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
    def __init__(self, name):
         self.name = name
         self.doors = Doors('dining', 'wall', 'statue', 'wall')
         self.inv = items.Inventory(['knife'])

    def flavourtext(self):
        print('The kitchen is as hot as a furnace!')
        print('The stove has been left on, flames rage from behind it\'s glass window.')
        print('You try and turn it off but it\'s knobs are too hot for you to touch.')
                
    def scene(self, player_inv):
        answer = input('What do you want to inspect in the kitchen?)')
        quitcheck(answer)
        if answer == 'knife':
            if 'knife' in self.inv.items:
                print('You see a sharp kitchen knife stabbed deep into the wooden countertop.')
                print('It\'s gleaming metallic surface looks out of place amongst this run down kitchen.')
                knife_get = get_a_yes_no('Take the knife?')
                if knife_get == True:
                    print('The knife feels good in your hand, like it\'s supposed to be there.')
                    self.inv.transfer_item(player_inv, 'knife')
                    print('The knife is added to your inventory.')
                else:
                    print('You leave it be, shining in the warm red light emanating from the oven.')
            else:
                print('You already have the knife, remember? It hasn\'t left your hand.')
        elif answer == 'stove':
            print('It\'s too hot to touch!')
        else:
            print('I did\'t understand that.')
                    
        
class Dining(Room):
    def __init__(self, name):
         self.name = name
         self.doors = Doors('wall', 'kitchen', 'entrance', 'wall')
         self.has_scene_played = False
         self.inv = items.Inventory(['candle'])

    def flavourtext(self):
        if self.has_scene_played == False:
            print('There\'s a table set with what looks like to have been roast chicken once.')
            print('It looks like it might have been out for a while.')
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
                    print('You blow out the candle.')
                    print('As soon as you do, the food resting on the dinner plates errupts into a cacophonous swirl of flies and cockroaches.')
                    time.sleep(1)
                    print('They fly thick and fast at your face; some get tangled in your hair, some get into your mouth.\n When they finally disapate enough that you can see again, you notice the plates are empty.')
                    time.sleep(3)
                    print('The smell remains.')
                    self.inv.transfer_item(user, 'candle')
                    time.sleep(3)
                    print('You pick up the candle and put it in your pocket.')
                if extinguish_candle == False:
                    print('You leave it be. The skin of the roast chicken ripples slightly as something moves from underneath it.')
    
        
