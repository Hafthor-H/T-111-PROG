class Shape:
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length
    
    def get_perimeter(self):
        return self.width * 2 + self.length * 2

    def __str__(self):
        area = self.get_area()
        perimeter = self.get_perimeter()

        return f"Rectangle with area of {area:.2f} and perimeter of {perimeter:.2f}"