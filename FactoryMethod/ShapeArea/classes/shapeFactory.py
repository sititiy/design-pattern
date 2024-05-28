from .circle import Circle
from .rectangle import Rectangle

class ShapeFactory:
    def create_shape(self,name,*args):
        self.shape_classes = {
            "Circle": Circle,
            "Rectangle": Rectangle
        }
        shape_class = self.shape_classes.get(name)
        return shape_class(name,*args)
