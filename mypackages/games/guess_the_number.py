from playsound import playsound
import os
user=os.getlogin()

def gng():
    playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/game audio/level 1.mp3')

    print('>>> LEVEL 1')

    print('')

    while True:

        range1 = 77

        player = int(input(f'>>> Guess what number your computer picked within the range 0 - 100: '))

        print('')

        if player < range1:

            print('>>> Too small, try again')

            print('')

        elif player > range1:

            print('>>> Too big, try again')

            print('')

        elif player == range1:

            print('>>> YOU HAVE WON!')

            print('')

            break

    print('NEW LEVEL')

    print()

    print('>>> LEVEL 2')

    print()

    while True:

        range2 = 864

        player = int(input(f'>>> Guess what number your computer picked within the range 100 - 900: '))

        print('')

        if player < range2:

            print('>>> Too small, try again')

            print('')

        elif player > range2:

            print('>>> Too big, try again')

            print('')

        elif player == range2:

            print('>>> YOU HAVE WON!')

            print()

            break

    print('NEW LEVEL')

    print('')

    print('>>> LEVEL 3')

    print()

    while True:

        range3 = 3550

        player = int(input(f'>>> Guess what number your computer picked within the range 1000 - 5000: '))

        print('')

        if player < range3:

            print('>>> Too small, try again')

            print('')

        elif player > range3:

            print('>>> Too big, try again')

            print('')

        elif player == range3:

            print('>>> YOU HAVE WON!')

            print('')

            print('>>> YOU HAVE 3 POINTS!!!')

            print('')

            print('>>>> Text the create of Proton for your prize on instagram. Username: the_proton_guy')
					
            print()

            break