from math import inf, sqrt

import random

import os

import datetime

from datetime import date

import pyttsx3

engine = pyttsx3.init()

from playsound import playsound

import speech_recognition as sr

from colorama import init

init()

from colorama import Fore, Back, Style

import wikipedia as wiki

from tkinter import *

# from pyDictionary import pyDictionary

# dictionary = pyDictionary()

min_length = 2

user = input('>>> Laptop user name: ')

print()

file_open = open('pass.txt', 'r')

read_file = file_open.read()

if 'Password' not in read_file:

	print('FIRST TIME USER')

	rate = engine.getProperty('rate')

	engine.setProperty('rate', 125)

	print(engine.say('Greetings human, welcome, I am your very own virtual assistant. Call me proton'))

	print(engine.say('I will need you to create a password, tell me your name, and some details about you. Lets go'))

	engine.runAndWait()

	engine.stop()

	print()

	while True:

		create_password = input('> Create Password: ')

		print()

		connirm_password = input('> Confirm Password: ')

		print()

		if create_password == connirm_password:

			filee = open('pass.txt', 'w')

			filee.write(f'> Password: {connirm_password}')

			filee.close()

			break

		elif create_password != connirm_password:

			print('---- Error, passwords do not match. Try again')

			print()

else:
	pass

file_open.close()

i = 0

while i < 3:

	Enter_pass = input('Enter Password: ')

	print()

	file_open = open('pass.txt', 'r')

	read_file = file_open.read()

	if Enter_pass not in read_file:

		i += 1

		print('----Error, wrong password. Try again')

		print()

		print(f'>> Tries left: {3 - i}')

		print()

	elif Enter_pass in read_file:
		
		break

	if i == 3:

		print('>>>> CLOSING PROTON')

		exit()

print()

filesize = os.path.getsize('about_user.txt')

size = str(filesize)

if size == '0':

	name = input('> What is your name: ')

	print()

	age = input('> How old are you: ')

	print()

	additional_info = input('> Add any other additional information(nil for none): ')

	print()

	hobby = input('> What are your hobbies: ')

	splitted_hobby = hobby.split(',')

	file = open('about_user.txt', 'w')

	file.write(f'> Your name is {name} \n')

	print()

	file.write(f'> You are {age} years old\n')

	print()

	file.write(f'> Some additional Information you told me about you: \n {additional_info} \n')

	print()

	file.write(f'> Your hobbies are: \n {splitted_hobby} \n')

	file.close()

else:
	pass

print('')

playsound(f'C:/Users/{user}/Desktop/Proton/voice/hi.mp3')

while True:

	name = input('> What is your name: ')

	print()
    
	if (len(name) >= min_length and name.isprintable() and name.isalpha()):
        
		break

	else:
		print()

		playsound(f'C:/Users/Ayodeji/Desktop/Proton/voice/error.mp3')
		
		print('>>> Error, name can only contain alphabets')

		print()

		print(name)

		print()

	password_entry = input('Enter Password: ')

	#if password_entry == 


rate = engine.getProperty('rate')

engine.setProperty('rate', 125)	
	
print(engine.say(f'> Hi there {name}'))

print(f'> Hi there {name}')

engine.runAndWait()

engine.stop()
	
print()

# start with unit conversi.txt

calculator2 = open(f'C:/Users/{user}/Desktop/Proton/txt files/calc.txt')

calc2 = calculator2.read()

file_path1 = open(f'C:/Users/{user}/Desktop/Proton/txt files/command.txt')

com = file_path1.read()

help_m = open(f'C:/Users/{user}/Desktop/Proton/txt files/help.txt')

help_me = help_m.read()

constant_ = open(f'C:/Users/{user}/Desktop/Proton/txt files/constants.txt')

constants = constant_.read()

unit_c = open(f'C:/Users/{user}/Desktop/Proton/txt files/unit conversion.txt')

unc = unit_c.read()

print(Fore.BLUE + '>>> Input s or start to start')

print()

print(Fore.BLUE + '>>> Input h or help for help')

print()

print(Fore.BLUE + '>>> Input com or commands to see commands')

