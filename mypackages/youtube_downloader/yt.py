from pytube import YouTube

from pytube.cli import on_progress

import os

user = os.getlogin()

def dowmload_yt():

    int_con = input('> Are you connected to the interet(y/n): ').lower()

    print()

    if int_con == 'y':

        try:

            desktop_content = os.listdir(f'C:/Users/{user}/Desktop')

            if 'YouTube Download' in desktop_content:

                save_path = f'C:/Users/{user}/Desktop/YouTube Download'

                search = input('> Enter video link: ')

                print()

                yt = YouTube(search, on_progress_callback=on_progress)

                print(f'-----> Video Title: {yt.title}')

                print()

                print('====================')

                print()

                print(f'-----> Number of views: {yt.views}')

                print()

                print('====================')

                print()

                print(f'-----> Thumbnail image: {yt.thumbnail_url}')

                print()

                print('====================')

                print()

                print('> These are the highest and lowest qualities/resolutions of the video')

                print()

                lowest = yt.streams.get_lowest_resolution().resolution

                highest = yt.streams.get_highest_resolution().resolution

                print(f'> Highest: {highest}')

                print()

                print(f'> Lowest: {lowest}')

                print()

                quality = input('> Which quality/resolution of the video will you like to download(h for highest -> l for lowest): ').lower()

                print()

                if quality == 'h':
                    
                    video = yt.streams.get_highest_resolution()

                    video_res = yt.streams.get_highest_resolution().resolution

                    print(f'> Downloading {yt.title} in {video_res}...')

                    print()

                    video.download(output_path=save_path)

                    print('> Video downloaded!')

                    print()

                elif quality == 'l':

                    video = yt.streams.get_highest_resolution()

                    video_res = yt.streams.get_lowest_resolution().resolution

                    print(f'> Downloading {yt.title} in {video_res}...')

                    print()

                    video.download(output_path=save_path)

                    print('> Video downloaded!')

                    print()

            elif 'YouTube Download' not in desktop_content:

                os.chdir(f'C:/Users/{user}/Desktop')

                os.mkdir('YouTube Download')

                save_path = f'C:/Users/{user}/Desktop/YouTube Download'

                search = input('> Enter video link: ')

                print()

                yt = YouTube(search, on_progress_callback=on_progress)

                print(f'-----> Video Title: {yt.title}')

                print()

                print('====================')

                print()

                print(f'-----> Number of views: {yt.views}')

                print()

                print('====================')

                print()

                print(f'-----> Thumbnail image: {yt.thumbnail_url}')

                print()

                print('====================')

                print()

                print('> These are the highest and lowest qualities/resolutions of the video')

                print()

                lowest = yt.streams.get_lowest_resolution().resolution

                highest = yt.streams.get_highest_resolution().resolution

                print(f'> Highest: {highest}')

                print()

                print(f'> Lowest: {lowest}')

                print()

                quality = input('> Which quality/resolution of the video will you like to download(h for highest -> l for lowest): ').lower()

                print()

                if quality == 'h':
                    
                    video = yt.streams.get_highest_resolution()

                    video_res = yt.streams.get_highest_resolution().resolution

                    print(f'> Downloading {yt.title} in {video_res}...')

                    print()

                    video.download(output_path=save_path)

                    print('> Video downloaded!')

                    print()

                elif quality == 'l':

                    video = yt.streams.get_highest_resolution()

                    video_res = yt.streams.get_lowest_resolution().resolution

                    print(f'> Downloading {yt.title} in {video_res}...')

                    print()

                    video.download(output_path=save_path)

                    print('> Video downloaded!')

                    print()

        except: 

            print('> Connect to the internet and try again')

            print()

    elif int_con == 'n':

        print('> Connect to the internet and try again')

        print()		
