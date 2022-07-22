import pyttsx3
import os

user = os.getlogin()
engine = pyttsx3.init()

def mab():

    file_exist = os.path.isdir('Audio book')

    audio_book = input('> Name of audio book: ')

    print()

    content = input('> Content: ')

    print()

    if file_exist == False:

        voice_type = input('> Do you want a male or a female voice?(m/f): ')

        print()

        if voice_type == 'm':  

            engine.setProperty('rate', 132)

            voices = engine.getProperty('voices')

            engine.setProperty('voice', voices[0].id)

            os.chdir(f'C:/Users/{user}/Desktop')

            os.mkdir('Audio book')

            path = f'C:/Users/{user}/Desktop/Audio book/{audio_book}.mp3'

            engine.save_to_file(content, path)

            engine.runAndWait()

            engine.stop()

            print('> In your desktop, check for a folder named "Audio Book". Your newly converted audio book is there.')

            print()

        elif voice_type == 'f':

            engine.setProperty('rate', 132)

            voices = engine.getProperty('voices')

            engine.setProperty('voice', voices[1].id)

            os.chdir(f'C:/Users/{user}/Desktop')

            os.mkdir('Audio book')

            path = f'C:/Users/{user}/Desktop/Audio book/{audio_book}.mp3'

            engine.save_to_file(content, path)

            engine.runAndWait()

            engine.stop()

            print('> In your desktop, check for a folder named "Audio Book". Your newly converted audio book is there.')

            print()
    
    elif file_exist == True:

        voice_type = input('> Do you want a male or a female voice?(m/f): ')

        print()

        if voice_type == 'm':

            engine.setProperty('rate', 132)

            voices = engine.getProperty('voices')

            engine.setProperty('voice', voices[0].id)

            os.chdir(f'C:/Users/{user}/Desktop')

            #os.mkdir('Audio book')

            path = f'C:/Users/{user}/Desktop/Audio book/{audio_book}.mp3'

            engine.save_to_file(content, path)

            engine.runAndWait()

            engine.stop()

            print('> In your desktop, check for a folder named "Audio Book". Your newly converted audio book is there.')

            print()

        elif voice_type == 'f':

            engine.setProperty('rate', 132)

            voices = engine.getProperty('voices')

            engine.setProperty('voice', voices[1].id)

            os.chdir(f'C:/Users/{user}/Desktop')

            #os.mkdir('Audio book')

            path = f'C:/Users/{user}/Desktop/Audio book/{audio_book}.mp3'

            engine.save_to_file(content, path)

            engine.runAndWait()

            engine.stop()

            print('> In your desktop, check for a folder named "Audio Book". Your newly converted audio book is there.')

            print()
