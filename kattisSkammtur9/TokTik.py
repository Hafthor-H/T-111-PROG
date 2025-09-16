n = int(input(""))

tokDict = {}
for i in range(n):
    tokTikker = input("").split()
    if tokTikker[0] in tokDict.keys():
        oldScore = tokDict.pop(tokTikker[0])
        tokDict[tokTikker[0]] = int(tokTikker[1]) + int(oldScore)
    else:
        tokDict[tokTikker[0]] = int(tokTikker[1])

highScore = max(tokDict.values())

for i in tokDict.items():
    if i[1] == highScore:
        print(i[0])
