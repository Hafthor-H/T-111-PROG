maxValue = 0

while True:
    num = int(input())
    if num < 0:
        break
    else: 
       if num > maxValue:
           maxValue = num
print(maxValue)