def correct_spelling(word:str)->str:
    
    """ Finds words from file and corrects spelling """
    spell_file = open ('aspell.txt', 'r')

    if word[0].isupper():
#        caps = True
        word = word.lower()
    for line in spell_file.readlines():

        if " " + word + " " in line:
            print('found it')
            word_list = word.split(":")
            word = word_list[0]
            break
        elif " " + word + "\n" in line:
            word_list = line.split(': ')
            word = word_list[0]
            break

    spell_text.close()

    word = word.capitalization()

    word_change = [char for char in word if char.isalpha()]

    word = ''.join(word_change)

    print(word)

def correct_line(line:str) ->str:
    """ """
