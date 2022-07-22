
# elif start == 'calc':

# 		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/calculate.mp3')
		
# 		calc=input(f'> Ok {name}, what do you want to calculate: ')

# 		print()
		
# 		#print('You have selected: ', calc)

# 		print()
		

# 		if calc == 'nothing':

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/ok.mp3')
			
# 			print('> ok')

# 		elif calc == 'find odd numbers' or calc == 'fon' or calc == 'prime numbers' or calc == 'pn': 

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/range of values.mp3')
			
# 			rangee = int(input('Range of numbers: '))

# 			print()
			
# 			for i in range(rangee):
				
# 				if i % 2 == 1:
					
# 					print(i)

# 			print()
					
# 			print('Done')

# 		elif calc == 'fen' or calc == 'find even numbers':

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/range of values.mp3')
 
# 			rangee2 = int(input('Range of numbers: '))

# 			for i in range(rangee2):

# 				if i % 2 == 0:
					
# 					print(i) 

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/done.mp3')
 
# 			print('Done')
 

# 		#stil under work
# 		elif calc == 'frequency' or calc == 'fre':
			
# 			Wavelength=float(input('Wave Length: '))

# 			print()
			
# 			print('Frequency: ', 3*10**8/Wavelength,'Hz')

# 			print()
			
# 			solution=input('Do you want to see the steps?(yes/y or no/n): ')

# 			print()
			
# 			if solution == 'yes' or solution == 'y':
				
# 				print('Frequency = speed of light/wavelength')

# 				print()
				
# 				print('=3*10**8/Wavelength')    

# 				print()
				
# 				print(f'=3*10**8/{Wavelength}')

# 				print()
				
# 				print('Frequency: ', 3*10**8/Wavelength,'Hz')

# 				print()
			
# 			if solution == 'no' or solution == 'n':

# 				playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/ok.mp3')
				
# 				print('Ok')

		
# 		elif calc == 'wavelength' or calc == 'wl':
			
# 			frequency=float(input('Frequency: '))
			
# 			print('Wave length: ', 3*10**8/frequency, 'm/s')
			
# 			solution=input('Do you want to see the steps?(yes/y or no/n): ')
			
# 			if solution == 'yes' or solution == 'y':
				
# 				print('Wavelength= speed of light/frequency')
				
# 				print('=3*10**8/frequency')    
				
# 				print(f'=3*10**8/{frequency}')
				
# 				print('Wavelength: ', 3*10**8/frequency,'Hz')
			
# 			if solution == 'no' or solution == 'no':
				
# 				print('Ok')

		
# 		elif calc == 'energy of a photon when planks constant and frequency are given' or calc == 'eoppf':
			
# 			frequency=float(input('Frequency: '))
			
# 			Energy_of_a_photon=6.63*10**-34 * frequency
			
# 			print('Energy of Photon: ', 6.63*10**-34 * frequency)
			
# 			ev=input('Are you converting into electron volts? (yes/y or no/n): ')
			
# 			if ev == 'yes' or ev == 'y':
				
# 				print('converting to electron volts...')
				
# 				print('converting to electron volts...')
				
# 				print('converting to electron volts...')
				
# 				print('converting to electron volts...')
				
# 				print('Energy of a photon(ev) : ', 1.602*10**-19*Energy_of_a_photon, 'j')
			
			
			
# 			elif ev == 'no' or ev == 'n':
				
# 				print('ok')
			
# 			solution=input('Do you want to see the steps?(yes/y or no/n): ')
			
# 			if solution == 'yes' or solution == 'y':
				
# 				print('Energy of Photon: ', 'planks constant * frequency')
				
# 				print('Energy of Photon: ', '6.63*10**-34 * frequency')
				
# 				print(f'Energy of Photon:  6.63*10**-34 * {frequency}')
				
# 				print('Energy of photon: ', 6.63*10**-34 * frequency,'J')
			
# 			if solution == 'no' or solution == 'n':
				
# 				print('Ok')

		
		
# 		elif calc == 'eoppsw' or calc == 'energy of a photon when planks constant, speed of light, and wavelength are given':
			
# 			Wavelength=float(input('Wave length: '))
			
# 			Energy_of_a_photon2=6.63*10**-34*3*10**8/Wavelength
			
# 			print('Energy of photon: ',6.63*10**-34*3*10**8/Wavelength, 'j')
			
# 			ev=input('Are you converting into electron volts? (yes/y or no/n): ')
			
			
# 			if ev == 'yes' or ev == 'y':
				
# 				print('converting to electron volts...')
				
# 				print('Energy of a photon(ev) : ', 1.602*10**-19*Energy_of_a_photon2, 'j')
			
			
# 			elif ev == 'no' or ev == 'n':
				
# 				print('ok')
			
# 			solution=input('Do you want to see the steps?(yes/y or no/n): ')
			
			
# 			if solution == 'yes' or solution == 'y':
				
# 				print('Energy of Photon: ', 'planks constant * speed of light / wave length')
				
# 				print('Energy of Photon: ', '6.63*10**-34 * 3*10**8 / wave length')
				
# 				print(f'Energy of Photon:  6.63*10**-34 * 3*10**8 / {Wavelength}')
				
# 				print('Energy of photon: ', 6.63*10**-34 * 3*10**8 / Wavelength,'J')
			
			
			
