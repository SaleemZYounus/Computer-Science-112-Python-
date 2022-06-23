from random import randint 
import random 
from string import digits
import collections
cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = cards*4
user = []
comp = []
#hand = []
#giver = ()
#taker = ()
#print(deck)


def welcome_message():
    print("You are playing go fish")
    input("Press enter to continue")
    print("The Goal of this game is to collect as many books as you can. 4 of the same cards")
def draw_card()->str:
    """draws a random card"""
    draw = random.choice(deck)
    deck.remove(draw)
    #print(draw)
    #print(deck)
   
    if deck == []:
        print("Deck is out of cards")
    
    return draw

def deal_cards()-> list:
    """ deals 7 cards alternating between """
# users first draw 
    #deal1u = draw_card()
    #deck.remove(deal1u)
    #user.insert(0, deal1u)
    #print(deal1u)
    #print(user)

    user.insert(0, draw_card())
    comp.insert(0, draw_card())
    user.insert(1, draw_card())
    comp.insert(1, draw_card())
    user.insert(2, draw_card())
    comp.insert(2, draw_card())
    user.insert(3, draw_card())
    comp.insert(3, draw_card())
    user.insert(4, draw_card())
    comp.insert(4, draw_card())
    user.insert(5, draw_card())
    comp.insert(5, draw_card())
    user.insert(6, draw_card())
    comp.insert(6, draw_card())

    
def go_fish(hand:list)->str:
    """draws  card and adds card to hand"""
    print('Go Fishies')

    card = draw_card()
    user.append(card)
    user.sort()
    #print(hand)

    if hand is user:
        print("you drew a " + str(card))
    else:
        print("computer drew a card")
        comp.append(card)
    return card

def give_cards(giver, taker, card)->tuple:
    print(" the card being transfered ")

    #card = go_fish(user)
    
    while (card in giver):
        
        giver.remove(card)
        taker.append(card)
        taker.sort()

    return giver, taker

def display():
    ask = input("type 'books' to view books")
    if ask == ("books"):
        print("your cards are" + str(user))
        print("computer has " + str(len(comp)) + ' cards')
        
    return None

def play_again():
    """asks user if they want to play again"""
    choice = input('play again??? (Y/N)')
    while True :
        if choice == "Y" or choice == "y" :
            deck.append(user)
            deck.append(comp)
            user.clear()
            comp.clear()
            deal_cards()
            return True
        
        elif choice == "N" or choice == "n" :
            return False
        else:
            print('invalid responce')
#Javi the tutor and Yamaris assisted me in this function
def ask_user() :
    """checks if the computer has a card of the users choice"""
    print(user)
    invalid = True
    while(invalid):
        request = input("choose one of the given: " )
        request = request.upper()
        #print(request)   
        if request in user:
            invalid = False   
        else:
            print('invalid response')
            ask_user()

    if request in comp:
            print('the computer has a ' + request)
            give_cards(comp, user, request)
            
    else:
            print('the computer does not have ' + request)
            go_fish(user)



def is_game_over():

    if deck != []:
        #print('not epty')
        return False

# b = ([item for item, count in collections.Counter(a).items() if count > 3])
    
    print(len(([item for item, count in collections.Counter(comp).items() if count < 4])))
    #unique_comp = set(comp)
    while True:

        if (len(([item for item, count in collections.Counter(comp).items() if count < 4]))) > 0:
            print('we have < 4 :(')
            return False
        elif (len(([item for item, count in collections.Counter(user).items() if count < 4]))) > 0:
            print('user < 4')
            return False
        else:
            print('we got 4 yay')
            return True

#collections list comprehension <- Refferrence : My Father
#uses collections to count accurance of items in the list and outputs those with less than 4 accurance
def ask_comp():
    
    potential_cards = []
    print(potential_cards)

    if (len(([item for item, count in collections.Counter(comp).items() if count < 4]))) > 0:
        potential_cards.extend(([item for item, count in collections.Counter(comp).items() if count < 4]))
    print(potential_cards)
    #for pair in potential_cards:
        #print(pair[1] +": ", pair[0])
       # print(pair[1])
       # print(pair[0])
      #  if pair[0] > 1:
      #      print("we got a repeat")

    pick1 = random.choice(potential_cards) #picking from potential cards
    pick2 = random.choice(comp)

    if potential_cards != []:
        print("The computer request from potential cards a: " + str(pick1))
        if pick1 in user:
            print("you have the card requested by computer")
            give_cards(user,comp,pick1)
        else:
            print('You do not have requsted card')
            go_fish(comp)
    else:
        print("The computer requests a: " + str(pick2))
        if pick2 in user:
            print("you have the card requested by computer")
            give_cards(user,comp,pick2)
        else:
            print('You do not have requsted card')
            go_fish(comp)
    print(pick1)

def score():
    
    user_score = 0
    comp_score = 0

    scoring = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13} 

    if user_score > comp_score:
        print("You won yay")
    elif comp_score < user_score:
        print("you lost hah")
    else:
        print("you tied -_-")

def game():
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

game()
a = ([item for item, count in collections.Counter(comp).items() if count < 4])
b = ([item for item, count in collections.Counter(user).items() if count < 4])

# MISSING - """triple quotes""" - \/score() dictionary thing - welcomr() rules -  wierd if state in ask_comp()
