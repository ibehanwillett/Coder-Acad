import items
class Character:
    def __init__(self, name, things):
        self.things = things
        self.inv = items.Inventory([self.things])
    
    def conversation(self):
        print('The ghost says \'No... please don\'t go... I don\'t want you to go...\'')
        print('I\'ll give you the key if you can answer my riddle; I saw a woman sit alone.')
        answer = input('What am I?')
        if answer == 'a mirror' or 'mirror':
            print('That\'s exactly right.')
        else:
            print('The ghost shrieks \'WRONG!\' A red cloud covers the mirror and when it disappates the ghost is gone.')


