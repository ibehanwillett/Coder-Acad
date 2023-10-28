import pytest
import rooms

# Door test
entrance_tester = rooms.Entrance('entrance')
def test_entrance_room_door():
    assert entrance_tester.doors.north == 'locked'  
    
