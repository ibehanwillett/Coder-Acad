import sys
from colorama import just_fix_windows_console
from termcolor import colored

def quitcheck(input):
    input = input.strip()
    input = input.lower()
    if input == 'quit':
        sys.exit()
    return input

def get_input(prompt):
    while True:
        try:
            x = input(prompt)
        except ValueError:
            print('No numbers please!')
            continue
        except:
            print('Something went wrong. Can you try that again?')
            continue
        else:
            quitcheck(x)
            return x


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

def print_red(input):
    text = colored(input, "red")
    print(text)

def print_green(input):
    text = colored(input, "green")
    print(text)

def print_blue(input):
    text = colored(input, "blue")
    print(text)

def print_yellow(input):
    text = colored(input, "yellow")
    print(text)