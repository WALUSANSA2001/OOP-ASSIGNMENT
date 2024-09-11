class Shape:
    def __init__(self, name):
        self.name = name  # The name of the shape (e.g., Circle, Square)

    def get_name(self):
        return f"This shape is a {self.name}."

# Checking
shape1 = Shape("Circle")
print(shape1.get_name())

shape2 = Shape("Square")
print(shape2.get_name())