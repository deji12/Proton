import pyttsx3
engine = pyttsx3.init()
import datetime

def current_time():
    x = datetime.datetime.now()

    rate = engine.getProperty('rate')

    engine.setProperty('rate', 120)

    print(f'> Time: {x.strftime("%I:%M%p")}')

    engine.say(f'> The Time is {x.strftime("%I:%M%p")}')

    engine.runAndWait()

    engine.stop()

    print()