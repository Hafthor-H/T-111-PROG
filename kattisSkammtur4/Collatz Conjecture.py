num = int(input())
print(num)
while True:
    if(num == 1):
        break
    elif (num % 2):
        num = 1 + num * 3 
        print(int(num))
    elif (num % 2) == 0:
        num = num / 2
        print(int(num))
    