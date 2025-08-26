# import math

# h = int(input(""))
# v = int(input(""))
# vRAD = math.radians(v)
# hypotenuse = h / math.sin(vRAD)
# print(round(hypotenuse))

import math 
h , v = input("").split() 
vRAD = math.radians(int(v))
hypotenuse = int(h) / math.sin(vRAD)
print(math.ceil(hypotenuse))