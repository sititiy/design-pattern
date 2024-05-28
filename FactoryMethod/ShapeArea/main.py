from classes.shapeFactory import ShapeFactory

def calculate_shape_area(name,*args):
    factory = ShapeFactory()
    shape = factory.create_shape(name,*args)
    return shape.area()

circle_area = calculate_shape_area('Circle',2)
rectangle_area = calculate_shape_area('Rectangle',2,3)
