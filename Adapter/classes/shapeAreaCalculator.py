from classes.shape import Shape
from classes.circle import Circle
from classes.rectangle import Rectangle

class ShapeAreaCalculator:

    def __init__(self,shape):
        if not isinstance(shape,Shape):
            raise TypeError("Input is not a shape!")
        self.shape = shape

    def calculate(self):
        if isinstance(self.shape,Circle):
            return 'Area of '+ self.shape.name + ' is: ' + self.CircleAdapter(self.shape).get_area()
        elif isinstance(self.shape,Rectangle):
            return 'Area of '+ self.shape.name + ' is: ' + self.RectangleAdapter(self.shape).get_area()
        else:
            raise NotImplementedError('There is no adapter for the input!')

    class CircleAdapter:
        
        def __init__(self,circle):
            if not isinstance(circle,Circle):
                raise TypeError("input is not a circle!")
            self.circle = circle    

        def get_area(self):
            return str(self.circle.area())
        

    class RectangleAdapter:
        
        def __init__(self,rectangle):
            if not isinstance(rectangle,Rectangle):
                raise TypeError("input is not a rectangle!")
            self.rectangle = rectangle    

        def get_area(self):
            return str(self.rectangle.area())
        