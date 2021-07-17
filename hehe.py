with open('C:/Users/Ayodeji/Desktop/Proton/notes/notes.txt', 'r') as file:
    lines = file.readlines()

ask_content = input('input name: ')
content = ask_content
with open('C:/Users/Ayodeji/Desktop/Proton/notes/notes.txt', 'w') as file:
    for line in lines:
        if line.strip("\n") != content:
            file.write(line)