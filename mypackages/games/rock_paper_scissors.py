import random
from playsound import playsound
import os
from colorama import init
init()
from colorama import Fore, Back, Style
user=os.getlogin()

def rps():

    player = 0

    cpu = 0

    while True:

        possible_input = ['rock', 'paper', 'scissors']

        while player < 3 and cpu < 3:

            cpu_pick = random.choice(possible_input)

            player_pick = input('> rock, paper, or scissors: ')

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

                    playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/game audio/cpu point.mp3')

                    print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

                    print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

                    print('')

                elif cpu_pick == 'scissors':

                    player += 1

                    playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/game audio/player point.mp3')

                    print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

                    print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

                    print('')

                elif player_pick == 'clear':

                    os.system('cls')

            elif player_pick == 'paper' or player_pick == 'PAPER' or player_pick == 'Paper' or player_pick == 'pipi' or player_pick == 'PIPA' or player_pick == 'Pipa':

                if cpu_pick == 'rock':

                    player += 1

                    playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/game audio/player point.mp3')

                    print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

                    print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

                    print('')

                elif cpu_pick == 'scissors':

                    cpu += 1

                    playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/game audio/cpu point.mp3')

                    print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

                    print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

                    print('')

            elif player_pick == 'scissors' or player_pick == 'SCISSORS':

                if cpu_pick == 'rock':

                    cpu += 1

                    playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/game audio/cpu point.mp3')

                    print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

                    print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

                    print('')

                elif cpu_pick == 'paper':

                    player += 1

                    playsound(f'C:/Users/{user}Desktop/Proton/Essentials/game audio/player point.mp3')

                    print(f'Player pick: {player_pick} VS           CPU pick: {cpu_pick}')

                    print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

                    print('')
                
            else:
                    
                print(Fore.RED + 'Invalid input!')

                print('')

        if player > cpu:

            print(Fore.GREEN + f'Player score: {player} VS           CPU Score: {cpu}')

            print(Fore.YELLOW + 'Player wins!')

            playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/game audio/player wins.mp3')

            break

        else:

            print(Fore.BLUE + 'CPU Wins!')

            playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/game audio/cpu wins.mp3')

            break