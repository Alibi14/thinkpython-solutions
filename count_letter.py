def func(word, letter, starting):
	count = 0
	new_var = word[starting:] 
	print(new_var)
	for index in new_var:
		if letter == index:
			count += 1

	print (count)

func('ananas', 'a', 0)
