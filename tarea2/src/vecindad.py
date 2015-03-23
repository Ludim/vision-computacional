#!/usr/bin/python
matriz = [[150,150,0,150,150],[150,0,0,0,150],[0,0,0,0,0],[150,0,0,0,150]]#,[150,150,0,150,150]]
visitados = []
vecindad = [] # lista de listas
aux = []
for w in range(len(matriz)): #img.size[0]):
	for h in range(len(matriz[0])):#img.size[0]):
		#print w,h
		if not((w,h) in visitados):
			vecindad = []
			siguiente = [(w,h)]		# posicion del pixel actual
			colPix = matriz[w][h] 	# color del pixel actual
			#print "siguiente = ", siguiente, " ",
			while siguiente:
				posPix = siguiente.pop()	# 0,0
				x = posPix[0]
				y = posPix[1]
				#print "   posPix = ", posPix
				visitados.append(posPix)
				if not(posPix in vecindad):
					vecindad.append(posPix)
				for i in range(x-1,x+2):
					for j in range(y-1,y+2):
						#print "(",i,j,")"
						if not(x == i and y == j): # no toma en cuenta el pixel actual
							if ((i >= 0 and j >= 0) and
								(i < len(matriz) and j < len(matriz[0])) 
								and (colPix == matriz[i][j])):
								posPix = (i,j)
								#print "posPix = ",posPix, "color = ",matriz[i][j]
								if (not(posPix in vecindad) and not(posPix in visitados)):
									#print " pixel anadido = ",posPix, " no esta en visitados ni vecindad"
									vecindad.append((i,j))
									siguiente.append((i,j))
				#print "\nsiguiente = ", siguiente
				#print " vecindad = ",vecindad
			#print "\n\n"

			####print "vecindad = ",vecindad
			aux.append(vecindad)
			###print "     aux = ",aux
			##print "\nsaliendo de while"
#print aux


for i in range(len(aux)):
	print aux[i]