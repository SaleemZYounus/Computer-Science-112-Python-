import string
def t_n (texts:str) -> int:
    '''on;y takes numbers 0-99'''

    
    value = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,
              'ten':10,'twenty':20,'thirty':30,'fourty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,
              'eleven':11,'twelve':12,'thirteen':13,'fourteeen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19
              }

    word_in_input = texts.split()
    print(word_in_input)

    if len(word_in_input) == 1:
        number = value [word_in_input[0] ]
        
    else:
        number = value [word_in_input [0] ] + value [word_in_input [1]]
    return number

#tup = 1,2,3,4,5
#>>> for num in tup:
#	print(num*2-1)

	
#1
#3
#5
#7
#9
#>>> for num in tup:
#	print(num + tup.index(num))

print("hi")
input('press enter')
print('yo')
