# Coder: Lee
# Time:  2022/11/9 10:28

filename = 'pi_digits.txt'

def read_pi_digits():
    with open('pi_digits.txt') as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    print(pi_string)
    print(len(pi_string))

filename_new = 'learning_python.txt'

def learning_python_file_1():
    with open(filename_new) as file_object:
        contents = file_object.read()
    print(contents)

def learning_python_file_2():
    with open(filename_new) as file_object:
        for line in file_object:
            print(line.rstrip())

def learning_python_file_3():
    with open(filename_new) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip().replace('python', 'solidity'))

if __name__ == '__main__':
    learning_python_file_3()



