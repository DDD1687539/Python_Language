# Coder: Lee
# Time:  2022/11/7 22:04

class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}, cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is opening.")

    def set_number_served(self, number):
        self.number_served = number
        
    def increment_number_served(self, increment):
        self.number_served += increment

    def print_number_served(self):
        print(f"Restaurant {self.restaurant_name} served {self.number_served} people.")

class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def ice_cream_flavors(self):
        for flavor in self.flavors:
            print(flavor)


class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User name: {self.first_name} {self.last_name}")

    def greet_user(self, greeting_words):
        print(self.first_name + ' ' + self.last_name + ', ' + greeting_words)

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []

    def add_privileges(self, privilege):
        self.privileges.append(privilege)

    def show_privileges(self):
        for item in self.privileges:
            print(item)

if __name__ == '__main__':
    admin = Admin('Lee', 'Effort')
    admin.add_privileges('can add post')
    admin.show_privileges()
    admin.add_privileges('can delete post')
    admin.add_privileges('can ban user')
    admin.show_privileges()
    


