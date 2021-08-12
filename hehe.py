# import os


# user = input('> user: ')

# print('> Developer options available: ')

# print()

# print('1. New html and css project')

# print()

# print('2. New html, css, and javascript project')

# print()

# dev_pick = int(input('> Which will you like me to create for you?(pick choice by entering number): '))

# print()

# if dev_pick == 1:

# 	output_folder = input('> Enter name of project folder: ')

# 	print()

# 	os.chdir(f'C:/Users/{user}/Desktop')

# 	os.mkdir(output_folder)

#     parent_html = open(f'C:/Users/{user}/Desktop/Proton/test.html', 'r')

#     parent_css = open(f'C:/Users/{user}/Desktop/Proton/style.css', 'r')

#     create_html = open(f'C:/Users/{user}/Desktop/{output_folder}/index.html', 'w')

#     create_css = open(f'C:/Users/{user}/Desktop/{output_folder}/style.css', 'w')

#     read_html = parent_html.read()

#     write_html = create_html.write(read_html)

#     read_css = parent_css.read()

#     write_css = create_css.write(read_css)

# elif dev_pick == 2:

#     output_folder = input('> Enter name of project folder: ')

# 	print()

# 	os.chdir(f'C:/Users/{user}/Desktop')

# 	os.mkdir(output_folder)

#     parent_html = open(f'C:/Users/{user}/Desktop/Proton/test.html', 'r')

#     parent_css = open(f'C:/Users/{user}/Desktop/Proton/style.css', 'r')

#     create_html = open(f'C:/Users/{user}/Desktop/{output_folder}/index.html', 'w')

#     create_css = open(f'C:/Users/{user}/Desktop/{output_folder}/style.css', 'w')

#     read_html = parent_html.read()

#     write_html = create_html.write(read_html)

#     read_css = parent_css.read()

#     write_css = create_css.write(read_css)

# # name_path = open(f'C:/Users/{user}/Desktop/Proton/AboutUser/Name.txt', 'w')

# # 	age_path = open(f'C:/Users/{user}/Desktop/Proton/AboutUser/age.txt', 'w')

# # 	add_info_path = open(f'C:/Users/{user}/Desktop/Proton/AboutUser/additional info.txt', 'w')

# # 	hobby_path = open(f'C:/Users/{user}/Desktop/Proton/AboutUser/hobby.txt', 'w')
	
# # 	name = input('> What is your name: ')

# # 	name_path.write(name)

# # 	print()

# # 	age = input('> How old are you: ')

# # 	age_path.write(age)

# # 	print()

# # 	additional_info = input('> Add any other additional information(nil for none): ')

# # 	add_info_path.write(additional_info)

# # 	print()

# # 	hobby = input('> What are your hobbies: ')

# # 	splitted_hobby = hobby.split(',')

# # 	hobby_path.write(f'{splitted_hobby} \n')


import os

user = input('user: ')

print()

folder_check = os.listdir(f'C:/Users/{user}/Desktop/Proton/notes')

#res = str(folder_check)[1:-1].strip(',')

for x in range(len(folder_check)):
    rolls = folder_check[x]
    stripped = rolls.strip(". md txt py")
    print(stripped)

#print(res)


