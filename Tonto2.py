#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Esto es un invento un poco loco.
#En esta version vamos a ordenar un poco el codigo de Tonto. 


import os
import sys 
import time
from datetime import date 
import re
#import pyttsx
plataforma = sys.platform

version = "1.5"
ideas = []

nombre = "[Tu nombre]"

#Ordenamos todas las frases que reproducira Tonto en una sola deficion
'''def voz(frase): 
	engine = pyttsx.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', 'spanish')
	engine.say(frase)
	engine.runAndWait()'''

def frases(numero): 
		if numero == "1":
				linea = "Aun no lo ha programado."
		elif numero == "2":
				linea = "Accediendo a banco de trabajo..."
		elif numero == "3":
				linea = "Necesitas algo mas? "
		elif numero == "4":
				linea = "[s = si] [n = no]"
		elif numero == "5":
				linea = "Que le vaya bien el dia :)"
		elif numero == "6":
				linea = "Se que no le gusta pero hoy ha de aguantarse"
		elif numero == "7":
				linea = "Abriendo carpeta de Documentos..."
		elif numero == "8":
				linea = "Accediendo a su carpeta de Música..."
		elif numero == "9":
				linea = "Abriendo repositorios"
		elif numero == "10":
				linea = "Accediendo a su editor de codigo favorito"
		elif numero == "11":
				linea = "estas son las ideas que ha recogido hasta ahora."
		elif numero == "12":
				linea = "ideas guardadas con exito"
		elif numero == "13":
				linea = "Algo más?"
		elif numero == "14":
				linea = "Selecione una de las dos "
		elif numero == "15": 
				linea = "Iniciando Ragnarock Online, ya que tiene los juegos desordenados por el disco duro."
		elif numero == "16": 
				linea = "Soy tu asistente personal para este pc, me has programado tu y actualmente me encuentro en la " + version
		elif numero == "17":
				linea = "Siempre es un placer poder descansar"
		elif numero == "18":
				linea = "Hola " + nombre + ", que te apeteceria hacer hoy?" 
		elif numero == "19":
				linea = """
[Trabajar] 
[Estudiar]
[Musica]
[Imagenes]
[Programar]
[Ideas]
[Jugar] 
[Quien eres?] 
[No requiero tu ayuda, gracias]	
"""
		elif numero == "20":
    			linea = "Accediendo a su carpeta de Imágenes..."

		print (linea)
		#voz(linea)

#Lo mismo que hacemos con las frases pero con la voz reproducida 
#def voz(diba):
	#if diba = "numerodiba": 
		#os.system('"RUTA DE LA CANCION A reproducira"')
		#Aparte de os.system() tambien hay soluciones usando diferentes librerias. 

def operation_system():
		if plataforma == "linux": # Firma del Linux
				os.system("clear")
		elif plataforma == "darwin": # Firma del Mac
				os.system("clear")
		elif plataforma == "win32": # Firam del Windows
				os.system("cls")
		else: # Otros sistemas operativos
				os.system("clear")

operation_system = operation_system()

#Este es el sitema de Busqueda o peticiones

def sistema(busqueda):
		#saludo = re.search(r'como estas(.*)', peticion)
		trabajar = re.search(r'trabaj(.*)', peticion)
		empollar = re.search(r'estudi(.*)', peticion)
		ritmo = re.search(r'musi(.*)', peticion)
		ver = re.search(r'imagen(.*)', peticion)
		codigo = re.search(r'programa(.*)', peticion)
		bideas = re.search(r'idea(.*)',peticion)
		jugar = re.search(r'jugar', peticion)
		quien = re.search(r'eres',peticion)
		descansar = re.search(r'descans(.*)', peticion)

		'''if saludo:
				print("¿Bien y usted?")
				operation_system'''

		if trabajar:
				print(trabajo(peticion))
				operation_system
		elif empollar:
				print(estudiar(peticion))
				operation_system
		elif ritmo:
				print(musica(peticion))
				operation_system
		elif ver:
				print(imagenes(peticion))
				operation_system
		elif codigo:
				print(programar(peticion))
				operation_system
		elif bideas:
				print(banco(peticion))
				operation_system
		elif jugar: 
				print(games(peticion))
				operation_system
		elif quien: 
				print(who(peticion))
				operation_system
		elif descansar: 
				print(fin(peticion))
				operation_system
		else: 
				frases("1")
				#Podriamos ordenar que reproduzca el sonido que queramos
				#voz(diba)
				time.sleep(3)
				operation_system

