import random
import time
import sys

game = "Russian Roulette"
name = input("Hello player, what is your name? ")

def wish_to_play():
    valid = False
    answer = input(f"Do you wish to play {game}, Yes or No? (Y/N) ")
    while not valid:
        if answer.upper() == 'Y' or answer.upper() == 'N':
            valid = True
        else:
            answer = input("Do you wish to play Russian Roulette, Yes or No? (Y/N)\nYou must pick Y/N ")
    if  answer.upper() == "Y":
        return True
    elif answer.upper() == "N":
        return False

def russian_roulette(bullet,pick):
    for shot in range(1,7):
        if shot == bullet and shot < pick:
            print("Now I gotta clean this mess up. SHERANE, DO YOUR JOB!")
            break
        elif shot == bullet and shot > pick:
            print("You got lucky, that was a boring game.")
            break
        elif shot != bullet and shot != pick:
            print("Guess you got lucky with this shot, next one!")
            shot += 1
            time.sleep(3)
        elif shot == bullet and shot == pick:
            print("Now I gotta clean this mess up. SHERANE, DO YOUR JOB!")
            break
        elif shot == pick and shot < bullet:
            print("You got lucky, that was a boring game.")
            break


def run_game():
    if wish_to_play() == False:
        print("""Where's the fun in that? Just leave already. (;_;)""")
        exit()
    else:
        b = random.randint(1,6)
        p = int(input("Pick a number 1-6 "))
        if 1 <= p <= 6:
            russian_roulette(b,p)
        else:
            while 1 > p or p > 6:
                p = int(input("Pick a number 1-6 "))
            russian_roulette(b,p)

run_game()