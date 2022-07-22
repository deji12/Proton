import os

def power_control():

    while True:

        print('1. Shutdown computer immediately.')

        print()

        print('2. Shutdown computer after given time.')

        print()

        print('3. Restart computer immediately.')

        print()

        print('4. Restart computer after given time.')

        print()

        print('5. Exit')

        print()

        shutdown_restart = input('> Enter number you wish to perform: ')

        if shutdown_restart == '1':

            os.system("shutdown /s /t 0")

        elif shutdown_restart == '2':

            time = int(input('> Enter number of seconds: '))

            print()

            str0ne = "shutdown /s /t "

            str2 = str(time)

            final = str0ne+str2

            os.system(final)

        elif shutdown_restart == '3':

            os.system("shutdown /r /t 0")

        elif shutdown_restart == '4':

            print()

            time = int(input('> Enter number of seconds: '))

            print()

            str0ne = "shutdown /r /t "

            str2 = str(time)

            final = str0ne+str2

            os.system(final)

        elif shutdown_restart == '5':

            print('> Ok')

            break

        else:

            print('> I do not understand')