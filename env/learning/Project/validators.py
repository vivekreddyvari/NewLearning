import weakref
from numbers import Integral


class IntegerField:

    def __init__(self, min_length=None, max_length=None):
        self.values = {}
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.prop_name} must be a Integer")
        if self.min_length is not None and value < self.min_length:
            raise ValueError(f"{self.prop_name} should be at least min={self.min_length}")
        if self.max_length is not None and value > self.max_length:
            raise ValueError(f"{self.prop_name} must be below the max={self.max_length}")
        instance.__dict__[self.prop_name] = value
        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), int(value))

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            values_tuple = self.values[(id(instance))]
            return values_tuple[1]

    def _remove_object(self, weak_ref):
        reverse_lookup = [key for key, value in self.values.items()
                          if value[0] is weak_ref]
        if reverse_lookup:
            key = reverse_lookup[0]
            del self.values[key]


class CharField:
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.property_name} must be a string")
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f"{self.property_name} should be at least {self.min_length} characters")
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f"{self.property_name} should be at least {self.max_length} characters")
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)



