from math import inf, sqrt

import random

import tkinter

import webbrowser

import requests

import os

from getpass import getpass

from pytube import YouTube

from pytube.cli import on_progress

import datetime

from datetime import date

from typing import final

import pyttsx3

engine = pyttsx3.init()

from playsound import playsound

import speech_recognition as sr

from colorama import init

init()

from colorama import Fore, Back, Style

import wikipedia as wiki

from tkinter import *

from tkinter import ttk

import time

#import winsound

from threading import *

from time import strftime 

from pygame import mixer

import array

# from PyDictionary import PyDictionary

# dictionary = PyDictionary()

from cryptography.fernet import Fernet

from mypackages.note.note import note

from mypackages.note.see_notes import see_notes

from mypackages.note.read_note import read_note

from mypackages.note.delete_note import delete_note

from mypackages.search.wiki import wiki_search

from mypackages.games.guess_the_number import gng

from mypackages.games.rock_paper_scissors import rps

from mypackages.message.whatsapp import send_whatsapp_message

from mypackages.search.google_search import gsearch

from mypackages.search.quick_search import quick_searchh

from mypackages.search.history import search_history

from mypackages.date.date import current_date

from mypackages.date.time import current_time

from mypackages.youtube_downloader.yt import dowmload_yt

from mypackages.currency_convert.cc import convert

from mypackages.generate_password.generate import generator

from mypackages.generate_password.recorver_generated_password import recorver

from mypackages.binary_text_conversion.binaty_to_text import btt

from mypackages.binary_text_conversion.text_to_binary import ttb

from mypackages.audio_books.create_audio_book import mab

from .mypackages.alarm.set_alarm import alarm

from mypackages.power.power import power_control

from mypackages.developer_mode.developer import developer

user = os.getlogin()

print()

