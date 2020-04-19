class ShapeInterface:
    # The Shape interface class we only use to have the method signature we want to override.
    def draw(self):
        pass

class Circle(ShapeInterface):
    # Just a class for circle that inherits and implements the ShapeInterface basically in a circle way.
    def draw(self):
        print("We do all the things we need to draw a circle.")


class Square(ShapeInterface):
    # Just a class for circle that inherits and implements the ShapeInterface basically in a square way.
    def draw(self):
        print("We do all the things we need to draw a square.")


class ShapeFactory:
    """
    This is our Shape Factory. We don't need staticmethod decorator, but it makes it easy to call the get_shape
    without creating an object from ShapeFactory. If the passed in type is any of the given, it will return an object
    type of the given as a centralized factory. Now this could be used to reuse of many, same configurations like
    when we have animals/machines all the same kind but they'd start/be configured differently. So they'd implement
    their own ways, but with this common method we just use the class as a factory basically.
    """
    @staticmethod
    def get_shape(type_of_shape):
        if type_of_shape == 'circle':
            return Circle()
        elif type_of_shape == 'square':
            return Square()
        assert 0, f"Can't find type {type_of_shape}"
