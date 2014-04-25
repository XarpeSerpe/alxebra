#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#VersiÃ³n 0.4
			

import random
import sys
import os
import time
t0 = time.clock
random.seed()

#if(len(sys.argv) > 1):
#	if sys.argv[1] == "help"
#		print "alxebra rexistro"
#		print "amosa un rexistro da ecolucion do conecemento alxebrico"
#	elif sys.argv[1] == "rexistro":
#		print "Amosando rexistro"
#	else:
#		print âExecute o comando: â
#		print "alxebra help para obter axuda"
os.system('clear')

def rexistra(numero, texto):
	rexistro = open('.alxebra/rexistro', 'w')
	rexistro.write(str(numero))
	rexistro.write("\n")	
	rexistro.write(texto)
	rexistro.write("\n")
	rexistro.close()

def inicia():
	try: #Comprueba la exitencia del registro de alumno, si existe el programa continua
		rexistro = file('.alxebra/rexistro', 'r')

	except: #Si no existe lo crea abriendolo y escribiendo en el la primera entrada nombre y fecha.
		print "Ista Ã© a primeira vez que usa o programa de alxebra"
		time.sleep(1)
		nome = raw_input("Escriba o seu nome e pulse a tecla enter para validarlo dato: ")
		print "#"		
		time.sleep(1)		
		print "Encantado de traballar contigo ", nome
		print "#"		
		if not os.path.isdir('.alxebra'):	
			os.mkdir('.alxebra')
		nivel = 1	
		rexistra(nivel, nome)	
	rexistro = open ('.alxebra/rexistro', 'r+')
	nivel = int(rexistro.readline())
	nome = (rexistro.readline())
	#while time.clock() < t0 + 10:
	#	print "*"
	print nome, "Imos comenzar no nivel ", nivel
	rexistro.close()
	time.sleep(1)
###
def xerador(fin): #Crea un conjunto numÃ©rico que ira entre patentesis
	for i in range(fin):
                if fin >= 6:# now create too many numbers, for level 6 need 1
		        numeros.append(random.randint(0,99999))
		else:
			numeros.append(random.randint(-9,9))
		
	return numeros
###
def signo(): #Crea o signo dos parentesis
	s = random.randint(0,1)
	if s == 1:
		ss = "+"		
	else:
	 	ss = "-"
	return ss
###
def creador_alxebra(fin): #Engade Ã³ conxunto numÃ©rico os parentesis mÃ¡is o signo dos mesmos
	if nivel < 3:
		alxebra.append(signo())
		alxebra.append("(")
		for i in range(fin):	
			alxebra.append(numeros[i])
		alxebra.append(")")		
		return alxebra
	elif nivel == 3:
		alxebra.append(signo())
		alxebra.append("(")
		for i in range(fin):	
			alxebra.append(numeros[i])
		alxebra.append(")")		
		return alxebra
	elif nivel == 4: # 3 nÃºmeros entre parentese 1 multiplicando
		alxebra.append(numeros[0])
		alxebra.append("Â·(")
		for i in range(1,fin):	
			alxebra.append(numeros[i])
		alxebra.append(")")		
		return alxebra
	elif nivel == 5: # 3 nÃºmeros entre parentese  2 multiplicando
		alxebra.append("(")		
		alxebra.append(numeros[0])
		alxebra.append(numeros[1])
		alxebra.append(")")
		alxebra.append("Â·(")
		for i in range(2,fin):	
			alxebra.append(numeros[i])
		alxebra.append(")")		
		return alxebra
	elif nivel == 6:
	        show("odd")
		dividend = max(numeros[0],numeros[1])
		divisor = min(numeros[0],mumeros[1])
		qoutien = dividend//divisor
		rest = dividend%divisor
		print "Reparte" + dividend 
		print "castañas en" + divisor 
		print "bolsas" 
		print "sempre podes dividir se segues estas normas"
		time.sleep(5)
		print "colledo do saco" + divisor
		print "castañas as veces que queiras"
		time.sleep(10)
		print "ata repartilas por igual nas bolsas"
		
		for i in range(len(quotien)):	
		    print "Sempre podes tomar " +quotien(i)
		    print "veces " +divisor
		    print "quedando no saco " +dividend-quotien(i)*divisor
		    print "..."
		#add xogo de coller entre 1,2 e 3 vs IA
	        
		        
		
	else:
		rexistra(nivel, nome)
###
def mostrar(lista): #Mostra por pantalla as operaciÃ³ns a realizar
	for i in range(len(lista)):
		if int == type(lista[i]):
			if lista[i] >= 0:
				print "\b"+"+"+str(lista[i]),
			else:
				print "\b"+str(lista[i]),
		else:
			print "\b"+str(lista[i]),
###
def resolver(lista,signo): #Soluciona as operaciÃ³ns
	suma = 0
	if len(lista) < 4:
		for i in range(len(lista)):
			suma = suma + lista[i]
		if str(signo[0]) == "-":
			suma = -1*suma

	elif len(lista) == 4:
		for i in range(1,len(lista)):
			suma = suma + lista[i]
		suma = lista[0]*suma 
	elif len(lista) == 5:
		for i in range(2,len(lista)):
			suma = suma + lista[i]
		suma = suma * (lista[0]+lista[1])
	return suma

	if len(lista) > 5:
		print "Ata aquÃ­ o programa"
		print "Se quere seguir practicando, lea o ficheiro orixinal"
		sair(rexistro)
