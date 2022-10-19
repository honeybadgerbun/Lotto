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