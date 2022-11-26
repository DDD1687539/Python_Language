# Coder: Lee
# Time:  2022/11/8 23:21

from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        current_side = randint(1, self.sides)
        return  current_side

if __name__ == '__main__':
    my_die = Die(6)

    my_die_10 = Die(10)
    my_die_20 = Die(20)

    print('--------------------------------')
    for i in range(0, 10):
        print(my_die.roll_die())

    print('--------------------------------')
    for i in range(0, 10):
        print(my_die_10.roll_die())
        
    print('--------------------------------')
    for i in range(0, 10):
        print(my_die_20.roll_die())


