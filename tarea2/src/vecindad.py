#!/usr/bin/python
from PIL import Image
import random

# poner el codigo en espanol, es decir variables en espanol no mezclado :P

#olvida la imagen y crea la matriz a partir de un archivo de texto
pixelesImagen = []

i = 0
with open("chitaoutput.txt","r") as archivo: # este archivo se genera cuando se umbraliza la imagen
	for linea in archivo:
		j = 0
		pixelesImagen.append([])
		for pixel in linea.split(","):
			if pixel != ' \n':
				pixelesImagen[i].append(int(pixel))
			j+=1
		i+=1


img = Image.open("../img/umbral")
#matriz = img.load()
anchoImag = img.size[0]
altoImag = img.size[1]
nuevaImag = Image.new(img.mode,img.size)
visitados = []
vecindad = [] # lista de listas
aux = []


#for w in range(width):
for w in range(anchoImag):
	for h in range(altoImag):
	#for h in range(height):
#		print w,h
		if not((w,h) in visitados):
			vecindad = []
			siguiente = [(w,h)]
			#colPix = matriz[w,h][0] # color pixel
			colPix = pixelesImagen[w][h] # color pixel
			print "Color ",colPix
			nuevocolor = random.randint(0,255)
			nuevaImag.putpixel((w,h),(nuevocolor,nuevocolor,nuevocolor))
			while siguiente:
				posPix = siguiente.pop() # posicion pixel
				x = posPix[0]
				y = posPix[1]
				visitados.append(posPix)
				if not(posPix in vecindad):
					vecindad.append(posPix)
				for i in range(x-1,x+2):
					for j in range(y-1,y+2):
						if not(x == i and y == j):
							if ((i >= 0 and j >= 0) and
								(i < anchoImag and j < altoImag) 
								and (colPix == pixelesImagen[i][j])):
								#and (colPix == matriz[i,j][0])):
								posPix = (i,j)
								#print "Color ",colPix, " Color vecino ", matriz[i,j][0]
								print "Color ",colPix, " Color vecino ", pixelesImagen[i][j]
								if (not(posPix in vecindad) and not(posPix in visitados)):
									nuevaImag.putpixel(posPix,(nuevocolor,nuevocolor,nuevocolor))
									vecindad.append((i,j))
									siguiente.append((i,j))
			print vecindad
			aux.append(vecindad)
nuevaImag.save("../img/umbral_VECINDAD", img.format)
for i in range(len(aux)):
	print aux[i]
