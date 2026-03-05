# Super Class


class Shape:
    def __init__(self, color, isFilled):
        self.color = color
        self.isFilled = isFilled

class Circle(Shape):
    def __init__(self,color,isFilled,radious):
        # self.color = color
        # self.isFilled = isFilled
        super().__init__(color,isFilled)
        self.radious = radious


class Square(Shape):
    def __init__(self, color, isFilled, side):
        # self.color = color
        # self.isFilled = isFilled
        super().__init__(color, isFilled)
        self.side = side


class Triangle(Shape):
    def __init__(self,color,isFilled,height,width):
        # self.color = color
        # self.isFilled = isFilled
        super().__init__(color,isFilled)

        self.height = height
        self.width = width
        



circle=Circle("red",True,5)
print(f"{circle.color} {circle.isFilled} {circle.radious}")

