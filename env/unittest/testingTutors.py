import unittest
from OOP.Descriptors.env.learning.Project.validatorTutors import IntegerFieldFinal, CharFieldFinal


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)


class TestIntegerField(unittest.TestCase):
    class Person:
        age = IntegerFieldFinal(0, 10)

    def test_set_age_ok(self):
        p = self.Person()
        p.age = 0
        self.assertEqual(0, p.age)


class TestIntegerFieldOne(unittest.TestCase):
    class Person:
        age = IntegerFieldFinal(0, 10)

    def create_person(self, min_, max_):
        self.Person.age = IntegerFieldFinal(5, 10)
        self.Person.age.__set_name__(self.Person, 'age')
        return self.Person()

    def test_set_age_ok(self):
        min_ = 5
        max_ = 10
        p = self.create_person(min_, max_)

        p.age = 5
        self.assertEqual(5, p.age)


class TestIntegerFieldTwo(unittest.TestCase):
    @staticmethod
    def create_test_class(min_, max_):
        obj = type('TestClass', (), {'age': IntegerFieldFinal(min_, max_)})
        return obj()

    def test_set_age_ok(self):
        """ Test that valid values can be assigned / retrieved """
        min_ = 5
        max_ = 10
        obj = self.create_test_class(min_, max_)
        valid_values = range(min_, max_ + 1)

        for i, value in enumerate(valid_values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

    def test_set_age_invalid(self):
        """ Test that valid value raise ValueError exceptions """
        min_ = -10
        max_ = 10

        obj= self.create_test_class(min_, max_)
        bad_values = list(range(min_, -5, min_))
        bad_values += list(range(max_ + 1, max_ + 5))
        bad_values += [10.5, 1 + 0j, 'abc', [1,2]]

        for i, value in enumerate(bad_values):
            with self.subTest(test_number = i):
                with self.assertRaises(ValueError):
                    obj.age = value

    def test_class_get(self):
        """ Test that class attribute retrieval the descriptor instance """
        obj = self.create_test_class(0, 0)
        obj_class = type(obj)
        self.assertIsInstance(obj_class.age, IntegerFieldFinal)

    def test_set_age_min_only(self):
        """Tests that we can specify min value only """

        min_ = 0
        max_ = None
        obj = self.create_test_class(min_, max_)
        values = range(min_, min_ + 100, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

    def test_set_age_max_only(self):
        """Test that we can specify a max value only """
        min_ = None
        max_ = 10
        obj = self.create_test_class(min_, max_)
        values = range(max_ - 100, max_, 10)
        for i, value in enumerate(values):
            with self.subTest(test_numbers=i):
                obj.age = value
                self.assertEqual(value, obj.age)

    def test_set_age_no_limits(self):
        """ Tests that we can use IntegerField without any limitation """
        min_ = None
        max_ = None
        obj = self.create_test_class(min_, max_)
        values = range(-100, 100, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)


class TestCharField(unittest.TestCase):
    @staticmethod
    def create_test_class(min_, max_):
        obj = type('TestClass', (), {'name': CharFieldFinal(min_, max_)})
        return obj()

    def test_set_name_ok(self):
        """ Test that valid values can be assigned / retrieved """
        min_ = 1
        max_ = 10
        obj = self.create_test_class(min_, max_)
        valid_lengths = range(min_, max_ + 1)

        for i, length in enumerate(valid_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.name)

if __name__ == "__main__":
    run_tests(TestIntegerFieldTwo)
    run_tests(TestCharField)