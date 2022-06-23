from random import randint
import random
import collections

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = cards * 4

user = []
comp = []

def welcome_message():
    print("You are playing go fish")
    input("Press enter to continue")
    print("The Goal of this game is to collect as many books as you can. A deck is 4 of the same cards.")
    input("Press enter to continue")
    print("The score of the book is determined by the type of card. The starting from 2 all the way to Ace")
    
def draw_card() -> str:
    """draws a single card and removes it from deck"""
 
    card = deck[randint(0, len(deck)-1)]
    deck.remove(card)

    if deck == []:
        print('“Deck is out of cards”')
        return None
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

# Help from Javi the Tutor
#first for loop creates the frequency var and sorts from highest to lowest. The second prints the crad type and frequency
def display():
    """Display the card  in users hand"""

    card_freq = []
    for card in set (user):
        freq = user.count (card)
        card_freq.append((freq, card))

    card_freq.sort(reverse = True)

    for pair in card_freq: 
        print (pair[1], ": ", pair[0])
    
    
    
    print ("The computer has ", len (comp), " cards.")
    # could this be better for the user?
    input("press enter to continue")


def play_again() -> bool:
    """prompts user if they wish to play again"""

    while(True):
        
        resp = input("Would you like to play again? (Y/N): ")
        resp = resp.upper()
        
        if resp == "Y":
            # renew deck
            deck.append(user)
            deck.append(comp)
            user.clear()
            comp.clear()
            game()
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

def is_game_over():
    """runs through to see if preprequisite for game to be are fulfilled"""

    uniq_comp = (set(comp)).difference(set(user))
    uniq_user = set(user).difference (set(comp))

    while True:

        if deck != []:

            return False
        else:
            for element in uniq_comp:
                cards_counted = comp.count (element)
                if cards_counted < 4:
                    return False

            for element in uniq_user: 
                cards_counted = user.count (element)
                if cards_counted < 4:
                    return False

            return True

#collections list comprehension <- Refferrence : My Father
#uses collections to count accurance of items in the list and outputs those with less than 4 accurance
def ask_comp():
    
    """The computer requests a card. the user is checked to see if they have the card and gives it if they do"""

    potential_cards = []
    
    uniq_comp = (set (comp)).difference(set(user))
# reference yamaris finnigin
    for card in uniq_comp:

        if comp.count(card) <4:
            potential_cards.append (card)

    if (len (potential_cards)) > 0:
        index = randint (0, len(potential_cards)-1 )
        random_draw = potential_cards [index] 
        print("The computer requests: ", random_draw) 
        input("press enter to continue")

    else:
        index = randint (0, len (comp)-1) 
        random_draw = comp[index]
        print("The computer requests: " + (random_draw)) 
        

    if random_draw in user:

        print("You have the card requested my the computer") 
        
        give_cards(user, comp, (random_draw))

    else:

        print ("You do not have the requested card. The computer drew a card")
        go_fish(comp)
    #--------
    

def score():
    """computes score for each player and determines winner"""
    user_score = 0
    comp_score = 0

    scoring = {"A": 14, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13} 
    uniq_comp = (set(comp)).difference(set(user))

    for element in uniq_comp:
        points = scoring[element]
        comp_score= comp_score + points

    uniq_user = set(user).difference (set(comp)) 
    #print (uniq_user) 

    for element in uniq_user: 
        points = scoring[element]
        user_score = user_score + points

    print ("Your score is: " + str (user_score)) 
    print ("Computer score is: " + str (comp_score))
    
    
    if user_score > comp_score:
        print("You won yay")
    elif comp_score < user_score:
        print("you lost hah")
    else:
        print("you tied -_-")
    play_again()
def game():
    """Brings all functions together and Completes game"""
    welcome_message()
    deal_cards()
    
    while is_game_over() is False:
        ask_user()
        if is_game_over():
            break
        ask_comp()
        display()
    print('The game is over')
    score()
    

