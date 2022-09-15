class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def get_area(self):
        return self.x * self.y

    def __add__(self, other):  # Plus
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Rectangle(novo_x, novo_y)

    def __sub__(self, other):  # Subtraction
        a1 = self.get_area()
        a2 = other.get_area()
        return a1 - a2

    def __mul__(self, other):  # Multiplication
        a1 = self.get_area()
        a2 = other.get_area()
        return a1 * a2

    def __truediv__(self, other): # You may be wondering? Where's the __div__ method, I think he was replaced, now we use __truediv__, it works the same way.
        a1 = self.get_area()
        a2 = other.get_area()
        return a1 / a2

    def __gt__(self, other):  # Greater than
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 > a2:
            return True
        else:
            return False

    def __lt__(self, other):  # Lower than
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 < a2:
            return True
        else:
            return False

    def __eq__(self, other):  # Equals to
        a1 = self.get_area()
        a2 = other.get_area()
        res = a1 == a2
        return res


r1 = Rectangle(10, 20)
r2 = Rectangle(25, 20)
r3 = r1 - r2
print(r3)
