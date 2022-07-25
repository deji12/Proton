import random
import os
import datetime
import array
import requests
user = os.getlogin()

def online_and_offline_generator(name):

    MAX_LEN = int(input('> Character length of password: '))

    print()

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
  
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
				'*', '(', ')', '<']

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)

    rand_upper = random.choice(UPCASE_CHARACTERS)

    rand_lower = random.choice(LOCASE_CHARACTERS)

    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):

        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array('u', temp_pass)

        random.shuffle(temp_pass_list)

    password = ""

    for x in temp_pass_list:

        password = password + x

    print(password)		

    print()

    token = open(f'C:/Users/{user}/Desktop/Proton/Essentials/token.txt', 'r').read()

    email = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/email.txt', 'r').read()


    response = requests.post(
        url= 'https://protonva.herokuapp.com/save-generated-password/',
        headers = {
			'authorization': f'Token {token}'
		},
        json = {
            'email': email,
            'password': password
        }
    )

    password_gen_parent_path = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

    if 'RP' in password_gen_parent_path:

        password_gen_path = open(f'C:/Users/{user}/Desktop/Proton/Essentials/RP/recorvery.txt', 'a')

        x = datetime.datetime.now()

        last_accessed = f'% Created on: {x.strftime("%A, %d %B. %Y")}, At: {x.strftime("%I:%M%p")}, By: {name} % \n'

        password_gen_path.write(f'Generated Password: {password} ----> {last_accessed}')

        password_gen_path.close()

    else: 

        os.chdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

        os.mkdir('RP')

        password_gen_path = open(f'C:/Users/{user}/Desktop/Proton/Essentials/RP/recorvery.txt', 'w')

        x = datetime.datetime.now()

        last_accessed = f'% Created on: {x.strftime("%A, %d %B. %Y")}, At: {x.strftime("%I:%M%p")}, By: {name} % \n'

        password_gen_path.write(f'Generated Password: {password} ----> {last_accessed}')

        password_gen_path.close()

def offline_generator(name):

    MAX_LEN = int(input('> Character length of password: '))

    print()

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
  
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
				'*', '(', ')', '<']

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)

    rand_upper = random.choice(UPCASE_CHARACTERS)

    rand_lower = random.choice(LOCASE_CHARACTERS)

    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):

        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array('u', temp_pass)

        random.shuffle(temp_pass_list)

    password = ""

    for x in temp_pass_list:

        password = password + x

    print(password)		

    print()

    save_password_to_backup = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/generated_passwords/{password}.txt', 'w').write(password)


    password_gen_parent_path = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

    if 'RP' in password_gen_parent_path:

        password_gen_path = open(f'C:/Users/{user}/Desktop/Proton/Essentials/RP/recorvery.txt', 'a')

        x = datetime.datetime.now()

        last_accessed = f'% Created on: {x.strftime("%A, %d %B. %Y")}, At: {x.strftime("%I:%M%p")}, By: {name} % \n'

        password_gen_path.write(f'Generated Password: {password} ----> {last_accessed}')

        save_password_offline = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/generated_passwords/{password}.txt', 'w').write(password)

        save_password_offline.close()

        password_gen_path.close()

    else: 

        os.chdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

        os.mkdir('RP')

        password_gen_path = open(f'C:/Users/{user}/Desktop/Proton/Essentials/RP/recorvery.txt', 'w')

        x = datetime.datetime.now()

        last_accessed = f'% Created on: {x.strftime("%A, %d %B. %Y")}, At: {x.strftime("%I:%M%p")}, By: {name} % \n'

        password_gen_path.write(f'Generated Password: {password} ----> {last_accessed}')

        save_password_offline = open(f'C:/Users/{user}/Desktop/Proton/Essentials/backup/generated_passwords/{password}.txt', 'w').write(password)

        save_password_offline.close()

        password_gen_path.close()

def generator(name='tpg24'):
    connected = input('> Are you connected to the internet(y/n): ')
    print()
    if connected == 'y' or connected == 'yes' or connected == 'Y':
        try:
            online_and_offline_generator(name=name)
        except:
            offline_generator(name=name)
    elif connected == 'n' or connected == 'N' or connected == 'no':
        offline_generator(name=name)
    else:
        print('> I do not unserstand')