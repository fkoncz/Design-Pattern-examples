from Creational.FactoryMethod.factory import ShapeFactory


def main():
    """ We use the static method in ShapeFactory and call each object's own implementation created with the factory. """
    ShapeFactory.get_shape('square').draw()
    ShapeFactory.get_shape('circle').draw()
    # Uncomment for testing exception if needed
    # ShapeFactory.get_shape('triangle').draw()


main()
