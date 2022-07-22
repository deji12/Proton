
def btt():
    
    binary_string = input('> Enter binary number: ')

    print()

    ascii_string = "".join([chr(int(binary, 2)) for binary in binary_string.split(" ")])

    print(ascii_string)

    print()