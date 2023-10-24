import rooms
import time

# GENERAL SCRIPT


position = 'entrance'

entrance = roooms.Entrance('Entrance')
library = rooms.Library('Library')
study = rooms.Study('Study')
statue = rooms.Statue('Statue')
bedroom = rooms.Bedroom('Bedroom')
kitchen = rooms.Kitchen('Kitchen')
dining = rooms.Dining('Dining Room')


# def whereto(move_choice):
#     if move_choice == 'locked':
#             print('The front door is locked! You jiggle the doorknob a couple times but nothing happens...')
#     if move_choice == 'wall':
#             print('There\'s no door to that direction!')
#     else:
#         global position
#         position = f'{move_choice}'


#START OF GAME
print('You wake in a spooky scary house! Uh oh!')
print('You try and open the door behind you...')

while True:
    if position == 'entrance':
        entrance.description()
        move_choice = entrance.doorpick()
        if move_choice == 'locked':
            print('The front door is locked! You jiggle the doorknob a couple times but nothing happens...')
        else:
            position = f'{move_choice}'
    if position == 'library':
        library.description()
        move_choice = library.doorpick()
        if move_choice == 'wall':
            print('There\'s no door to that direction!')
        else:
            position = f'{move_choice}'
    if position == 'study':
        study.description()
        move_choice = study.doorpick()
        if move_choice == 'wall':
            print('There\'s no door to that direction!')
        else:
            position = f'{move_choice}'
    if position == 'statue':
        statue.description()
        move_choice = statue.doorpick()
        if move_choice == 'wall':
            print('There\'s no door to that direction!')
        else:
            position = f'{move_choice}'
    if position == 'kitchen':
        kitchen.description()
        move_choice = kitchen.doorpick()
        if move_choice == 'wall':
                print('There\'s no door to that direction!')
        else:
            position = f'{move_choice}'
    if position == 'dining':
        dining.description()
    
        move_choice = dining.doorpick()
        if move_choice == 'wall':
            print('There\'s no door to that direction!')
        else:
            position = f'{move_choice}'
    if position == 'bedroom':
        bedroom.description()
        move_choice = bedroom.doorpick()
        if move_choice == 'wall':
            print('There\'s no door to that direction!')
        else:
            position = f'{move_choice}'


    
    


    

