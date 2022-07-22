import os
import pyttsx3
from cryptography.fernet import Fernet
import datetime
from getpass import getpass

engine = pyttsx3.init()
user = os.getlogin()

def see_notes(Enter_pass): 
    find_if_folder_exists = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

    if 'notes' in find_if_folder_exists:

        password_file_size = os.path.getsize(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/pass.txt')

        if password_file_size > 0:
            
            pass

        else:

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

                    file_path = f'C:/Users/{user}/Desktop/Proton/Essentials/notes/pass.txt'

                    filee = open(file_path, 'wb')

                    filee.write(encrypted)

                    filee.close()

                    break

                elif create_password != confirm_password:

                    print('---- Error, passwords do not match. Try again')

                    print()

        i = 0

        while i < 3:

            while True:

                pass_word = getpass('> Enter password: ')

                print()

                key = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/note_content.key', 'rb').read()

                password_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/notes/pass.txt', 'rb').read()

                fernet = Fernet(key)

                decrypted = fernet.decrypt(password_file)

                decoded = decrypted.decode()

                if not pass_word:

                    print('> Error, empty input, enter password')

                    print()

                elif len(Enter_pass) > 2:

                    break
		
            if pass_word == decoded:

                print('> Here are all your notes:')

                print()

                note_list = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/notes')

                note_list.remove('pass.txt')

                for x in range(len(note_list)):

                    rolls = note_list[x]

                    stripped = rolls.split(".")

                    print(stripped[0])

                print()

                break

            elif pass_word != decoded:

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