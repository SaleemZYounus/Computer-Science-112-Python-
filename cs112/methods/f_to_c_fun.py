# create a function that takes in a temp in fahrenheit
# converts it to celsius
# prints the celsius

print("Type 'fahrenheit_to_celsius()' to make a conversion")

def fahrenheit_to_celsius():

    print("Input temperature in Fahrenheit and press enter:")
    f_temp = input() # temp in fahrenheit
    f_temp = float(f_temp)
    c_temp = (f_temp - 32) * 5 / 9
    print("Here is the same temperature in Celsius:")
    c_temp = round(c_temp, ndigits=1)
    print(c_temp)

    return None

def fahr2 (f_temp = 70) :
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp