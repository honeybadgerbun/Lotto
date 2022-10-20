import random
import time
import sys

def wish_to_play(game):
    valid = False
    answer = input(f"Do you wish to play {game}, Yes or No? (Y/N) ")
    while not valid:
        if answer.upper() == 'Y' or answer.upper() == 'N':
            valid = True
        else:
            answer = input(f"Do you wish to play {g}, Yes or No? (Y/N)\nYou must pick Y/N ")
    if  answer.upper() == "Y":
        return True
    elif answer.upper() == "N":
        return False

def spin(list):
    print("",end="")
    for i in range(3):
        print(f"{list[i]} ",end='')
        time.sleep(1)