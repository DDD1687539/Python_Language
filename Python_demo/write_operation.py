# Coder: Lee
# Time:  2022/11/9 11:17

import time

filename = 'programming.txt'

def write_message_0():
    with open(filename, 'w') as file_object:
        file_object.write("I love programming.\n")
        file_object.write("I love creating new games.\n")

def write_message_1():
    with open(filename, 'a') as file_object:
        file_object.write("I also love finding meaning in large datasets.\n")
        file_object.write("I love creating apps that can run in a browser.\n")

filename_guest = 'guest.txt'

def input_guest_name_0():
    with open(filename_guest, 'w') as file_object:
        guest_name = input("Pls input guest name: ")
        file_object.write(guest_name)

def input_guest_name_1():
    with open(filename_guest, 'a') as file_object:
        while True:
            guest_name = input("Pls input guest name: ")
            if guest_name == 'none':
                break
            file_object.write(f"{guest_name}\n")

if __name__ == '__main__':
    input_guest_name_1()
