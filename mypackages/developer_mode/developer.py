import os
user = os.getlogin()

def developer():

    print('> Developer options available: ')

    print()

    print('> Frontend web development:')

    print()

    print('		1. New html and css project')

    print()

    print('		2. New html, css, and javascript project')

    print()

    print('		3. Nav-Bar template - Number 1')

    print()

    print('		3.1 Nav-bar template - number 2')

    print('> Backend web development')

    print()

    print('		4. Guide for setting up new django project')

    print()

    dev_pick = int(input('> Which will you like me to create for you?(pick choice by entering number): '))

    print()

    if dev_pick == 4:

        file_path = open(f'C:/Users/{user}/Desktop/Proton/Essentials/guides/django setup.txt', 'r')

        read_file = file_path.read()

        print(read_file)

        print()

    elif dev_pick == 3:

        project_name = input('> Project folder name: ')

        print()

        html_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/templates/nav-bars/nav-bar-1/index.html', 'r')

        css_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/templates/nav-bars/nav-bar-1/style.css', 'r')

        read_html_file = html_file.read()

        read_css_file = css_file.read()

        os.chdir(f'C:/Users/{user}/Desktop')

        os.mkdir(project_name)

        create_new_html = open(f'C:/Users/{user}/Desktop/{project_name}/index.html', 'w')

        create_new_css = open(f'C:/Users/{user}/Desktop/{project_name}/style.css', 'w')

        create_new_html.write(read_html_file)

        create_new_css.write(read_css_file)

        html_file.close()

        css_file.close()

        create_new_html.close()

        create_new_css.close()

        print('> Check your desktop. The project folder has been created.')

        print()

    elif dev_pick == 3.1:

        project_name = input('> Project folder name: ')

        print()

        html_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/templates/nav-bars/nav-bar-2/index.html', 'r')

        css_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/templates/nav-bars/nav-bar-2/style.css', 'r')

        read_html_file = html_file.read()

        read_css_file = css_file.read()

        os.chdir(f'C:/Users/{user}/Desktop')

        os.mkdir(project_name)

        create_new_html = open(f'C:/Users/{user}/Desktop/{project_name}/index.html', 'w')

        create_new_css = open(f'C:/Users/{user}/Desktop/{project_name}/style.css', 'w')

        create_new_html.write(read_html_file)

        create_new_css.write(read_css_file)

        html_file.close()

        css_file.close()

        create_new_html.close()

        create_new_css.close()

        print('> Check your desktop. The project folder has been created.')

        print()

    elif dev_pick == 1:

        output_folder = input('> Enter name of project folder: ')

        print()

        os.chdir(f'C:/Users/{user}/Desktop')

        os.mkdir(output_folder)

        parent_html = open(f'C:/Users/{user}/Desktop/Proton/Essentials/templates/test.html', 'r')

        parent_css = open(f'C:/Users/{user}/Desktop/Proton/Essentials/templates/style.css', 'r')

        create_html = open(f'C:/Users/{user}/Desktop/{output_folder}/index.html', 'w')

        create_css = open(f'C:/Users/{user}/Desktop/{output_folder}/style.css', 'w')

        read_html = parent_html.read()

        write_html = create_html.write(read_html)

        read_css = parent_css.read()

        write_css = create_css.write(read_css)

        parent_html.close()

        parent_css.close()

        create_css.close()

        create_html.close()

    elif dev_pick == 2:

        output_folder = input('> Enter name of project folder: ')

        print()

        os.chdir(f'C:/Users/{user}/Desktop')

        os.mkdir(output_folder)

        parent_html = open(f'C:/Users/{user}/Desktop/Proton/Essentials/templates/test.html', 'r')

        parent_css = open(f'C:/Users/{user}/Desktop/Proton/Essentials/templates/style.css', 'r')

        create_html = open(f'C:/Users/{user}/Desktop/{output_folder}/index.html', 'w')

        create_css = open(f'C:/Users/{user}/Desktop/{output_folder}/style.css', 'w')

        create_js = open(f'C:/Users/{user}/Desktop/{output_folder}/myscript.js', 'w')

        read_html = parent_html.read()

        write_html = create_html.write(read_html)

        read_css = parent_css.read()

        write_css = create_css.write(read_css)

        parent_html.close()

        parent_css.close()

        create_css.close()

        create_html.close()

        create_js.close()