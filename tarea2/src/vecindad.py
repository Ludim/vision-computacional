#!/usr/bin/python
from PIL import Image
import random

img = Image.open("../img/umbral")
matriz = img.load()
width = img.size[0]
height = img.size[1]
new = Image.new(img.mode,img.size)
visitados = []
vecindad = [] # lista de listas
aux = []

colores = []
for i in range(width):
	for j in range(height):
		print img.getpixel((i,j))
		print matriz[i,j][0], ",",matriz[i,j][1],",",matriz[i,j][2]
		#colores.append(matriz[i,j][0])
#a = colores.sort()
#print colores
exit()

for w in range(width):
	for h in range(height):
#		print w,h
		if not((w,h) in visitados):
			vecindad = []
			siguiente = [(w,h)]
			colPix = matriz[w,h][0] # color pixel
			print "Color ",colPix
			nuevocolor = random.randint(0,255)
			new.putpixel((w,h),(nuevocolor,nuevocolor,nuevocolor))
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
								(i < width and j < height) 
								and (colPix == matriz[i,j][0])):
								posPix = (i,j)
								print "Color ",colPix, " Color vecino ", matriz[i,j][0]
								if (not(posPix in vecindad) and not(posPix in visitados)):
									new.putpixel(posPix,(nuevocolor,nuevocolor,nuevocolor))
									vecindad.append((i,j))
									siguiente.append((i,j))
			print vecindad
			aux.append(vecindad)
new.save("../img/umbral_VECINDAD", img.format)
for i in range(len(aux)):
	print aux[i]
