#!/bin/bash
echo """                                  
         _   _         _   _         
 ___ ___| |_|_|_ _ ___| |_|_|___ ___ 
| .'|  _|  _| | | | .'|  _| | . |   |
|__,|___|_| |_|\_/|__,|_| |_|___|_|_|                                   
"""

python3 -m venv path/to/venv
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
chmod +x *
