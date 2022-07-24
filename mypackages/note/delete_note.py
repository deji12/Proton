import os
import pyttsx3
from cryptography.fernet import Fernet
import datetime
from getpass import getpass
user=os.getlogin()
engine = pyttsx3.init()
import requests

def delete_note_online_and_offline():
    find_if_folder_exists = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

    if 'notes' in find_if_folder_exists:

        note_list = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/notes')

        note_list.remove('pass.txt')

        for x in range(len(note_list)):

            rolls = note_list[x]

            stripped = rolls.split(".")

            print(stripped[0])

            print()
        
        del_file = input('> Enter note you want to delete: ')

        print()

        if os.path.exists(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{del_file}.txt'):

            token = open(f'C:/Users/{user}/Desktop/Proton/Essentials/token.txt', 'r').read()

            email = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/email.txt', 'r').read()

            response = requests.post(
				url = 'http://127.0.0.1:8000/delete-note/',
				headers = {
					'authorization': f'Token {token}'
				},
				json = {
					'email': email,
					'name': del_file,
				}
			)

            os.remove(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{del_file}.txt')

            rate = engine.getProperty('rate')

            engine.setProperty('rate', 125)

            print(f'> Note has been deleted successfully')

            engine.say(f'> Note has been deleted successfully')

            print()

            engine.runAndWait()

            engine.stop()	

        else:

            print(f'---- Error, {del_file} does not exist')

            print()

            rate = engine.getProperty('rate')

            engine.setProperty('rate', 125)

            engine.say(f' Error, {del_file} does not exist')

            engine.runAndWait()

            engine.stop()

        print()		
    
    else:
        print('> There are no notes')

        print()

def delete_note_offline():

    find_if_folder_exists = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

    if 'notes' in find_if_folder_exists:

        note_list = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/notes')

        note_list.remove('pass.txt')

        for x in range(len(note_list)):

            rolls = note_list[x]

            stripped = rolls.split(".")

            print(stripped[0])

            print()
        
        del_file = input('> Enter note you want to delete: ')

        print()

        if os.path.exists(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{del_file}.txt'):

            os.remove(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{del_file}.txt')

            rate = engine.getProperty('rate')

            engine.setProperty('rate', 125)

            print(f'> Note has been deleted successfully')

            engine.say(f'> Note has been deleted successfully')

            print()

            engine.runAndWait()

            engine.stop()	

        else:

            print(f'---- Error, {del_file} does not exist')

            print()

            rate = engine.getProperty('rate')

            engine.setProperty('rate', 125)

            engine.say(f' Error, {del_file} does not exist')

            engine.runAndWait()

            engine.stop()

        print()		
    
    else:
        print('> There are no notes')

        print()

def delete_note():
    connected = input('> Are you connected to the internet(y/n): ')
    print()
    if connected == 'y' or connected == 'yes' or connected == 'Y':
        try:
            delete_note_online_and_offline()
        except:
            delete_note_offline()
    elif connected == 'n' or connected == 'N' or connected == 'no':
        delete_note_offline()
    else:
        print('> I do not unserstand')
