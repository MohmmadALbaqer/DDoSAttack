import requests
import os
from time import sleep
from colorama import Fore, Style, Back, init
from termcolor import colored
os.system("clear")

init()

R = f"\033[91;1m"  # Red
G = f"\033[92;1m"  # Green
B = f"\033[94;1m"  # Blue
Y = f"\033[93;1m"  # Yellow
C = f"\033[96;1m"  # Cyan
M = f"\033[95;1m"  # Magenta
W = f"\033[97;1m"  # White

sign = f"{G}[{B}*{G}]{W}"
ERROR = f"{Y}[{R}!{Y}]{R}"
INFO = f'{B}[{G}INFO{B}]'

print(fr'''{Y}
   ________              __  _       __                _ __     
  / ____/ /_  ___  _____/ /_| |     / /__  ____  _____(_) /____ 
 / /   / __ \/ _ \/ ___/ //_/ | /| / / _ \/ __ \/ ___/ / __/ _ \
/ /___/ / / /  __/ /__/ ,<  | |/ |/ /  __/ /_/ (__  ) / /_/  __/
\____/_/ /_/\___/\___/_/|_| |__/|__/\___/ .___/____/_/\__/\___/ 
                                       /_/                      
{W}''')

print(f"{Back.RED} It checks the status of the website whether it is available or not {Style.RESET_ALL}")
print(1*"\n")
def check_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code

        if status_code == 200:
            print(f"{INFO} Good website condition: {status_code} - OK{Style.RESET_ALL}")
        elif status_code == 404:
            print(f"{R}Error! Status Code: {status_code} - Not Found{Style.RESET_ALL}")
        elif status_code == 403:
            print(f"{Y}Error! Status Code: {status_code} - Forbidden{Style.RESET_ALL}")
        elif status_code == 401:
            print(f"{B}Error! Status Code: {status_code} - Unauthorized{Style.RESET_ALL}")
        elif status_code == 500:
            print(f"{Y}Error! Status Code: {status_code} - Internal Server Error{Style.RESET_ALL}")
        elif status_code == 301:
            print(f"{M}Redirect! Status Code: {status_code} - Moved Permanently{Style.RESET_ALL}")
        elif status_code == 307:
            print(f"{C}Redirect! Status Code: {status_code} - Temporary Redirect{Style.RESET_ALL}")
        else:
            print(f"{Y}[{R}!{Y}] Unknown Status Code:{W} {status_code}")

    except requests.exceptions.RequestException as e:
        print(f"{ERROR}: {e}{W}")

url_to_check = input(f"{sign} please Enter URL wepsite: {Y}")
check_status(url_to_check)
