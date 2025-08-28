r, g ,b = input(" ").split()

r = int(r)
g = int(g)
b = int(b)

if (r == 255 and g == 255 and b == 255):
    print("hvitur")
elif (r == 0 and g == 0 and b == 0):
    print("svartur")
elif(r > g and r > b):
    print("raudur")
elif(g > r and g > b):
    print("graenn")
elif(b > g and b > r):
    print("blar")

elif(r == g and b < r):
    print("gulur")
elif(r == b and g < r):
    print("fjolubleikur")
elif(g == b and r < g):
    print("blagraenn")
elif(r == g and g == b):
    print("grar")
else:
    print("othekkt")


