import speech_recognition as sr

print('>>> Listening...')

print()

r = sr.Recognizer()

mic = sr.Microphone()

try:

    with mic as source:

        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)

        start = r.recognize_google(audio)

        print(start)

except:

    print('could not hear you sir')