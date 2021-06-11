'''
	file containing functions used to query data from users on chess dot com 

	created on: 06/10/21
	created by: CAT
'''

from scoreboard.python.data.users import Users


def test_func():
	for u in Users:
		print("{}: {}".format(u, u.value))


if __name__ == "__main__":
	test_func()