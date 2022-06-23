from random import randint

def hilow (actual:int, guess:int) :
    """ print wether too high or too low """
    if actual < guess :
        print ("too hi try again")
    else :
        print ("too low try again")

def repeat (actual:int) :
    """come again"""

    guess = int(input(prompt = " enter #"))
    if guess == actual :
        print("yay so great")
    hilow (actual, guess)
    repeat (actual)

def playagain() :
    rep = input("again na?")
    if res == "y" :
         hilow()
    elif response == "n" :
        print('thx')
    else : playagain
    

def hilow() :
    """shellgame"""
    print("hi   plsy guess")
    actual = randint(1, 10)
    repeat(actual)


    
#fin returns






