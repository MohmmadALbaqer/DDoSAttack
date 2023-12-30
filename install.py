import os
import pyfiglet
import random
from termcolor import colored
os.system("clear")

colors = ['red', 'green', 'yellow', 'blue']

selected_color = random.choice(colors)

text = 'Install'

lo = pyfiglet.figlet_format(text)
colored_lo = colored(lo, color=selected_color)

print(colored_lo)

libraries_to_install = [
    "cfscrape",
    "httpx",
    "asyncio",
    "pysocks",
    "socket",
    "Thread",
    "Style",
    "Fore",
    "colored",
    "pyfiglet",
    "requests",
    "os",
    "sys"
]

for library in libraries_to_install:
    os.system(f"pip install {library}")
    
