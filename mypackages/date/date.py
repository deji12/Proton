import datetime
import pyttsx3
engine = pyttsx3.init()

def current_date():
    
    x = datetime.datetime.now()

    rate = engine.getProperty('rate')

    engine.setProperty('rate', 120)

    print(f'> {x.strftime("%A, %d %B. %Y")}')

    engine.say(f'> Todays date is {x.strftime("%A, %d %B %Y")}')

    engine.runAndWait()

    engine.stop()

    print()