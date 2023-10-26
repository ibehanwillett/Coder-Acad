import sys
# import keyboard

def quitcheck(input):
    input = input.strip()
    input = input.lower()
    if input == 'quit':
        sys.exit()
    return input

def get_a_yes_no(prompt):
    while True:
        try:
            answer = input(prompt)
        except ValueError:
            print('No numbers please!')
            continue
        quitcheck(answer)
        if answer == ('yes' or 'y'):
            return True
        elif answer == ('no' or 'n'):
            return False
        else:
            print('Yes or no please!')
            continue
     


# def leave(room):
#     def where_from(room):
#         print('Where would you like to go?')
#         print('Hit the arrows keys to choose a direction or hit q to quit the game.')
#         if keyboard.is_pressed(0x48): # Up Arrow
#             return room.north
#         if keyboard.is_pressed(0x4B): # Left Arrow
#             return room.west
#         if keyboard.is_pressed(0x4D): # Right Arrow
#             return room.east
#         if keyboard.is_pressed(0x50): # Down Arror
#             return room.south
#         if keyboard.is_pressed(16): # Q key
#             print('Thanks for playing!')
#             quit()
    
#     while True:
#         where = where_from(room)
#         if where == 'locked':
#             print('It\'s locked.')
#             continue
#         elif where == 'wall':
#             print('There\'s no door here!')
#             continue
#         else:
#             return where
        
def win_condition_met(username):
    print('You open the door!')
    print('Outside the day is bright and sunny! You sprint off into the warm sunlight.')
    print('You don\'t even notice the little pale ghost face at the bedroom window.')
    print('You certainly don\'t hear the whisper...')
    print(f'\"Goodbye... {username}')
    print("YOU WON!")
    quit()