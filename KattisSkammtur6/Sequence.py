n = int(input())
listinn = [1,2,3]

for i in range(3, n):
    nextNum = listinn[i-1] + listinn[i-2] + listinn[i-3]

    listinn.append(nextNum)


for j in range(len(listinn)):
    print(listinn[j])


