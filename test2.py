class Shape:
    def __init__(self, color):
        self.color = color

class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)  # Call parent's constructor
        self.width = width
        self.height = height