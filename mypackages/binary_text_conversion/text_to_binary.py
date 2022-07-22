

def ttb():
    text: str = input('> Enter text: ')

    print()

    code = ' '.join(format(x, 'b') for x in bytearray(text, 'utf-8'))

    print(code)

    print()