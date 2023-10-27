import rooms
import general
from general import quitcheck
from general import win_condition_met
import sys
import time
import characters



# Player and Charater Set Up
player = characters.Character('Player', [])
ghost = characters.ghost
# Position Set Up
position = 'entrance'
# Room set up
entrance = rooms.Entrance('entrance', 'locked', 'statue','library','dining','There is a door to the east, west and south.')
library = rooms.Library('library', 'wall', 'study', 'wall', 'entrance', 'There\'s a door to the south and the west.')
study = rooms.Study('study', 'library', 'wall', 'wall', 'statue', 'There is a door on the west and the north.')
statue = rooms.Statue('statue room', 'entrance', 'bedroom', 'study', 'kitchen','There is a door to your west, north and east. To the south, a spiral staircase winds up to darkness.' )
bedroom = rooms.Bedroom('bedroom','statue', 'wall', 'wall', 'wall', 'You are in the bedroom. The only exit is north, the stairwell going back downstairs.' )
kitchen = rooms.Kitchen('kitchen', 'dining', 'wall', 'statue', 'wall','There is a door to the east and the north.')
dining = rooms.Dining('dining room', 'wall', 'kitchen', 'entrance', 'wall', 'There\'s a door to the south and another to the east.')






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
        position = general.leave(entrance)
        # move_choice = entrance.door_pick()
        # quitcheck(move_choice)
        # if (move_choice == 'locked' and 'key' in player.inv.items):
        #     print('You unlock the door!')
        #     win_conditon_met(username)
        # if (move_choice == 'locked' and 'key' not in player.inv.items):
        #     print('The front door is locked! You jiggle the doorknob a couple times but nothing happens...')
        # else:
        #     position = f'{move_choice}'
    if position == 'library':
        library.description()
        library.flavourtext()
        library.print_item_list(library.inv.items)
        library.scene()
        move_choice = library.door_pick()
        if move_choice == 'wall':
            print('There\'s no door to that direction!')
        else:
            position = f'{move_choice}'
    if position == 'study':
        study.description()
        study.flavourtext(player.inv)
        study.print_item_list(study.inv.items)
        study.scene(player.inv)
        move_choice = study.door_pick()
        if move_choice == 'wall':
            print('There\'s no door to that direction!')
        else:
            position = f'{move_choice}'
    if position == 'statue':
        statue.description()
        statue.flavourtext()
        move_choice = statue.door_pick()
        if move_choice == 'wall':
            print('There\'s no door to that direction!')
        else:
            position = f'{move_choice}'
    if position == 'kitchen':
        kitchen.description()
        kitchen.flavourtext()
        kitchen.print_item_list(kitchen.inv.items)
        kitchen.scene(player.inv)
        move_choice = kitchen.door_pick()
        if move_choice == 'wall':
                print('There\'s no door to that direction!')
        else:
            position = f'{move_choice}'
    if position == 'dining':
        dining.description()
        dining.flavourtext()
        dining.print_item_list(dining.inv.items)
        dining.scene(player.inv)
        move_choice = dining.door_pick()
        if move_choice == 'wall':
            print('There\'s no door to that direction!')
        else:
            position = f'{move_choice}'
    if position == 'bedroom':
        bedroom.description()
        bedroom.scene(player.inv, ghost.inv, username)
        move_choice = bedroom.door_pick()
        if move_choice == 'wall':
            print('There\'s no door to that direction!')
        else:
            position = f'{move_choice}'



    
    


    

