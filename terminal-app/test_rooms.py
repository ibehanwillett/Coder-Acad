import pytest
import rooms

# Door test
entrance_tester = rooms.Entrance('entrance', 'locked', 'statue','library','dining','Test entrance')
def test_entrance_room_door():
    assert entrance_tester.north == 'locked'  
    
