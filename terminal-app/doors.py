import general
import time

class Doors:
    def __init__(cls, north, south, east, west):
        cls.north = north
        cls.south = south
        cls.east = east
        cls.west = west
 
    def leave(cls, player_inventory):
        def where_from(cls, player_inventory):
            while True:
                print(f'To the north, {cls.north}.')
                print(f'To the south, {cls.south}.')
                print(f'To the east, {cls.east}')
                print(f'To the west, {cls.west}')
                print('Type the direction you\'d like to go,' \
                ' or inv to check your inventory.')
                direction = input('Where would like to go?  ')
                general.quitcheck(direction)
                match direction:
                    case 'north':
                        return cls.north
                    case 'south':
                        return cls.west
                    case 'east':
                        return cls.east
                    case 'west':
                        return cls.west
                    case 'inv':
                        player_inventory.view_inventory()
                        time.sleep(1)
                        continue
                    case _:
                        print('Sorry, I didn\'t understand.')
                        continue
        
        while True:
            where = where_from(cls, player_inventory)
            if where == 'locked':
                print('It\'s locked.')
                if 'key' in player_inventory.items:
                    print('The key slides into the locked door!')
                    general.win_condition_met()
                else:
                    continue
            elif where == 'wall':
                print('There\'s no door here!')
                continue
            else:
                return (f'{where}')

   
