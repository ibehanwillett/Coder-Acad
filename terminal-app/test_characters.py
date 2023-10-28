import characters
import pytest

def test_inv_transfer_item(monkeypatch):
    ghosttest = characters.Character('testghost', 'key')
    playertest = characters.Character('testplayer', '')
    monkeypatch.setattr('builtins.input', lambda _: 'mirror')
    ghosttest.conversation (playertest.inv, 'testplayer')
    assert 'key' in playertest.inv.items