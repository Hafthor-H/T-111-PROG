##Virkar ekki

msg1 = "G`hk+~B`dr`q"
msg2 = "Vd~`ss`bj~`s~c`vm"
msg3 = "Sgd~dmdlx~g`r~addm~o`qsxhmf~`kk~mhfgs"
msg4 = "Aqtstr~hr~`mmnxdc~sg`s~gd~b`m&s~inhm~hm"

# msg1 = "Mfnq1%Hfjxfw&"
# msg2 = "Mt|%nx%ymj%|jfymjwD"
# msg3 = "Ny,x%{jw~%mty%t{jw%mjwj3"
# msg4 = "ux3%Gwzyzx%ktwlty%mnx%xfsifqx3"

firstLine = msg1[:13]

summa = 0
for i in range(len(firstLine)):
    a = ord(firstLine[i])
    summa += a

    
if summa > 1082:
    x = (1082 - summa) // 13
elif summa < 1082:
    x = (summa - 1082) // 13

print(x)


def decoder(msg):
    for k in range(len(msg)):
        b = ord(msg[k])
        c = b + x 
        if(c < 32 or c > 126):
            print("c er fyrir utan")
        utkoma = chr(int(c))
        print(utkoma, end="")
    print()

decoder(msg1)
decoder(msg2)
decoder(msg3)
decoder(msg4)
