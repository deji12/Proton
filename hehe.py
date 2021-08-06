import speech_recognition as sr

while True:

    try:

        print('>>> Listening...')

        r = sr.Recognizer()

        mic = sr.Microphone()

        with mic as source:

            r.adjust_for_ambient_noise(source)

            audio = r.listen(source)

        start = r.recognize_google(audio)

        print(start)

    except:

        print('could not hear')

        print()

