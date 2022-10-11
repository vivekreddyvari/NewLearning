from time import time


Abstraction = """
Abstraction: A process that hides the details of a particular function to allow the user
or client to view it a very high level.
ADT: Abstraction data type is logical representation on how we view the data and the operations
that are allowed without regard to how they will be implemented.
"""

Encapsulation  = """
Encapsulation: By providing the high level abstraction, we are encapsulating the details of 
the implementation, basically, hiding the information from users view.
"""

Inheritance = """
Inheritance: Inheritance, referring or using the properties of a function in another function.
e.g. A class Details can be inherited by many other classes Like Employee, Department, etc.
"""

print(f'What is abstraction = {Abstraction}', end='\n\n')
print(f'What is encapsulation = {Encapsulation}', end = '\n\n')
print(f'What is inheritance = {Inheritance}', end = '\n\n')

# Python Basics:
""" Built in numeric classes """
print(f" int is {type(int)}")
print(f" float is {type(float)}")

print(f" Arithmetic Operations are +, -, *, / **, % - modulo operator [remainder] and // ")

# List Operation
a_list = ['True', 'False', '0.0', 1.34, "n", 200, 200]

# Append:   Adds new item to the list
a_list.append('Vivek')
print(a_list)

# insert: Insert an item at the i-th position
a_list.insert(6, 'Roja')
print(a_list)

# pop: remove the last element from the list
a_list.append('Garbage')
print(a_list)
for _ in a_list:
    if _ == 'Garbage':
        a_list.pop()
print(a_list)

# pop: remove i-th item from the list
print(f"removing `n` from the a_list = {a_list.pop(4)}")

# sort: sorting the list
b_list = [1, 8, 9, 11, 19, 3, 14]
print(f"b_list if not sorted {b_list} -> {b_list.sort()} => if sorted, then {b_list}")

# reverse: reverse the list
print(f" the list {a_list} if reversed {a_list.reverse()} => {a_list}")

# index: returns the index of the first occurrence of the item
print(f"the index of the a_list['0.0'] = {a_list.index('0.0')}")

# count: Return the numbers of occurrence of the item.
print(f" `200`s counted in a_list = {a_list.count(200)}")

# remove: removes the first occurrence of the list
print(a_list)
print(f"the first element is removed from {a_list} = {a_list.remove(200)} = {a_list}")

# __add__
number_1 = 999
number_2 = 111

print(f"{number_1} is added to {number_2} = {number_1.__add__(number_2)}")

# range
print(f"range of 10 = {range(10)}")
print(f"list of range(10) = {list(range(10))}")
print(f"list of range(5,10) = {list(range(5,10))}")
print(f"list of odd's range(5,10,2) = {list(range(5,10,2))}")
print(f"list of range(10, 1, -1) = {list(range(10, 1, -1))} ")
