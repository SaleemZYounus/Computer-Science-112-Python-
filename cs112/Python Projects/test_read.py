# test_read.py is saved to my desktop

# assume info.txt is saved to the desktop as well

info_file = open("info.txt")

# method 1: way to read lines
for line in info_file.readlines(): #file object is iterable; line is a string
    print(line) #prints the content of each line

info_file.close()
