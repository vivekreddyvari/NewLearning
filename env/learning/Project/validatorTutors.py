import numbers
import weakref


class IntegerField:

    def __init__(self, min_=None, max_=None):
        self._min = min_
        self._max = max_
        self.values = {}

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f"{self.prop_name} must be a Integer")
        if self._min is not None and value < self._min:
            raise ValueError(f"{self.prop_name} should be at least min={self._min}")
        if self._max is not None and value > self._max:
            raise ValueError(f"{self.prop_name} must be below the max={self._max}")
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

    def __init__(self, min_=None, max_=None):
        min_ = min_ or 0
        min_ = max(0, min_)
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.prop_name} must be a string")
        if self._min is not None and len(value) < self._min:
            raise ValueError(f"{self.prop_name} should be at least min={self._min} chars")
        if self._max is not None and len(value) > self._max:
            raise ValueError(f"{self.prop_name} must be below the max={self._max} chars")
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.prop_name, None)


class BaseValidator:

    def __init__(self, min_=None, max_=None):
        min_ = min_ or 0
        min_ = max(0, min_)
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.prop_name, None)

    def validate(self, value):
        # this will need to implemented specifically by each subclass
        pass

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.prop_name] = value


class IntegerFieldFinal(BaseValidator):

    def validate(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f"{self.prop_name} must be a Integer")
        if self._min is not None and value < self._min:
            raise ValueError(f"{self.prop_name} should be at least min={self._min}")
        if self._max is not None and value > self._max:
            raise ValueError(f"{self.prop_name} must be below the max={self._max}")


class CharFieldFinal(BaseValidator):
    def __init__(self, min_, max_):
        min_ = max(min_ or 0, 0)
        super().__init__(min_, max_)

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.prop_name} must be a string")
        if self._min is not None and len(value) < self._min:
            raise ValueError(f"{self.prop_name} should be at least min={self._min} chars")
        if self._max is not None and len(value) > self._max:
            raise ValueError(f"{self.prop_name} must be below the max={self._max} chars")