###
def proba():
	#raw_input()
		
	mostrar(operacions)
	proposta = (raw_input("= "))
	resultado = resolver(A,operacions)
	if int(proposta) == resultado:
		print "Ben resolto"
                time.sleep(7)# aquÃ­ funciÃ³n de menxase Ã³ azar

	else:
		axuda(nivel)		
		print "Voltao pensar con calma"
		
		proba()

###
def show(chapter):
	if chapter == "odd":
	        print "A división e un concepto de reparto."
		time.sleep(3)
		print "Separar os elementos dun conxunto numérico en subgrupos do mesmo tamaño"
		time.sleep(9)
		print "Vinte catro castañas dun saco repartidas entre tres bolsas ... "
		time.sleep(10)
		print "Oito castañas en cada bolsa"
		time.sleep(4)
		print "Pero ..."
		time.sleep(2)
		print "E, vinte cinco castañas dun saco repatidas entre tres bolsas ..."
		time.sleep(11)
		print "Podes repartir vinte catro das vinte cinco, pero sobra unha castaña"
		time.sleep(12)
		print "da que poderas repatir un tercio en cada bolsa"
		time.sleep(7)
		print "Oito castañas e un tercio en cada bolsa ..."
		time.sleep(13)
		print "Imos comenzar a división"
		time.sleep(2)
	else:
	        pass
###
def axuda(nivel):
	if nivel == 1:
		print "Se o signo que estÃ¡ fora do parentese e negativo, enton cambiamos o signo do nÃºmero enteiro contido dentro do parentese"
	        print "O signo non é máis que o sentido no percorrido na recta dos números"
		print "Se perde algo negativo, entón é algo positivo"
	elif nivel == 2:
		print "A adiciÃ³n de nÃºmeros enteiros estÃ¡ rexida polos signos dos mesmos"
		print "Se todos teÃ±en o mesmo signo sumanse os valores absolutos dos nÃºmeros e Ã³ resultado ponselle o signo que tiÃ±an todos."
		print "Se teÃ±en distinto signo a o valor absoluto do maior quitÃ¡moslle o valor absoluto do menor e deixamos o signo do que teÃ±a o maior valor absoluto"
		print " +3+2 = +5;   +2+3 = +5"
		print " -3-2 = -5;   -2-3 = -5"
		print " +3-2 = +1;   -2+3 = +1"
		print " -3+2 = -1;   +2-3 = -1"
		# Add level to abs() absolute value
	elif nivel == 3:
		print "Na multiplicaciÃ³n de números enteiros, multiplicase primeiro o valor absoluto dun nÃºmero polo outro para engadirlle a multiplicaciÃ³n dos signos que segue estas regras"
		print "Se os signos son iguais o resultado Ã© positivo"
		print "Se os signos son distintos o resultado Ã© negativo"
		print " +3·+2 = +6;   +2·+3 = +6"
		print " -3·-2 = +6;   -2·-3 = +6"
		print " +3·-2 = -6;   -2·+3 = -6"
		print " -3·+2 = -6;   +2·-3 = -6"
		# Add random examples
	elif nivel == 4:
		print "Lembre sempre a prioridade das operaciÃ³ns"
		print "Primeiro parentese"
		print "Segundo potencias e raÃ­ces"
		print "Terceiro multiplicaciÃ³ns e divisiÃ³ns"
		print "Cuarto operaciÃ³ns de adiciÃ³ns, coÃ±ecidas como sumas e restas"
	else:
		print "Consulte os sÃ©us aputamentos, compaÃ±eiros, libros, profesor, www.wikipedia.org"		
###
def rexistro(nivel):
	ficherio = open(".alxebra/rexistro", 'w')
	ficheiro.write(nivel)
	#ficheiro.write("\n")
	#ficheiro.close()
###
inicia()

acertos = 0
ficheiro = open('.alxebra/rexistro', 'r')
nivel = int(ficheiro.readline())
nome = (ficheiro.readline())
ficheiro.close()
print "Resolva as seguintes operaciÃ³ns, ben nunha folla, ben mentalmente e introduza o resultado (pulsa enter para continuar) \n"
			
while True:
	numeros = []
	alxebra = []
	A = xerador(nivel)
	operacions = creador_alxebra(nivel)
	proba()
	acertos = acertos +1
	if acertos%2 == 0:
		acertos = 0
		nivel = nivel + 1
		print "Acadas o nivel ", nivel
		rexistra(nivel, nome)
		for i in range(1,nivel):
			print "*",nivel,
		time.sleep(nivel/2)
		print " "		
	os.system('clear')
#PARA CERRAR SESIÃN USAR TECLAS DE ESC CON CONFIRMACIÃN Y USAR close .REXISTRO TRAS ESCRIBIRLO
sair(rexistro)
