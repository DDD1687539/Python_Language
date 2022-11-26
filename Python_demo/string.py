print('1', '123'.isnumeric())
print('2', '三'.isnumeric())
print('3', '李'.isnumeric())

str = 'hello,Python,Python,Python'
print(str.replace('Python', 'C++', 2))

print(ord('A'))
print(ord('a'))

print(r"Hello\nPython")

language = 'Python'

print(f"{language} is useful.")


def fun(arg1, arg2):
    print("arg1", arg1)
    print("arg2", arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1', arg1)
    print('arg2', arg2)


n1 = 11
n2 = [22, 33, 44]
fun(n1, n2)
print("--------------------")
print(n1)
print(n2)


