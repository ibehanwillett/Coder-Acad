import general
import pytest

# Testing Yes or No input for yes
def test_yes_no_input_for_yes(monkeypatch):
    # Monkey patch stimulating a 'yes' input
    monkeypatch.setattr('builtins.input', lambda _: 'yes')
    answer = general.get_a_yes_no('Yes or no?')
    assert answer == True

def test_yes_no_input_for_no(monkeypatch):
    # Monkey patch stimulating a 'yes' input
    monkeypatch.setattr('builtins.input', lambda _: 'no')
    answer = general.get_a_yes_no('Yes or no?')
    assert answer == False
