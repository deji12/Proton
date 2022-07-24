import os
import pyttsx3
from cryptography.fernet import Fernet
import datetime
from getpass import getpass

engine = pyttsx3.init()
user = os.getlogin()

def see_notes(): 
    find_if_folder_exists = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

    if 'notes' in find_if_folder_exists:

        print('> Here are all your notes:')

        print()

        note_list = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/notes')

        note_list.remove('pass.txt')

        for x in range(len(note_list)):

            rolls = note_list[x]

            stripped = rolls.split(".")

            print(stripped[0])

        print()

    else:
        print('> There are no notes')

        print()