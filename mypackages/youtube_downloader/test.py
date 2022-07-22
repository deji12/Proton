from pytube import YouTube

link = 'https://www.youtube.com/watch?v=Qf9eJ55MrF4'

yt = YouTube(link)

lowest = yt.streams.get_lowest_resolution().resolution

highest = yt.streams.get_highest_resolution().resolution

print(f'> Highest: {highest}')

print()

print(f'> Lowest: {lowest}')