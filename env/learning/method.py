from time import time, sleep


class Classy:
    def method(self, par):
        print("Method:", par)

obj = Classy()

for i in range(1, 5):
    obj.method(i)


class TestClassy1:
    varia = 2

    def method(self):
        print(self.varia, self.var)


test_obj_1 = TestClassy1()
test_obj_1.var = 3
test_obj_1.method()


# Self parameter is also used to invoke other object/class method from inside the class
class TestClassy2:
    def other(self):
        print('other')

    def method(self):
        print("method", end="\n\n")
        self.other()

test_obj_2 = TestClassy2()
test_obj_2.method()


# Inner life of classes and object
class TestClassy3:

    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass

test_obj_3 = TestClassy3()
print(test_obj_3.__dict__, end='\n\n')
print(TestClassy3.__dict__, end='\n\n')

# Learning
class Snake:
    def __init__(self, victims):
        self.victims = victims

    def increment(self):
        self.__victims += 1


class Emoji:
    def __init__(self, emoji):
        self.emoji = emoji

    def dog(self):
        self.emoji = "\N{dog}"
        return self.emoji

    def horse(self):
        self.emoji = "\N{horse}"
        return self.emoji

d = Emoji('dog')
print(d.dog())
h = Emoji('horse')
print(h.horse())
end = time()
sleep(3)
m, s = divmod(time() - end, 60)
h, m = divmod(m, 60)
time_str = "%02d:%02d:%02d" % (h, m, s)
print(time_str)


