class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self):
        return self.x + self.y

    def __sub__(self):
        return self.x - self.y

    def __mul__(self):
        return self.x * self.y

    def __truediv__(self):
        return self.x / self.y


calc = Calculator(10, 5)

print("Addition: ", calc.__add__())
print("Subtraction: ", calc.__sub__())
print("Multiplication: ", calc.__mul__())
print("Division: ", calc.__truediv__())