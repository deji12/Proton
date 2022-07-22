import requests

def convert():
    connected_or_not = input('> This action requires internet connection. Are you connected(y/n): ').lower()

    print()

    if connected_or_not == 'y' or connected_or_not == 'yes':

        try:

            url = 'https://api.exchangerate.host/convert'
            response = requests.get(url, params={
				"from": input('> From Currency(Enter country currency code): ').upper(),
				"to": input('> To Currency(Enter country currency code): ').upper(),
				"amount": input('> Amount: ')
            })
            print()
            data = response.json()['result']
            print(f'> Converted Amount: {data}')

            print()

        except:

            print('> Connect to the internet and try again.')

            print()	
    elif connected_or_not == 'n' or connected_or_not == 'no':

        print('> Connect to the internet and try again.')

        print()	