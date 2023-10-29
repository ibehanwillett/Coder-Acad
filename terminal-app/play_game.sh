#!/bin/bash

if ! [[ -x "$(command -v pip3)" ]]
then
  echo 'Uh oh!
    it looks like pip3 is not installed.
    To install pip3, please go to https://pypi.org/project/pip/' >&2
  exit 1
fi
cd ./src;
echo 'Thank you for playing Haunted House!'
source .venv/bin/activate
echo "Installing the game now..."
pip3 install -r requirements.txt 
echo 'All done! Have fun! :)'
python3 main.py
deactivate