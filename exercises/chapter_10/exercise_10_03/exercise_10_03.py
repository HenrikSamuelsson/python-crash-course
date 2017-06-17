# 10-3. Guest

file_name = 'guests.txt'

with open(file_name, 'w') as file_object:
	print ("Enter your user name: ", end='')
	user_name = input()
	file_object.write(user_name)
