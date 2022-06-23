from random import randint
user = ['4', '4', '7', '9', 'A', 'J', 'K']

comp = ['4', '4', '4', '4']


def display():

    """Display the card  in users hand"""

    print ("Below are the contents of your hand as well as its frequency: (Card, Frequency)")
    x = set(user)
    y = list(x)
    for card in y: 
        
        freq = user.count (card)
        
        card_freq = (freq) ,card
        print(freq)
        #card_freq.sort(key=lambda y: y[1])
        print(card_freq)
    print ("The computer has ", len (comp), " cards.")
    
display()
