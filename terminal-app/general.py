import sys
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
        except:
            print('Something went wrong. Please try again!')
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
    print('Outside the day is bright and sunny!')
    print('You sprint off into the warm sunlight.')
    print('You don\'t even notice the face at the bedroom window.')
    print('You certainly don\'t hear the whisper...')
    print(f'\"Goodbye... {username}')
    print("YOU WON!")


def print_colour(input, colour=None):
    if colour is None:
        print(input)
    else:
        text = colored(input, colour)
        print(text)


def script(filename):
    room = []
    with open(filename, 'rt') as script:
        for line in script:
            room.append(line.rstrip('\n'))
    return room


def print_text(script, start, end, colour=None):
    for line in range(start, end):
        print_colour(script[line], colour)

def room_content(room, player_inv, username):
    room.description()
    room.flavourtext(player_inv)
    room.print_item_list(room.inv.items)
    room.scene(player_inv, username)
    return room.doors.leave(player_inv)