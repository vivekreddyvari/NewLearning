# Set: Set is an unordered collection of zero or more immutable python data objects.
# sets do not allow duplicates and are written as comma-delimited values enclosed in curly braces
a_set = {'Vivek', 35, 'Roja', 29, 'Karunya', 3, 'Suhruth', 0}
print(f"a_set = {a_set}")

b_set = {'Vivek', 'Viswanath', 'Surekha', 'Roja', 'Karunya', 'Suhruth', 'None'}
c_set = {'Vivek', 'Viswanath', 'Surekha', 'Roja', 'Karunya', 'Suhruth', 'None'}
print(f"length of a_set= {len(a_set)} and b_set = {len(b_set)}", end='\n\n')
print(f"is element `vivek` in a_set?, {'Vivek' in a_set} ")
print(f"is element `chandu` in a_set?, {'Chandu' in a_set} ")

# Union
print(f" a_set union b_set = {a_set.union(b_set)}")

# intersection
print(f"intersection `return elements common in both sets` = {a_set.intersection(b_set)}")

# difference
print(f"difference will all elements in a_set and not in b_set = {a_set.difference(b_set)}")

# issubset
print(f"whether all elements of one set are in the other = {b_set.issubset(a_set)}")

# add
print(f"Add {b_set.add('Chandu')}, {b_set}")

# remove
print(f"remove {b_set.remove('Chandu'),} {b_set} ")

# pop - Removes an random element from the set
print(f"pop {b_set.pop()}, {b_set}")

# clear
print(f"clears the set {c_set.clear(), c_set}")