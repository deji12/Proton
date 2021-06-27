import random

from colorama import init

init()

from playsound import playsound

import speech_recognition as sr

import os

from colorama import Fore, Back, Style

def guess():

    player = 0

    cpu = 0


    while True:

        possible_input = ['rock', 'paper', 'scissors']

        while player < 3 and cpu < 3:

            print(Fore.GREEN + '>>> Listening...')
            
            cpu_pick = random.choice(possible_input)

            r = sr.Recognizer()

            mic = sr.Microphone()

            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            player_pick = r.recognize_google(audio)


            print('')

            print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

            print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

            print('')

            if player_pick == cpu_pick:
                
                print(Fore.WHITE + 'Its a tie!')

                print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

                print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

            elif player_pick == 'rock' or player_pick == 'roar' or player_pick == 'Rock' or player_pick == 'ROCK' or player_pick == 'Roar' or player_pick == 'ROAR' :

                if cpu_pick == 'paper':

                    cpu += 1

                    playsound(r'C:\Users\Ayodeji\Desktop\rock_paper_scissors\phone.mp3')

                    print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

                    print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

                    print('')

                elif cpu_pick == 'scissors':

                    player += 1

                    playsound(r'C:\Users\Ayodeji\Desktop\rock_paper_scissors\player.mp3')

                    print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

                    print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

                    print('')

            elif player_pick == 'clear':

                os.system('cls')

            elif player_pick == 'paper' or player_pick == 'PAPER' or player_pick == 'Paper' or player_pick == 'pipi' or player_pick == 'PIPA' or player_pick == 'Pipa':

                if cpu_pick == 'rock':

                    player += 1

                    playsound(r'C:\Users\Ayodeji\Desktop\rock_paper_scissors\player.mp3')

                    print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

                    print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

                    print('')

                elif cpu_pick == 'scissors':

                    cpu += 1

                    playsound(r'C:\Users\Ayodeji\Desktop\rock_paper_scissors\phone.mp3')

                    print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

                    print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

                    print('')

            elif player_pick == 'scissors' or player_pick == 'SCISSORS':

                if cpu_pick == 'rock':

                    cpu += 1

                    playsound(r'C:\Users\Ayodeji\Desktop\rock_paper_scissors\phone.mp3')

                    print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

                    print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

                    print('')

                elif cpu_pick == 'paper':

                    player += 1

                    playsound(r'C:\Users\Ayodeji\Desktop\rock_paper_scissors\player.mp3')

                    print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

                    print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

                    print('')

            else:
                print(Fore.RED + 'Invalid input!')

                print('')

        if player > cpu:

            print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

            print(Fore.YELLOW + 'Player wins!')

            playsound(r'C:\Users\Ayodeji\Desktop\rock_paper_scissors\player wins.mp3')

        else:

            print(Fore.BLUE + 'CPU Wins!')

#guess()

