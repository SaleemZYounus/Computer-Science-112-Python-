diet_log = []
waste_log = []
goodies = ["cookie", "cookies", "brownie"] #cookie monster likes these yummy foods

def cm():
    food = input("What will u feed Cookie Monster: ")
    food = food.lower()
    if food in goodies:
        print("yummy yummy " + food)
        diet_log.append(food)

    else:
        print("Cookie Monster dont eat that")
        waste_log.append(food)

    print("Food Log: " + str(diet_log))
    print("Waste Log: ", str(waste_log))
    cm()
cm()
