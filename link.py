# Made by ††#7777 | https://github.com/TT-Tutorials | https://dsc.gg/raided
# You need to have tokens.txt at same folder, at tokens.txt put your own tokens. For token bruteforcer you need to create .txt file named grab.txt
# You need to write to cmd: pip install discord, pip install pyautoui, pip install requests, pip install websocket, pip install emoji, pip install json, pip intall base64, pip install colorama. Without it, the code will not work.
# GANG discord multi tool©


# Copyright (c) 2021 ††#7777

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

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
title = '        ・         GANG Multi Tool            ・           Made by ††#7777'
system(f'title {title}')
tokens = open('tokens.txt', 'r').read().splitlines()


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text


def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }


def secondHeader(token):
    return {
        ':authority': 'discord.com',
        ':method': 'PATCH',
        ':path': '/api/v9/users/@me',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': token,
        'content-length': '124',
        'content-type': 'application/json',
        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        'origin': 'https://canary.discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}


def spammer():
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    clear()

    colorama.init()
    print('')
    print('')
    print(f'                                       {Fore.LIGHTMAGENTA_EX}/$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$')
    print(f'                                      /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$')
    print(f'                                     | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/')
    print(f'                                     | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$')
    print(f'                                     | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$')
    print(f'                                     | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$')
    print(f'                                     |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/')
    print(f'{Fore.WHITE}> Made by ††#7777{Fore.RESET}                     {Fore.LIGHTMAGENTA_EX}\______/ |__/  |__/|__/  \__/ \______/')
    print(f'{Fore.WHITE}> https://github.com/TT-Tutorials{Fore.RESET}') 
    print(f'{Fore.LIGHTMAGENTA_EX}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Spammer         {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[9]{Fore.RESET} About/Activity     {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[17]{Fore.RESET} MassReport{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} DM Spammer      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[10]{Fore.RESET} Joiner            {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[18]{Fore.RESET} Server Nuker{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[3]{Fore.RESET} Friend Spammer  {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[11]{Fore.RESET} Leaver            {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[19]{Fore.RESET} Account Nuker{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[4]{Fore.RESET} Reaction Spam   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[12]{Fore.RESET} TokenChecker      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[20]{Fore.RESET} Token Bruteforcer{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[5]{Fore.RESET} WebhookSpammer  {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[13]{Fore.RESET} Token Onliner     {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[21]{Fore.RESET} Token Grabber{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[6]{Fore.RESET} Typing Spammer  {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[14]{Fore.RESET} HypeSquad Joiner  {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[22]{Fore.RESET} Group Spammer{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[7]{Fore.RESET} VC Spammer      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[15]{Fore.RESET} NickName Changer  {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[23]{Fore.RESET} About {Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[8]{Fore.RESET} Mass DM         {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[16]{Fore.RESET} Status Changer    {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[24]{Fore.RESET} {Fore.LIGHTRED_EX}Exit{Fore.RESET} {Fore.RESET}')

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



