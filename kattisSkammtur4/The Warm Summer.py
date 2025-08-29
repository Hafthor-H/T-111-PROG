flag = True

while True:
    if(flag):
        print("You need something doubled? (Y)es?")
        flag = False
    else:    
         print("You need something else doubled? (Y)es?")

    strengur = input("")
    if(strengur == "Y"):
        print("All right, then. Give me a number, and I'll double it for ya:")
        num = float(input(""))
        print(num*2)
    else:
        break