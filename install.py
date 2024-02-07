import os
os.system("clear")

print('''
  _____    __  __  _____  _      __    __  
  \_   \/\ \ \/ _\/__   \/_\    / /   / /  
   / /\/  \/ /\ \   / /\//_\\  / /   / /   
/\/ /_/ /\  / _\ \ / / /  _  \/ /___/ /___ 
\____/\_\ \/  \__/ \/  \_/ \_/\____/\____/                                    
''')

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

os.system("python -m venv venv")
print("source venv/bin/activate")
os.system("chmod +x DDoSAttack.py")
os.system("chmod +x Check.py")
