import sys 

myDict = {}
flag = True

for text in sys.stdin:
    words = text.split()
    if text != "\n" and flag:
        myDict[words[1]] = words[0]
    elif text == "\n":
        flag = False
        continue
    else:
        translation = myDict.get(words[0])
        if translation == None:
            print("eh")
        else:
            print(translation)

