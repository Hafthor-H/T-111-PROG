import math

num = int(input())
numSqrt =  math.sqrt(num)
counter = 2
isPrime = True

if (num != 1):
    while counter <= numSqrt:
        if( num % counter == 0):
            isPrime = False
            break
        counter += 1
    if(isPrime):
        print("Prime")
    else:
            print("Not prime")
else:
    print("Not prime")