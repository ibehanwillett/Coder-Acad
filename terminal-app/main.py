import rooms
from general import quitcheck
import sys
import time
import characters



# Player and Charater Set Up
player = characters.Character('Player', [])
ghost = characters.Character('Ghost', ['key'])
# Position Set Up
position = 'entrance'
# Room set up
entrance = rooms.Entrance('entrance', 'locked', 'statue','library','dining','The entrance is a room. Placeholder description. There is a door on the east wall, west wall and south wall.')
library = rooms.Library('library', 'wall', 'study', 'wall', 'entrance', 'You\'re in a library. There\'s a door on south wall and west wall.')
study = rooms.Study('study', 'library', 'wall', 'wall', 'statue', 'You\'re in the study. There is a door on the west wall and the north wall.')
statue = rooms.Statue('statue', 'entrance', 'bedroom', 'study', 'kitchen','You\'re in a room full of statutes. Doors surround you on all all four cardinal directions.' )
bedroom = rooms.Bedroom('Bedroom','statue', 'wall', 'wall', 'wall', 'You are in the bedroom. There is only one door to the north.' )
kitchen = rooms.Kitchen('Kitchen', 'dining', 'wall', 'statue', 'wall','You\'re in the kitchen. There is a door on the east wall and north wall.')
dining = rooms.Dining('Dining Room', 'wall', 'kitchen', 'entrance', 'wall', 'You\'re in the dining room. There\'s a door on the south wall and east wall.')





# def whereto(move_choice):
#     if move_choice == 'locked':
#             print('The front door is locked! You jiggle the doorknob a couple times but nothing happens...')
#     if move_choice == 'wall':
#             print('There\'s no door to that direction!')
#     else:
#         global position
#         position = f'{move_choice}'


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
        move_choice = entrance.door_pick()
        quitcheck(move_choice)
        if move_choice == 'locked' and key in player.inv:
            print('You unlock the door!')
            break
        if move_choice == 'locked':
            print('The front door is locked! You jiggle the doorknob a couple times but nothing happens...')
        else:
            position = f'{move_choice}'
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
        move_choice = statue.door_pick()
        if move_choice == 'wall':
            print('There\'s no door to that direction!')
        else:
            position = f'{move_choice}'
    if position == 'kitchen':
        kitchen.description()
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


    
    


    

