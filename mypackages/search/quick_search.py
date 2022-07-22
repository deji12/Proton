import pywhatkit as kit
import os
import datetime 
user=os.getlogin()

def quick_searchh():
    internet_access = input('> This action requires internet connection. Are you connected(y/n): ').lower()

    print()

    if internet_access == 'y':

        try:

            quick_search = input('> What do you want to search for: ')

            kit.info(quick_search)

            check_2 = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

            if 'history' in check_2:

                check = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/history')

                if 'QuickSearchHistory.txt' not in check:

                    create_quickSearch_history_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/history/QuickSearchHistory.txt', 'w')

                    x = datetime.datetime.now()

                    date_time_search = f'{x.strftime("%A, %d %B. %Y")} / {x.strftime("%I:%M%p")}'

                    create_quickSearch_history_file.write(f'Search: {quick_search} ----- Date/Time of search: {date_time_search} \n')

                    create_quickSearch_history_file.write('')

                elif 'QuickSearchHistory.txt' in check: 

                    save_quickSearch_history_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/history/QuickSearchHistory.txt', 'a')

                    x = datetime.datetime.now()

                    date_time_search = f'{x.strftime("%A, %d %B. %Y")} / {x.strftime("%I:%M%p")}'

                    save_quickSearch_history_file.write(f'Search: {quick_search} ----- Date/Time of search: {date_time_search} \n')

                    save_quickSearch_history_file.write('')

            else:

                os.chdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

                os.mkdir('history')

                check = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/history')

                if 'QuickSearchHistory.txt' not in check:

                    create_quickSearch_history_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/history/QuickSearchHistory.txt', 'w')

                    x = datetime.datetime.now()

                    date_time_search = f'{x.strftime("%A, %d %B. %Y")} / {x.strftime("%I:%M%p")}'

                    create_quickSearch_history_file.write(f'Search: {quick_search} ----- Date/Time of search: {date_time_search} \n')

                    create_quickSearch_history_file.write('')
                
                elif 'QuickSearchHistory.txt' in check: 

                    save_quickSearch_history_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/history/QuickSearchHistory.txt', 'a')

                    x = datetime.datetime.now()

                    date_time_search = f'{x.strftime("%A, %d %B. %Y")} / {x.strftime("%I:%M%p")}'

                    save_quickSearch_history_file.write(f'Search: {quick_search} ----- Date/Time of search: {date_time_search} \n')

                    save_quickSearch_history_file.write('')
            print()

        except:

            print('> Error, connect to the internet and try again')

            print()

    elif internet_access == 'n':

        print('> Error, connect to the internet and try again')

        print()