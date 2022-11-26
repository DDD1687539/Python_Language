# Coder: Lee
# Time:  2022/11/8 23:16

from collections import OrderedDict

if __name__ == '__main__':
    favorite_languages = OrderedDict()

    favorite_languages['jen'] = 'python'
    favorite_languages['sarah'] = 'c'
    favorite_languages['edward'] = 'ruby'
    favorite_languages['phil'] = 'python'

    for name, language in favorite_languages.items():
        print(name.title() + "'s favorite language is " +
              language.title() + ".")




