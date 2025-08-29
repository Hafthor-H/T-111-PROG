a = int(input())
b = int(input())
c = int(input())

def andGate(num1, num2):
    if(num1 == num2 == 1):
        return  1
    else:
        return  0

def notGate(num1):
    if(num1 == 0):
        return 1
    else: 
        return 0

def orGate(num1, num2):
    if(num1 == num2 == 0):
        return 0
    else:
        return 1
    
b2 = notGate(b)
ab = andGate(a, b2)
a1 = notGate(a)
ac = andGate(a1,c)

result = orGate(ab, ac)
print(result)