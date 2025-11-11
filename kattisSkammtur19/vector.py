import math

class Vector:
    def __init__(self,x = 0,y = 0,z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"[[ {self.x} {self.y} {self.z} ]]"

    def __abs__(self):
        x = self.x**2
        y = self.y**2
        z = self.z**2
        return math.sqrt(x+y+z)

    def __add__(self,other):
        x1 = self.x
        y1 = self.y
        z1 = self.z

        x2 = other.x
        y2 = other.y
        z2 = other.z

        return f"[[ {x1+x2} {y1+y2} {z1+z2} ]]"
    
    def __sub__(self,other):
        x1 = self.x
        y1 = self.y
        z1 = self.z

        x2 = other.x
        y2 = other.y
        z2 = other.z

        return f"[[ {x1-x2} {y1-y2} {z1-z2} ]]"

v = Vector(12,3,4)
print(v)
print(abs(v))

u = Vector(0,10,-14)

w = v - u
print(type(v) == Vector)
print(w)