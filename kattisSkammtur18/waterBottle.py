class WaterBottle:
    def __init__(self,max_capacity:float = 2.0):
        self.max_capacity = max_capacity
        self.current_contents = 0.0

    def fill(self):
        self.current_contents = self.max_capacity

    def drink(self,ammount):
        if ammount <= 0:
            return 0.0
        elif self.current_contents <= ammount:
            extracted = self.current_contents
            self.current_contents = 0.0
            return extracted
        else:
            self.current_contents -= ammount
            return ammount

    def __str__(self):
        return f"The bottle currently holds {round(self.current_contents,1)}L of water."