import sys
from pynput import keyboard


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
     

    

        
def win_condition_met(username):
    print('You open the door!')
    print('Outside the day is bright and sunny! You sprint off into the warm sunlight.')
    print('You don\'t even notice the little pale ghost face at the bedroom window.')
    print('You certainly don\'t hear the whisper...')
    print(f'\"Goodbye... {username}')
    print("YOU WON!")
    quit()