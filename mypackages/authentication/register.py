from inquirer import password
import pyttsx3 
engine = pyttsx3.init()
import os
user = os.getlogin()
from getpass import getpass
from cryptography.fernet import Fernet
import requests
import time

def create_user_locally_and_online():
    file_size = os.path.getsize(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt')
    if file_size == 0:
        print('FIRST TIME USER')
        print()
        print('> NOTE: While typing in or trying to create passwords, whatever you type in will not be displayed on the screen but it is being saved. Type in the password and press enter!')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 130)
        engine.say('Greetings human, welcome, I am your very own virtual assistant. Call me proton')
        engine.say('I will need you to create a password, tell me your name, and some details about you. Lets go')
        engine.runAndWait()
        engine.stop()
        print()
        while True:
            username = input('> Enter a username: ')
            print()
            email = input('> Enter your email: ')
            print()
            first_name = input('> First name: ')
            print()
            last_name = input('> Last name: ')
            print()
            create_password = getpass('> Create Password: ')
            print()
            connirm_password = getpass('> Confirm Password: ')
            print()

            if create_password == connirm_password:

                print('> Saving data...')
                print()
                url = 'http://127.0.0.1:8000/create-user/'
                response = requests.post(
                url,
                json = {
                    'username': username,
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                    'password': create_password,
                    're_password': connirm_password
                    }
                ) 
                time.sleep(5)
                print(response._content)

                # success = b'{"success":"User Created Successfully"}'
                # if response._content != success:
                #     print('breaking')
                    

                os.chdir(f'C:/Users/{user}/Desktop/Proton/Essentials')
                os.mkdir('gibberish')
                key = Fernet.generate_key()
                write_key = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/gibberish.key', 'wb')
                write_key.write(key)
                write_key.close()
                open_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/gibberish.key', 'rb')
                key = open_file.read()
                open_file.close()
                encoded = connirm_password.encode()
                fernet = Fernet(key)
                encrypted = fernet.encrypt(encoded)
                filee = open(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt', 'wb')
                filee.write(encrypted)
                filee.close()



                os.chdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

                os.mkdir('AboutUser')
                create_name_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/Name.txt', 'w')
                create_email_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/email.txt', 'w')
                create_hobby_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/hobby.txt', 'w')
                create_username_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/username.txt', 'w')
                create_gender = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/gender.txt', 'w')
                name_input = f'{first_name} {last_name}'
                create_name_file.write(name_input)
                create_name_file.close()
                create_email_file.write(email)
                create_email_file.close()
                create_username_file.write(username)
                create_username_file.close()
                print()
                # age_input = input('> How old are you?: ')
                # create_age_file.write(age_input)
                # create_age_file.close()
                print()
                gender = input('> Gender(m/f): ')
                create_gender.write(gender)
                create_gender.close()
                print()
                hobby_input = input('> What are your hobbies(biking, swimming): ')
                splitted_hobby = hobby_input.split(',')
                create_hobby_file.write(f'{splitted_hobby} \n')
                create_hobby_file.close()
                print()
                # add_info_input = input('> Additional information about you(enter nil for nothing): ')
                # create_additional_info_file.write(add_info_input)
                # create_additional_info_file.close()
                # print()
                print()
                profile_url = 'http://127.0.0.1:8000/create-profile/'
                response = requests.post(
                    profile_url,
                    json = {
                        'email': email,
                        'gender': gender,
                        'hobby': hobby_input
                    }
                )

                print('Retrieving Welcome Information...')
                time.sleep(5)
                open_beginner = open(f'C:/Users/{user}/Desktop/Proton/Essentials/txt files/beginner.txt').read()
                print(open_beginner)
                print()

                break
            
            elif create_password != connirm_password:
                print('---- Error, passwords do not match. Try again')
                print()
    else:
        pass

def create_user_locally():
    file_size = os.path.getsize(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt')
    if file_size == 0:
        print('FIRST TIME USER')
        print()
        print('> NOTE: While typing in or trying to create passwords, whatever you type in will not be displayed on the screen but it is being saved. Type in the password and press enter!')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 130)
        engine.say('Greetings human, welcome, I am your very own virtual assistant. Call me proton')
        engine.say('I will need you to create a password, tell me your name, and some details about you. Lets go')
        engine.runAndWait()
        engine.stop()
        print()
        while True:
            username = input('> Enter a username: ')
            while not username:
                username = input('> Enter a username: ')
            print()
            email = input('> Enter your email: ')
            while not email:
                email = input('> Enter your email: ')
            print()
            first_name = input('> First name: ')
            while not first_name:
                first_name = input('> First name: ')
            print()
            last_name = input('> Last name: ')
            while not last_name:
                last_name = input('> Last name: ')
            print()
            create_password = getpass('> Create Password: ')
            while not create_password:
                create_password = getpass('> Create Password: ')
            print()
            connirm_password = getpass('> Confirm Password: ')
            while not connirm_password:
                connirm_password = getpass('> Confirm Password: ')
            print()

            if create_password == connirm_password:
                os.chdir(f'C:/Users/{user}/Desktop/Proton/Essentials')
                os.mkdir('gibberish')
                key = Fernet.generate_key()
                write_key = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/gibberish.key', 'wb')
                write_key.write(key)
                write_key.close()
                open_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/gibberish.key', 'rb')
                key = open_file.read()
                open_file.close()
                encoded = connirm_password.encode()
                fernet = Fernet(key)
                encrypted = fernet.encrypt(encoded)
                filee = open(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt', 'wb')
                filee.write(encrypted)
                filee.close()

                os.chdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

                os.mkdir('AboutUser')
                create_name_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/Name.txt', 'w')
                create_email_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/email.txt', 'w')
                create_hobby_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/hobby.txt', 'w')
                create_username_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/username.txt', 'w')
                create_gender = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/gender.txt', 'w')
                name_input = f'{first_name} {last_name}'
                create_name_file.write(name_input)
                create_name_file.close()
                create_email_file.write(email)
                create_email_file.close()
                create_username_file.write(username)
                create_username_file.close()
                print()
                


                create_user_backup_username = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/username.txt', 'w').write(username)
                create_user_backup_email = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/email.txt', 'w').write(email)
                create_user_backup_first_name = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/first_name.txt', 'w').write(first_name)
                create_user_backup_last_name = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/last_name.txt', 'w').write(last_name)
                create_user_backup_password = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/pass.txt', 'w').write(create_password)
               
                


            
                print()
                gender = input('> Gender(m/f): ')
                while not gender:
                    gender = input('> Gender(m/f): ')
                if gender != 'm' and gender != 'f':
                    print('> Invalid input')
                    print()
                create_gender.write(gender)
                create_gender.close()
                print()
                hobby_input = input('> What are your hobbies(biking, swimming): ')
                while not hobby_input:
                    hobby_input = input('> What are your hobbies(biking, swimming): ')
                splitted_hobby = hobby_input.split(',')
                create_hobby_file.write(f'{splitted_hobby} \n')
                create_hobby_file.close()

                create_user__profile_backup_hobby = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/hobby.txt', 'w').write(hobby_input)
                create_user__profile_backup_gender = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/authentication/gender.txt', 'w').write(gender)
              


                print()
                # add_info_input = input('> Additional information about you(enter nil for nothing): ')
                # create_additional_info_file.write(add_info_input)
                # create_additional_info_file.close()
                # print()
                print()
                print('Retrieving Welcome Information...')
                time.sleep(5)
                open_beginner = open(f'C:/Users/{user}/Desktop/Proton/Essentials/txt files/beginner.txt').read()
                print(open_beginner)
                print()
                break
            
            elif create_password != connirm_password:
                print('---- Error, passwords do not match. Try again')
                print()

    else:
        pass




def register_new_user():
    connected = input('> Greetings. Are you connected to a stable internet(y/n): ')
    print()
    if connected == 'y' or connected == 'Y' or connected == 'yes':
        try:
            create_user_locally_and_online()
        except:
            print()
            print('Network Error, Try again')
            print()
            create_user_locally()
    elif connected == 'n' or connected == 'N' or connected == 'no':
        print('> Ok')
        print()
        create_user_locally()

    else:
        print('> I do not understand')
        print()
