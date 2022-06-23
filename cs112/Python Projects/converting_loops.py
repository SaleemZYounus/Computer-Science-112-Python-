#CONVERT LOOP TO LIST COMPREHENTION

sentence = "the student was clueless"
#word = sentence.split()
#wordlist = []
#for word in words:
  #  wordlist.append(len(word))

#print(wordlist)

wordlength = [len(word) for word in sentence.split() if word != 'the']

numbers = [1,2,3,-44,-5,566]
pos = [num for num in numbers if num > 0]
neg = [num for num in numbers if num < 0]

#SETS COMP

#KEY :VALUE
# .split wil output full words not letters