file_size = os.path.getsize(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt')

if file_size == 0:

	print('FIRST TIME USER')

	print()

	print('> NOTE: While typing in or trying to create passwords, whatever you type in will not be displayed on the screen but it is being saved. Type in the password and press enter!')

	rate = engine.getProperty('rate')

	engine.setProperty('rate', 130)

	engine.say('Greetings human, welcome, I am your very own virtual assistant. Call me proton')

	engine.say('I will need you to create a password, tell me your name, and some details about you. Lets go')

	engine.runAndWait()

	engine.stop()

	print()

	while True:

		create_password = getpass('> Create Password: ')

		print()

		connirm_password = getpass('> Confirm Password: ')

		print()

		if create_password == connirm_password:

			os.chdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

			os.mkdir('gibberish')

			key = Fernet.generate_key()

			write_key = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/gibberish.key', 'wb')

			write_key.write(key)

			write_key.close()

			open_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/gibberish.key', 'rb')

			key = open_file.read()

			open_file.close()

			encoded = connirm_password.encode()

			fernet = Fernet(key)

			encrypted = fernet.encrypt(encoded)

			# print(encrypted)

			filee = open(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt', 'wb')

			filee.write(encrypted)

			filee.close()

			break

		elif create_password != connirm_password:

			print('---- Error, passwords do not match. Try again')

			print()

else:
	pass


i = 0

while i < 3:

	while True:

		Enter_pass = getpass('Enter Password: ')

		open_key_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/gibberish/gibberish.key', 'rb')

		key = open_key_file.read()

		open_key_file.close()

		fernet = Fernet(key)

		open_pass_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt', 'rb').read()

		decrypted = fernet.decrypt(open_pass_file)

		decode_decrypted = decrypted.decode()

		print()

		if not Enter_pass:

			print('> Error, empty input, enter password')

			print()

		elif len(Enter_pass) > 2:

			break
	
	# file_open = open(f'C:/Users/{user}/Desktop/Proton/Essentials/pass.txt', 'rb')

	# read_file = file_open.read()

	# print(read_file)

	if Enter_pass != decode_decrypted:

		i += 1

		print('----Error, wrong password. Try again')

		print()

		print(f'>> Tries left: {3 - i}')

		print()

	elif Enter_pass == decode_decrypted:
		
		break

	if i == 3:

		print('>>>> CLOSING PROTON')

		exit()

print()

folder_check = os.listdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

if 'AboutUser' not in folder_check:

	os.chdir(f'C:/Users/{user}/Desktop/Proton/Essentials')

	os.mkdir('AboutUser')

	create_name_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/Name.txt', 'w')

	create_age_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/Age.txt', 'w')

	create_hobby_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/hobby.txt', 'w')

	create_additional_info_file = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/additional info.txt', 'w')

	create_gender = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/gender.txt', 'w')

	name_input = input('> What is your name: ')

	create_name_file.write(name_input)

	create_name_file.close()

	print()

	age_input = input('> How old are you?: ')

	create_age_file.write(age_input)

	create_age_file.close()

	print()

	gender = input('> Gender(m/f): ')

	create_gender.write(gender)

	create_gender.close()

	print()

	hobby_input = input('> What are your hobbies: ')

	splitted_hobby = hobby_input.split(',')

	create_hobby_file.write(f'{splitted_hobby} \n')

	create_hobby_file.close()

	print()

	add_info_input = input('> Additional information about you(enter nil for nothing): ')

	create_additional_info_file.write(add_info_input)

	create_additional_info_file.close()

	print()

	open_beginner = open(f'C:/Users/{user}/Desktop/Proton/Essentials/txt files/beginner.txt').read()

	print(open_beginner)

	print()

else:
	pass

print('')

greeting_path = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/gender.txt', 'r')

read_path = greeting_path.read()

if 'm' in read_path:

	hour = datetime.datetime.now().hour

	if hour>=0 and hour<12:

		print('> Good morning sir.')

		print()

		rate = engine.getProperty('rate')

		engine.setProperty('rate', 130)

		engine.say('Good morning sir.')

		engine.runAndWait()

		engine.stop()

	elif hour>=12 and hour<18:

		print('> Good afternoon sir.')

		print()

		rate = engine.getProperty('rate')

		engine.setProperty('rate', 130)

		engine.say('Good afternoon sir.')

		engine.runAndWait()

		engine.stop()

	else:

		print('> Good evening sir.')

		print()

		rate = engine.getProperty('rate')

		engine.setProperty('rate', 130)

		engine.say('Good evening sir.')

		engine.runAndWait()

		engine.stop()

elif 'f' in read_path:

	hour = datetime.datetime.now().hour

	if hour>=0 and hour<12:

		print('> Good morning Miss.')

		print()

		rate = engine.getProperty('rate')

		engine.setProperty('rate', 130)

		engine.say('Good morning Miss.')

		engine.runAndWait()

		engine.stop()

	elif hour>=12 and hour<18:

		print('> Good afternoon Miss.')

		print()

		rate = engine.getProperty('rate')

		engine.setProperty('rate', 130)

		engine.say('Good afternoon Miss.')

		engine.runAndWait()

		engine.stop()

	else:

		print('> Good evening Miss.')

		print()

		rate = engine.getProperty('rate')

		engine.setProperty('rate', 130)

		engine.say('Good evening Miss.')

		engine.runAndWait()

		engine.stop()

playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/hi.mp3')

while True:

	min_length = 2

	name = input('> What is your name: ')

	print()
    
	if (len(name) >= min_length and name.isprintable() and name.isalpha()):
        
		break

	else:
		print()

		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/error.mp3')
		
		print('>>> Error, name can only contain alphabets')

		print()

		print(name)

		print()

	#password_entry = input('Enter Password: ')

	#if password_entry == 


rate = engine.getProperty('rate')

engine.setProperty('rate', 125)	
	
engine.say(f'> Hi there {name}')

print(f'> Hi there {name}')

engine.runAndWait()

engine.stop()
	
print()

# start with unit conversi.txt

calculator2 = open(f'C:/Users/{user}/Desktop/Proton/Essentials/txt files/calc.txt')

calc2 = calculator2.read()

file_path1 = open(f'C:/Users/{user}/Desktop/Proton/Essentials/txt files/command.txt')

com = file_path1.read()

help_m = open(f'C:/Users/{user}/Desktop/Proton/Essentials/txt files/help.txt')

help_me = help_m.read()

constant_ = open(f'C:/Users/{user}/Desktop/Proton/Essentials/txt files/constants.txt')

constants = constant_.read()

unit_c = open(f'C:/Users/{user}/Desktop/Proton/Essentials/txt files/unit conversion.txt')

unc = unit_c.read()

print(Fore.BLUE + '>>> Input s or start to start')

print()

print(Fore.BLUE + '>>> Input h or help for help')

print()

print(Fore.BLUE + '>>> Input com or commands to see commands')

playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/input.mp3')

print()

def main():

	#playsound(f'C:/Users/{user}/Desktop/Proton/voice/how may i help you today.mp3')

	rate = engine.getProperty('rate')

	engine.setProperty('rate', 125)

	engine.say(f'How may i help you today {name}')

	engine.runAndWait()

	engine.stop()
	
	start = input(Fore.GREEN + f'> How may i help you today {name}: ').lower()

	print()

	#========================
		# mathematics and physics constants
	#========================

	if start == 'youtube download' or start == 'youtube downloader' or start == 'yd':

		dowmload_yt()

	elif start == 'cc' or start == 'convert currency':

		convert()

	elif start == 'password generator' or start == 'pg' or start == 'generate password' or start == 'gp':

		generator(name=name)

	elif start == 'recorver generated password' or start == 'rgp':

		recorver()	

	elif start == 'text to binary' or start == 'ttb':
		
		ttb()

	elif start == 'binary to text' or start == 'btt':

		btt()

	elif start == 'make audio book' or start == 'mab':

		mab()

	elif start == 'set alarm' or start == 'sa':

		alarm()

	# elif start == 'dict' or start == 'dictionary':

	# 	print('> This action requires internet connection')

	# 	print()

	# 	ask = input('> Are you connected(y/n): ')

	# 	print()

	# 	if ask == 'y':

	# 		try:

	# 			word = input('> What word are you searching for: ')

	# 			print()

	# 			meaning = dictionary.meaning(word)

	# 			print(f'> {meaning}')

	# 			print()

	# 		except:

	# 			print('> Make sure you are connected and try again.')

	# 			print()

	# 	elif ask  == 'n':

	# 		print('> Make sure you are connected and try again.')

	# 		print()

	elif start == 'shutdown' or start == 'restart':

		power_control()

	elif start == 'what do you know about me' or start == 'info on me':

		name_path = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/Name.txt', 'r')

		age_path = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/age.txt', 'r')

		add_info_path = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/additional info.txt', 'r')

		hobby_path = open(f'C:/Users/{user}/Desktop/Proton/Essentials/AboutUser/hobby.txt', 'r')

		read_name_path = name_path.read()

		read_age_path = age_path.read()

		read_add_info_path = add_info_path.read()

		read_hobby_path = hobby_path.read()

		print(f'> Your name is {read_name_path}')

		print()

		print(f'> You are {read_age_path} years old')

		print()

		print(f'> Additional info about you: {read_add_info_path}')

		print()

		print(f'> Your hobbies are: {read_hobby_path}')

		print()

	elif start == 'new note' or start == 'nn':

		note(name=name)

	elif start == 'see notes' or start == 'sn':

		see_notes(Enter_pass=Enter_pass)

	elif start =='read note' or start == 'rn':

		read_note(name=name, Enter_pass=Enter_pass)
		

	elif start == 'del note' or start == 'delete note' or start == 'dn':

		delete_note()

	elif start == 'wiki search' or start == 'ws':

		wiki_search()

	elif start == 'introduce':

		print('>> Greetings human. I am proton, a virtual assistant designed to carry out a lot of tasks to make life easier.  I was designed by Ayodeji Adesola. You are currently using Proton version 1.0.0 <<')

		print()

		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/introduce.mp3')

	elif start == 'game':

		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/game audio/games available.mp3')

		print('>>> There are a few games available: ')
		
		print('')

		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/game audio/rps.mp3')

		print('		> 1 Rock paper scissors(rps for short)')

		print('')

		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/game audio/gtng.mp3')

		print('		> 2 Guess the number(gtn for short)')

		print('')

		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/game audio/Which would you like to play.mp3')

		print('> Enter nothing if you do not want to play any.')

		print()

		play = input('> Which would you like to play?: ').lower()

		print('')

		if play == 'gtn' or play == '2' or play == 'guess the number':

			gng()


		elif play == 'rps' or play == 'rock paper scissors':
			
			rps()

	elif start == 'send whatsapp message' or start == 'swm':

		send_whatsapp_message()

	elif start == 'google search' or start == 'gs':

		gsearch()

	elif start == 'quick search' or start == 'qs':

		quick_searchh()
		
	elif start == 'search history' or start == 'sh':

		search_history()

	elif start == 'date':

		current_date()

	elif start == 'time':

		current_time()

	elif start == 'exit':

		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/goodbye.mp3')	
		
		exit()

	# elif start == 'ndir':

	# 	def ndir():

	# 		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/new directory.mp3')

	# 		ndir_ = input('Name of new directory: ')

	# 		print()
			
	# 		os.chdir(f'C:/Users/{user}/Desktop')
			
	# 		os.mkdir(ndir_)

	# 		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/directory created.mp3')

	# 	ndir()

	#==========================
		# calculate
	#==========================

	else:

		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/error2.mp3')
		
		print(f'----- Error, {start}, is not a command, try again')

		print('')

while True:
	
	start = input('> Input s, h, or com: ').lower()

	print()
	
	if start == 's' or start == 'S' or start == 'start':
		
		main()

	elif start == 'h' or start == 'H' or start == 'help':

		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/help details.mp3')

		x = input('Do you want me to read the help details to you?(y/n): ')	

		if x == 'y':

			print()

			print(help_me)
			
			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/help audio.mp3')

		elif x == 'n':

			print()

			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/ok.mp3')
				
			print('> Ok')

			print()
		
			print(help_me)

		elif x != 'y' and x != 'n':

			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/i do not understand.mp3')
			
			print('I do not understand')

			print()


	# elif start == 'bk' or start == 'back':
	# 	print() 

	elif start == 'com' or start == 'commands':

		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/read commands.mp3')

		x = input('Do you want me to read the commands to you?(y/n): ')

		print()

		if x == 'y':
			
			print(com)

			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/commands audio.mp3')

			print()

		elif x == 'n':

			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/ok.mp3')
				
			print('> Ok')

			print()

			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/runnable commands.mp3')
		
			print(com)

		elif x != 'y' and x != 'n':

			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/i do not understand.mp3')
			
			print('I do not understand')

			print()

	elif start == 'developer':

		developer()

	elif start == 'exit':

		#playsound(f'C:/Users/{user}/Desktop/Proton/voice/goodbye.mp3')	

		rate = engine.getProperty('rate')

		engine.setProperty('rate', 125)

		engine.say(f'I hope i was helpful. Goodbye {name}')

		engine.runAndWait()

		engine.stop()

		exit()

	else:

		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/error2.mp3')
		
		print(f'----- Error, {start}, is not a command, try again')

		print()
	





