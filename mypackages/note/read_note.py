import os
import pyttsx3
from cryptography.fernet import Fernet
import datetime
from getpass import getpass
user=os.getlogin()
engine = pyttsx3.init()
import time

def read_note(name):
    find_if_folder_exists = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

    if 'notes' in find_if_folder_exists:

        note_list = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/notes')

        note_list.remove('pass.txt')

        print('> Here are all your available notes: ')

        print()

        for x in range(len(note_list)):

            rolls = note_list[x]

            stripped = rolls.split(".")

            print(stripped[0])

        print()

        which_read_choice = input('> Which note will you like to read: ')

        print()

        check = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/notes')

        if f'{which_read_choice}.txt' not in check:

            print(f'> Error, "{which_read_choice}" does not exist')

            print()

        else:

            print(f'Retrieving {which_read_choice}...')
            print()
            time.sleep(3)
     
            key = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/note_content.key', 'rb').read()

            note_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{which_read_choice}.txt', 'rb').readlines()

            f = Fernet(key)

            for line in note_file:

                dec = f.decrypt(line)

                print(dec.decode())

                print()

            x = datetime.datetime.now()

            new_appended_date = f'% Accessed on: {x.strftime("%A, %d %B. %Y")} --> At: {x.strftime("%I:%M%p")} --> By: {name} %'.encode()

            enc_nad = f.encrypt(new_appended_date)

            note_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{which_read_choice}.txt', 'ab').write(enc_nad)

            write_space = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{which_read_choice}.txt', 'a').write('\n')


    else:
        print('> There are no notes')

        print()

    