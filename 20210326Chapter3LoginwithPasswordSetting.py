# Login with Password Setting
i = 0

while i < 3:
	password = input('Please input password:')
	if password == 'a123456':
		print('Successful login')
		break
	elif password != 'a123456':
		print('Wrong password')
		if 2-i > 0:
			print('and you still have remaining chance(s):', 2-i)
		else: 
			print('Your account has been locked, and please contact the customer service.')
	i = i + 1