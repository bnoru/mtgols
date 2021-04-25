from random import random
from os import system
import os

os.system("")

# Group of ***different*** functions for different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

winrates = [0.55, 0.56, 0.57, 0.58, 0.59, 0.60, 0.61, 0.62, 0.63, 0.64, 0.65]
matches = input("How many matches to simulate? ")
matches = int(matches)
system('cls')
print("")
print("Matches played in each method:", matches)
print("")
print("Dropping at 0-4 only:")
print("")
print(style.GREEN + "WR     Balance    EV      Leagues" + style.RESET)

for winrate in winrates:
    wins = 0
    losses = 0
    saldo = 1000
    ligas = 0
    for x in range(matches):
        if saldo >= 100:
            result = random()
            if result <= winrate:
                wins = wins+1
                if wins+losses == 5:
                    if wins == 0 or wins == 1:
                        saldo = saldo-100
                    elif wins == 2:
                        saldo = saldo-50
                    elif wins == 3:
                        saldo = saldo+23
                    elif wins == 4:
                        saldo = saldo+135
                    elif wins == 5:
                        saldo = saldo+303
                    wins = 0
                    losses = 0
                    ligas = ligas+1
                
            else:
                losses = losses+1
                if wins == 0 and losses == 4:
                    saldo = saldo-100
                    wins = 0
                    losses = 0
                    ligas = ligas+1
                elif wins+losses == 5:
                    if wins == 0 or wins == 1:
                        saldo = saldo-100
                    elif wins == 2:
                        saldo = saldo-50
                    elif wins == 3:
                        saldo = saldo+23
                    elif wins == 4:
                        saldo = saldo+135
                    elif wins == 5:
                        saldo = saldo+303
                    wins = 0
                    losses = 0
                    ligas = ligas+1
        else:
            print("{:02.2f}".format(winrate), style.GREEN + "|" + style.RESET, saldo, style.GREEN + "|" + style.RESET, "{:0>5}".format("{:02.2f}".format((saldo-1000)/x)), style.GREEN + "|" + style.RESET, ligas)
            break
        
    print("{:02.2f}".format(winrate), style.GREEN + "|" + style.RESET, saldo, style.GREEN + "|" + style.RESET, "{:0>5}".format("{:02.2f}".format((saldo-1000)/x)), style.GREEN + "|" + style.RESET, ligas)
    
print("")
print("Dropping at 0-3:")
print("")
print(style.GREEN + "WR     Balance    EV      Leagues" + style.RESET)
for winrate in winrates:
    wins = 0
    losses = 0
    saldo = 1000
    ligas = 0
    for x in range(matches):
        if saldo >= 100:
            result = random()
            if result <= winrate:
                wins = wins+1
                if wins+losses == 5:
                    if wins == 0 or wins == 1:
                        saldo = saldo-100
                    elif wins == 2:
                        saldo = saldo-50
                    elif wins == 3:
                        saldo = saldo+23
                    elif wins == 4:
                        saldo = saldo+135
                    elif wins == 5:
                        saldo = saldo+303
                    wins = 0
                    losses = 0
                    ligas = ligas+1
                
            else:
                losses = losses+1
                if  wins == 0 and losses == 3:
                    saldo = saldo-100
                    wins = 0
                    losses = 0
                    ligas = ligas+1
                elif wins+losses == 5:
                    if wins == 0 or wins == 1:
                        saldo = saldo-100
                    elif wins == 2:
                        saldo = saldo-50
                    elif wins == 3:
                        saldo = saldo+23
                    elif wins == 4:
                        saldo = saldo+135
                    elif wins == 5:
                        saldo = saldo+303
                    wins = 0
                    losses = 0
                    ligas = ligas+1
        else:
            print("{:02.2f}".format(winrate), style.GREEN + "|" + style.RESET, saldo, style.GREEN + "|" + style.RESET, "{:0>5}".format("{:02.2f}".format((saldo-1000)/x)), style.GREEN + "|" + style.RESET, ligas)
            break
        
    print("{:02.2f}".format(winrate), style.GREEN + "|" + style.RESET, saldo, style.GREEN + "|" + style.RESET, "{:0>5}".format("{:02.2f}".format((saldo-1000)/x)), style.GREEN + "|" + style.RESET, ligas)
    
print("")
print("Dropping at 1-3:")
print("")
print(style.GREEN + "WR     Balance    EV      Leagues" + style.RESET)
for winrate in winrates:
    wins = 0
    losses = 0
    saldo = 1000
    ligas = 0
    for x in range(matches):
        if saldo >= 100:
            result = random()
            if result <= winrate:
                wins = wins+1
                if wins+losses == 5:
                    if wins == 0 or wins == 1:
                        saldo = saldo-100
                    elif wins == 2:
                        saldo = saldo-50
                    elif wins == 3:
                        saldo = saldo+23
                    elif wins == 4:
                        saldo = saldo+135
                    elif wins == 5:
                        saldo = saldo+303
                    wins = 0
                    losses = 0
                    ligas = ligas+1
                
            else:
                losses = losses+1
                if  wins == 0 and losses == 3:
                    saldo = saldo-100
                    wins = 0
                    losses = 0
                    ligas = ligas+1
                elif  wins == 1 and losses == 3:
                    saldo = saldo-100
                    wins = 0
                    losses = 0
                    ligas = ligas+1
                elif wins+losses == 5:
                    if wins == 0 or wins == 1:
                        saldo = saldo-100
                    elif wins == 2:
                        saldo = saldo-50
                    elif wins == 3:
                        saldo = saldo+23
                    elif wins == 4:
                        saldo = saldo+135
                    elif wins == 5:
                        saldo = saldo+303
                    wins = 0
                    losses = 0
                    ligas = ligas+1
        else:
            print("{:02.2f}".format(winrate), style.GREEN + "|" + style.RESET, saldo, style.GREEN + "|" + style.RESET, "{:0>5}".format("{:02.2f}".format((saldo-1000)/x)), style.GREEN + "|" + style.RESET, ligas)
            break
        
    print("{:02.2f}".format(winrate), style.GREEN + "|" + style.RESET, saldo, style.GREEN + "|" + style.RESET, "{:0>5}".format("{:02.2f}".format((saldo-1000)/x)), style.GREEN + "|" + style.RESET, ligas)


