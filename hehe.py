# import speech_recognition as sr 

# import playsound

# import gtts

# import googletrans

# #print(googletrans.LANGUAGES)

# r = sr.Recognizer()

# mic = sr.Microphone()

# translator = googletrans.Translator()

# input_lang = 'es-MX'

# output_lang = 'ru'

# try:
#     with mic as source:
#         print('> Speak now')
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source)
#         result = r.recognize_google(audio, input_lang)
#         print(result)
# except:
#     pass

# translated = translator.translate(result, dest=output_lang)

# print(translated.result)

# converted_audio = gtts.gTTS(translated.result, lang=output_lang)

# converted_audio.save('romantic.mp3')

# playsound.playsound('romantic.mp3')

from pytube import YouTube
from pytube.cli import on_progress

# search = input('> Input link: ')

# print()

# yt = YouTube(search)

# for stream in yt.streams.order_by('resolution'):
#     print(stream.resolution)

# print(yt.title)

# print(yt.views)

#print(yt.description)

# lowest = (yt.streams.get_lowest_resolution().resolution)

# highest = (yt.streams.get_highest_resolution().resolution)


# yt_streams = yt.streams.filter(file_extension ='mp4').get_by_resolution()

# yt_streams.download(output_path='C:/Users/Ayodeji/Desktop/YouTube Download')

save_path = f'C:/Users/Ayodeji/Desktop/YouTube Download'

search = input('> Enter video link: ')

print()

yt = YouTube(search, on_progress_callback=on_progress)

print(f'> Video Title: {yt.title}')

print()

print('==============================')

print()

print(f'> Number of views: {yt.views}')

print()

print('==============================')

print()

print(f'> Thumbnail image: {yt.thumbnail_url}')

print()

print('====================================')

print()

lowest = (yt.streams.get_lowest_resolution().resolution)

highest = (yt.streams.get_highest_resolution().resolution)

print(highest)
print(lowest)

#print('> These are the qualities/resolutions of the video')

# print()

# for stream in yt.streams.order_by('resolution'):
    
# 		print(stream.resolution)

#quality = input("> Which quality/resolution of the video will you like to download: ")

print()

print(f'> Downloading {yt.title}...')

print()

video = yt.streams.get_lowest_resolution()

video.download(output_path=save_path)

print('> Video downloaded!')