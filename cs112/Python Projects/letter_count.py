from string import digits
import collections
lcl = []


def letter_count(sent:str)->list:
    """returns a letter count of sent"""

    sent = sent.lower()
    
    for letter in digits:
        letter_count = sent.count(letter)
        if letter_count > 0 :
            letter_tuple = (letter_count, letter)
            lcl.append(letter_tuple)

#    lcl.sort(reverse=True)

    return lcl

def countprint():
    letter_count('11')
    for pair in lcl:
        #print(pair[1] +": ", pair[0])
        print(pair[1])
        print(pair[0])
        if pair[0] > 1:
            print("we got a repeat")
            
def alpha_printup():
    '''alp print of count'''
    alphalist = []
    for pair in lcl:
        alpha_tuple = (pair[1], pair[0])
        alphalist.append(alpha_tuple)

    alphalist.sort() #shoud reverse na ?
    for pair in alphalist:
        print(pair[0] +": ", pair[1])
a = ['4', '4', '4', '4', '2', '2', '2', '2']
def rep():
    import collections

   # b = ([item for item, count in collections.Counter(a).items() if count > 3])
    cards_less_than_4 = ([item for item, count in collections.Counter(a).items() if count < 4])
#print(len(b))
    print(cards_less_than_4)
    if (len(cards_less_than_4)) > 0:
        print('we have < 4 :(')
        return False
    else:
        print('we got 4 yay')
        return True

rep()
