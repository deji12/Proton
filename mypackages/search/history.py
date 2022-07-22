import os
user = os.getlogin()

def search_history():

    check_if_folder_exist = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

    if 'history' in check_if_folder_exist:

        check_if_exist = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/history')

        if 'GoogleSearchHistory.txt' in check_if_exist:

            google_search = open(f'C:/Users/{user}/Desktop/Proton/Essentials/history/GoogleSearchHistory.txt', 'r')

            read_google_history = google_search.read()

            print('> Google search history: ')

            print()

            print(read_google_history)

            google_search.close()

            print()

        elif 'GoogleSearchHistory.txt' not in check_if_exist:

            print('> No Google Search history')

            print()

        check_if_exist2 = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/history')

        if 'QuickSearchHistory.txt' in check_if_exist2:

            quick_search = open(f'C:/Users/{user}/Desktop/Proton/Essentials/history/QuickSearchHistory.txt', 'r')

            read_quick_search_history = quick_search.read()

            print('> Quick search history: ')

            print()

            print(read_quick_search_history)

            print()

            quick_search.close()

        elif 'QuickSearchHistory.txt' not in check_if_exist2:

            print('> No quick Search history')

            print()

    elif 'history' not in check_if_folder_exist:

        os.chdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

        os.mkdir('history')

        check_if_exist = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/history')

        if 'GoogleSearchHistory.txt' in check_if_exist:

            google_search = open(f'C:/Users/{user}/Desktop/Proton/Essentials/history/GoogleSearchHistory.txt', 'r')

            read_google_history = google_search.read()

            print('> Google search history: ')

            print()

            print(read_google_history)

            google_search.close()

            print()

        elif 'GoogleSearchHistory.txt' not in check_if_exist:

            print('> No Google Search history')

            print()

        check_if_exist2 = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials/history')

        if 'QuickSearchHistory.txt' in check_if_exist2:

            quick_search = open(f'C:/Users/{user}/Desktop/Proton/Essentials/history/QuickSearchHistory.txt', 'r')

            read_quick_search_history = quick_search.read()

            print('> Quick search history: ')

            print()

            print(read_quick_search_history)

            print()

            quick_search.close()

        elif 'QuickSearchHistory.txt' not in check_if_exist2:

            print('> No quick Search history')

            print()