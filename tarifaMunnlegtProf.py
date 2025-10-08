megabytes = int(input()) #Tökum inn megabytes sem heiltölur
months = int(input()) #Tökum inn months sem heiltölu

remainder = 0 #Summann okkar eftir n+1 mánuði
for i in range(months): #Keyrum einu sinni fyrir hvern mánuð
    use = int(input()) #Notkun í hverjum mánuði
    remainder += megabytes - use #Bætum við remainderinn það sem við eigum í afgang í hverjum mánuði
print(remainder + megabytes) #Prentum remainderinn ásamt 10 megabytum fyrir + 1 mánuðinn

