from random import randint
from string import ascii_uppercase

def cipher_puzzle(sentence:str)-> str:
    n = randint(1,25)
    sentence = sentence.upper()

    print(n)
    print(ascii_uppercase)
    print(sentence)
    for i in sentence:
        if i in ascii_uppercase:
            new = ascii_uppercase.index(i)+n
            print(ascii_uppercase.index[new])
