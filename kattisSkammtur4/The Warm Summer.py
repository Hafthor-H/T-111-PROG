while True:
    strengur = input("You need something doubled? (Y)es?")
    if(strengur == "Y"):
        num = float(input("All right, then. Give me a number, and I'll double it for ya: "))
        print(num*2)
        num = 0
    else:
        break