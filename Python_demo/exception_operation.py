# Coder: Lee
# Time:  2022/11/9 11:55

import json

def division_fun_0():
    try:
        print(5 / 0)
    except ZeroDivisionError:
        print("You can't divide by zero!")

def division_fun_1():
    try:
        print(5 / 0)
    except Exception as e:
        print(e)

def addition_fun():
    while True:
        try:
            num_a = int(input("Pls input a number: "))
            num_b = int(input("Pls input another number: "))
        except Exception as e:
            print(e)
        else:
            print("Sum is " + str(num_a + num_b))

        option = input("Would you wanna continue?")
        if option == 'N' or option == 'n':
            break

def read_write_fun():
    try:
        rfile = open('cats.txt', 'r')
        wfile = open('dogs.txt', 'a')
    except Exception as e:
        print("Catch error")
        print(e)
    else:
        wfile.write(rfile.read())

def word_count():
    line = "Row, row, row your boat"
    print("Count of row is " + str(line.count('row')))
    print("Count of row/Row is " + str(line.lower().count('row')))


def number_writer_fun():
    numbers = [2, 3, 5, 7, 11, 13]

    filename_json = 'number.json'
    with open(filename_json, 'w') as file_object:
        json.dump(numbers, file_object)

def remember_me_fun():
    username = input("What is your name?")

    filename_json = 'username.json'
    with open(filename_json, 'w') as file_object:
        json.dump(username, file_object)
        print("We'll remember you when you come back, " + username + "!")

def input_number_fun():
    try:
        favorite_number = input("Pls input your favorite number: ")
    except Exception as e:
        print(e)
        return

    filename_favorite_name = 'favorite_name.json'
    with open(filename_favorite_name, 'w') as file_object:
        json.dump(favorite_number, file_object)
        print("We'll get you, " + str(favorite_number) + "!")

def got_number_fun():
    filename_favorite_name = 'favorite_name.json'
    try:
        with open(filename_favorite_name) as file_object:
            favorite_number = json.load(file_object)
    except FileNotFoundError:
        input_number_fun()
    else:
        print(f"I know your favorite number!It's {favorite_number}")

def refactor_remember_me():
    filename_refactor = 'username.json'
    try:
        with open(filename_refactor) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename_refactor, 'w') as file_object:
            json.dump(username, file_object)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

def get_stored_username():
    filename_stored = 'username.json'
    try:
        with open(filename_stored) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = get_stored_username()
    user = input("Pls input your name: ")
    if username == user and user != "":
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name?")
        filename_greet = 'username.json'
        with open(filename_greet, 'w') as filename_greet:
            json.dump(username, filename_greet)
            print("We'll remember you when you come back, " + username + "!")

def get_stored_number():
    filename_number = 'number.json'
    try:
        with open(filename_stored) as file_object:
            numbers = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return numbers

def additional_info():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name?")
        filename_greet = 'username.json'
        with open(filename_greet, 'w') as filename_greet:
            json.dump(username, filename_greet)
            print("We'll remember you when you come back, " + username + "!")

if __name__ == '__main__':
    greet_user()


