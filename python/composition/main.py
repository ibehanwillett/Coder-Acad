import rpg

aragon = rpg.Character('Aragon', 'Human')
galadriel = rpg.Character('Galadriel', 'Elf')
frodo = rpg.Character('Frodo', 'Hobbit')

frodo.inv.set_currency(10, 5, 0)

chest = rpg.Chest(['longsword', 'iron helm'], 2, 25, 10)

#print(chest.inv.__dict__)
# print(aragon.__dict__)
# print(frodo.__dict__)
# print(galadriel.__dict__)

chest.inv.transfer(frodo.inv)

print(frodo.inv.__dict__)
print(frodo.inv.get_currency())
print(chest.inv.__dict__)