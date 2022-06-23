def get_coins()-> float :
    """input coins to get cash"""
#maddie helped me reads directions 
    quarters = int(input("how many quarters! "))
    dimes = int(input("how many dimes! "))
    nickles = int(input("how many nickles! "))
    pennies = int(input("how many pennies! "))
    ctotal = (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)
    print("total dollars = $" + str(round(ctotal, ndigits = 2)))
    return ctotal

def make_change(money = 0) :
    """tAAKes total monay and converts to cash"""    

    #money = float(input("what is total dollar value? "))
    #print("total " + str(money))
    money = float(money)
#$100
    hunin = int(money/100)
    money = round(money % 100, ndigits=2)
    print(str(hunin) + " hundred dollar bills")
    #print("remainder after 100 = " + str(money))

    fifty = int(money/50)
    money = round(money % 50, ndigits=2)
    print(str(fifty) + " fifty dollar bills")

    twenty = int(money/20)
    money = round(money % 20, ndigits=2)
    print(str(twenty) + " twenty dollar bills")

    ten = int(money/10)
    money = round(money % 10, ndigits=2)
    print(str(ten) + " ten dollar bills")

    five = int(money/5)
    money = round(money % 5, ndigits=2)
    print(str(five) + " five dollar bills")

    one = int(money/1)
    money = round(money % 1, ndigits=2)
    print(str(one) + " one dollar bills")

    quarters = int(money/.25)
    money = round(money % .25, ndigits=2)
    print(str(quarters) + " quarters")

    dime = int(money/.1)
    money = round(money % .1, ndigits=2)
    print(str(dime) + " dime")

    nicks = int(money/.05)
    money = round(money % .05, ndigits=2)
    print(str(nicks) + " nickels")

    pennies = int(money/.01)
    money = round(money % .01, ndigits=2)
    print(str(pennies) + " pennies")

    return None

def coins_to_cash():
 
    cash_value = get_coins()
    #print("hi " + str(cash_value))
    make_change(cash_value)
    

coins_to_cash()
 

    

    
    

    

    
    
    
