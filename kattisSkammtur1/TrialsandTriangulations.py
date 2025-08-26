import math

a = float(input(""))
b = float(input(""))
c = float(input(""))

s = (a+b+c)/2
svar = math.sqrt((s*(s-a)*(s-b)*(s-c)))
print(svar)