def trabajo(seleccion):	
		frases("2")
		#voz(diba)
		time.sleep(3)
		os.system('"RUTA A TU EDITOR DE TEXTO FAVORITO"')
		frases("3")
		#voz(diba)
		frases("4")
		d2 =  input("-->:")
		decision1 = re.search(r's(.*)', d2)
		decision2 = re.search(r'n(.*)', d2)
		if decision1:
				operation_system
		elif decision2:
				operation_system
				frases("5")
				#voz(diba)
				time.sleep(3)	
				sys.exit(0) 

def estudiar(Albert): 
		frases("6")
		#voz(diba)
		time.sleep(4)
		frases("7")
		#voz(diba)
		time.sleep(4)
		if plataforma == "linux": # Firma del Linux
				os.system("nautilus $HOME/Documents") # Requiere instalar nautilus (sudo apt install nautilus)
		elif plataforma == "darwin": # Firma del Mac
				os.system("FALTA EL COMANDO DE RUTA")
		elif plataforma == "win32": # Firam del Windows
				os.system("start %USERPROFILE%/Documents")
		else: # Otros sistemas operativos
				os.system("nautilus $HOME/Documents") # Requiere instalar nautilus (sudo apt install nautilus)
		time.sleep(3)
		frases("3")
		#voz(diba)
		frases("4")
		d2 = input("-->:")
		decision1 = re.search(r's(.*)', d2)
		decision2 = re.search(r'n(.*)', d2)
		if decision1:
				operation_system
		elif decision2:
				operation_system
				frases("5")
				#voz(diba)
				time.sleep(3)	
				sys.exit(0) 	

def musica(beethoven):
		frases("8")
		#voz(diba)
		time.sleep(3)
		if plataforma == "linux": # Firma del Linux
				os.system("nautilus $HOME/Music") # Requiere instalar nautilus (sudo apt install nautilus)
		elif plataforma == "darwin": # Firma del Mac
				os.system("FALTA EL COMANDO DE RUTA")
		elif plataforma == "win32": # Firam del Windows
				os.system("start %USERPROFILE%/Music")
		else: # Otros sistemas operativos
				os.system("nautilus $HOME/Music") # Requiere instalar nautilus (sudo apt install nautilus)
		frases("3")
		#voz(diba)
		frases("4")
		d2 = input("-->: ")
		decision1 = re.search(r's(.*)', d2)
		decision2 = re.search(r'n(.*)', d2)
		if decision1:
				operation_system
		elif decision2:
				operation_system
				frases("5")
				#voz(diba)
				time.sleep(3)	
				sys.exit(0) 

def imagenes(recuerdos):
			frases("20")
			#voz(diba)
			time.sleep(3)
			if plataforma == "linux": # Firma del Linux
					os.system("nautilus $HOME/Pictures") # Requiere instalar nautilus (sudo apt install nautilus) 
			elif plataforma == "darwin": # Firma del Mac
					os.system("FALTA EL COMANDO DE RUTA")
			elif plataforma == "win32": # Firam del Windows
					os.system("start %USERPROFILE%/Pictures")
			else: # Otros sistemas operativos
					os.system("nautilus $HOME/Pictures") # Requiere instalar nautilus (sudo apt install nautilus)
			frases("3")
			#voz(diba)
			frases("4")
			time.sleep(2)
			d2 = input("-->: ")
			decision1 = re.search(r's(.*)', d2)
			decision2 = re.search(r'n(.*)', d2)
			if decision1:
					operation_system
			elif decision2:
					operation_system
					frases("5")
					#voz(diba)
					time.sleep(3)	
					sys.exit(0) 

