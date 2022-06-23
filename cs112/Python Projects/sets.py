from string import punctuation, whitespace

# sets  -  bag of stuff , no repeats  [can convert things to sets]   , no order(index) ,
def sets():
    set_A = {"A", "K", "P", "L", "E"}
    set_B = set(["A", "A", "A", "R", "R"])

    print(set_A)
    print(set_B)
    print('^AandB^')

    print( 'intersection ->' + str(set_A.intersection(set_B)))
#{'A'}
    print ( 'union ->' + str(set_A.union(set_B)))
#{'P', 'E', 'K', 'R', 'A', 'L'}
    print ( 'difference A-B->' + str(set_A.difference(set_B)))
#{'P', 'E', 'L', 'K'}
    print( 'difference B-A ->' + str(set_B.difference(set_A)))
#{'R'}
    print( 'sym difference ->' + str(set_A.symmetric_difference(set_B)))
#{'P', 'E', 'K', 'L', 'R'}
def common_letters(sent1:str, sent2:str)->list:
    '''yes'''

    sent1 = sent1.upper()
    sent2 = sent2.upper()

    set1 = set (sent1)
    set2 = set (sent2)

    #sent1 = input("say it")
    print(set(sent1))
    set(sent2)

    set3 = set1.difference(set(punctuation))
    set3 = set3.difference(set(whitespace))

    answer_list = list(set3)
    answer_list.sort()
    print(set3)
    return answer_list
