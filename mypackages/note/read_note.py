import os
import pyttsx3
from cryptography.fernet import Fernet
import datetime
from getpass import getpass
user=os.getlogin()
engine = pyttsx3.init()

def read_note(Enter_pass, name):
    print('> Notice: Password created at the see notes request is the password to be used here.')

    print()

    find_if_folder_exists = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

    if 'notes' in find_if_folder_exists:

        password_size_path = os.path.getsize(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/pass.txt')

        if password_size_path > 0:

            pass
    
        elif password_size_path == 0:

            create_password = getpass('> Create Password: ')

            print()

            confirm_password = getpass('> Confirm Password: ')

            print()

            key = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/note_content.key', 'rb').read()

            fernet = Fernet(key)

            encoded = confirm_password.encode()

            encrypted = fernet.encrypt(encoded)

            while True:

                if create_password == confirm_password:

                    file_path = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/pass.txt', 'wb').write(encrypted)

                    break

                elif create_password != confirm_password:

                    print('---- Error, passwords do not match. Try again')

                    print()

                    break

        i = 0

        while i < 3:
                    
            while True:

                pass_word = getpass('> Enter password: ')

                print()

                file_pass_path = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/pass.txt', 'rb').read()

                key = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/note_content.key', 'rb').read()

                fernet = Fernet(key)

                decrypted = fernet.decrypt(file_pass_path)

                decoded = decrypted.decode()

                if not pass_word:

                    print('> Error, empty input, enter password')

                    print()

                elif len(Enter_pass) > 2:

                    break

            if decoded == pass_word:

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
                    
                    key = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/note_content.key', 'rb').read()

                    note_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{which_read_choice}.txt', 'rb').readlines()

                    f = Fernet(key)

                    for line in note_file:

                        dec = f.decrypt(line)

                        print(dec.decode())

                        print()

                    x = datetime.datetime.now()

                    new_appended_date = f'% Last accessed on: {x.strftime("%A, %d %B. %Y")} --> At: {x.strftime("%I:%M%p")} --> By: {name} %'.encode()

                    enc_nad = f.encrypt(new_appended_date)

                    note_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{which_read_choice}.txt', 'ab').write(enc_nad)

                    write_space = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/{which_read_choice}.txt', 'a').write('\n')

                    break

            else:

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
                            
                engine.say('suspicious activity detected')

                engine.runAndWait()

                engine.stop()

                exit()

    else:
        print('> There are no notes')

        print()