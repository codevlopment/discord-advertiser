from lib2to3.pgen2 import token
import requests, threading, os, random, time
from colored import fg, attr
import colorama 
import sys
import ctypes
import subprocess
import json
import time
import datetime
from colorama import Fore, init
from capmonster_python import RecaptchaV2Task

# ===============================================================
# cmd, coded by craigslol#0001

cfg = json.load(open("config.json", "r"))
ctypes.windll.kernel32.SetConsoleTitleW("    Discord Auto Advertiser V.2 | co#2000")

# ===============================================================
# auth, coded by craigslol#0001



# ===============================================================
# config values, coded by craigslol#0001

delay = 60*60 # In seconds
messages = []
tokens = []
count = 0

init(convert=True)

messages = open('messages.txt', encoding='utf-8').read().splitlines()

def timecurrent():
    return datetime.datetime.utcnow().strftime('%H:%M:%S')

# ===============================================================
# menu, coded by craigslol#0001


menu = f"""{Fore.WHITE}                                  
    [{timecurrent()}{Fore.RESET}] [{Fore.CYAN}INFO{Fore.RESET}] || [{Fore.RED}!{Fore.RESET}] {Fore.CYAN}SERVERS LOADED - {len(cfg.keys())}{Fore.RESET}
    [{timecurrent()}{Fore.RESET}] [{Fore.CYAN}INFO{Fore.RESET}] || [{Fore.RED}!{Fore.RESET}] {Fore.CYAN}DELAY LOADED - {str(delay)}s{Fore.RESET}
"""


os.system('cls')
print(menu)

# ===============================================================
# end, coded by craigslol#0001

if __name__ == '__main__':
    print(f"    [{timecurrent()}{Fore.RESET}] [{Fore.CYAN}INFO{Fore.RESET}] || [{Fore.RED}!{Fore.RESET}] {Fore.CYAN}READING MESSAGES.TXT{Fore.RESET}")
    time.sleep(1)
    print(f"    [{timecurrent()}{Fore.RESET}] [{Fore.CYAN}INFO{Fore.RESET}] || [{Fore.RED}!{Fore.RESET}] {Fore.CYAN}STARTING {len(cfg.keys())} SERVERS{Fore.RESET}\n")
    with open('messages.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        messages.append(line.replace('\n', ''))
    while True:

        for channel in cfg:
                message_num = random.choice(messages)
                message_send = requests.post(f'https://discord.com/api/v9/channels/{channel}/messages',
                    headers={
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Accept-Language": "ko",
                        "Authorization": cfg[channel],
                        "Content-Type": "application/json",
                        "origin": "https://discord.com",
                        #"referer": f"https://discord.com/channels/{serverids}/{channel}",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "",
                        "x-debug-options": "bugReporterEnabled",
                        "x-discord-locale": "en-US",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC40MyIsIm9zX3ZlcnNpb24iOiIxMC4wLjE5MDQ0Iiwib3NfYXJjaCI6Ing2NCIsInN5c3RlbV9sb2NhbGUiOiJrbyIsImNsaWVudF9idWlsZF9udW1iZXIiOjExMjY3MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                    }, data=json.dumps({
                    "content": message_num,
                    "nonce": random.randint(9999999999, 999999999999),
                    "tts": False
                    }))

                print(f"    [{timecurrent()}{Fore.RESET}] [{Fore.CYAN}DEBUG{Fore.RESET}] || [{Fore.GREEN}+{Fore.RESET}] {Fore.CYAN}MESSAGE SENT{Fore.RESET}")
        print(f"\n    [{timecurrent()}{Fore.RESET}] [{Fore.CYAN}INFO{Fore.RESET}] || [{Fore.YELLOW}!{Fore.RESET}] {Fore.CYAN}ALL {len(cfg.keys())} SERVERS HAVE BEEN MESSAGED, WAITING {str(delay)}S{Fore.RESET}")
        time.sleep(delay)

