from abc import ABC
import time
import characters
import items
from items import odyssey, carson, riddle
import random
from doors import Doors
from general import get_a_yes_no, get_input, win_condition_met
from general import script, line_start_and_end

# Scripts
ent_script = script('entrance.txt')
descript_script = script('descriptions.txt')
lib_script = script('library.txt')

# Room base class
class Room:
    def __init__(self, name):
        self.name = name
        self.inv = items.Inventory([])

    def description(self):
        print(f'You are in the {self.name}.')
        random.seed()
        num = random.randint(1, 10)
        match num:
            case 1:
                line_start_and_end(descript_script, 0, 1)
            case 2:
                line_start_and_end(descript_script, 1, 2)
            case 3:
                line_start_and_end(descript_script, 2, 3, 'light_blue')
            case 4:
                line_start_and_end(descript_script, 3, 4)
            case 5:
                line_start_and_end(descript_script, 4, 5)
            case 6:
                line_start_and_end(descript_script, 5, 6)
            case 7:
                line_start_and_end(descript_script, 6, 7)
            case 8:
                line_start_and_end(descript_script, 7, 8)
            case 9:
                line_start_and_end(descript_script, 8, 9)
            case 10:
                line_start_and_end(descript_script, 9, 10)
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


# Rooms themselves definition
class Entrance(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('locked', 'statue', 'library', 'dining')
        self.inv = items.Inventory(['locked door'])

    def flavourtext(self, player_inv):
       line_start_and_end(ent_script,0, 5, 'dark_grey')

    def scene(self, player_inventory, username):
        answer = get_a_yes_no('Do you try and open the locked door?  ')
        if answer == True:
            if 'key' in player_inventory.items:
                win_condition_met(username)
            else:
                line_start_and_end(ent_script, 5, 7, 'dark_grey')
        else:
            line_start_and_end(ent_script, 7, 8, 'dark_grey')


class Library(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('wall', 'study', 'wall', 'entrance')
        self.inv = items.Inventory([odyssey, carson, riddle])

    def flavourtext(self):
        line_start_and_end(lib_script, 0, 1, 'blue')
        time.sleep(1)
        line_start_and_end(lib_script, 1, 2, 'blue')
        time.sleep(1)
        line_start_and_end(lib_script, 2, 3, 'blue')
        time.sleep(1)
        line_start_and_end(lib_script, 3, 4, 'blue')
        time.sleep(1)
        line_start_and_end(lib_script, 4, 5, 'blue')
        time.sleep(1)
        line_start_and_end(lib_script, 5, 6, 'blue')
        time.sleep(1)
        line_start_and_end(lib_script, 6, 7, 'blue')
        time.sleep(1)
        line_start_and_end(lib_script, 7, 8, 'blue')
        time.sleep(1)
        line_start_and_end(lib_script, 8, 9, 'blue')
        time.sleep(1)
        line_start_and_end(lib_script, 9, 10, 'blue')
        time.sleep(1)
        line_start_and_end(lib_script, 10, 11, 'blue')

    def scene(self):
        answer = get_a_yes_no('Do you want to read any of the books?  ')
        if answer == True:
            while True:
                book_pick = get_input('Which book do you want to read?  ')
                if book_pick == 'book with a blue spine' or book_pick == 'blue book':
                    odyssey.interact()
                    break
                if book_pick == 'book with a red spine' or book_pick == 'red book':
                    carson.interact()
                    break
                if book_pick == 'book with a black spine' or book_pick == 'black book':
                    riddle.interact()
                    break
                if book_pick == 'none':
                    break
                else:
                    print('I can\'t find that book;'), \
                        (' try again or write \'exit\' to leave.')
        if answer == False:
            line_start_and_end(lib_script, 11, 12, 'blue')


class Study(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('library', 'wall', 'wall', 'statue')
        self.inv = items.Inventory(['matches'])
        self.has_scene_played = False

    def flavourtext(self, player_inv):
        print('The study\'s wall are covered in writing.')
        time.sleep(1)
        print('The words spiral out from the writing desk')
        time.sleep(1)
        print('like someone starting writing and couldn\'t stop.')
        time.sleep(1)
        print('The writing gets more erratic as it goes on.')
        time.sleep(1)
        print('Eventually the ink runs out'), \
            ('and the words are scratched into the wall instead.')
        time.sleep(1)
        print(' ...then the writer found a new kind of ink.')
        time.sleep(1)
        if 'knife' in player_inv.items:
            print_red('You can read the words out now.')
            time.sleep(1)
            print_red('How could you not?')
            time.sleep(1)
            print_red('They reads \"MEAT MEAT MEAT MEAT MEAT\"')
            time.sleep(1)
            print_red('They\'re lyrics and you know the song.')

    def scene(self, player_inv):
        if self.has_scene_played == False:
            answer = get_input('What do you want to interact with?  ')
            if answer == 'matches':
                print('You see some scattered matches on the table.')
                print('Most of them have been ruined by the... ink.'), \
                    (' but some are still good.')
                get_matches = get_a_yes_no('Pick them up?  ')
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
        num = random.randint(1, 5)
        match num:
            case 1:
                print('The room is full of different statutes'), \
                    (' of men grappling with snakes.')
            case 2:
                print('All the statues are facing you.')
                print('Have they always faced this direction?'), \
                    ('Did they always look this angry?')
            case 3:
                print('There\'s only one statue in the room.')
                time.sleep(1)
                print('It\'s of a young women.'), \
                    ('She\'s looking into a handmirror and crying.')
                time.sleep(1)
                print_blue('She looks... familiar.')
            case 4:
                print('The room is filled with horse statues.')
                time.sleep(1)
                print('The horses are bitng and tearing at each other.')
                time.sleep(1)
                print('Eurgh!')
            case 5:
                print('There\'s a statue of...')
                time.sleep(1)
                print_blue('you?')
                time.sleep(1)
                print('You\'re looking into a handmirror and crying.')


class Bedroom(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('statue', 'wall', 'wall', 'wall')

    def scene(self, player_inventory, ghost_inventory, username):
        print('It\'s so dark...')
        if ('candle' in player_inventory.items and
                'matches' not in player_inventory.items):
            print('It\'s too dark to see.')
            print('You have a candle, but nothing to light it with!')
            print('You should probably leave.')
        elif ('matches' in player_inventory.items and
              'candle' not in player_inventory.items):
            print('You try to light some matches...')
            time.sleep(2)
            print_yellow('You get a second of light!'), \
                ('You see briefly what look\'s to be a bedroom- wait.')
            time.sleep(2)
            print('Did something just move?')
            time.sleep(2)
            print('The match burns out,'), \
                ('leaving you with only burnt fingertips'), \
                ('and a stone of dread rising in your throat.')
            print('Best return with something to light the candle.')
        elif (('candle' in player_inventory.items and
              'matches' in player_inventory.items)) or \
             ('lit candle' in player_inventory.items):
            print_yellow('You see a spooky ghost girl!')
            characters.ghost.conversation(
                player_inventory, username)
        else:
            print('It\'s too dark to see!')
            print('You get a feeling you should leave.')


class Kitchen(Room):
    def __init__(self, name):
        self.name = name
        self.doors = Doors('dining', 'wall', 'statue', 'wall')
        self.inv = items.Inventory(['knife'])

    def flavourtext(self):
        print_red('The kitchen is as hot as a furnace!')
        print_red(
            'The stove has been left on, flames rage from behind it\'s glass window.')
        print_red(
            'You try and turn it off but it\'s knobs are too hot for you to touch.')

    def scene(self, player_inv):
        answer = get_input('What do you want to inspect in the kitchen?  ')
        if answer == 'knife':
            if 'knife' in self.inv.items:
                print(
                    'You see a sharp kitchen knife stabbed deep into the wooden countertop.')
                print(
                    'It\'s gleaming metallic surface looks out of place amongst this run down kitchen.')
                knife_get = get_a_yes_no('Take the knife?  ')
                if knife_get == True:
                    print(
                        'The knife feels good in your hand, like it\'s supposed to be there.')
                    self.inv.transfer_item(player_inv, 'knife')
                    print('The knife is added to your inventory.')
                else:
                    print(
                        'You leave it be, shining in the warm red light emanating from the oven.')
            else:
                print('You already have the knife, remember? It hasn\'t left your hand.')
        elif answer == 'stove':
            print_red('It\'s too hot to touch!')
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
            print_green('There\'s a dinner table set for two.')
            print_green('There\'s lovely silverwear, crisp white napkins.')
            print_green(
                'In the centre, something that used to be a roast chicken.')
            time.sleep(1)
            print_green('It looks like it might have been out for a while.')
            time.sleep(2)
            print_green('... It smells like it\'s been out for a while.')
            time.sleep(2)
            print_green('A tall white candle gives off warm light.')
        if self.has_scene_played == True:
            print_green('There\'s a table set for two,'), \
                ('the bone-whiteplates are empty. The smell of rot is intense.')

    def scene(self, user):
        answer = get_input('What would you like to interact with?  ')
        if answer == 'nothing':
            print_green('You leave it be.')
            return
        if answer == 'candle' or 'the candle':
            if self.has_scene_played == False:
                extinguish_candle = (get_a_yes_no('Blow out candle?  '))
                if extinguish_candle == True:
                    self.has_scene_played = True
                    print_green('You blow out the candle.')
                    print_red('As soon as you do, the food resting on the dinner plates'), \
                        (' errupts into a cacophonous flurry of flies and cockroaches.')
                    time.sleep(1)
                    print_red('They fly thick and fast at your face;'), \
                        ('some get tangled in your hair,'), \
                        (' some get into your mouth.')
                    print_green(
                        'When they finally dissipate, the plates are empty.')
                    time.sleep(3)
                    print_green('The smell remains.')
                    self.inv.transfer_item(user, 'candle')
                    time.sleep(3)
                    print('You pick up the candle and put it in your pocket.')
                if extinguish_candle == False:
                    print_green('You leave it be.'), \
                        (' The skin of the roast chicken bulges slightly.')
