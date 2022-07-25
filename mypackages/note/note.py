import os
import pyttsx3
from cryptography.fernet import Fernet
import datetime
import requests


engine = pyttsx3.init()
user = os.getlogin()

def note(name):

	find_if_folder_exists = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

	if 'notes' not in find_if_folder_exists:

		os.chdir(f'C:/Users/{user}/Desktop/Proton/Essentials/')

		os.mkdir('notes')

		make_password_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/pass.txt', 'w')

		make_password_file.close()

		gen_key = Fernet.generate_key()

		write_note_key = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/note_content.key', 'wb').write(gen_key)

	else:
		pass

	while True:

		new_note_input = input('> Name of new note: ')

		print()

		find_if_note_exists = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/notes')

		if f'{new_note_input}.txt' in find_if_note_exists:

				print(f'---- Error, a note with the name "{new_note_input}" already exists. Pick a new name')
					
				print()

		else:

			

			print()


			x = datetime.datetime.now()

			datetime_of_creation = f'% Date of creation: {x.strftime("%A, %d %B. %Y")} --> Time of creation: {x.strftime("%I:%M%p")} %'.encode()

			new_note_content = input('> Body: ')

			token = open(f'C:/Users/{user}/Desktop/Proton/Essentials/token.txt', 'r').read()

			email = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/email.txt', 'r').read()

			response = requests.post(
				url = 'https://protonva.herokuapp.com/add-note/',
				headers = {
					'authorization': f'Token {token}'
				},
				json = {
					'email': email,
					'name': new_note_input,
					'body': new_note_content
				}
			)

			created_note = f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{new_note_input}.txt'

			created_note_ = open(created_note, 'x')

			created_note_.close()

			# print(response._content)

			new_note_content_ = f'-----> Body: {new_note_content} <-----'.encode()

			print()

			key = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/note_content.key', 'rb').read()

			fernet = Fernet(key)

			enc_datetime = fernet.encrypt(datetime_of_creation)

			con_enc = fernet.encrypt(new_note_content_)

			write_date_time = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{new_note_input}.txt', 'wb').write(enc_datetime)

			write_space = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{new_note_input}.txt', 'a').write('\n')

			write_note_con = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{new_note_input}.txt', 'ab').write(con_enc)

			write_space2 = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{new_note_input}.txt', 'a').write('\n')

			rate = engine.getProperty('rate')

			engine.setProperty('rate', 125)

			print(f'> Note has been saved {name}')

			print()

			engine.say(f'> Note has been saved {name}')

			engine.runAndWait()

			engine.stop()

			break

def create_note_locally(name):
	find_if_folder_exists = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

	if 'notes' not in find_if_folder_exists:

		os.chdir(f'C:/Users/{user}/Desktop/Proton/Essentials/')

		os.mkdir('notes')

		make_password_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/pass.txt', 'w')

		make_password_file.close()

		gen_key = Fernet.generate_key()

		write_note_key = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/note_content.key', 'wb').write(gen_key)

	else:
		pass

	while True:

		new_note_input = input('> Name of new note: ')

		print()

		find_if_note_exists = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/notes')

		if f'{new_note_input}.txt' in find_if_note_exists:

				print(f'---- Error, a note with the name "{new_note_input}" already exists. Pick a new name')
					
				print()

		else:

			print()

			x = datetime.datetime.now()

			datetime_of_creation = f'% Date of creation: {x.strftime("%A, %d %B. %Y")} --> Time of creation: {x.strftime("%I:%M%p")} %'.encode()

			new_note_content = input('> Body: ')

			created_note = f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{new_note_input}.txt'

			create_note_backup = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/notes/{new_note_input}.txt', 'w').write(new_note_content)
			

			created_note_ = open(created_note, 'x')

			created_note_.close()

			new_note_content_ = f'-----> Body: {new_note_content} <-----'.encode()

			print()

			key = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/note_content.key', 'rb').read()

			fernet = Fernet(key)

			enc_datetime = fernet.encrypt(datetime_of_creation)

			con_enc = fernet.encrypt(new_note_content_)

			write_date_time = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{new_note_input}.txt', 'wb').write(enc_datetime)

			write_space = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{new_note_input}.txt', 'a').write('\n')

			write_note_con = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{new_note_input}.txt', 'ab').write(con_enc)

			write_space2 = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{new_note_input}.txt', 'a').write('\n')

			rate = engine.getProperty('rate')

			engine.setProperty('rate', 125)

			print(f'> Note has been saved {name}')

			print()

			engine.say(f'> Note has been saved {name}')

			engine.runAndWait()

			engine.stop()

			break

def create_note(name):
	connected = input('> Are you connected to the internet(y/n): ')
	print()
	if connected == 'y' or connected == 'yes' or connected == 'Y':
		try:
			note(name=name)
		except:
			create_note_locally(name=name)
	elif connected == 'n' or connected == 'N' or connected == 'no':
		create_note_locally(name=name)
	else:
		print('> I do not unserstand')
		