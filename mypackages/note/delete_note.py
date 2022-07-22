import os
import pyttsx3
from cryptography.fernet import Fernet
import datetime
from getpass import getpass
user=os.getlogin()
engine = pyttsx3.init()

def delete_note():
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