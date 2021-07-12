import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')

engine.setProperty('rate', 125)

print(engine.say('i am a boy'))

engine.runAndWait()

engine.stop()