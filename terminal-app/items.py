from general import get_a_yes_no
import time

# Items
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def inspect(self):
        print(f'{self.description}')


class Book(Item):
    def __init__(self, name, description, excerpt):
        self.name = name
        self.description = description
        self.excerpt = excerpt

    def __str__(self):
        return f'{self.name}'   

    def interact(self):
        print('You flip to a random page and begin to read ...')
        time.sleep(2)
        print(f'\"{self.excerpt}\"')
        time.sleep(3)
        print('Hmm... a lot to think about.')

# Book instances
odyssey = Book('A book with a blue spine', 'The Odyssey by Homer', '“But the great leveler, Death: not even the gods can defend a man, not even one they love, that day when fate takes hold and lays him out at last.”')
carson = Book('A book with a red spine', 'Autobiography of Red by Anne Carson', 'XIII. HERAKLES\' KILLING CLUB\nLittle red dog did not see it he felt it\nAll events carry but one')
riddle = Book('A book with a black spine', 'A book about Anglo-Saxon riddles.', '...although contentious, most scholars agree the answer to the riddle \'I saw a...(There\'s a stain on the page here.) ...alone is a mirror.')


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
                print('You now have a lit candle in your inventory.\nIt gives off a lovely light.')
            if answer == False:
                return
                