import pytest
import rooms

# Door test
entrance_tester = rooms.Entrance('entrance', 'locked', 'statue','library','dining','Test entrance')
def test_entrance_room_door():
    assert entrance_tester.north == 'locked'  
    
# Test Movement
def test_leave():
    print('Where would you like to go?')
    print('Hit the arrows keys to choose a direction or hit q to quit the game.')
    if keyboard.on_press(pynput.keyboard.up): # Up Arrow
        print('You went up')
    if keyboard.on_press(pynput.keyboard.left): # Left Arrow
        print('You went left')
    if keyboard.on_press(pynput.keyboard.right): # Right Arrow
        print('You went right')
    if keyboard.on_press(pynput.keyboard.down): # Down Arror
        print('You went down')
    if keyboard.on_press(pynput.keyboard.esc): # Esc Key
        print('Thanks for playing!')
        quit()