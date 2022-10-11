# tuple : Similar to lists, they are heterogeneous of data, a tupble cannot be changed
a_tuple = ('Vivek', 35, 'Roja', 29, 'Karunya', 3, 'Suhruth', 0)

print(f"length of a_tuple = {a_tuple.__len__()}")
print(f"first element of tuple[0] = {a_tuple[0]}")
print(f"enlarging the tuple in 3x times = {a_tuple * 3}")
print(f"slicing the tuple : {a_tuple[0:2]}")
try:
    a_tuple[0] = 'VIVEK'
except TypeError as ex:
    print(ex)