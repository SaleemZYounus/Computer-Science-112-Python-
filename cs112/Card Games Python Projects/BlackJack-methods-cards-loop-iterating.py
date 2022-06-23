from random import randint
#yamiana = "yamiana = good child"
#yes = input("who is my friend? ")
#print(yes + " is my friend")
#mean = input("how mean is ur friend ")
#print(yes + " is " + mean)

def  scorehand() :
    """takes hand and calcultes score"""

deck = ["A",2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,"J", "Q", "K"]
full = deck*4
sign = ["heart", "clover", "spade", "diamond"]
print(deck[0] + sign[1])
deck.remove(5)
print(deck)

def draw ():
    index = randint(0, len(full))

    card = full[index]
    full.remove(card)

    return card

x = ["apple", "banana", "cherry"]

y = "apple"

if x is y :
    print('hi')
x.append('weird')

for z in y:
    print(z)
