from rooms import entrance, library, entrance_door, library_door

# GENERAL SCRIPT
howto_move = print('To move to another room, input the direction you want to move)')





def whereto():
    direction = str(input("What direction would you like to go?  "))
    return direction


#START OF GAME
print('You wake in a spooky scary house! Uh oh!')
print('You try and open the door behind you...')

position = entrance
while True:
    if position == entrance:
        entrance.description()
        move_choice = whereto()
        if move_choice == 'east':
            library_door.move()
            position = library
        else:
            print('I have\'t coded that yet, sorry!')
    if position == library:
        library.description()
        move_choice = whereto()
    if position == study:
        pass
    if position == statue:
        pass
    if position == kitchen:
        pass
    if postion == dining:
        pass
    if position == bedroom:
        pass


    
    


    

