#####################################################
## Aura Generator                                  ##
## Çok Seksi Hediye Kartı Üretici                  ##
## discord.gg/ssex                                 ##
## Kodlayan = AuraEdit#1447                        ##
#####################################################


# Importlar
import json
import time
import pyfade
import random
from colorama import Fore, Style, init
import os
import requests
import discord
from datetime import datetime
import subprocess
import sys

# Global Değişkenler
now = datetime.now()
curtime = now.strftime("%H:%M")
author = "AuraEdit#1447"

# Tanımlar
def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')
def back():
    input(f"{Fore.YELLOW}Geri Dönmek İçin ENTER Tuşuna Basın")
def underdev():
    print(f"{Fore.RED}{curtime}{Fore.LIGHTWHITE_EX} Bu Proje Şu Anda Geliştirilme Aşamasındadır")
    back()
    clearcmd()
def options():
    print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red, """
   
  /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$ /$$   /$$
 /$$__  $$| $$  | $$| $$__  $$ /$$__  $$ /$$__  $$| $$_____/| $$$ | $$
| $$  \ $$| $$  | $$| $$  \ $$| $$  \ $$| $$  \__/| $$      | $$$$| $$
| $$$$$$$$| $$  | $$| $$$$$$$/| $$$$$$$$| $$ /$$$$| $$$$$   | $$ $$ $$
| $$__  $$| $$  | $$| $$__  $$| $$__  $$| $$|_  $$| $$__/   | $$  $$$$
| $$  | $$| $$  | $$| $$  \ $$| $$  | $$| $$  \ $$| $$      | $$\  $$$
| $$  | $$|  $$$$$$/| $$  | $$| $$  | $$|  $$$$$$/| $$$$$$$$| $$ \  $$
|__/  |__/ \______/ |__/  |__/|__/  |__/ \______/ |________/|__/  \__/                        
                                                                          """))
    print(f'''{Fore.LIGHTWHITE_EX}                    [Yapımcı {Fore.YELLOW}AuraEdit#1447 {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print("""
    [1] Üreticiler
    [2] Yakında

    [3] Ayarlar
    [4] Çık
    
    
    """)
    USER_OPTION = input(f"Seçenek\n{Fore.RED}>")
    if USER_OPTION == "1":
        clearcmd()
        generators()
    elif USER_OPTION == "2":
        pass
    elif USER_OPTION == "3":
        pass
    elif USER_OPTION == "4":
        clearcmd()
        quit()
    else:
        print(f"\n{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Girdiğiniz Seçeneği Fark Etmedi {Fore.YELLOW}{USER_OPTION}{Fore.LIGHTWHITE_EX}, Tekrar Deneyin")
        time.sleep(1)
        back()
        clearcmd()
        options()

def generators():
    print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red, """
   
  /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$ /$$   /$$
 /$$__  $$| $$  | $$| $$__  $$ /$$__  $$ /$$__  $$| $$_____/| $$$ | $$
| $$  \ $$| $$  | $$| $$  \ $$| $$  \ $$| $$  \__/| $$      | $$$$| $$
| $$$$$$$$| $$  | $$| $$$$$$$/| $$$$$$$$| $$ /$$$$| $$$$$   | $$ $$ $$
| $$__  $$| $$  | $$| $$__  $$| $$__  $$| $$|_  $$| $$__/   | $$  $$$$
| $$  | $$| $$  | $$| $$  \ $$| $$  | $$| $$  \ $$| $$      | $$\  $$$
| $$  | $$|  $$$$$$/| $$  | $$| $$  | $$|  $$$$$$/| $$$$$$$$| $$ \  $$
|__/  |__/ \______/ |__/  |__/|__/  |__/ \______/ |________/|__/  \__/                        
                                                                          """))
    print(f'''{Fore.LIGHTWHITE_EX}                    [Yapımcı {Fore.YELLOW}AuraEdit#1447 {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print("""
    [1] Amazon Hediye Kartı Üretici
    [2] Netflix Hediye Kartı Üretici
    [3] Roblox Hediye Kartı Üretici
    [4] Apple Hediye Kartı Üretici
    [5] Steam Hediye Kartı Üretici
    [6] Google Play Hediye Kartı Üretici
    [7] Spotfiy Hediye Kartı Üretici

    [8] Bilgi
    [9] Geri
    
    
    """)
    USER_OPTION = input(f"Seçenek\n{Fore.RED}>")
    if USER_OPTION == "1":
        clearcmd()
        amazon()
    elif USER_OPTION == "2":
        netflix()
        generators()
    elif USER_OPTION == "3":
        clearcmd()
        roblox()
    elif USER_OPTION == "4":
        clearcmd()
        apple()
    elif USER_OPTION == "5":
        clearcmd()
        steam()
    elif USER_OPTION == "6":
        clearcmd()
        googleplay()
    elif USER_OPTION == "7":
        clearcmd()
        spotify()
    elif USER_OPTION == "8":
        underdev()
        generators()
    elif USER_OPTION == "9":
        clearcmd()
        options()
    else:
        print(f"\n{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Girdiğiniz Seçeneği Fark Etmedi {Fore.YELLOW}{USER_OPTION}{Fore.LIGHTWHITE_EX}, Tekrar Deneyin")
        time.sleep(1)
        back()
        clearcmd()
        generators()

def amazon():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red,"""
     
     █████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗ ███╗   ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║    ██╔════╝ ██╔════╝████╗  ██║
    ███████║██╔████╔██║███████║  ███╔╝ ██║   ██║██╔██╗ ██║    ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║   ██║██║╚██╗██║    ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                   
    """))
    print(f'''{Fore.LIGHTWHITE_EX}                    [Yapımcı {Fore.YELLOW}AuraEdit#1447 {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print(f"{Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Kuruluyor...")
    time.sleep(1)
    print(f"\nAmazon Hediye Kartı Formatı: {Fore.YELLOW}XXXX-XXXXXX-XXXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.BLUE}[?] Kaç Tane Oluşturmak İstiyorsunuz, Bu Önceki Hediye Kartlarını Kaldıracaktır: ")

    with open("./generated/amazon.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(6)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(5)))

            result = firstrandom + "-" + secondrandom + "-" + thirdrandom 
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Üretiliyor...")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Hediye Kartları {Fore.YELLOW}{howmany}{Fore.LIGHTWHITE_EX} Başarıyla Üretildi ./generated/amazon.txt")
    back()
    clearcmd()
    generators()
def netflix():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red,"""
     
    ███╗   ██╗███████╗████████╗███████╗██╗     ██╗██╗  ██╗     ██████╗ ███████╗███╗   ██╗
    ████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║     ██║╚██╗██╔╝    ██╔════╝ ██╔════╝████╗  ██║
    ██╔██╗ ██║█████╗     ██║   █████╗  ██║     ██║ ╚███╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
    ██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██║     ██║ ██╔██╗     ██║   ██║██╔══╝  ██║╚██╗██║
    ██║ ╚████║███████╗   ██║   ██║     ███████╗██║██╔╝ ██╗    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝     ╚══════╝╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                            
    """))
    print(f'''{Fore.LIGHTWHITE_EX}                    [Yapımcı {Fore.YELLOW}AuraEdit#1447 {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print(f"{Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Kuruluyor...")
    time.sleep(1)
    print(f"\nNetflix Hediye Kartı Formatı: {Fore.YELLOW}XXXX-XXXXXX-XXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.BLUE}[?] Kaç Tane Oluşturmak İstiyorsunuz, Bu Önceki Hediye Kartlarını Kaldıracaktır: ")

    with open("./generated/netflix.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(6)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))

            result = firstrandom + "-" + secondrandom + "-" + thirdrandom 
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Üretiliyor...")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Hediye Kartları {Fore.YELLOW}{howmany}{Fore.LIGHTWHITE_EX} Başarıyla Üretildi ./generated/netflix.txt")
    back()
    clearcmd()
    generators()
def roblox():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red,"""

    ██████╗  ██████╗ ██████╗ ██╗      ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗██╔═══██╗██╔══██╗██║     ██╔═══██╗╚██╗██╔╝    ██╔════╝ ██╔════╝████╗  ██║       
    ██████╔╝██║   ██║██████╔╝██║     ██║   ██║ ╚███╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██╗██║   ██║██╔══██╗██║     ██║   ██║ ██╔██╗     ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║╚██████╔╝██████╔╝███████╗╚██████╔╝██╔╝ ██╗    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                       
    """))
    print(f'''{Fore.LIGHTWHITE_EX}                    [Yapımcı {Fore.YELLOW}AuraEdit#1447 {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print(f"{Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Kuruluyor...")
    time.sleep(1)
    print(f"\nRoblox Hediye Kartı Formatı: {Fore.YELLOW}XXXX-XXXX-XXXX-XXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.BLUE}[?] Kaç Tane Oluşturmak İstiyorsunuz, Bu Önceki Hediye Kartlarını Kaldıracaktır: ")

    with open("./generated/roblox.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            fourthrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))

            result = firstrandom + "-" + secondrandom + "-" + thirdrandom + "-" + fourthrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Üretiliyor...")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Hediye Kartları {Fore.YELLOW}{howmany}{Fore.LIGHTWHITE_EX} Başarıyla Üretildi ./generated/roblox.txt")
    back()
    clearcmd()
    generators()

def apple():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red,"""

     █████╗ ██████╗ ██████╗ ██╗     ███████╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
    ███████║██████╔╝██████╔╝██║     █████╗      ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██║██╔═══╝ ██╔═══╝ ██║     ██╔══╝      ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║██║     ██║     ███████╗███████╗    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                                   
    """))
    print(f'''{Fore.LIGHTWHITE_EX}                    [Yapımcı {Fore.YELLOW}AuraEdit#1447 {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print(f"{Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Kuruluyor")
    time.sleep(1)
    print(f"\nApple Hediye Kartı Formatı: {Fore.YELLOW}XXXXXXXXXXXXXXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.BLUE}[?] Kaç Tane Oluşturmak İstiyorsunuz, Bu Önceki Hediye Kartlarını Kaldıracaktır: ")

    with open("./generated/apple.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Üretiliyor...")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Hediye Kartları {Fore.YELLOW}{howmany}{Fore.LIGHTWHITE_EX} Başarıyla Üretildi ./generated/apple.txt")
    back()
    clearcmd()
    generators()

def steam():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red,"""

    ███████╗████████╗███████╗ █████╗ ███╗   ███╗     ██████╗ ███████╗███╗   ██╗
    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║    ██╔════╝ ██╔════╝████╗  ██║
    ███████╗   ██║   █████╗  ███████║██╔████╔██║    ██║  ███╗█████╗  ██╔██╗ ██║
    ╚════██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║    ██║   ██║██╔══╝  ██║╚██╗██║
    ███████║   ██║   ███████╗██║  ██║██║ ╚═╝ ██║    ╚██████╔╝███████╗██║ ╚████║
    ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                                                                                               
    """))
    print(f'''{Fore.LIGHTWHITE_EX}                    [Yapımcı {Fore.YELLOW}AuraEdit#1447 {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print(f"{Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Kuruluyor...")
    time.sleep(1)
    print(f"\nSteam Hediye Kartı Üretildi: {Fore.YELLOW}XXXXX-XXXXX-XXXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.BLUE}[?] Kaç Tane Oluşturmak İstiyorsunuz, Bu Önceki Hediye Kartlarını Kaldıracaktır: ")

    with open("./generated/steam.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Üretiliyor..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Hediye Kartları {Fore.YELLOW}{howmany}{Fore.LIGHTWHITE_EX} Başarıyla Üretildi ./generated/steam.txt")
    back()
    clearcmd()
    generators()

def googleplay():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red,"""

     ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ███████╗    ██████╗      ██████╗ ███████╗███╗   ██╗
    ██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝ ██║     ██╔════╝    ██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║
    ██║  ███╗██║   ██║██║   ██║██║  ███╗██║     █████╗█████╗██████╔╝    ██║  ███╗█████╗  ██╔██╗ ██║
    ██║   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝╚════╝██╔═══╝     ██║   ██║██╔══╝  ██║╚██╗██║
    ╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗    ██║         ╚██████╔╝███████╗██║ ╚████║                                                                                                                                                                                                                                                                                                                                                                                                                                       
    """))
    print(f'''{Fore.LIGHTWHITE_EX}                    [Yapımcı {Fore.YELLOW}AuraEdit#1447 {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print(f"{Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Kuruluyor...")
    time.sleep(1)
    print(f"\nGoogle Play Hediye Kartı Formatı: {Fore.YELLOW}XXXXXXXXXXXXXXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.BLUE}[?] Kaç Tane Oluşturmak İstiyorsunuz, Bu Önceki Hediye Kartlarını Kaldıracaktır: ")

    with open("./generated/googleplay.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Üretiliyor...")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Hediye Kartları {Fore.YELLOW}{howmany}{Fore.LIGHTWHITE_EX} Başarıyla Üretildi ./generated/googleplay.txt")
    back()
    clearcmd()
    generators()

def spotify():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red,"""
     
    ███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║
    ███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
    ╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝      ██║   ██║██╔══╝  ██║╚██╗██║
    ███████║██║     ╚██████╔╝   ██║   ██║██║        ██║       ╚██████╔╝███████╗██║ ╚████║
    ╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    """))
    print(f'''{Fore.LIGHTWHITE_EX}                    [Yapımcı {Fore.YELLOW}AuraEdit#1447 {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print(f"{Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Kuruluyor...")
    time.sleep(1)
    print(f"\Spotify Hediye Kartı Formatı: {Fore.YELLOW}XXXX-XXXX-XXXX-XXXX-XXXX-XX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.BLUE}[?] Kaç Tane Oluşturmak İstiyorsunuz, Bu Önceki Hediye Kartlarını Kaldıracaktır: ")

    with open("./generated/spotify.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Üretiliyor...")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Hediye Kartları {Fore.YELLOW}{howmany}{Fore.LIGHTWHITE_EX} Başarıyla Üretildi ./generated/spotfiy.txt")
    back()
    clearcmd()
    generators()



# Main Code
def main():
    try:
        clearcmd()
        options()
    except KeyboardInterrupt:
        print(f"{Fore.RED}{curtime} CTRL + C Algılandı, Ana Menüye Geri Dönülüyor!")
        time.sleep(1)
        options()

main()
