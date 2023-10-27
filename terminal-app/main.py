import rooms
import general
from general import quitcheck
from general import win_condition_met
import sys
import time
import characters



# Player and Charater Set Up
player = characters.Character('Player', ' ')
ghost = characters.ghost
# Position Set Up
position = 'entrance'
# Room set up
entrance = rooms.Entrance('entrance','There is a door to the east, west and south.')
library = rooms.Library('library', 'There\'s a door to the south and the west.')
study = rooms.Study('study', 'There is a door on the west and the north.')
statue = rooms.Statue('statue room', 'There is a door to your west, north and east. To the south, a spiral staircase winds up to darkness.' )
bedroom = rooms.Bedroom('bedroom','You are in the bedroom. The only exit is north, the stairwell going back downstairs.' )
kitchen = rooms.Kitchen('kitchen', 'There is a door to the east and the north.')
dining = rooms.Dining('dining room', 'There\'s a door to the south and another to the east.')






#START OF GAME
username = input('What\'s your name?  ')
print('You wake in a spooky scary house! Uh oh!')
print('You try and open the door behind you...')
time.sleep(1)
print('...it\'s locked...')
time.sleep(1)
print('You\'re stuck in here.')
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
        move_choice = statue.door_pick()
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
        bedroom.scene(player.inv, ghost.inv, username)
        position = bedroom.doors.leave(player.inv)



    
    


    

