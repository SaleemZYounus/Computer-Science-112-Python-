import sys

def correct_spelling(word:str)->str:

    """ Finds words from file and corrects spelling """
    spell_file = open ('aspell.txt', 'r')

    if word[0].isupper():
        #caps = True
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




#    word_change = [char for char in word if char.isalpha()]
####BAADD
#    word = ''.join(word_change)
###BAAADjob
    beginning = ""

    for char in word:
        if char.isalpha():
            break

        else:

            beginning += char
            word = word.istrip(char)

    end = ''
    for char in word[::-1]:

        if char.isalpha():
            break

        else:
            end = char + end
            word = word.rstrip(char)

    spell_file.close()

    return word

def correct_line(line:str) ->str:
    """ takes all words and spell checks"""
    word_list = line.split()
    corrected_words = ''.join(map(correct_spelling ,word_list))

    return corrected_words

def correct_file(filename:str):
    """Cretes corrected file"""

    words_file = open(filename,"r")

    corrected_file = open(str(filename) + "_corrected.txt", "w")

    correct_words = []

    for line in words_file.readlines():
        corrected_file.append(correct_line(line))

    corrected_file.writeLines(str(correct_words))

    correct_file('blurb.txt')

def main():

    args = sys.argv[1:]

    print(args)

    correct_file(args[0])



if __name__ == "__main__":

    main()
