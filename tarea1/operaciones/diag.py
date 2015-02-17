import numpy
from PIL import Image
import math   
img = Image.open("fldrimg/1")
#img = Image.open("fldrimg/oscura")
w = img.size[0]
h = img.size[1]
print w,",",h
matrizImg = img.load() # la imagen debe estar en escala de grises
matriz = []
for i in range(h):
    matriz.append([])
    for j in range(w):
        valor = (matrizImg[j,i][0] + matrizImg[j,i][1] + matrizImg[j,i][2]) / 3
        matriz[i].append(valor)
#print numpy.array(matriz)
matrixNm = numpy.array(matriz)
promedioCol = numpy.median(matrixNm,axis=0)
promedioFil = numpy.median(matrixNm,axis=1)
print "Promedio columnas ",len(numpy.median(matrixNm,axis=0))
print "Promedio filas    ",len(numpy.median(matrixNm,axis=1))
# shift vertical
mitadIm = int(math.floor(w/2))
print mitadIm
newIm = Image.new(img.mode,img.size)
# se usa el de columnas
for x in xrange(mitadIm):
    for y in xrange(h): # recorre para abajo
        if y == h-1: # 1 porque toma el pixel de la posicion x +1
            r,g,b = img.getpixel((0,y))
            r1,g1,b1 = img.getpixel((0,y))
        else:
            r,g,b = img.getpixel((x,y+1))
            r1,g1,b1 = img.getpixel((w-x-1,y+1))

        r = int((promedioCol[x] * r) / promedioCol[len(promedioCol)-x-1])
        g = int((promedioCol[x] * g) / promedioCol[len(promedioCol)-x-1])
        b = int((promedioCol[x] * b) / promedioCol[len(promedioCol)-x-1])
        r1 = int(((promedioCol[len(promedioCol)-x-1] * r1) / promedioCol[x]))
        g1 = int(((promedioCol[len(promedioCol)-x-1] * g1) / promedioCol[x]))
        b1 = int(((promedioCol[len(promedioCol)-x-1] * b1) / promedioCol[x]))
        newIm.putpixel((x,y),(r,g,b))
        newIm.putpixel((w-x-1,y),(r1,g1,b1))
newIm.save("fldrimg/shiftDiagonal",img.format)
