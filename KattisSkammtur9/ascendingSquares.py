n = int(input())

squares = []
for i in range(n+1):
    if i == 0:
        continue
    else:
        square = i**2
        squares.append(square)
print(squares)

