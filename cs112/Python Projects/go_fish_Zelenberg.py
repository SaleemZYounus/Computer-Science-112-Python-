from random import randint

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = cards * 4

user = []
comp = []

def draw_card() -> str:
    """draws a single card and removes it from deck"""
 
    card = deck[randint(0, len(deck)-1)]
    deck.remove(card)
    
    #what if deck is empty?

    return card


def deal_cards():
    """deals cards for user and computer"""

    for i in range(7):
        user.append(draw_card())
        comp.append(draw_card())

    user.sort()
    comp.sort()


def go_fish(hand:list) -> str:
    """Prints go fish and draws a card"""

    print("Go fish!")

    card = draw_card()

    hand.append(card)
    hand.sort()

    if hand is user:
        print("Now adding " + card + " to you hand.")
    else:
        print("The computer has drawn a card.")

    return card



def give_cards(giver:list, taker:list, card:str) -> tuple:
    """Passes cards from one hand to another"""

    print("Transfering card " + card)

    while( card in giver ):
        giver.remove(card)
        taker.append(card)

    taker.sort()
    
    return giver, taker


def display():
    """Display the contents of the hands"""

    print("Your cards are: ", user)
    print("The computer has ", len(comp), " cards.")
    # could this be better for the user?
    

def play_again() -> bool:
    """prompts user if they wish to play again"""

    while(True):
        
        resp = input("Would you like to play again? (Y/N): ")
        resp = resp.upper()
        
        if resp == "Y":
            # renew deck 
            return True
        
        if resp == "N":
            return False
        
        print("Invalid input")

def ask_user():
    """Asks the user to request a card"""

    invalid = True

    while(invalid):
        
        print("What card would you like? ")
        
        resp = input("Enter something from " + str(user) + ": ")
        resp = resp.upper() 
        
        if resp in user:
            invalid = False
        else:
            print("Invalid response")

    if resp in comp:
        print("Computer has card")
        give_cards(comp, user, resp)
    else:
        print("Computer does not have card")
        go_fish(user)
