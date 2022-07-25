import json
import progressbar
import urllib.request
import os
import requests
import time

user = os.getlogin()

def download_template():
    print()

    print('> Retrieving data..')
    print()
    time.sleep(2)
    token = open(f'C:/Users/{user}/Desktop/Proton/Essentials/token.txt', 'r').read()

    email = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/email.txt', 'r').read()
    response = requests.get(
        url = 'https://protonva.herokuapp.com/get-available-templates/',
        headers = {
			'authorization': f'Token {token}'
		},
    )
    result = response._content.decode()
    dump = json.dumps(result)
    loaded = json.loads(dump)
    # splitted = result.split("}")[0]

    # print(splitted.split(",")[1])
    print(loaded)


download_template()