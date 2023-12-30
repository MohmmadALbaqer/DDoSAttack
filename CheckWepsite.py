import requests
import os
import sys
import time 
from time import sleep
from colorama import Fore, Style
from termcolor import colored
import random

os.system("clear")

print(f'''{Fore.YELLOW}

_________  /\                   __     __      __                      __  __          
\_   ___ \|  |__   ____   ____ |  | __/  \    /  \ ____ ______   ________|/  |_  ____  
/    \  \/|  |  \_/ __ \_/ ___\|  |/ /\   \/\/   // __ \\____ \ /  ___/  |   __\/ __ \ 
\     \____      \  ___/_  \___|    \  \        /\  ___/_  |_\ \\___ \|  ||  | \  ___/_
 \______  /___|  /\___  /\___  /__|_ \  \__/\  /  \___  /   ___/____  \__||__|  \___  /
        \/     \/     \/     \/     \/       \/       \/|__|        \/              \/ 


{Style.RESET_ALL}''')

def wait_with_spinner(seconds, colors):
    symbols = "/-|\\"

    for _ in range(int(seconds)):
        for symbol in symbols:
            random_color = random.choice(colors)
            colored_symbol = colored(symbol, random_color)
            sys.stdout.write(f"\rPlease wait {colored_symbol}  ")
            sys.stdout.flush()
            time.sleep(0.25)

    sys.stdout.write("\r" + " " * 20 + "\r")

wait_time = 2.5
colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
wait_with_spinner(wait_time, colors)

def check_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code

        if status_code == 200:
            print(f"{Fore.GREEN}Success! Status Code: {status_code} - OK{Style.RESET_ALL}")
        elif status_code == 404:
            print(f"{Fore.RED}Error! Status Code: {status_code} - Not Found{Style.RESET_ALL}")
        elif status_code == 403:
            print(f"{Fore.YELLOW}Error! Status Code: {status_code} - Forbidden{Style.RESET_ALL}")
        elif status_code == 401:
            print(f"{Fore.BLUE}Error! Status Code: {status_code} - Unauthorized{Style.RESET_ALL}")
        elif status_code == 500:
            print(f"{Fore.YELLOW}Error! Status Code: {status_code} - Internal Server Error{Style.RESET_ALL}")
        elif status_code == 301:
            print(f"{Fore.WHITE}Redirect! Status Code: {status_code} - Moved Permanently{Style.RESET_ALL}")
        elif status_code == 307:
            print(f"{Fore.WHITE}Redirect! Status Code: {status_code} - Temporary Redirect{Style.RESET_ALL}")
        else:
            print(f"Unknown Status Code: {status_code}")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

url_to_check = input(f"please {Fore.YELLOW}Enter {Fore.RED}URL {Fore.WHITE}wepsite :{Style.RESET_ALL}")
check_status(url_to_check)



