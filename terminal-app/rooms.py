from abc import ABC, abstractmethod
import time
import characters
import items
from items import odyssey, carson, riddle
import random
from doors import Doors
from general import get_a_yes_no, get_input, win_condition_met
from general import script, print_text

# General Script
descript_script = script('descriptions.txt')

# Room base class


class Room(ABC):
    def __init__(self, name):
        self.name = name
        self.inv = items.Inventory([])

    def description(self):
        print(f'You are in the {self.name}.')
        random.seed()
        num = random.randint(1, 10)
        match num:
            case 1:
                print_text(descript_script, 0, 1)
            case 2:
                print_text(descript_script, 1, 2)
            case 3:
                print_text(descript_script, 2, 3, 'light_cyan')
            case 4:
                print_text(descript_script, 3, 4)
            case 5:
                print_text(descript_script, 4, 5)
            case 6:
                print_text(descript_script, 5, 6)
            case 7:
                print_text(descript_script, 6, 7)
            case 8:
                print_text(descript_script, 7, 8)
            case 9:
                print_text(descript_script, 8, 9)
            case 10:
                print_text(descript_script, 9, 10)
        time.sleep(1)

    def print_item_list(self, room_inv):
        answer = get_a_yes_no('Do you want to look around?  ')
        if answer == True:
            if room_inv == []:
                print('There\'s nothing interesting here.')
            else:
                print('Here\'s what you see:')
                for item in range(len(room_inv)):
                    print(room_inv[item])
        if answer == False:
            pass

    @abstractmethod
    def flavourtext(self, player_inv):
        pass

    @abstractmethod
    def scene(self, player_inv, username):
        pass

