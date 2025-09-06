msg1 = input()
msg2 = input()
msg3 = input()
msg4 = input()

firstLetter = msg1[:1]
x = 72 - ord(firstLetter)

def decoder(msg):
    for k in range(len(msg)):
        b = ord(msg[k])
        c = b + x 
        if(c < 32):
            c += 95
        elif(c > 126):
            c -= 95 
        utkoma = chr(int(c))
        print(utkoma, end="")
    print()

decoder(msg1)
decoder(msg2)
decoder(msg3)
decoder(msg4)
