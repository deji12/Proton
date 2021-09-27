# # import speech_recognition as sr

# # while True:

# #  	print('>>> Listening...')

# #  	print()

# #  	r = sr.Recognizer()

# #  	mic = sr.Microphone()

# #  	with mic as source:

# #  		r.adjust_for_ambient_noise(source)

# #  		audio = r.listen(source)

# #  	try:

# #  		start = r.recognize_google(audio)

# #  		print(start)

# # 		file = open('C:/Users/Ayodeji/Desktop/listen.txt', 'w')

# # 		write_file = file.write(start)

# # 		write_file.close()

# #  	except:
# #  		print('')
# #  		continue

# import speech_recognition as sr

# while True:

# 	print('> Listening...')

# 	print()

# 	r = sr.Recognizer()

# 	mic = sr.Microphone()

# 	with mic as source:

# 		r.adjust_for_ambient_noise(source)

# 		audio = r.listen(source)

# 		try:

# 			start = r.recognize_google(audio)

# 			print(start)

# 			file = open('C:/Users/Ayodeji/Desktop/listen.txt', 'w')

# 			write_file = file.write(start)

# 		except:
# 			# print('oops!')
# 			continue

# word = 'dhffv ijkilmnop'

# splitted_word = word.split()

# for i in splitted_word:
	
# 	len_splitted_word = len(splitted_word[0])

# 	# print(len_splitted_word)

# 	len_splitted_word2 = len(splitted_word[1]) 

# 	if len_splitted_word > len_splitted_word2:

# 		print(f'First word: {splitted_word[0]}')

# 		print()

# 		print(f'Length of first word: {len_splitted_word} VS Length of second word: {len_splitted_word2}')

# 		print()

# 	else: 

# 		print(f'Second word: {splitted_word[1]}')

# 		print()

# 		print(f'Length of first word: {len_splitted_word} VS Length of second word: {len_splitted_word2}')

# 		print()


# def debt(owe = float(input('> How much do you owe: ')), duration = float(input('> Enter Duration: ')), total_interest = float(input('> Enter interest: '))):

# 	debt = owe

# 	#debt = money owed

# 	interest = total_interest

# 	#interest = interest payed with money owed

# 	timeframe = duration

# 	#timeframe = money needs to be paid within this timeframe

# 	payment_per_month = debt/timeframe

# 	interest_payment_per_month = interest/timeframe

# 	payment_per_month_with_interest = payment_per_month + interest_payment_per_month

# 	print(f'> Monthly Payment: {payment_per_month_with_interest}')

# debt()

# from tkinter.constants import X

while True:

	ask = input('> Operation: ')

	if ask == 'btt':
		
		binary_string = input('> Enter binary number: ')

		print()

		ascii_string = "".join([chr(int(binary, 2)) for binary in binary_string.split(" ")])

		print(ascii_string)

	else:
		text = input('> Enter text: ')

		print()

		code = ' '.join(format(x, 'b') for x in bytearray(text, 'utf-8'))

		print(code)
