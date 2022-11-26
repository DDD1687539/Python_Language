# Coder: Lee
# Time:  2022/11/7 15:40

def display_message():
    print("This chapter refers to function")

def favorite_book(book):
    print(f'One of my favorite books is {book}')

def describe_pet(animal_type, pet_name):
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


def make_shirt(size, words="I love Python"):
    print(f"size is [{size}], words is [{words}]")


def describe_city(city, nation):
    print(f"{city.title()} is in {nation.title()}")

def get_formatted_name_fun(first_name, last_name):
    full_name = first_name + ', ' + last_name
    return full_name.title()

def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

def make_album(music, album, num=''):
    dictionary = {}
    dictionary[music] = album
    if num:
        dictionary['num'] = num

    return dictionary

def function_fun():
    musician = build_person('jimi', 'hendrix', age=27)
    print(musician)

    city_country = {'santiago': 'chile', 'shanghai': 'china', 'tokyo': 'japan'}
    for city, country in city_country.items():
        print(get_formatted_name_fun(city, country))

    album_list = []
    album_0 = make_album('tongji', 'xiaoge', 2)
    album_list.append(album_0)

    album_1 = make_album('SJTU', 'xiaoge')
    album_list.append(album_1)

    album_2 = make_album('shuimuqinghua', 'qinghua')
    album_list.append(album_2)

    album_3 = make_album('Peking', 'beijing')
    album_list.append(album_3)

    for item in album_list:
        print(item)

    while True:
        singer = input('Pls input singer name: ')
        if singer == 'none':
            break
        album_name = input('Pls input album name: ')
        album = make_album(singer, album_name)
        album_list.append(album)

    print('----------------------------------------')
    for item in album_list:
        print(item)

def printing_models_fun():
    unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    completed_models = []

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

    print('--------------------------------------------')
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    magicians_lst_new = []
    for magician in magicians:
        magician_new = f'the Great {magician}'
        magicians_lst_new.append(magician_new)

    magicians.clear()
    for item in magicians_lst_new:
        magicians.append(item)

    return magicians

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile

import pizza

if __name__ == '__main__':
    pizza.make_pizza(16, 'pepperoni')
    pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


