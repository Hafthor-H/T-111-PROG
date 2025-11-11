from shapes import Shape

class Square(Shape):
    def __init__(self, length):
        super().__init__(length, length)
    
    def __str__(self):
        return super().__str__()