playsound(f'C:/Users/{user}/Desktop/Proton/voice/input.mp3')

print()

def main():

	#playsound(f'C:/Users/{user}/Desktop/Proton/voice/how may i help you today.mp3')

	rate = engine.getProperty('rate')

	engine.setProperty('rate', 125)

	print(engine.say(f'How may i help you today {name}'))

	engine.runAndWait()

	engine.stop()
	
	start = input(Fore.GREEN + f'> How may i help you today {name}: ')
	#print(f'>>> How may i help you today {name}')

	print()

	#print('>>> Listening...')

	#print()

	# r = sr.Recognizer()

	# mic = sr.Microphone()

	# with mic as source:

	# 	r.adjust_for_ambient_noise(source)

	# 	audio = r.listen(source)

	# start = r.recognize_google(audio)

	# print(start)

	if start == 'sc' or start == 'see constants':

		playsound(f'C:/Users/{user}/Desktop/Proton/voice/constants.mp3')
		
		print(constants)

	elif start == 'cls':

		os.close('cls')

	# elif start == 'dict':

	# 	word = input('> What word are you searching for: ')

	# 	print('> ', dictionary.meaning(word))

	elif start == 'what do you know about me' or start == 'info on me':

		file = open('about_user.txt', 'r')

		read_file = file.read()

		print(read_file)

	elif start == 'new note' or start == 'nn':

		while True:

			new_note_input = input('> Name of new note: ')

			find_if_note_exists = os.listdir(f'C:/Users/{user}/Desktop/Proton/notes')

			if new_note_input in find_if_note_exists:

				print(f'---- Error, a note with the name {new_note_input} already exists. Pick a new name')

			else:

				pass
				
				break

		print()

		created_note = f'C:/Users/{user}/Desktop/Proton/notes/{new_note_input}'

		created_note_ = open(created_note, 'x')

		x = datetime.datetime.now()

		datetime_of_creation = f'% Date of creation: {x.strftime("%A, %d %B. %Y")}, Time of creation: {x.strftime("%I:%M%p")} % \n'

		new_note_content = input('> Body: ')

		print()

		rate = engine.getProperty('rate')

		engine.setProperty('rate', 125)

		print(f'> Note has been saved {name}')

		print(engine.say(f'> Note has been saved {name}'))

		engine.runAndWait()

		engine.stop()

		# note_list_1 = f'C:/Users/{user}/Desktop/Proton/notes/notes.txt'

		# note_list_read_1 = open(note_list_1, 'a')

		# note_list_read_1.write(f'> {new_note_input} \n')

		# created_note_.close()

		opened_new_note = f'C:/Users/{user}/Desktop/Proton/notes/{new_note_input}'

		opened_new_note_ = open(opened_new_note, 'a')

		opened_new_note_.write(f'{datetime_of_creation} \n > Body: {new_note_content} \n \n')

		opened_new_note_.close()

	elif start == 'see notes' or start == 'sn':

		password_path = f'C:/Users/{user}/Desktop/Proton/notes/pass.txt'

		password_path_open = open(password_path, 'r')

		password_path_open_read = password_path_open.read()

		if 'Password' in password_path_open_read:

			pass

		elif 'Password' not in password_path_open_read:

			create_password = input('> Create Password: ')

			print()

			confirm_password = input('> Confirm Password: ')

			print()

			while True:

				if create_password == confirm_password:

					file_path = f'C:/Users/{user}/Desktop/Proton/notes/pass.txt'

					filee = open(file_path, 'w')

					filee.write(f'> Password: {confirm_password}')

					filee.close()

					break

				elif create_password != confirm_password:

					print('---- Error, passwords do not match. Try again')

					print()

		i = 0

		while i < 3:

			file_pass_path = open(f'C:/Users/{user}/Desktop/Proton/notes/pass.txt')

			read_file = file_pass_path.read()
			
			pass_word = input('> Enter password: ')

			print()

			if pass_word in read_file:

				print('> Here are all your notes:')

				print('> Ignore the pass.txt file')

				print()

				note_list = f'C:/Users/{user}/Desktop/Proton/notes'

				note_folder_directory = os.listdir(note_list)

				print(note_folder_directory)

				print()

				break

			elif pass_word not in read_file:

				i += 1

				print('---- Error, wrong password. Try again')

				print()

				print(f'>> Tries left: {3 - i}')

				print()

			if i == 3:

				print('>>> Suspicious activity detected')

				print()

				print('>>>> CLOSING PROTON. GOODBYE.')

				rate = engine.getProperty('rate')

				engine.setProperty('rate', 125)	
					
				print(engine.say('suspicious activity detected'))

				engine.runAndWait()

				engine.stop()

				exit()

	elif start =='read note' or start == 'rn':

		password_path = f'C:/Users/{user}/Desktop/Proton/notes/pass.txt'

		password_path_open = open(password_path, 'r')

		password_path_open_read = password_path_open.read()

		if 'Password' in password_path_open_read:

			pass

		elif 'Password' not in password_path_open_read:

			create_password = input('> Create Password: ')

			print()

			confirm_password = input('> Confirm Password: ')

			print()

			while True:

				if create_password == confirm_password:

					file_path = f'C:/Users/{user}/Desktop/Proton/notes/pass.txt'

					filee = open(file_path, 'w')

					filee.write(f'> Password: {confirm_password}')

					filee.close()

					break

				elif create_password != confirm_password:

					print('---- Error, passwords do not match. Try again')

					print()

		i = 0

		while i < 3:

			file_pass_path = open(f'C:/Users/{user}/Desktop/Proton/notes/pass.txt')

			read_file = file_pass_path.read()
			
			pass_word = input('> Enter password: ')

			print()

			if pass_word in read_file:

				note_list = f'C:/Users/{user}/Desktop/Proton/notes'

				note_folder_directory = os.listdir(note_list)

				print(note_folder_directory)

				print()

				which_read_choice = input('> Which note will you like to read?: ')

				print()

				read_choice = f'C:/Users/{user}/Desktop/Proton/notes/{which_read_choice}'

				read_choice_ = open(read_choice, 'r')

				read_file = read_choice_.read()

				#print(read_file)

				#print()

				x = datetime.datetime.now()
				
				open_for_new_date = open(read_choice, 'a')

				new_appended_date = open_for_new_date.write(f'% This note was accessed on: {x.strftime("%A, %d %B. %Y")}, At: {x.strftime("%I:%M%p")}, By: {name} %')

				#print()

				print(read_file)

				print()

				read_choice_.close()

				break

			elif pass_word not in read_file:

				i += 1

				print('---- Error, wrong password. Try again')

				print()

				print(f'>> Tries left: {3 - i}')

				print()

			if i == 3:

				print('>>> Suspicious activity detected')

				print()

				print('>>>> CLOSING PROTON. GOODBYE.')

				rate = engine.getProperty('rate')

				engine.setProperty('rate', 125)	
					
				print(engine.say('suspicious activity detected'))

				engine.runAndWait()

				engine.stop()

				exit()

	elif start == 'del note' or start == 'delete note' or start == 'dn':

		note_list = f'C:/Users/{user}/Desktop/Proton/notes'

		note_folder_directory = os.listdir(note_list)

		print(note_folder_directory)

		print()

		del_file = input('> Enter note you want to delete: ')

		print()

		if os.path.exists(f'C:/Users/{user}/Desktop/Proton/notes/{del_file}'):

			os.remove(f'C:/Users/{user}/Desktop/Proton/notes/{del_file}')

		else:

			print(f'---- Error, {del_file} does not exist')

			print()

			rate = engine.getProperty('rate')

			engine.setProperty('rate', 125)

			print(engine.say(f' Error, {del_file} does not exist'))

			engine.runAndWait()

			engine.stop()		

		print()

		rate = engine.getProperty('rate')

		engine.setProperty('rate', 125)

		print(f'> Note has been deleted successfully')

		print(engine.say(f'> Note has been deleted successfully'))

		engine.runAndWait()

		engine.stop()		

	elif start == 'make search' or start == 'ms':

		root = Tk()

		root.title('Proton.com . Wikipedia')

		root.geometry('700x675')

		def clear():

			my_entry.delete(0, END)

			my_text.delete(0.0, END)

		def search():

			data = wiki.page(my_entry.get())

			clear()

			my_text.insert(0.0, data.content)	

		my_label_frame = LabelFrame(root, text='Search Wikipedia')

		my_label_frame.pack(pady=20)

		my_entry = Entry(my_label_frame, font=('Helvetica', 18), width=47)

		my_entry.pack(pady=20, padx=20)

		my_frame = Frame(root)

		my_frame.pack(pady=5)

		text_scroll = Scrollbar(my_frame)

		text_scroll.pack(side=RIGHT, fill=Y)

		hor_scroll = Scrollbar(my_frame, orient='horizontal')

		hor_scroll.pack(side=BOTTOM, fill=X)

		my_text = Text(my_frame, yscrollcommand=text_scroll.set, wrap='none', xscrollcommand=hor_scroll.set)

		my_text.pack()

		text_scroll.config(command=my_text.yview)

		hor_scroll.config(command=my_text.xview)

		button_frame = Frame(root)

		button_frame.pack(pady=10)

		search_button = Button(button_frame, text='Lookup', font=('Helvetica', 32), fg='#3a3a3a', command=search)

		search_button.grid(row=0, column=0, padx=20)

		clear_button = Button(button_frame, text='Clear', font=('Helvetica', 32), fg='#3a3a3a', command=clear)

		clear_button.grid(row=0, column=1)


		root.mainloop()

	elif start == 'introduce':

		print('>> Greetings human. I am proton, a virtual assistant designed to carry out a lot of tasks to make life easier.  I was designed by Ayodeji Adesola. You are currently using Proton version 0.2 <<')

		print()

		playsound(f'C:/Users/{user}/Desktop/Proton/voice/introduce.mp3')

	elif start == 'uc' or start == 'unit conversion':

		playsound(f'C:/Users/{user}/Desktop/Proton/voice/unit conversions.mp3')
		
		print(unc)

	elif start == 'game':

		playsound(f'C:/Users/{user}/Desktop/Proton/game audio/games available.mp3')

		print('>>> There are two games available: ')
		
		print('')

		playsound(f'C:/Users/{user}/Desktop/Proton/game audio/rps.mp3')

		print('		> Rock paper scissors(rps for short)')

		print('')

		playsound(f'C:/Users/{user}/Desktop/Proton/game audio/gtng.mp3')

		print('		> Guess the number game(gng for short)')

		print('')

		playsound(f'C:/Users/{user}/Desktop/Proton/game audio/Which would you like to play.mp3')

		play = input('> Which would you like to play?: ')

		print('')

		if play == 'gng':

			playsound(f'C:/Users/{user}/Desktop/Proton/game audio/level 1.mp3')

			print('>>> LEVEL 1')

			print('')

			while True:

				range1 = 77

				player = int(input(f'>>> Guess what number your computer picked within the range 0 - 100: '))

				print('')

				if player < range1:

					print('>>> Too small, try again')

					print('')

				elif player > range1:

					print('>>> Too big, try again')

					print('')

				elif player == range1:

					print('>>> YOU HAVE WON!')

					print('')

					break


			print('NEW LEVEL')

			print()

			print('>>> LEVEL 2')

			while True:

				range2 = 864

				player = int(input(f'>>> Guess what number your computer picked within the range 100 - 900: '))

				print('')

				if player < range2:

					print('>>> Too small, try again')

					print('')

				elif player > range2:

					print('>>> Too big, try again')

					print('')

				elif player == range2:

					print('>>> YOU HAVE WON!')

					break

			print('NEW LEVEL')

			print('')

			print('>>> LEVEL 3')

			while True:

				range3 = 3550

				player = int(input(f'>>> Guess what number your computer picked within the range 1000 - 5000: '))

				print('')

				if player < range3:

					print('>>> Too small, try again')

					print('')

				elif player > range3:

					print('>>> Too big, try again')

					print('')

				elif player == range3:

					print('>>> YOU HAVE WON!')

					print('')

					print('>>> YOU HAVE 3 POINTS!!!')

					print('')

					break


		elif play == 'rps':

			def rps():

				player = 0

				cpu = 0

				while True:
					
					possible_input = ['rock', 'paper', 'scissors']

					while player < 3 and cpu < 3:

						print(Fore.GREEN + '>>> Listening...')
						
						cpu_pick = random.choice(possible_input)

						r = sr.Recognizer()

						mic = sr.Microphone()

						with mic as source:
							r.adjust_for_ambient_noise(source)
							audio = r.listen(source)

						player_pick = r.recognize_google(audio)


						print('')

						print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

						print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

						print('')

						if player_pick == cpu_pick:
							
							print(Fore.WHITE + 'Its a tie!')

							print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

							print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

						elif player_pick == 'rock' or player_pick == 'roar' or player_pick == 'Rock' or player_pick == 'ROCK' or player_pick == 'Roar' or player_pick == 'ROAR' :

							if cpu_pick == 'paper':

								cpu += 1

								playsound(f'C:/Users/{user}/Desktop/Proton/game audio/cpu point.mp3')

								print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

								print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

								print('')

							elif cpu_pick == 'scissors':

								player += 1

								playsound(f'C:/Users/{user}/Desktop/Proton/game audio/player point.mp3')

								print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

								print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

								print('')

						elif player_pick == 'clear':

							os.system('cls')

						elif player_pick == 'paper' or player_pick == 'PAPER' or player_pick == 'Paper' or player_pick == 'pipi' or player_pick == 'PIPA' or player_pick == 'Pipa':

							if cpu_pick == 'rock':

								player += 1

								playsound(f'C:/Users/{user}/Desktop/Proton/game audio/player point.mp3')

								print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

								print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

								print('')

							elif cpu_pick == 'scissors':

								cpu += 1

								playsound(f'C:/Users/{user}/Desktop/Proton/game audio/cpu point.mp3')

								print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

								print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

								print('')

						elif player_pick == 'scissors' or player_pick == 'SCISSORS':

							if cpu_pick == 'rock':

								cpu += 1

								playsound(f'C:/Users/{user}Desktop/Proton/game audio/cpu point.mp3')

								print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

								print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

								print('')

							elif cpu_pick == 'paper':

								player += 1

								playsound(f'C:/Users/{user}Desktop/Proton/game audio/player point.mp3')

								print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

								print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

								print('')

						else:
							print(Fore.RED + 'Invalid input!')

							print('')

					if player > cpu:

						print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

						print(Fore.YELLOW + 'Player wins!')

						playsound(f'C:/Users/{user}/Desktop/Proton/game audio/player wins.mp3')

					else:

						print(Fore.BLUE + 'CPU Wins!')

						playsound(f'C:/Users/{user}/Desktop/Proton/game audio/cpu wins.mp3')


					print('')

			rps()	

	elif start == 'send whatsapp message' or start == 'swm':

		import pywhatkit

		num = input('> Enter recipient number(in format +2349827640745): ')

		print()

		message = input('> Type your message: ')

		print()

		time_input = input('> Enter time this message should be sent(hh, mm format (eg 08, 43)): ')

		splitted_time = time_input.split(',')

		split_1 = splitted_time[0]

		split_2 = splitted_time[1]

		hour = int(split_1)

		minute = int(split_2)

		pywhatkit.sendwhatmsg(num, message, hour, minute, 60)

	elif start == 'date':

		x = datetime.datetime.now()

		rate = engine.getProperty('rate')

		engine.setProperty('rate', 120)

		print(f'> {x.strftime("%A, %d %B. %Y")}')

		print(engine.say(f'> Todays date is {x.strftime("%A, %d %B %Y")}'))

		engine.runAndWait()

		engine.stop()

		print()

	elif start == 'time':
		
		x = datetime.datetime.now()

		#playsound(f'C:/Users/{user}/Desktop/Proton/voice/time.mp3')

		x = datetime.datetime.now()

		rate = engine.getProperty('rate')

		engine.setProperty('rate', 120)

		print(f'> Time: {x.strftime("%I:%M%p")}')

		print(engine.say(f'> The Time is {x.strftime("%I:%M%p")}'))

		engine.runAndWait()

		engine.stop()

		print()

	elif start == 'exit':

		playsound(f'C:/Users/{user}/Desktop/Proton/voice/goodbye.mp3')	
		
		exit()

	elif start == 'ndir':

		def ndir():

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/new directory.mp3')

			ndir_ = input('Name of new directory: ')

			print()
			
			os.chdir(f'C:/Users/{user}/Desktop')
			
			os.mkdir(ndir_)

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/directory created.mp3')

		ndir()

			
	elif start == 'calc':

		playsound(f'C:/Users/{user}/Desktop/Proton/voice/calculate.mp3')
		
		calc=input(f'> Ok {name}, what do you want to calculate: ')

		print()
		
		#print('You have selected: ', calc)

		print()
		

		if calc == 'nothing':

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/ok.mp3')
			
			print('> ok')

		elif calc == 'find odd numbers' or calc == 'fon' or calc == 'prime numbers' or calc == 'pn': 

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/range of values.mp3')
			
			rangee = int(input('Range of numbers: '))

			print()
			
			for i in range(rangee):
				
				if i % 2 == 1:
					
					print(i)

			print()
					
			print('Done')

		elif calc == 'fen' or calc == 'find even numbers':

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/range of values.mp3')
 
			rangee2 = int(input('Range of numbers: '))

			for i in range(rangee2):

				if i % 2 == 0:
					
					print(i) 

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/done.mp3')
 
			print('Done')
 

		#stil under work
		elif calc == 'frequency' or calc == 'fre':
			
			Wavelength=float(input('Wave Length: '))

			print()
			
			print('Frequency: ', 3*10**8/Wavelength,'Hz')

			print()
			
			solution=input('Do you want to see the steps?(yes/y or no/n): ')

			print()
			
			if solution == 'yes' or solution == 'y':
				
				print('Frequency = speed of light/wavelength')

				print()
				
				print('=3*10**8/Wavelength')    

				print()
				
				print(f'=3*10**8/{Wavelength}')

				print()
				
				print('Frequency: ', 3*10**8/Wavelength,'Hz')

				print()
			
			if solution == 'no' or solution == 'n':

				playsound(f'C:/Users/{user}/Desktop/Proton/voice/ok.mp3')
				
				print('Ok')

		
		elif calc == 'wavelength' or calc == 'wl':
			
			frequency=float(input('Frequency: '))
			
			print('Wave length: ', 3*10**8/frequency, 'm/s')
			
			solution=input('Do you want to see the steps?(yes/y or no/n): ')
			
			if solution == 'yes' or solution == 'y':
				
				print('Wavelength= speed of light/frequency')
				
				print('=3*10**8/frequency')    
				
				print(f'=3*10**8/{frequency}')
				
				print('Wavelength: ', 3*10**8/frequency,'Hz')
			
			if solution == 'no' or solution == 'no':
				
				print('Ok')

		
		elif calc == 'energy of a photon when planks constant and frequency are given' or calc == 'eoppf':
			
			frequency=float(input('Frequency: '))
			
			Energy_of_a_photon=6.63*10**-34 * frequency
			
			print('Energy of Photon: ', 6.63*10**-34 * frequency)
			
			ev=input('Are you converting into electron volts? (yes/y or no/n): ')
			
			if ev == 'yes' or ev == 'y':
				
				print('converting to electron volts...')
				
				print('converting to electron volts...')
				
				print('converting to electron volts...')
				
				print('converting to electron volts...')
				
				print('Energy of a photon(ev) : ', 1.602*10**-19*Energy_of_a_photon, 'j')
			
			
			
			elif ev == 'no' or ev == 'n':
				
				print('ok')
			
			solution=input('Do you want to see the steps?(yes/y or no/n): ')
			
			if solution == 'yes' or solution == 'y':
				
				print('Energy of Photon: ', 'planks constant * frequency')
				
				print('Energy of Photon: ', '6.63*10**-34 * frequency')
				
				print(f'Energy of Photon:  6.63*10**-34 * {frequency}')
				
				print('Energy of photon: ', 6.63*10**-34 * frequency,'J')
			
			if solution == 'no' or solution == 'n':
				
				print('Ok')

		
		
		elif calc == 'eoppsw' or calc == 'energy of a photon when planks constant, speed of light, and wavelength are given':
			
			Wavelength=float(input('Wave length: '))
			
			Energy_of_a_photon2=6.63*10**-34*3*10**8/Wavelength
			
			print('Energy of photon: ',6.63*10**-34*3*10**8/Wavelength, 'j')
			
			ev=input('Are you converting into electron volts? (yes/y or no/n): ')
			
			
			if ev == 'yes' or ev == 'y':
				
				print('converting to electron volts...')
				
				print('Energy of a photon(ev) : ', 1.602*10**-19*Energy_of_a_photon2, 'j')
			
			
			elif ev == 'no' or ev == 'n':
				
				print('ok')
			
			solution=input('Do you want to see the steps?(yes/y or no/n): ')
			
			
			if solution == 'yes' or solution == 'y':
				
				print('Energy of Photon: ', 'planks constant * speed of light / wave length')
				
				print('Energy of Photon: ', '6.63*10**-34 * 3*10**8 / wave length')
				
				print(f'Energy of Photon:  6.63*10**-34 * 3*10**8 / {Wavelength}')
				
				print('Energy of photon: ', 6.63*10**-34 * 3*10**8 / Wavelength,'J')
			
			
			
			if solution == 'no' or solution == 'n':

				playsound(f'C:/Users/{user}/Desktop/Proton/voice/ok.mp3')
				
				print('Ok')

		elif calc == 'wf' or calc == 'work function':
			
			threshold_frequency=float(input('Threshold Frequency: '))

			print()
			
			print('Work function: ', 6.63*10**-34*threshold_frequency, 'j')

			print()
			
			solution=input('Do you want to see the steps?(yes/y or no/n): ')
			
			if solution == 'yes' or solution == 'y':

				print()
				
				print('Work function: planks constant * threshold frequency')

				print()
				
				print('6.63*10**-34 * threshold frequency')

				print()
				
				print(f'6.63*10**-34 * {threshold_frequency}')

				print()
				
				print('Work function: ', 6.63*10**-34*threshold_frequency, 'j')

			elif solution == 'no' or solution == 'n':

				print()

				playsound(f'C:/Users/{user}/Desktop/Proton/voice/ok.mp3')
				
				print('Ok')
			
		elif calc == 'energy of a photon when work function and kinetic energy are present':
			
			kinetic_energy_work_function = input('Were kinetic energy given and work function?(yes/y or no/n): ')
			
			if kinetic_energy_work_function == 'yes' or kinetic_energy_work_function == 'y':
				
				KE = float(input('Kinetic Energy: '))
				
				work_function2 = int(input('Work function: '))
				
				result = print('Energy of photon: ', work_function2 + KE, 'j')
				
				print(result)
			
			if kinetic_energy_work_function == 'no' or kinetic_energy_work_function == 'n':
				
				mass = float(input('Mass: '))
				
				velocity = float(input('Velocity: '))
				
				KE2 = (0.5 * mass * velocity)
				
				threshold_frequency3 = float(input('Threshold frequency: '))
				
				work_function3 = (6.63*10**-34 * threshold_frequency3)
				
				print('Energy of a photon: ', KE2 + work_function3, 'j')

		#work ends here
		
		
		
		elif calc == 'what can you calculate' or calc == 'whc':

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/i can calculate.mp3')
			
			print(calc2)

		
		elif calc == 'quadratic equation' or calc == 'qe':

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/quadratic equation.mp3')
			
			a=float(input('a: '))

			print()
			
			b=float(input('b: '))

			print()
			
			c=float(input('c: '))

			print()
			
			
			r = b**2 - 4*a*c
			
			if r > 0:
				
				num_roots = 2
				
				x1 = (((-b) + sqrt(r))/(2*a))
				
				x2 = (((-b) - sqrt(r))/(2*a))
				
				print('The roots are: %f and %f' % (x1, x2))
			
			
			elif r == 0:
				
				num_roots = 1
				
				x = (-b) / 2*a
				
				print('There is one root: ', x)
			
			
			else:
				
				num_roots = 0
				
				print('No roots, discriminant < 0.')

		elif calc == 'percentage' or calc == 'per':

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/percentage, given number.mp3')
			
			num=float(input('Enter given number: '))

			print()

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/percentage, percentage given.mp3')
			
			num2=float(input('Enter the percentage given: '))

			print()
			
			print(num2/100*num)

		elif calc == 'add':

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/addition.mp3')
			
			num1 = float(input('First number: '))

			print()

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/add second number.mp3')
			
			num2 = float(input('Second number: '))

			print()
			
			add = num1 + num2
			
			print('Result: ',add)

		elif calc == 'sub':

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/subtraction.mp3')

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/input first number.mp3')
			
			num1 = float(input('First number: '))

			print()

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/add second number.mp3')
			
			num2 = float(input('Second number: '))

			print()
			
			sub = num1 - num2
			
			print('Result: ',sub)

		elif calc == 'mul':

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/multiplication.mp3')

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/input first number.mp3')
			
			num1 = float(input('First number: '))

			print()

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/add second number.mp3')
			
			num2 = float(input('Second number: '))

			print()
			
			mul = num1 * num2
			
			print('Result: ',mul)

		elif calc == 'div':

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/dividion.mp3')

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/input first number.mp3')
			
			num1 = float(input('First number: '))

			print()

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/add second number.mp3')
			
			num2 = float(input('Second number: '))

			print()
			
			div = num1 / num2
			
			print('Result: ',div) 

		else:

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/i do not understand.mp3')
			
			print('I do not understand')

		print()

		playsound(f'C:/Users/{user}/Desktop/Proton/voice/another operation.mp3')

		Repeat = input('> Do you want to perform another operation?(yes/y or no/n): ').lower()

		print('')
		
		if Repeat == 'yes' or Repeat == 'y': 
			
			main()

		
		elif Repeat == 'back' or Repeat == 'bk':
			
			print(start)

		elif Repeat == 'exit':

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/goodbye.mp3')	
			
			print('Bye', name)
			
			exit()

	else:

		playsound(f'C:/Users/{user}/Desktop/Proton/voice/error2.mp3')
		
		print(f'----- Error, {start}, is not a command, try again')

		print('')