# Rooms themselves definition
class Entrance(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('locked', 'statue', 'library', 'dining')
        self.inv = items.Inventory('locked door')
        self.script = script('entrance.txt')

    def flavourtext(self, player_inventory):
        if 'key' not in player_inventory.items:
            print_text(self.script, 0, 5, 'light_grey')
        else:
            print('Quickly, you\'re almost free!')

    def scene(self, player_inventory, username):
        answer = get_a_yes_no('Do you try and open the locked door?  ')
        if answer == True:
            if 'key' in player_inventory.items:
                win_condition_met(username)
            else:
                print_text(self.script, 5, 7, 'light_grey')
        else:
            print_text(self.script, 7, 8, 'light_grey')


class Library(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('wall', 'study', 'wall', 'entrance')
        self.inv = items.Inventory([odyssey, carson, riddle])
        self.script = script('library.txt')

    def flavourtext(self, player_inventory):
        print_text(self.script, 0, 1, 'blue')
        time.sleep(1)
        print_text(self.script, 1, 2, 'blue')
        time.sleep(1)
        print_text(self.script, 2, 3, 'blue')
        time.sleep(1)
        print_text(self.script, 3, 4, 'blue')
        time.sleep(1)
        print_text(self.script, 4, 5, 'blue')
        time.sleep(1)
        print_text(self.script, 5, 6, 'blue')
        time.sleep(1)
        print_text(self.script, 6, 7, 'blue')
        time.sleep(1)
        print_text(self.script, 7, 8, 'blue')
        time.sleep(1)
        print_text(self.script, 8, 9, 'blue')
        time.sleep(1)
        print_text(self.script, 9, 10, 'blue')
        time.sleep(1)
        print_text(self.script, 10, 11, 'blue')

    def scene(self, username):
        answer = get_a_yes_no('Do you want to read any of the books?  ')
        if answer == True:
            while True:
                book_pick = get_input(f'Which book do you want to read {username}?  ')
                if book_pick == 'book with a blue spine' or book_pick == 'blue book':
                    odyssey.interact(0, 1, 'blue')
                    break
                if book_pick == 'book with a red spine' or book_pick == 'red book':
                    carson.interact(1, 4, 'red')
                    break
                if book_pick == 'book with a black spine' or book_pick == 'black book':
                    riddle.interact(4, 5, 'dark_grey')
                    break
                if book_pick == 'none':
                    break
                else:
                    print('I can\'t find that book;')
        if answer == False:
            print_text(self.script, 11, 12, 'blue')


class Study(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('library', 'wall', 'wall', 'statue')
        self.inv = items.Inventory(['matches'])
        self.script = script('study.txt')
        self.has_scene_played = False

    def flavourtext(self, player_inv):
        print_text(self.script, 0, 1, 'light_grey')
        time.sleep(1)
        print_text(self.script, 1, 2, 'light_grey')
        time.sleep(1)
        print_text(self.script, 2, 3, 'light_grey')
        time.sleep(1)
        print_text(self.script, 3, 4, 'light_grey')
        time.sleep(1)
        print_text(self.script, 4, 5, 'light_grey')
        time.sleep(1)
        if 'knife' in player_inv.items:
            print_text(self.script, 5, 6, 'light_grey')
            time.sleep(1)
            print_text(self.script, 6, 7, 'light_grey')
            time.sleep(1)
            print_text(self.script, 7, 8, 'red')
            time.sleep(1)
            print_text(self.script, 8, 9, 'light_grey')

    def scene(self, player_inv, username):
        if self.has_scene_played == False:
            answer = get_input(f'What thing do you interact with {username}?  ')
            if answer == 'matches':
                print_text(self.script, 9, 10, 'light_grey')
                time.sleep(1)
                print_text(self.script, 10, 11, 'light_grey')
                get_matches = get_a_yes_no('Pick them up?  ')
                if get_matches == True:
                    self.inv.transfer_item(player_inv, 'matches')
                    self.has_scene_played = True
                    print_text(self.script, 11, 13, 'light_grey')
                if get_matches == False:
                    print_text(self.script, 13, 14, 'light_grey')
            else:
                print_text(self.script, 14, 15, 'light_grey')
        if self.has_scene_played == True:
            print_text(self.script, 15, 16, 'light_grey')


class Statue(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('entrance', 'bedroom', 'study', 'kitchen')
        self.inv = items.Inventory([])
        self.script = script('statue.txt')

    def print_item_list(self, room_inv):
        pass

    def flavourtext(self, player_inventory):
        random.seed()
        num = random.randint(1, 5)
        match num:
            case 1:
                print_text(self.script, 0, 3, 'light_grey')
            case 2:
                print_text(self.script, 3, 6, 'light_grey')
            case 3:
                print_text(self.script, 6, 7, 'light_grey')
                time.sleep(1)
                print_text(self.script, 7, 9, 'light_grey')
                time.sleep(1)
                print_text(self.script, 9, 10, 'light_cyan')
            case 4:
                print_text(self.script, 10, 11, 'light_grey')
                time.sleep(1)
                print_text(self.script, 11, 12, 'light_grey')
                time.sleep(1)
                print_text(self.script, 12, 13, 'light_grey')
            case 5:
                print_text(self.script, 13, 14, 'light_grey')
                time.sleep(1)
                print_text(self.script, 14, 15, 'light_grey')
                time.sleep(1)
                print_text(self.script, 15, 16, 'light_blue')
                time.sleep(1)
                print_text(self.script, 16, 17, 'light_grey')

    def scene(self, player_inventory, username):
        pass


class Bedroom(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('statue', 'wall', 'wall', 'wall')
        self.script = script('bedroom.txt')

    def flavourtext(self, player_inventory):
        pass

    def print_item_list(self, room_inv):
        pass
    
    def scene(self, player_inventory, username):
        print_text(self.script, 0, 1, 'dark_grey')
        if ('candle' in player_inventory.items and
                'matches' not in player_inventory.items):
            print_text(self.script, 1, 2, 'dark_grey')
            print_text(self.script, 2, 3, 'dark_grey')
            time.sleep(1)
            print_text(self.script, 3, 4, 'dark_grey')
            time.sleep(1)
            print_text(self.script, 4, 5, 'dark_grey')
        elif ('matches' in player_inventory.items and
              'candle' not in player_inventory.items):
            print_text(self.script, 5, 6, 'dark_grey')
            time.sleep(2)
            print_text(self.script, 6, 7, 'yellow')
            time.sleep(1)
            print_text(self.script, 7, 8, 'dark_grey')
            print_text(self.script, 8, 9, 'dark_grey')
            time.sleep(1)
            print_text(self.script, 9, 10, 'light_cyan')
            time.sleep(2)
            print_text(self.script, 10, 11, 'dark_grey')
            time.sleep(1)
            print_text(self.script, 11, 12, 'dark_grey')
        elif (('candle' in player_inventory.items and
              'matches' in player_inventory.items)) or \
             ('lit candle' in player_inventory.items):
            print_text(self.script, 12, 13, 'yellow')
            time.sleep(1)
            print_text(self.script, 13, 14, 'yellow')
            time.sleep(1)
            print_text(self.script, 14, 19, 'yellow')
            time.sleep(1)
            print_text(self.script, 19, 20, 'yellow')
            time.sleep(1)
            print_text(self.script, 20, 21, 'yellow')
            time.sleep(1)
            print_text(self.script, 21, 22, 'yellow')
            time.sleep(1)
            print_text(self.script, 22, 23, 'yellow')
            time.sleep(1)
            print_text(self.script, 23, 24, 'yellow')
            time.sleep(1)
            print_text(self.script, 24, 25, 'yellow')
            characters.ghost.conversation(
                player_inventory, username)
        else:
            print_text(self.script, 25, 26, 'dark_grey')
            time.sleep(1)
            print_text(self.script, 26, 27, 'dark_grey')
            time.sleep(1)
            print_text(self.script, 27, 28, 'dark_grey')
            time.sleep(1)
            print_text(self.script, 28, 29, 'dark_grey')


class Kitchen(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('dining', 'wall', 'statue', 'wall')
        self.inv = items.Inventory(['knife'])
        self.script = script('kitchen.txt')

    def flavourtext(self, player_inventory):
        print_text(self.script, 0, 4, 'light_red')

    def scene(self, player_inv, username):
        answer = get_input(f'Do you want to look at {username}?  ')
        if answer == 'knife':
            if 'knife' in self.inv.items:
                print_text(self.script, 4, 6, 'light_red')
                knife_get = get_a_yes_no('Take the knife?  ')
                if knife_get == True:
                    print_text(self.script, 6, 8, 'light_red')
                    self.inv.transfer_item(player_inv, 'knife')
                else:
                    print_text(self.script, 8, 9, 'light_red')
            else:
                print_text(self.script, 9, 10, 'light_red')
        elif answer == 'stove':
            print_text(self.script, 10, 11, 'light_red')
        else:
            print_text(self.script, 11, 12, 'light_red')


class Dining(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('wall', 'kitchen', 'entrance', 'wall')
        self.has_scene_played = False
        self.inv = items.Inventory(['candle'])
        self.script = script('dining.txt')

    def flavourtext(self, player_inventory):
        if self.has_scene_played == False:
            print_text(self.script, 0, 11, 'light_grey')
        if self.has_scene_played == True:
            print_text(self.script, 11, 13, 'light_grey')

    def scene(self, player_inventory, username):
        answer = get_input(f'What do you interact with {username}?  ')
        if answer == 'nothing':
            print('You leave it be.')
            return
        if answer == 'candle' or 'the candle':
            if self.has_scene_played == False:
                extinguish_candle = (get_a_yes_no('Blow out candle?  '))
                if extinguish_candle == True:
                    self.has_scene_played = True
                    print_text(self.script, 13, 14, 'light_grey')
                    time.sleep(1)
                    print_text(self.script, 14, 19, 'light_grey')
                    time.sleep(3)
                    print_text(self.script, 19, 23, 'light_grey')
                    self.inv.transfer_item(player_inventory, 'candle')
                if extinguish_candle == False:
                    print_text(self.script, 23, 24, 'light_grey')
