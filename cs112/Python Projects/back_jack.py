from random import randint

# define our deck as a variable that all functions can access
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
full_deck = cards*4 # defines our full deck


def draw() -> str:
    """Draws a card from full_deck and deletes entry"""
    index = randint(0, len(full_deck)-1)

    card = full_deck[index] #saves card
    full_deck.remove(card)  #remove card from deck

    return card



def hand_info(hand:list):
    """Print first card and total cards in list"""

    print("The computer has ", len(hand), "cards")
    print("Their first card is ", hand[0])



def score_hand(hand:list) -> int:
    """Return the total score of a black jack hand """

    score = 0
    aces = 0 #because aces can be two different values, we'll count them last

    for i in range(0, len(hand)):
        card = hand[i]
        if str(card) in "JQK":
            score = score + 10
        elif str(card) == "A":
            aces = aces + 1 # store aces separately
        else:
            score = score + card

    # score is now the score w/o aces

    # at most, 1 ace will be worth 11 pts.
    # if there is more than one ace, count those as 1 pt.
    while(aces > 1):
        score = score + 1
        aces = aces - 1

    #if there is 1 ace
    if aces == 1:
        #should it be worth 11 points?
        if score <= 10:
            score = score + 11
            aces = aces - 1
        #or just 1 pt?
        else:
            score = score + 1
            aces = aces - 1

    return score



def hit() -> bool:
    """Returns True if user wants to hit"""

    choice = input("Enter H to 'hit' or S to 'stay': ")

    if choice == "H" or choice == "h":
        print("You chose to hit")
        return True
    elif choice == "S" or choice == "s":
        print("You chose to stay")
        return False
    else:
        print("Invalid input.")
        hit()



def one_game() -> bool:
    """Plays out one game of blackjack"""

    comp_hand = [] #list that stores computer's cards
    user_hand = [] #list that stores user's cards

    #reset deck for each game
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    full_deck = cards*4

    # initialize game
    print("---------------------------------")
    print("Welcome to Black Jack!")
    print("---------------------------------")

    # deal cards -- player goes first in dealing
    user_hand.append(draw())
    comp_hand.append(draw())
    user_hand.append(draw())
    comp_hand.append(draw())

    #show user their hand
    print("Your hand is ", user_hand)
    print("Your potential score is ", score_hand(user_hand))

    #display computer hand
    hand_info(comp_hand)

    #prompt user
    while(hit()): #while the user chooses to hit, we will do the following
        #add card to user hand
        user_hand.append(draw())
        print("Your hand is ", user_hand)
        print("Your potential score is ", score_hand(user_hand))


        if score_hand(user_hand) > 21:
            print("You busted! You lose")#game end
            return False
        if score_hand(comp_hand) < 18:
            comp_hand.append(draw())
            hand_info(comp_hand)
        if score_hand(comp_hand) > 21:
            print("Computer busts! You win!") #game end
            print("Computer hand is ", comp_hand)
            print("Computer score is ", score_hand(comp_hand))
            return True
        if score_hand(comp_hand) >= 18:
            print("Computer has elected to stay")
            hand_info(comp_hand)

    #user has stayed, but computer should hit
    while(score_hand(comp_hand) < 18):
        comp_hand.append(draw())
        hand_info(comp_hand)
        if score_hand(comp_hand) > 21:
            print("Computer busts! You win!") #game end
            print("Computer hand is ", comp_hand)
            print("Computer score is ", score_hand(comp_hand))
            return True


    comp_score = score_hand(comp_hand)
    user_score = score_hand(user_hand)
    print("You scored:", user_score)
    print("The computer scored:", comp_score)
    if user_score < comp_score:
        print("You lost")#game end
        return False
    else:
        print("You won")#game end
        return True


def play_again() -> bool:
    """prompts user if they wish to play again"""

    play = input("Would you like to play again? (Y/N): ")

    if play == "Y" or play == "y":
        return True
    elif play == "N" or play == "n":
        return False
    else:
        print("Invalid input")
        play_again()


def multi_games():
    """Allows user to play multiple games of black jack"""


    win, loss = 0, 0
    #first game
    if one_game() == True:
        win = win + 1
    else:
        loss = loss + 1

    print("Wins:", win, "Losses:", loss) #print win/loss totals

    #subsequent games
    while(play_again() == True):

        if one_game() == True:
            win = win + 1
        else:
            loss = loss + 1

        print("Wins:", win, "Losses:", loss) #print win/loss totals

    #end of play
    print("Goodbye!")

multi_games()
