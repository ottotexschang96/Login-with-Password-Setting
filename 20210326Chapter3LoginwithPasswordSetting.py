# Login with Password Setting
i = 0

while i < 3:
	password = input('Please input password:')
	if password == 'a123456':
		print('Successful login')
		break
	elif password != 'a123456':
		print('Wrong password, and you still have remaining chance(s):', 2-i)
	i = i + 1