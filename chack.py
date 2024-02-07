import requests
import os
from time import sleep
from colorama import Fore, Style, Back
from termcolor import colored
os.system("clear")

print(f'''{Fore.YELLOW}
   ________              __  _       __                _ __     
  / ____/ /_  ___  _____/ /_| |     / /__  ____  _____(_) /____ 
 / /   / __ \/ _ \/ ___/ //_/ | /| / / _ \/ __ \/ ___/ / __/ _ \\
/ /___/ / / /  __/ /__/ ,<  | |/ |/ /  __/ /_/ (__  ) / /_/  __/
\____/_/ /_/\___/\___/_/|_| |__/|__/\___/ .___/____/_/\__/\___/ 
                                       /_/                      
{Style.RESET_ALL}''')

print(f"{Back.RED} It checks the status of the website whether it is available or not {Style.RESET_ALL}")
print(1*"\n")
def check_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code

        if status_code == 200:
            print(f"{Fore.WHITE}[{Fore.GREEN}INFO{Fore.WHITE}] {Fore.BLUE}Good website condition: {status_code} - OK{Style.RESET_ALL}")
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
            print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] Unknown Status Code:{Style.RESET_ALL} {status_code}")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.YELLOW}[{Fore.RED}Error{Fore.YELLOW}]: {e}{Style.RESET_ALL}")

url_to_check = input(f"{Fore.GREEN}[+] {Fore.BLUE}please Enter URL wepsite: {Fore.YELLOW}")
check_status(url_to_check)
