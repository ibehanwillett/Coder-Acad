import pytest
import rooms

# Door test
entrance_tester = rooms.Entrance('entrance', 'locked', 'statue','library','dining','Test entrance')
def entrance_room_door_test():
    assert entrance_tester.north == 'locked'  
    
