class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, value):
        self.__stack_list.append(value)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


def test_stack_single():

    stack_object = Stack()

    for x in range(5):
        stack_object.push(x)
        print(f'Push =  x is now incremented by {x}')
    print('\n')
    for x in range(5):
        print(f'POP = from stack a element is deleted: {stack_object.pop()}')


def test_stack_double():
    stack_object1 = Stack()
    stack_object2 = Stack()

    for x in range(5):
        stack_object1.push(x)
        print(f"Push = {x}")
        stack_object2.push(stack_object1.pop())
        print(f"POP in object2: {stack_object2.pop()}")
    print('\n')
