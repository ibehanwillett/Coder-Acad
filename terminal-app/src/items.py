from general import get_a_yes_no, script, print_text
import time

# Items
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def inspect(self):
        print(f'{self.description}')


class Book(Item):
    def __init__(self, name):
        self.name = name
        self.script = script('book.txt')

    def __str__(self):
        return f'{self.name}'

    def interact(self, start, end, color):
        print('You flip to a random page and begin to read ...')
        time.sleep(2)
        print_text(self.script, start, end, color)
        time.sleep(3)
        print('Hmm... a lot to think about.')


# Book Instances
odyssey = Book('A book with a blue spine')
carson = Book('A book with a red spine')
riddle = Book('A book with a black spine')


# Inventory
class Inventory:

    def __init__(self, items):
        self.items = items

    def give(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def transfer_item(self, other_inv, item):
        other_inv.give(item)
        self.items.remove(item)

    def view_inventory(self):
        for item in range(len(self.items)):
            print(self.items[item])
        if ('candle' in self.items and 'matches' in self.items):
            answer = get_a_yes_no('Light the candle with the matches?')
            if answer == True:
                self.items.append('lit candle')
                self.items.remove('matches')
                self.items.remove('candle')
                print('You now have a lit candle in your inventory.')
                print('It gives off a lovely light.')
            if answer == False:
                return
