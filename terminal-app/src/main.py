import rooms
import general
from general import room_content
import time
from colorama import just_fix_windows_console
from termcolor import colored
import characters

# Colour Set Up
just_fix_windows_console()

# Player and Charater Set Up
player = characters.Character('Player','')
ghost = characters.ghost

# Room set up
entrance = rooms.Entrance('entrance')
library = rooms.Library('library')
study = rooms.Study('study')
statue = rooms.Statue('statue room')
bedroom = rooms.Bedroom('bedroom')
kitchen = rooms.Kitchen('kitchen')
dining = rooms.Dining('dining room')

# Position Set Up
position = 'entrance'
map = {'entrance': entrance, 'library': library, 'study': study,
       'statue': statue, 'bedroom': bedroom, 'kitchen': kitchen,
       'dining': dining}

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
    position = room_content(map[position], player.inv, username)
