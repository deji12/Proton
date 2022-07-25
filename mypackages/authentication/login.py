import os
from cryptography.fernet import Fernet
from getpass import getpass
from inquirer import password
user = os.getlogin()
import requests


def login_user_online():

    try:

        i = 0

        while i < 3:

            while True:

                Enter_pass = getpass('Enter Password: ')

                print()

                open_key_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/gibberish.key', 'rb')

                open_username_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/username.txt', 'r').read()

                key = open_key_file.read()

                open_key_file.close()

                fernet = Fernet(key)

                open_pass_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt', 'rb').read()

                decrypted = fernet.decrypt(open_pass_file)

                decode_decrypted = decrypted.decode()

                print()

                if not Enter_pass:

                    print('> Error, empty input, enter password')

                    print()

                elif len(Enter_pass) > 2:

                    break
            
            # file_open = open(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt', 'rb')

            # read_file = file_open.read()

            # print(read_file)

            if Enter_pass != decode_decrypted:

                i += 1

                print('----Error, wrong password. Try again')

                print()

                print(f'>> Tries left: {3 - i}')

                print()

            elif Enter_pass == decode_decrypted:
    
                check_if_new_backups_exist_for_new_user = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/')
                if 'username.txt' in check_if_new_backups_exist_for_new_user:
                    username = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/username.txt', 'r').read()
                    email = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/email.txt', 'r').read()
                    first_name = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/first_name.txt', 'r').read()
                    last_name = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/last_name.txt', 'r').read()
                    password = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/pass.txt', 'r').read()
                    hobby = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/hobby.txt', 'r').read()
                    gender = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/gender.txt', 'r').read()

                    url = 'https://protonva.herokuapp.com/create-user/'
                    response = requests.post(
                        url,
                        json = {
                            'username': username,
                            'email': email,
                            'first_name': first_name,
                            'last_name': last_name,
                            'password': password,
                            're_password': password
                        }
                            ) 

                    profile_url = 'https://protonva.herokuapp.com/create-profile/'
                    response = requests.post(
                        profile_url,
                        json = {
                            'email': email,
                            'gender': gender,
                            'hobby': hobby
                        }
                    )

                    os.remove(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/username.txt')
                    os.remove(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/email.txt')
                    os.remove(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/first_name.txt')
                    os.remove(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/last_name.txt')
                    os.remove(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/pass.txt')
                    os.remove(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/hobby.txt')
                    os.remove(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/gender.txt')

                else:
                    pass

                login_url = 'https://protonva.herokuapp.com/token/login/'
                response = requests.post(
                    login_url,
                    json  = {
                        'username': open_username_file,
                        'password': Enter_pass,
                    }
                )

                LOGIN_TOKIN = response._content.decode().split(":")[1].strip('""}')

                save_token = open(f'C:/Users/{user}/Desktop/Proton/Essentials/token.txt', 'w').write(LOGIN_TOKIN)

                print('> Updating Profile...')
                print()

                token = open(f'C:/Users/{user}/Desktop/Proton/Essentials/token.txt', 'r').read()
                email = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/email.txt', 'r').read()


                    #send generated password to api for saving
                check_if_new_backups_exist_for_generated_password = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/generated_passwords/')
                if not check_if_new_backups_exist_for_generated_password:
                    pass
                else:
                    for i in check_if_new_backups_exist_for_generated_password:
                        password_val = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/generated_passwords/{i}', 'r').read()
                        response = requests.post(
                            url= 'https://protonva.herokuapp.com/save-generated-password/',
                            headers = {
                                'authorization': f'Token {token}'
                            },
                            json = {
                                'email': email,
                                'password': password_val
                            }
                        )

                        os.remove(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/generated_passwords/{i}')

                # send new notes to api for saving
                check_if_new_backups_exist_for_note = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/notes/')
                if not check_if_new_backups_exist_for_note:
                    pass
                else:
                    for i in check_if_new_backups_exist_for_note:
                        note_content = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/notes/{i}', 'r').read()
                        note_name = i.split(".")[0]
                        response = requests.post(
                            url = 'https://protonva.herokuapp.com/add-note/',
                            headers = {
                                'authorization': f'Token {token}'
                            },
                            json = {
                                'email': email,
                                'name': note_name,
                                'body': note_content
                            }
                        )
                        os.remove(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/notes/{i}')



                
                break

            if i == 3:

                print('>>>> CLOSING PROTON')

                exit()
    
    except:
        i = 0

        while i < 3:

            while True:

                Enter_pass = getpass('Enter Password: ')

                open_key_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/gibberish.key', 'rb')

                open_username_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/username.txt', 'r').read()

                key = open_key_file.read()

                open_key_file.close()

                fernet = Fernet(key)

                open_pass_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt', 'rb').read()

                decrypted = fernet.decrypt(open_pass_file)

                decode_decrypted = decrypted.decode()

                print()

                if not Enter_pass:

                    print('> Error, empty input, enter password')

                    print()

                elif len(Enter_pass) > 2:

                    break
            
            # file_open = open(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt', 'rb')

            # read_file = file_open.read()

            # print(read_file)

            if Enter_pass != decode_decrypted:

                i += 1

                print('----Error, wrong password. Try again')

                print()

                print(f'>> Tries left: {3 - i}')

                print()

            elif Enter_pass == decode_decrypted:
                
                break

            if i == 3:

                print('>>>> CLOSING PROTON')

                exit()

def login_user_locally():
    
    i = 0

    while i < 3:

        while True:

            Enter_pass = getpass('Enter Password: ')

            open_key_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/gibberish.key', 'rb')

            open_username_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/username.txt', 'r').read()

            key = open_key_file.read()

            open_key_file.close()

            fernet = Fernet(key)

            open_pass_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt', 'rb').read()

            decrypted = fernet.decrypt(open_pass_file)

            decode_decrypted = decrypted.decode()

            print()

            if not Enter_pass:

                print('> Error, empty input, enter password')

                print()

            elif len(Enter_pass) > 2:

                break
            
        # file_open = open(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt', 'rb')

        # read_file = file_open.read()

        # print(read_file)

        if Enter_pass != decode_decrypted:

            i += 1

            print('----Error, wrong password. Try again')

            print()

            print(f'>> Tries left: {3 - i}')

            print()

        elif Enter_pass == decode_decrypted:
                
            break

        if i == 3:

            print('>>>> CLOSING PROTON')

            exit()

import time
def login_user():

    connected = input('> Greetings. Are you connected to a stablee internet(y/n): ')
    print()
    if connected == 'y' or connected == 'Y' or connected == 'yes':
        try:
            login_user_online()

        except:
            print()
            print('Network Error, Try again')
            print()
            login_user_locally()

    elif connected == 'n' or connected == 'N' or connected == 'no':
        print('> Ok')
        print()
        login_user_locally()

    else:
        print('> I do not understand')
        print()
