import rooms
import general
import time
from colorama import just_fix_windows_console
from termcolor import colored
import characters

# Colour Set Up
just_fix_windows_console()

# Player and Charater Set Up
player = characters.Character('Player', '')
ghost = characters.ghost

# Position Set Up
position = 'entrance'

# Room set up
entrance = rooms.Entrance('entrance')
library = rooms.Library('library')
study = rooms.Study('study')
statue = rooms.Statue('statue room')
bedroom = rooms.Bedroom('bedroom')
kitchen = rooms.Kitchen('kitchen')
dining = rooms.Dining('dining room')

# START OF GAME
with open('house.txt') as x:
    house = x.read()
    house = colored(house, 'green')
    print(house)
time.sleep(1)
with open('intro.txt') as y:
    intro = y.read()
    intro = colored(intro, 'yellow')
    print(intro)
start_game = general.get_a_yes_no('')
if start_game == False:
    quit()
else:
    pass
username = input('What\'s your name?  ')
if username == 'quit':
    quit()
print('You wake in a spooky scary house! Uh oh!')
print('You try and open the door behind you...')
time.sleep(1)
print('...it\'s locked...')
time.sleep(1)
general.print_colour('You\'re stuck in here.', 'red')
time.sleep(1)
print('You take a look around.')

while True:
    if position == 'entrance':
        entrance.description()
        entrance.flavourtext(player.inv)
        entrance.scene(player.inv, username)
        position = entrance.doors.leave(player.inv)
    if position == 'library':
        library.description()
        library.flavourtext()
        library.print_item_list(library.inv.items)
        library.scene()
        position = library.doors.leave(player.inv)
    if position == 'study':
        study.description()
        study.flavourtext(player.inv)
        study.print_item_list(study.inv.items)
        study.scene(player.inv)
        position = study.doors.leave(player.inv)
    if position == 'statue':
        statue.description()
        statue.flavourtext()
        position = statue.doors.leave(player.inv)
    if position == 'kitchen':
        kitchen.description()
        kitchen.flavourtext()
        kitchen.print_item_list(kitchen.inv.items)
        kitchen.scene(player.inv)
        position = kitchen.doors.leave(player.inv)
    if position == 'dining':
        dining.description()
        dining.flavourtext()
        dining.print_item_list(dining.inv.items)
        dining.scene(player.inv)
        position = dining.doors.leave(player.inv)
    if position == 'bedroom':
        bedroom.description()
        bedroom.scene(player.inv, username)
        position = bedroom.doors.leave(player.inv)
