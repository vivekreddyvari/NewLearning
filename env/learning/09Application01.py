

# Application Example: Decorators as validators and its range of use.
class Int:
    def __set_name__(self,
                     owner_class,
                     property_name):
        self.property_name = property_name

    # data descriptor
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.property_name} must be an integer')
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.property_name, None)


class Float:
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    # data descriptor
    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise ValueError(f'{self.property_name} must be an float')
        instance.__dict__[self.property_name] = value

    def __get__(self,
                instance,
                owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.property_name, None)


class List:
    def __set_name__(self,
                     owner_class,
                     property_name):
        self.property_name = property_name

    # data descriptor
    def __set__(self,
                instance,
                value):
        if not isinstance(value, list):
            raise ValueError(
                f'{self.property_name} must be a list'
            )
        instance.__dict__[self.property_name] = value

    def __get__(self,
                instance,
                owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.property_name, None)


class PersonOne:
    age = Int()
    height = Float()
    tags = List()
    favorite_foods = List()


he = PersonOne()

try:
    he.tags = 'abc'
except ValueError as ex:
    print(ex)


class ValidType:

    def __init__(self, type_):
        self._type = type_

    def __set_name__(self,
                     owner_class,
                     property_name):
        self.property_name = property_name

    # data descriptor
    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f'{self.property_name} must be of type {self._type.__name__}')
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.property_name, None)


class PersonTwo:
    age = ValidType(int)
    height = ValidType(float)
    tags = ValidType(list)
    favourite_foods = ValidType(tuple)

heOne = PersonTwo()

try:
    heOne.age = 10.1
except ValueError as ex:
    print(ex)

