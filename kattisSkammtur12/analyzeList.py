import math
numList = [] 

while len(numList) <= 0:
    numbers = input()
    numList = numbers.split(",")
    for j in numList:
        if j.isnumeric():
            if int(j) < 0:
                print("Incorrect input! Please try again.")
                numList.clear
        else:
            print("Incorrect input! Please try again.")
            numList.clear()

numList = [int(item) for item in numList]
sortedList = sorted(numList)

def minMaxAve(someList):
    least = min(someList)
    most = max(someList)

    mid = sum(someList) / len(someList)
    mid = f"{mid:.2f}"
    return least, most, mid

values = minMaxAve(numList)

def isPrime(num):
    numSqrt =  math.sqrt(num)
    counter = 2
    isPrime = True
    if num == 1:
        return True
    if (num != 1):
        while counter <= numSqrt:
            if( num % counter == 0):
                isPrime = False
                break
            counter += 1
        if(isPrime):
            return True
        else:
            return False
    else:
        return False

def removePrimes(remList:list):
    primeLess = []
    for i in remList:
        if isPrime(int(i)):
            continue
        else:
            primeLess.append(int(i))
    primeSet = set(primeLess)
    primeLess = list(primeSet)
    return primeLess

print("Input list: ", numList)
print("Sorted list: ",sortedList)
print("Composite list: ",removePrimes(sortedList))
print("Min: {}, Max: {}, Average: {}".format(values[0], values[1], values[2]))





