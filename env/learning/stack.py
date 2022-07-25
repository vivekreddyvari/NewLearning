stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val

for x in range(5):
    push(x)
print(stack)

for x in range(5):
    print(pop())

print(stack)
