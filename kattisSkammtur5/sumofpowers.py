k = int(input(""))
n = int(input(""))

summa = 0
for i in range(n):
    x = int(input())
    summa += k**x
    print(summa)

print(summa)