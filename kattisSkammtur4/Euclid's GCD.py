a = int(input())
b = int(input())

while True:
    if(b == 0):
        break
    a, b = b, a%b
print(a)