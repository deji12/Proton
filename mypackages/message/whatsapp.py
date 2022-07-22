import pywhatkit

def send_whatsapp_message():
    num = input('> Enter recipient number(in format +2349827640745): ')

    print()

    message = input('> Type your message: ')

    print()

    time_input = input('> Enter time this message should be sent(hh, mm format (eg 08, 43)): ')

    splitted_time = time_input.split(',')

    split_1 = splitted_time[0]

    split_2 = splitted_time[1]

    hour = int(split_1)

    minute = int(split_2)

    pywhatkit.sendwhatmsg(num, message, hour, minute, 60)