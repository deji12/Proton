import datetime
from cryptography.fernet import Fernet
key = open('key.key', 'rb').read()
f = Fernet(key)
# sentence = 'i am a boy'.encode()
# x = datetime.datetime.now()
# datetime_of_creation = f'% Date of creation: {x.strftime("%A, %d %B. %Y")} --> Time of creation: {x.strftime("%I:%M%p")} %'.encode()
# enc = f.encrypt(sentence)
# enc_date = f.encrypt(datetime_of_creation)
# write_sen = open('note.txt', 'wb').write(enc)
# space = open('note.txt', 'a').write('\n')
# write_space = open('note.txt', 'ab').write(enc_date)
open_file = open('note.txt', 'rb').readlines()
for line in open_file:
    dec = f.decrypt(line)
    print(dec.decode())