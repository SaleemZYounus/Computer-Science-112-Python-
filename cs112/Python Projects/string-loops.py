import string

def clasiffy(sentence:str = 'qwertyuiop1'):
    '''hi'''
    for char in sentence:
        if char in "EAIOUaeiou":
            print("vowel")
        elif char in string.ascii_letters:
            print("consonent")
        elif char in string.punctuation:
            print("punc")
        elif char in string.digits :
            print('cool numbers')
        else:
            print('gotnun')
