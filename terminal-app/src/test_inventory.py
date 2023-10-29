import characters
import rooms
import items
import pytest

## Transfer Tests

# This function is designed to test charater to charater inventory transfer.
# In particular, it test that an correct answer to the riddle 
# successfully intiates the inventory transfer.
def test_inv_transfer_item(monkeypatch):
    ghosttest = characters.Character('testghost', 'key')
    playertest = characters.Character('testplayer', '')
    monkeypatch.setattr('builtins.input', lambda _: 'mirror')
    ghosttest.conversation(playertest.inv, 'testplayer')
    assert 'key' in playertest.inv.items
# The expected result is the key is in playertest.inv.items

# This function is desgined to test the room to player inventory transfer.

# def test_inv_transfer_item_library():
    roomtest = rooms.Library('testlibrary')
    playertest = characters.Character('testplayer', '')
    roomtest.inv.transfer_item(playertest.inv, items.carson)
    assert items.carson in playertest.inv.items

    # The expected result is carson is in playertest.inv.items

def test_inv_transfer_item_dining():
    roomtest = rooms.Dining('testdining')
    playertest = characters.Character('testplayer', '')
    roomtest.inv.transfer_item(playertest.inv, 'candle')
    assert 'candle' in playertest.inv.items
    # The expected result is that 'candle' is in playertest.inv.items


# Inventory - explicit combination.
# This function tests that the prompt to combine
#  matches and candle automatically runs & successfully combines.
def test_inventory_prompt(monkeypatch):
    test_inventory = items.Inventory(['candle', 'matches'])
    monkeypatch.setattr('builtins.input', lambda _: 'yes')
    test_inventory.view_inventory()
    assert 'lit candle' in test_inventory.items