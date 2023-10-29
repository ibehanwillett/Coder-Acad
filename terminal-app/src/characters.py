import items
import time
from general import get_input, script, print_text


class Character:
    def __init__(self, name, things):
        self.things = things
        self.inv = items.Inventory([self.things])
        self.has_had_conversation = False
        self.script = script('conversation.txt')

    def conversation(self, player_inv, username):
        if self.has_had_conversation == False:
            print_text(self.script, 0, 1, 'light_cyan')
            time.sleep(1)
            print_text(self.script, 1, 2, 'light_cyan')
            time.sleep(1)
            print_text(self.script, 2, 3, 'light_cyan')
            time.sleep(1)
            print_text(self.script, 3, 5, 'light_cyan')
            time.sleep(1)
            print_text(self.script, 5, 7, 'light_cyan')
            time.sleep(1)
            print('She asks:')
            answer = get_input(' I saw a woman sit alone. What am I?  ')
            if (answer == 'a mirror' or answer == 'mirror'):
                print_text(self.script, 7, 8, 'light_cyan')
                self.inv.transfer_item(player_inv, 'key')
                print_text(self.script, 8, 11, 'light_cyan')
                print(f'\"It\'s not to late to stay {username}!\"')
            else:
                print_text(self.script, 11, 15, 'light_cyan')
        if self.has_had_conversation == True:
            print_text(self.script, 15, 16, 'light_cyan')


ghost = Character('Ghost', 'key')
