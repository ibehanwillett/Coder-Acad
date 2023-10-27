import pynput
from pynput import Key, Listener



def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
# Test Movement
# def test_leave():

#     print('Where would you like to go?')
#     print('Hit the arrows keys to choose a direction or hit q to quit the game.')
#     on_press(up) # Up Arrow
#     print('You went up')
#     keyboard.on_press(Key.left) # Left Arrow
#     print('You went left')
#     keyboard.on_press(Key.right) # Right Arrow
#     print('You went right')
#     keyboard.on_press(Key.down) # Down Arror
#     print('You went down')
#     keyboard.on_press(Key.esc) # Esc Key
#     print('Thanks for playing!')
#     quit()

listener = keyboard.Listener(
    on_press = on_press,
    on_release = on_release)
listener.start()