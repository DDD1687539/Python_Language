# Coder: Lee
# Time:  2022/11/8 23:06

from class_car import Car, ElectricCar

if __name__ == '__main__':
    my_beetle = Car('volkswagen', 'beetle', 2016)
    print(my_beetle.get_descriptive_name())

    my_tesla = ElectricCar('tesla', 'roadster', 2016)
    print(my_tesla.get_descriptive_name())