def programar(Wozniak):
			frases("9") 
			#voz(diba)
			if plataforma == "linux": # Firma del Linux
					os.system("nautilus $HOME/Documents/GitHub") # Requiere instalar nautilus (sudo apt install nautilus) 
			elif plataforma == "darwin": # Firma del Mac
					os.system("FALTA EL COMANDO DE RUTA")
			elif plataforma == "win32": # Firam del Windows
					os.system("start %USERPROFILE%/Documents/GitHub")
			else: # Otros sistemas operativos
					os.system("nautilus $HOME/Documents/GitHub") # Requiere instalar nautilus (sudo apt install nautilus)
			time.sleep(3)
			frases("10") 
			#voz(diba)
			os.system('"RUTA EDITOR DE CODIGO"')
			time.sleep(3)
			frases("3")
			#voz(diba)
			frases("4")
			d2 = input("-->: ")
			decision1 = re.search(r's(.*)', d2)
			decision2 = re.search(r'n(.*)', d2)
			if decision1:
					operation_system
			elif decision2:
					operation_system
					frases("5")
					#voz(diba)
					time.sleep(3)	
					sys.exit(0) 

def banco(delacalle):
		while True:
				recogedor = open('banco_ideas.txt','a+')
				for item in recogedor:
						ideas.append(item)
				frases("11")
				#voz(diba)
				time.sleep(3)
				print(ideas)
				#voz(diba)
				idea = input("Que se le ha ocurrido?:  ")
				ideas.append(idea)
				ideas.append(date.today())
				print(ideas)
				time.sleep(3)
				#voz(diba)
				d3 = input("Ajunto otra idea señor?: ") 
				if d3 == "s":
						operation_system
						print(idea)
				elif d3 == "n":
						i = str(ideas)
						banco_ideas = open('banco_ideas.txt', 'a+')
						print(ideas)
						banco_ideas.write(i)
						banco_ideas.close()
						#voz(diba)
						frases("12")
						time.sleep(3)
						frases("13")
						#voz(diba)
						frases("4")
						d2 = input("-->: ")
						decision1 = re.search(r's(.*)', d2)
						decision2 = re.search(r'n(.*)', d2)
						if decision1:
								operation_system
						elif decision2:
								operation_system
								frases("5")
								#voz(diba)
								time.sleep(3)
								sys.exit(0)
				else: 
						frases("14")
						#voz(diba)
						time.sleep(5)

def games(juegos):
		frases("15")
		#voz(diba)
		time.sleep(5)
		os.system('"RUTA A JUEGO O CAPERTA DE JUEGOS"')
		time.sleep(3)
		frases("13")
		#voz(diba)
		frases("4")
		d2 =  input("-->: ")
		decision1 =  re.search(r's(.*)', d2)
		decision2 = re.search(r'n(.*)', d2)
		if decision1:
				operation_system
		elif decision2:
				operation_system
				frases("14")
				#voz(diba)
				time.sleep(3)	
				sys.exit(0) 

def who(Snifer):
		frases("16")
		#voz(diba)
		time.sleep(7)
		frases("13")
		#voz(diba)
		frases("4")
		d2 =  input("-->: ")
		decision1 =  re.search(r's(.*)', d2)
		decision2 = re.search(r'n(.*)', d2)
		if decision1:
				operation_system
		elif decision2:
				operation_system
				frases("14")
				#voz(diba)
				time.sleep(3)	
				sys.exit(0) 

def fin(apagar):
		frases("17")
		#voz(diba)
		time.sleep(3)
		operation_system
		sys.exit(0)	

#Saludo, molaria personalizarle el nombre a la maquina

frases("18")
#voz(diba)
time.sleep(4)

'''Antes de esto me podria dar la tempertura de mi region. Tendre que mirarlo
estoy ira así facil y comodo xD'''

'''La parte peticion = raw_input("") no es compatible con Python 3.x asi que quien trabaje con versiones
anteriores lo tendra que canviar'''

while True: 
		frases("19")

		peticion = input("-->: ")
		print(sistema(peticion))

