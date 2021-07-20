while True:

		Enter_pass = input('Enter Password: ')

		print()

		if not Enter_pass:

			print('> Error, empty input, enter password')

			print()

		elif len(Enter_pass) > 2:

			break
	