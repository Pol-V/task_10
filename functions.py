import random
import string
import pprint


def make_groups(number=10):
	letters = string.ascii_letters
	digits = string.digits
	res = []
	for name in range(number):
		name_sep = '-'
		name_lets = ''.join([random.choice(letters) for i in range(2)])
		name_digs = ''.join([random.choice(digits) for i in range(2)])
		res.append(name_lets+name_sep+name_digs)
	return res


def make_students():
	names = ['John', 'Jack', 'Tom', 'Jerry', 'Robin', 'Brad', 'Leo', 'Alex', 'Vlad', 'Helen', 'Angelina', 'Kim', 'Olga',
	         'Kate', 'Sam', 'Kris', 'Dan', 'Pam', 'Lin', 'Karl']
	surnames = ['Dicaprio', 'Hardi', 'Robbi', 'Banderas', 'Suinton', 'Anderson', 'Hanks', 'Smit', 'Jolie', 'Pitt',
	            'Aniston', 'Cooper', 'Todd', 'Limb', 'Kots', 'Taylor', 'Batler', 'Porter', 'Carter', 'Crus']
	res = []
	for student in range(200):
		res.append(' '.join([random.choice(names), random.choice(surnames)]))
	return res


def fill_groups(list_of_groups=make_groups(), names=make_students()):
	dic = {k:[] for k in list_of_groups}
	for key, value in dic.items():
		for numbers in range(random.randint(10,30)):
			value.append(random.choice(names))
	return dic


pprint.pprint(fill_groups())
for i in fill_groups():
	print(len(fill_groups()[i]))