# 			if solution == 'no' or solution == 'n':

# 				playsound(f'C:/Users/{user}/Desktop/Proton/voice/ok.mp3')
				
# 				print('Ok')

# 		elif calc == 'wf' or calc == 'work function':
			
# 			threshold_frequency=float(input('Threshold Frequency: '))

# 			print()
			
# 			print('Work function: ', 6.63*10**-34*threshold_frequency, 'j')

# 			print()
			
# 			solution=input('Do you want to see the steps?(yes/y or no/n): ')
			
# 			if solution == 'yes' or solution == 'y':

# 				print()
				
# 				print('Work function: planks constant * threshold frequency')

# 				print()
				
# 				print('6.63*10**-34 * threshold frequency')

# 				print()
				
# 				print(f'6.63*10**-34 * {threshold_frequency}')

# 				print()
				
# 				print('Work function: ', 6.63*10**-34*threshold_frequency, 'j')

# 			elif solution == 'no' or solution == 'n':

# 				print()

# 				playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/ok.mp3')
				
# 				print('Ok')
			
# 		elif calc == 'energy of a photon when work function and kinetic energy are present':
			
# 			kinetic_energy_work_function = input('Were kinetic energy given and work function?(yes/y or no/n): ')
			
# 			if kinetic_energy_work_function == 'yes' or kinetic_energy_work_function == 'y':
				
# 				KE = float(input('Kinetic Energy: '))
				
# 				work_function2 = int(input('Work function: '))
				
# 				result = print('Energy of photon: ', work_function2 + KE, 'j')
				
# 				print(result)
			
# 			if kinetic_energy_work_function == 'no' or kinetic_energy_work_function == 'n':
				
# 				mass = float(input('Mass: '))
				
# 				velocity = float(input('Velocity: '))
				
# 				KE2 = (0.5 * mass * velocity)
				
# 				threshold_frequency3 = float(input('Threshold frequency: '))
				
# 				work_function3 = (6.63*10**-34 * threshold_frequency3)
				
# 				print('Energy of a photon: ', KE2 + work_function3, 'j')

# 		#work ends here
		
		
		
# 		elif calc == 'what can you calculate' or calc == 'whc':

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/i can calculate.mp3')
			
# 			print(calc2)

		
# 		elif calc == 'quadratic equation' or calc == 'qe':

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/quadratic equation.mp3')
			
# 			a=float(input('a: '))

# 			print()
			
# 			b=float(input('b: '))

# 			print()
			
# 			c=float(input('c: '))

# 			print()
			
			
# 			r = b**2 - 4*a*c
			
# 			if r > 0:
				
# 				num_roots = 2
				
# 				x1 = (((-b) + sqrt(r))/(2*a))
				
# 				x2 = (((-b) - sqrt(r))/(2*a))
				
# 				print('The roots are: %f and %f' % (x1, x2))
			
			
# 			elif r == 0:
				
# 				num_roots = 1
				
# 				x = (-b) / 2*a
				
# 				print('There is one root: ', x)
			
			
# 			else:
				
# 				num_roots = 0
				
# 				print('No roots, discriminant < 0.')

# 		elif calc == 'percentage' or calc == 'per':

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/percentage, given number.mp3')
			
# 			num=float(input('Enter given number: '))

# 			print()

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/percentage, percentage given.mp3')
			
# 			num2=float(input('Enter the percentage given: '))

# 			print()
			
# 			print(num2/100*num)

# 		elif calc == 'add':

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/addition.mp3')
			
# 			num1 = float(input('First number: '))

# 			print()

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/add second number.mp3')
			
# 			num2 = float(input('Second number: '))

# 			print()
			
# 			add = num1 + num2
			
# 			print('Result: ',add)

# 		elif calc == 'sub':

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/subtraction.mp3')

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/input first number.mp3')
			
# 			num1 = float(input('First number: '))

# 			print()

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/add second number.mp3')
			
# 			num2 = float(input('Second number: '))

# 			print()
			
# 			sub = num1 - num2
			
# 			print('Result: ',sub)

# 		elif calc == 'mul':

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/multiplication.mp3')

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/input first number.mp3')
			
# 			num1 = float(input('First number: '))

# 			print()

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/add second number.mp3')
			
# 			num2 = float(input('Second number: '))

# 			print()
			
# 			mul = num1 * num2
			
# 			print('Result: ',mul)

# 		elif calc == 'div':

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/dividion.mp3')

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/input first number.mp3')
			
# 			num1 = float(input('First number: '))

# 			print()

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/add second number.mp3')
			
# 			num2 = float(input('Second number: '))

# 			print()
			
# 			div = num1 / num2
			
# 			print('Result: ',div) 

# 		else:

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/i do not understand.mp3')
			
# 			print('I do not understand')

# 		print()

# 		playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/another operation.mp3')

# 		Repeat = input('> Do you want to perform another operation?(yes/y or no/n): ').lower()

# 		print('')
		
# 		if Repeat == 'yes' or Repeat == 'y': 
			
# 			main()

		
# 		elif Repeat == 'back' or Repeat == 'bk':
			
# 			print(start)

# 		elif Repeat == 'exit':

# 			playsound(f'C:/Users/{user}/Desktop/Proton/Essentials/voice/goodbye.mp3')	
			
# 			print('Bye', name)
			
# 			exit()