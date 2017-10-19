from random import randint

#generates a random integer from 1-100
#then the user guess if the number
#the program responds with "too high", "too low", or "nice"
def guess():
    num = randint(1,100)
    while(True):
        choice = int(input("What is the number?\n"))
        if choice> num:
            print("Too high, try again")
        elif choice < num:
            print("Too low, try again")
        else:
            print("Nice. You won")
            break 
guess()