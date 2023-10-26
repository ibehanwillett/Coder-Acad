from abc import ABC, abstractmethod
# Items
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def inspect(self):
        print(f'{self.description}')

    @abstractmethod
    def interact(self):
        pass

class Book(Item):
    def __init__(self, name, description, excerpt):
        self.excerpt = excerpt
    def interact():
        print('You flip to a random page and begin to read ...')
        time.sleep(2)
        print(f'{self.excerpt}')
        time.sleep(3)
        print('Hmm... a lot to think about.')