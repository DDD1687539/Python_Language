# Coder: Lee
# Time:  2022/11/6 15:25

import time

def invitation():
	guests = ['张倩格', '刘福姐', '崔惠淼']
	print('----------------------------------------')
	for guest in guests:
		print(f"I'd like to invite {guest} to dinner!")
	
	miss = guests.pop(2)
	print(f"Lady {miss} can not come to dinner")
	
	guests.insert(0, '林其英')
	guests.insert(2, '李强')
	guests.append('林庆德')
	
	print('----------------------------------------')
	for guest in guests:
		print(f"I'd like to invite {guest} to dinner!")
	
	print('----------------------------------------')
	print("Sorry, I only can invite two guests to dinner.")
	while True:
		if len(guests) > 2:
			guest = guests.pop()
			print(f'Sorry {guest}, I can not invite you to dinner.')
		else:
			break
	
	print('----------------------------------------')
	for guest in guests:
		print(f'{guest}, I can invite you to dinner.')
	
	print('----------------------------------------')
	del guests[0]
	del guests[0]
	print('Now the list content are: ' + str(guests))
	
def travel():
	places = ['NewYork', 'HongKong', 'Finland', 'LosAngeles', 'Tokyo']
	for visit in places:
		print(visit, end='  ')
	
	print('-----------------------------------')
	print('Original list:')
	print(places)
	
	print('-----------------------------------')
	print('Sorted list:')
	print(sorted(places))
	
	print('-----------------------------------')
	print('Here is the original list again:')
	print(places)
	
	print('-----------------------------------')
	print('List use reverse():')
	places.reverse()
	print(places)
	
	print('-----------------------------------')
	print('List use reverse() again:')
	places.reverse()
	print(places)
	
	print('-----------------------------------')
	print('List use sort():')
	places.sort()
	print(places)
	
	print('-----------------------------------')
	print('List use sort(reverse=True):')
	places.sort(reverse=True)
	print(places)

def for_function():
	print([value ** 2 for value in range(1, 11)])
	
	lst = list(range(1, 1000001))
	begin_time = time.time()
	summary = sum(lst)
	end_time = time.time()
	time_delta = end_time - begin_time
	print('begin time: ', begin_time)
	print('end time: ', end_time)
	print('time delta: ', time_delta)
	print('summary: ', summary)
	
	lst = list(range(1, 20, 2))
	print("odd number list: ", lst)
	
	lst = list(range(3, 30, 3))
	print("divisible by 3 numbers are: ", lst)
	
	lst = []
	for num in range(1, 11):
		lst.append(num ** 3)
	print(lst)
	
def splice_function():
	players = ['charles', 'martina', 'michael', 'florence', 'eli']
	print(players[-3:4])
	print(players[-3:-5])
	
	my_foods = ['pizza', 'falafel', 'carrot cake']
	friend_foods = my_foods[:]
	print(my_foods)
	print(friend_foods)
	
	my_foods.append('chocolate')
	print(my_foods)
	print(friend_foods)
	
def tuple_function():
	dimensions = (200, 500)
	print(dimensions[0])
	print(dimensions[1])
	
	dimensions = (200, 300, 400, 500, 600, 700)
	for item in dimensions:
		print(item, end='  ')
		
def if_function():
	cars = ['audi', 'bmw', 'subaru', 'toyota']
	for car in cars:
		if car == 'bmw':
			print(car.upper())
		else:
			print(car.title())
	
	print('-------------------------------')
	requested_toppings = ['mushrooms', 'onions', 'pineapple']
	print('mushrooms' in requested_toppings)
	
	age = 17
	if age >= 18:
		print("You are old enough to vote!")
		print("Have you registered to vote yet?")
	else:
		print("Sorry, you are too young to vote.")
		print("Please register to vote as soon as you turn 18!")
	
def select_from_list():
	available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
	requested_toppings = ['mushrooms', 'fresh fries', 'extra cheese']
	
	for requested_topping in requested_toppings:
		if requested_topping in available_toppings:
			print("Adding " + requested_topping + '.')
		else:
			print("Sorry, we don't have " + requested_topping + '.')
	print('Finished making your pizza!')

def login_function():
	users = ['admin', 'Lee', 'Lin', 'David', 'Kobe']
	users.clear()
	if len(users) != 0:
		for user in users:
			if user == 'admin':
				print(f'Hello {user}, would you like to see a status report?')
			else:
				print(f"Hello {user}, thank you for logging in again.")
	else:
		print("We need to find some users!")

def select_users():
	current_users = ['admin', 'Lee', 'Lin', 'David', 'Kobe']
	new_users = ['Lee', 'Glenn', 'Ryan', 'Kobe', "Michael"]
	for user in new_users:
		if user in current_users:
			print(f'{user} has been used, pls input other user name')
		else:
			print(f'{user} has not been used.')

def print_english_nums():
	for num in range(1, 10):
		if num == 1:
			print(f'{num}st')
		elif num == 2:
			print(f'{num}nd')
		elif num == 3:
			print(f'{num}rd')
		else:
			print(f'{num}th')

if __name__ == '__main__':
	print_english_nums()