while True:
	
	start = input('> Input s, h, or com: ')

	print()
	
	if start == 's' or start == 'S' or start == 'start':
		
		main()

	elif start == 'h' or start == 'H' or start == 'help':

		playsound(f'C:/Users/{user}/Desktop/Proton/voice/help details.mp3')

		x = input('Do you want me to read the help details to you?(y/n): ')	

		if x == 'y':

			print()

			print(help_me)
			
			playsound(f'C:/Users/{user}/Desktop/Proton/voice/help audio.mp3')

		elif x == 'n':

			print()

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/ok.mp3')
				
			print('> Ok')

			print()
		
			print(help_me)

		elif x != 'y' and x != 'n':

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/i do not understand.mp3')
			
			print('I do not understand')

			print()


	# elif start == 'bk' or start == 'back':
	# 	print() 

	elif start == 'com' or start == 'commands':

		playsound(f'C:/Users/{user}/Desktop/Proton/voice/read commands.mp3')

		x = input('Do you want me to read the commands to you?(y/n): ')

		print()

		if x == 'y':
			
			print(com)

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/commands audio.mp3')

			print()

		elif x == 'n':

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/ok.mp3')
				
			print('> Ok')

			print()

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/runnable commands.mp3')
		
			print(com)

		elif x != 'y' and x != 'n':

			playsound(f'C:/Users/{user}/Desktop/Proton/voice/i do not understand.mp3')
			
			print('I do not understand')

			print()

	elif start == 'exit':

		#playsound(f'C:/Users/{user}/Desktop/Proton/voice/goodbye.mp3')	

		rate = engine.getProperty('rate')

		engine.setProperty('rate', 125)

		print(engine.say(f'I hope i was helpful. Goodbye {name}'))

		engine.runAndWait()

		engine.stop()

		exit()

	else:

		playsound(f'C:/Users/{user}/Desktop/Proton/voice/error2.mp3')
		
		print(f'----- Error, {start}, is not a command, try again')

		print()
	





