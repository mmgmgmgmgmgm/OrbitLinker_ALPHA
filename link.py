
import os
from os import system

try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    from requests import get
except:
    os.system("pip install requests")
    from requests import get

import threading

try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama

try:
    import discord
except:
    os.system("pip install discord")
    import discord

from discord.ext import commands

try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui

import time
import re

try:
    import http.client
except:
    os.system('pip install python-http-client')
    import http.client

import random

try:
    import json
except:
    os.system('pip install json')
    import json


try:
    import base64
except:
    os.system('pip install base64')
    import base64

import string
import sys
from colorama import Fore

try:
    import emoji as ej
except:
    os.system('pip install emoji')
    import emoji as ej

try:
    import websocket
except:
    os.system('pip install websocket')
    import websocket

try:
    import asyncio
except:
    os.system('pip install asyncio')
    import asyncio

try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install beautifulsoup4')

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    os.system('pip install webdriver-manager')
    from webdriver_manager.chrome import ChromeDriverManager

try:
    from PIL import Image
except:
    os.system('pip install pillow')
    from PIL import Image

try:
    import discum
except:
    os.system('pip install discum')
    import discum

try:
    from selenium import webdriver
except:
    os.system('pip install selenium')
    from selenium import webdriver

ur = 'https://discord.com/api/v9/channels/messages'
title = '        ・         Orbit Multi Tool            ・           Made by Ishaan
system(f'title {title}')
tokens = open('tokens.txt', 'r').read().splitlines()


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def spammer():
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    clear()

    colorama.init()
    print('')
    print('')
    print(f'                                       {Fore.LIGHTMAGENTA_EX} $$$$$$\  $$\           $$\                  ')
    print(f'                                       $$  __$$\ $$ |          $$ |                
    print(f'                                       $$ /  $$ |$$ | $$$$$$\  $$$$$$$\   $$$$$$\ 
    print(f'                                       $$$$$$$$ |$$ |$$  __$$\ $$  __$$\  \____$$\ 
    print(f'                                       $$  __$$ |$$ |$$ /  $$ |$$ |  $$ | $$$$$$$ |
    print(f'                                       $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$  __$$ |
    print(f'                                       $$ |  $$ |$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$ |
    print(f'{Fore.WHITE}> Made by Ishaan{Fore.RESET} {Fore.LIGHTMAGENTA_EX}'\__|  \__|\__|$$  ____/ \__|  \__| \_______|
              $$ |                          
              $$ |                          
              \__|   )
    print(f'{Fore.WHITE}> WIP{Fore.RESET}') 
    print(f'{Fore.LIGHTMAGENTA_EX}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} DO NOT USE       {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[9]{Fore.RESET} DO NOT USE     {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[17]{Fore.RESET} DO NOT USE{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} DO NOT USE      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[10]{Fore.RESET} DO NOT USE     {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[18]{Fore.RESET} DO NOT USE{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[3]{Fore.RESET} DO NOT USE      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[11]{Fore.RESET} DO NOT USE     {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[19]{Fore.RESET} DO NOT USE{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[4]{Fore.RESET} DO NOT USE      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[12]{Fore.RESET} DO NOT USE     {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[20]{Fore.RESET} DO NOT USE{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[5]{Fore.RESET} DO NOT USE      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[13]{Fore.RESET} DO NOT USE     {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[21]{Fore.RESET} DO NOT USE{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[6]{Fore.RESET} DO NOT USE      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[14]{Fore.RESET} DO NOT USE     {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[22]{Fore.RESET} DO NOT USE{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[7]{Fore.RESET} DO NOT USE      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[15]{Fore.RESET} DO NOT USE     {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[23]{Fore.RESET} About {Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[8]{Fore.RESET} DO NOT USE      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[16]{Fore.RESET} DO NOT USE     {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[24]{Fore.RESET} {Fore.LIGHTRED_EX}Exit{Fore.RESET} {Fore.RESET}')

    print(f'{Fore.LIGHTMAGENTA_EX}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
    choice = input('[(Currently only 23 works)>>>]')

    if choice == '23':
        print(f'''{Fore.WHITE} Hello, just a quick message talking about this nuker!
- This "GANG Multi Tool was created / dev by Ishaan
- This is a work in progress
- 12 years old and mainly code with python
- Thanks for using my tool!
- if you enjoy this make sure to star it and follow my github!
{Fore.RESET}''')


        exit = input('press any key: ')
        exit = clear()
        exit = spammer()


    if choice == '24':
        os.system('exit')



