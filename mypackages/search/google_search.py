import os
import datetime 
user=os.getlogin()

def gsearch():

    internet_access = input('> This action requires internet connection. Are you connected(y/n): ').lower()

    print()

    if internet_access == 'y':

        try:

            import pywhatkit as kit

            search = input('> What do you want to search for: ')

            print()

            kit.search(search)

            check_2 = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

            if 'history' in check_2:

                check = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/history')

                if 'GoogleSearchHistory.txt' not in check:

                    create_googleSearch_history_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/history/GoogleSearchHistory.txt', 'w')

                    x = datetime.datetime.now()

                    date_time_search = f'{x.strftime("%A, %d %B. %Y")} / {x.strftime("%I:%M%p")}'

                    create_googleSearch_history_file.write(f'Search: {search} ----- Date/Time of search: {date_time_search} \n')

                    create_googleSearch_history_file.write('')

                elif 'GoogleSearchHistory.txt' in check: 

                    save_googleSearch_history_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/history/GoogleSearchHistory.txt', 'a')

                    x = datetime.datetime.now()

                    date_time_search = f'{x.strftime("%A, %d %B. %Y")} / {x.strftime("%I:%M%p")}'

                    save_googleSearch_history_file.write(f'Search: {search} ----- Date/Time of search: {date_time_search} \n')

                    save_googleSearch_history_file.write('')
            else:
                os.chdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

                os.mkdir('history')

                check = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/history')

                if 'GoogleSearchHistory.txt' not in check:

                    create_googleSearch_history_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/history/GoogleSearchHistory.txt', 'w')

                    x = datetime.datetime.now()

                    date_time_search = f'{x.strftime("%A, %d %B. %Y")} / {x.strftime("%I:%M%p")}'

                    create_googleSearch_history_file.write(f'Search: {search} ----- Date/Time of search: {date_time_search} \n')

                    create_googleSearch_history_file.write('')

                elif 'GoogleSearchHistory.txt' in check: 

                    save_googleSearch_history_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/history/GoogleSearchHistory.txt', 'a')

                    x = datetime.datetime.now()

                    date_time_search = f'{x.strftime("%A, %d %B. %Y")} / {x.strftime("%I:%M%p")}'

                    save_googleSearch_history_file.write(f'Search: {search} ----- Date/Time of search: {date_time_search} \n')

                    save_googleSearch_history_file.write('')

        except:

            print('> Error, connect to the internet and try again')

            print()

    elif internet_access == 'n':

        print('> Error, connect to the internet and try again')

        print()