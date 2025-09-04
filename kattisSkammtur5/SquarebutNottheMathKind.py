d = int(input())

for i in range(d):
    print("*", end=" ")
print()
for j in range(d-3):
    print("*",end=" ")
    for k in range(d-2):
        print(" ", end=" ")