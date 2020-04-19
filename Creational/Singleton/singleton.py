class MySingleton:
    are_we_instantiated_value = None

    '''
    __new__ happens even before __init__ that would be a constructor for the object created so that's the "first step".
    We override the __new__ method with the tracked class variable that is called "are_we_instantiated_value".
    We first set the "are_we_instantiated_value" to None, then the __new__ gets overridden in a way that if the class
    variable's value is None, we instantiate the object, otherwise we just return the same object all the time.
    This ensures that it's only been created once.
    '''

    def __new__(cls):
        if cls.are_we_instantiated_value is None:
            cls.are_we_instantiated_value = object.__new__(cls)
            cls.internal_value = 10
        return cls.are_we_instantiated_value


# Let's create the first object.
first_object = MySingleton()
# Let's print out the object's internal value.
print(first_object.internal_value)

# Let's set the internal value to 20 to ensure we changed it.
first_object.internal_value = 20
# Let's print out the memory address and the changed value - of the first object.
print(first_object)
print(first_object.internal_value)

# So let's create a second object.
second_object = MySingleton()
# Let's create the second object's internal value to another value
second_object.internal_value = 30
# And see the memory address of the second object!
print(second_object)
# See the second object's internal value and first being the same now?
print(first_object.internal_value)
print(second_object.internal_value)

# You get the idea now I guess
third_object = MySingleton()
third_object.internal_value = 40
print(third_object)
print(third_object.internal_value)
