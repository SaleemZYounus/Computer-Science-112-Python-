import string
import collections
def t_n (texts:str) -> int:
    '''on;y takes numbers 0-99'''

    
    value = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,
              'ten':10,'twenty':20,'thirty':30,'fourty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,
              'eleven':11,'twelve':12,'thirteen':13,'fourteeen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19
              }

    word_in_input = texts.split()


    if len(word_in_input) == 1:
        number = value [word_in_input[0] ]
        
    else:
        number = value [word_in_input [0] ] + value [word_in_input [1]]
    return number

a = ['5','5','5','5']
a.sort()
print(a)
import collections
b = ([item for item, count in collections.Counter(a).items() if count < 4])
print(b)
if (len(b)) > 0:
            #print('we have < 4 :(')
    print(False)
else:
            #print('we got 4 yay')
    print(True)
