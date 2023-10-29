import pytest
import rooms
import characters
import doors


# Door test
entrance_tester = rooms.Entrance('entrance')
statue_tester = rooms.Statue('statue')
playertest = characters.Character('testplayer', '')
def test_entrance_room_door():
    assert entrance_tester.doors.north == 'locked'  
    
# Test regarding a the correct string is returned after user 
# input. This is the fundamental function the movement feature is
# based on.
def test_where_from_entrance(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'west')
    result = entrance_tester.doors.leave(playertest.inv)
    assert result == 'dining'

# The expected result is that result will equal 'dining'

def test_where_from_statue(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'east')
    result = statue_tester.doors.leave(playertest.inv)
    assert result == 'study'

# The expected result is that result will equal  'study'.