from random import randint
def userplay() :
    """enter RPS"""
    choice = input("enter rock(r) parper(p) scissors(s)")

    if choice == "r" or choice == "R":
        return "rock"
    elif choice  == "p":
        return "paper"
    elif choice == "s":
        return "scissors"
    else:
        print("nono")
        userplay()

def complay():
    plays = ["rock","paper","scissors"]

    index = randint[0, 2]

    return plays[index]

def score ( user : str, comp : str ) :
  
    if user == comp:
        print("heh u tied")
        return 3
    elif user == "rock" and comp == "paper":
        return 2
    elif user == "paper" and comp == "scissor":
        return 2
    elif user == "scissor" and comp == "rock":
        return 2
    elif user == "paper" and comp == "rock":
        return 1
    elif user == "scissor" and comp == "paper":
        return 1
    elif user == "rock" and comp == "scissor":
        return 1
   
def pla():
   

    pa = input("wanna go ? y/n")
    if pa == "y":
        return True
    elif pa == 'n' :
        return False
    
   
def rps():
    """runs game"""
    win, loss, tie = 0, 0, 0

    result = score(userplay(), complay())

    if result == 3:
        tie += 1
    elif result == 1:
        win += 1
    else:
        loss += 1

    print("wins: ", win, "losses ", loss, "ties", tie)

    while (pa()):
         results = score(userplay(), complay())
         if results == 3:
             tie += 1
         elif result == 1:
            win += 1
         else:
            loss += 1

            print("wins: ", win, "losses ", loss, "ties", tie)
