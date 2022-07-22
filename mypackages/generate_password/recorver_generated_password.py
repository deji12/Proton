from getpass import getpass
import os
from cryptography.fernet import Fernet

user = os.getlogin()

def recorver():

    proton_password = getpass('> What is your Proton account password: ')

    print()

    file_key = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/gibberish.key', 'rb')

    key = file_key.read()

    file_key.close()

    fernet = Fernet(key)

    open_password_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt', 'rb').read()

    decrypted = fernet.decrypt(open_password_file)

    decoded_decrypted = decrypted.decode()

    if proton_password == decoded_decrypted:

        recorvery_path = open(f'C:/Users/{user}/Desktop/Proton/Essentials/RP/recorvery.txt', 'r')	

        read_recorvery_path = recorvery_path.read()

        print(read_recorvery_path)

        recorvery_path.close()

        print()

    else:

        print('> Error, wrong password!')

        print()		