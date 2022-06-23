#trials
from string import printable
import collections
def show_books():
    test = input("")
    if test == ("books"):
        print('booking')
    show_books()

list1 = [1,2,3,4,5,5,6,6]
list2 = [2,3,4,5,6,7,8]
set1 = set(list1)
set2 = set(list2)
print(set1.difference(set2))
def clear_():
    list.clear()

    
def checkIfDuplicates_2(listOfElems):
    ''' Check if given list contains any duplicates '''    
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)         
    return False

listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
result = checkIfDuplicates_2(listOfElems)
if result:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')
# REMOVING DUPLICATES
def duplicates():
    res = []
    for i in list1:
        if i not in res:
            res.append(i)
    print(res)

    a=(Counter[1,2,3])
    b=(Counter[2,3,4])
    c=b-a


def hand():
    for cardsinhand in printable:
        card_count = comp.count(cardsinhand)
        if card_count > 0 :
            card_tuple = (card_count, cardsinhand)
            comp_pair.append(card_tuple)
        #print(cardsinhand[1])
comp = ['3', 'A', 'Q', 'Q', '5', '3', 'J']
compset = set(comp)
ucomp = list(compset)
yes = comp.remove(ucomp[0])

print(comp)
comp  = [1,2,3,3,3,3,4,5,6]
[item for item, count in collections.Counter(comp).items() if count < 4]

uniq = set(comp)
#x = [for uniq in comp if comp.count() < 4]

sentence = "Every moment is a fresh beginning."
my_list = [len(word) for word in sentence.split()]    #.split outputs the words from string in a list


#NOTES 10-12-21
#ITERABLES  THINGS WITH MULTIPLE ENTRIES  - TUPLE LIST SETS DICT RANGE SSTRINGS
#FUNCTIONAL PROGRAMIN - PROMOTES USING FUNCTIONS IN EVERY TASK (HASKEL MATHMATICA)
#MAP(FUNC, ITTER)  ->generic outcome change by adding list[] - dict{}
#lambda condencing a function  func = lambda: expression +-*/%**    //-INT DEVISION ROUNDS DOWN
# INT BOOL LIST DICT SET MAP STR TUPLE FLT
# FLT ROUND()
#BOOL T and F   cond statements - while loops
#str var[index] (grabbin)
var = 'yo'
#for charector in var:
    #something with the charecter

#SET .intersection .clear .difference .symetric_difference
    #no dictionary methods
#    var.split()
#tuple lexomographic order
# know the syntax    and conlrole flow

#var = x for member i iterable if #condition

#map non pythonic

square = lambda: num**2
