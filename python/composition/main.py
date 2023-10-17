import rpg

aragon = rpg.Ranger('Aragon', 'Human', 100, 50)
galadriel = rpg.Mage('Galadriel', 'Elf', 120, 75)
frodo = rpg.Burglar('Frodo', 'Hobbit', 50, 25)
saruman = rpg.Wizard('Saruman', 'Human', 80, 100)

frodo.inv.set_currency(10, 5, 0)

chest = rpg.Chest(['longsword', 'iron helm'], 2, 25, 10)

saruman.battle(aragon)
galadriel.battle(aragon)

print(galadriel.__dict__)
#print(chest.inv.__dict__)
# print(aragon.__dict__)
# print(frodo.__dict__)
# print(galadriel.__dict__)


# Frodo loots a chest!
# chest.inv.transfer(frodo.inv)

# print(frodo.inv.__dict__)
# print(frodo.inv.get_currency())
# print(chest.inv.__dict__)