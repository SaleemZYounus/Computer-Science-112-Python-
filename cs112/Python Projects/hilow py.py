def hilow (actual:int, guess:int) :
    """ print wether too high or too low """
    if actual < guess :
        print ("too hi try again")
    else :
        print ("too low try again")

def repeat (actual:int) :
    """come again"""

    guess = int(input(prompt = " enter #"))
    if guess == actual :
        print("yay so great")
    hilow (actual, guess)
    repeat (actual)

#fin returns

n = int(input("innitial price = "))
i = float(input("intrest = "))
y = int(input("years = "))

cf_comp = n * ((1 + i)**y)
cf_simp = n + (n*i) * y
print( "compound intrest = " + str(round(cf_comp, ndigits = 2)))
print( "simple intrest = " + str(cf_simp))
