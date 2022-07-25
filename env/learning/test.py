print('Mike' > 'Mikey')

try:
    print("5"/10)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("Zero")
except:
    print("some")

x = '\''
print(len(x))

print(3 * 'abc' + 'xyz')
print(ord('c') - ord('a'))
print(chr(ord('z') - 2))

item = [1,2,3,4]

val = item[0]
print(val)