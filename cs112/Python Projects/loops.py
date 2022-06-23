from random import randint

def recur10(counter:int):
    """ ends after 10  """
    print ("this is #" + str(counter))
    counter = counter - 3
    if counter > 0:
        recur10(counter)
    else:
        return None
recur10(19)

for counter in range(30,-0,-3):
    print("step"+str(counter))

    while(num !=10)
