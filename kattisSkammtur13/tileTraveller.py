gameLoop = True
northFlag = True
southFlag = True
westFlag = True
eastFlag = True

position = [1, 1]

def north(p):
    if p[1] > 2 :
        print("Not a valid direction!")
        return p 
    else:
        return [p[0], p[1] + 1]
    
def south(p):
    if p[1] < 2:
        print("Not a valid direction!")
        return p 
    else:
        return [p[0], p[1] - 1]

def west(p):
    if p[0] < 2:
       print("Not a valid direction!")
       return p 
    else:
        return [p[0] - 1, p[1]] 

def east(p):
    if p[0] > 2:
        print("Not a valid direction!")
        return p 
    else:
        return [ p[0] + 1, p[1]]

def checkForWall(p):
    global northFlag
    global southFlag
    global westFlag
    global eastFlag

    northFlag = True
    southFlag = True
    westFlag = True
    eastFlag = True

    if p == [1 , 1]:
        eastFlag = False
    elif p == [2,1]:
        westFlag = False
        eastFlag = False
    elif p == [3,1]:
        westFlag  = False
    elif p == [2,2]:
        northFlag = False
        eastFlag = False
    elif p == [2, 3]:
        southFlag = False
    elif p == [3 , 2]:
        westFlag = False
        
def validDirections(p):
    if p == [1,1] or p == [2, 1]:
        print("You can travel: (N)orth.")
    elif p == [1, 2]:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif p == [1,3]:
        print("You can travel: (E)ast or (S)outh.")
    elif p == [2,2] or p == [3,3]:
        print("You can travel: (S)outh or (W)est.")
    elif p == [2,3]:
        print("You can travel: (E)ast or (W)est.")
    elif p == [3,2]:
        print("You can travel: (N)orth or (S)outh.")

while gameLoop:
    if position == [3,1]:
        print("Victory!")
        break
    validDirections(position)
    checkForWall(position)
    print("Direction: ")
    playerMove = input()
    if playerMove == "n" and northFlag or playerMove == "N" and northFlag:
        position = north(position)
    elif playerMove == "s" and southFlag or playerMove == "S" and southFlag:
         position = south(position)
    elif playerMove == "w" and westFlag or playerMove == "W" and westFlag:
         position = west(position)
    elif playerMove == "e" and eastFlag or playerMove == "E" and eastFlag:
         position = east(position)
     
    else:
        print("Not a valid direction!")