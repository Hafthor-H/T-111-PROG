n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)
numbers.reverse()

for i in numbers:
    print(i)