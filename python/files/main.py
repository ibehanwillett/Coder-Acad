# with open('shopping.txt') as f:
#     shopping_list = []
#     for line in f:
#         shopping_list.append(line.strip())
#         # data = f.read()
#         # shopping_list = data.split('\n')
#         # 

#     print(shopping_list)

# shows = [
#     'The Mandalornian'
#     'The Witcher'
#     'The X-Files'
# ]
# with open('tv-shows.txt', 'w') as f:
#     for i, s in enumerate(shows):
#         f.write(f'{i + 1}. {s}\n')

item = input('What do you need to buy?')
with open('shopping.txt', 'a') as f:
    f.write(f'\n{item}')