import pytest
import items
# Testing that the prompt to combine matches and candle automatically runs & successfully combines.


def test_inventory_prompt(monkeypatch):
    test_inventory = items.Inventory(['candle', 'matches'])
    monkeypatch.setattr('builtins.input', lambda _: 'yes')
    test_inventory.view_inventory()
    assert 'lit candle' in test_inventory.items
