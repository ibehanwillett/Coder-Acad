class Character:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.copper = 0
        self.inv = Inventory([], 0, 0, 0)
    



class Inventory:
    def __init__(self, items, gold, silver, copper):
        self.items = items
        self.set_currency(gold,silver,copper) # Delegation

        #Setter- sets one or more attributes
    def set_currency(self, gold, silver, copper):
            self.copper = gold * 10000 + silver * 100 + copper

    def transfer(self, to_inv):
        #Add all the items from from_inv to to_inv
        to_inv.items.extend(self.items)
        #Delete all the items from from_inv
        self.items = []
        # Add the currency from the from_inv to to_inv
        to_inv.copper += self.copper
        self.copper = 0


    # Getter- gets information out of the object
    def get_currency(self):
        gold = self.copper // 10000
        silver = (self.copper % 10000) // 100
        copper = self.copper % 100
        return gold, silver, copper


# chest object must own/ have an instance of inventory object. COMPOSITIONAL relationship.
# order in this case doesn't matter- chest doesn't need to know what an inventory is until a chest is called in the main py file, which will have imported this entire module at that point. 
class Chest:
    def __init__(self, items, gold, silver, copper):
        self.inv = Inventory(items, gold, silver, copper) # contains an instance of another class