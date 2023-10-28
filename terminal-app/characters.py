import items
import time
from general import quitcheck, get_input


class Character:
    def __init__(self, name, things):
        self.things = things
        self.inv = items.Inventory([self.things])
        self.has_had_conversation = False

    def conversation(self, player_inv, username):
        convo_line = []
        with open ('conversation.txt', 'rt') as convo_script:
            for convo_line in convo_script:
                convo_line.append(convo_line.rstrip('\n'))
        if self.has_had_conversation == False:
            print(convo_line(0))
            time.sleep(1)
            print('The ghost is crying. She was beautiful once.')
            time.sleep(1)
            print('The ghost looks up at you through pale and watery eyes.')
            time.sleep(1)
            print(
                'The ghost toys with the brass key hanging on her neck.\nShe seems to come to a descion.')
            print(
                '\"Fine,\" she says \" Fine, I\'ll give you the key- if you can answer my riddle.\"')
            time.sleep(1)
            print('Her eye flash with- what? Spite? Rage? Sorrow?\nYou can\'t tell.')
            time.sleep(1)
            print('She asks:')
            answer = get_input(' I saw a woman sit alone. What am I?  ')
            if (answer == 'a mirror' or answer == 'mirror'):
                print('\"That\'s exactly right.\"')
                self.inv.transfer_item(player_inv, 'key')
                print(player_inv.items)
                print('You feel the key slide into you pocket. It\'s cold as ice.')
                print(f'The ghost says sadly \"It\'s not to late to stay {username}!\"')
            else:
                print(
                    'The ghost shrieks \'WRONG!\' A red cloud covers the mirror and when it disappates the ghost is gone.')
        if self.has_had_conversation == True:
            print(
                'The ghost is gone. You hear the sound of muffled sobbing through the walls.')


ghost = Character('Ghost', ['key'])
