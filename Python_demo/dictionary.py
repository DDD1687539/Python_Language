# Coder: Lee
# Time:  2022/11/7 10:17

def alien_function():
    alien = {'color': 'green', 'points': 5}
    new_points = alien['points']
    print("You just earned " + str(new_points) + " points!")

    print('---------------------------------------')
    print('Before del: ', end='')
    print(alien)
    del alien['color']
    print('After del: ', end='')
    print(alien)

def dict_function():
    info = {'first_name': 'Blockchain',
            'last_name': 'Lee',
            'age': 26,
            'city': 'FuZhou'}
    for item in info:
        print(item + ":" + str(info[item]))

    print('---------------------------------------')
    for k, v in info.items():
        print('key is ' + k + ', value is ' + str(v))

    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
    }

    print("The following languages have been mentioned: ")
    for language in favorite_languages.values():
        print(language.title())

def dict_insertion():
    dictionary = {
        'C': "Basic Language",
        'C++': "Application Language",
        'Python': "Script Language",
        'Java': "Web Language",
        'Shell': "Script Language"
    }

    for k, v in dictionary.items():
        print('Key is ' + k, end=', ')
        print('Value is ' + v)

    dictionary['if'] = 'control keyword'
    dictionary['int'] = 'variable type'
    dictionary['def'] = 'function definition'
    dictionary['class'] = 'class keyword'
    dictionary['+'] = 'algorithm operator'

    for k, v in dictionary.items():
        print('Key is ' + k, end=', ')
        print('Value is ' + v)

def river_function():
    rivers = {
        'nile': 'Egypt',
        'the yellow river': 'China',
        'The Mississippi River': 'America'
    }

    for k, v in rivers.items():
        print("The " + k.title() + " runs through " + v.upper())

    print('-----------------------------------------')
    for item in rivers.keys():
        print(item.title())

    print('-----------------------------------------')
    for item in rivers.values():
        print(item.title())

def aliens_fun():
    alien_0 = {'color': 'green', 'points': 5}
    alien_1 = {'color': 'yellow', 'points': 10}
    alien_2 = {'color': 'red', 'points': 15}

    aliens = [alien_0, alien_1, alien_2]
    for alien in aliens:
        print(alien)

def pizza_fun():
    pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese']
    }

    print("You ordered a " + pizza['crust'] + '-crust pizza' +
          "with the following toppings:")

    for topping in pizza['toppings']:
        print("\t" + topping)

def many_users_fun():
    users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton'
        },

        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris'
        },
    }

    for username, user_info in users.items():
        print("Username: " + username)
        full_name = user_info['first'] + " " + user_info['last']
        location = user_info['location']

        print('\tFull name: ' + full_name.title())
        print('\tLocation: ' + location.title())
        print()

def people_fun():
    people_0 = {'Lee', 'Lin'}
    people_1 = {'Huang', 'Zheng'}
    people_2 = {'Tree', 'Micheal'}

    dictionary = []
    dictionary.append(people_0)
    dictionary.append(people_1)
    dictionary.append(people_2)
    for item in dictionary:
        print(item)
        print('------------------------------')

def input_fun():
    while True:
        car = input("Pls input what car you want: ")
        if car == 'quit':
            break
        print(f'Let me see if I can find you a {car}')

def order_table():
    num = int(input('How many guests are coming to dinner?'))
    if num > 8:
        print("There is no empty seats.")
    else:
        print("Ok, We will serve.")

def times_of_ten():
    num = int(input('Pls input a number?'))
    if num % 10 == 0:
        print(f'Number {num} is divisible by 10.')
    else:
        print(f'Number {num} can not be divisible by 10')

def confirmed_users_fun():
    unconfirmed_users = ['alice', 'brian', 'candace']
    confirmed_users = []

    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print("Verifying user: " + current_user.title())
        confirmed_users.append(current_user)

    print('\nThe following users have been confirmed: ')
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())

    print('-------------------------------------')
    print('unconfirmed_users: ', end=' ')
    print(unconfirmed_users)
    print('confirmed_users: ', end=' ')
    print(confirmed_users)

def mountain_poll_fun():
    responses = {}
    polling_active = True

    while polling_active:
        name = input('What is your name? ')
        response = input("Which mountain would you like to climb someday?")

        responses[name] = response
        repeat = input("Would you like to let another person respond?(yes/no)")
        if repeat == 'no' or repeat == 'No':
            polling_active = False

    print("\n--------- Poll Results ---------")
    for name, response in responses.items():
        print(name + " would like to climb " + response + ".")

def sandwich_order_fun():
    sandwich_orders = ['Grilled cheese sandwich', 'pastrami', 'Vegetable sandwich',
                       'pastrami', 'Chicken sandwich', 'pastrami']
    finished_orders = []

    while sandwich_orders:
        sandwich = sandwich_orders.pop()
        print(sandwich)
        finished_orders.append(sandwich)

    print(sandwich_orders)
    print(finished_orders)

    print('-----------------------------------')
    print('Pastrami sandwich has been sold out.')
    flag = True
    while 'pastrami' in finished_orders:
        finished_orders.remove('pastrami')
        print('remove pastrami')

    print('-----------------------------------')
    print(finished_orders)

def visit_fun():
    prompt = 'If you could visit one place in the world, where would you go? '
    while True:
        place = input(prompt)
        if place == "none":
            break
        else:
            print(f'You wanna go to {place}')

if __name__ == '__main__':
    visit_fun()









