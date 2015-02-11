import numpy
from PIL import Image
import math
img = Image.open("fldrimg/grislm")
#img = Image.open("fldrimg/oscura")
w = img.size[0]
h = img.size[1]
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
mitadIm = int(math.floor(h/2))
print mitadIm
newIm = Image.new(img.mode,img.size)
# # se usa el de columnas
# for y in xrange(w):
#     for x in xrange(mitadIm):
#         print y,x
#         r,g,b = img.getpixel((y,x))
#         r1,g1,b1 = img.getpixel((h-x-1,x))
#         r = int((promedioFil[y] * r) / promedioFil[len(promedioFil)-y-1])
#         g = int((promedioFil[y] * g) / promedioFil[len(promedioFil)-y-1])
#         b = int((promedioFil[y] * b) / promedioFil[len(promedioFil)-y-1])
#         r1 = int(((promedioFil[len(promedioFil)-x-1] * r1) / promedioFil[x]))
#         g1 = int(((promedioFil[len(promedioFil)-x-1] * g1) / promedioFil[x]))
#         b1 = int(((promedioFil[len(promedioFil)-x-1] * b1) / promedioFil[x]))
#         newIm.putpixel((y,x),(r,g,b))
#         newIm.putpixel((h-y-1,x),(r1,g1,b1))
# newIm.save("fldrimg/shiftHorizontal",img.format)
for y in xrange(w):
    for x in xrange(mitadIm):
        r,g,b = img.getpixel((y,x))
        r1,g1,b1 = img.getpixel((y,h-x-1))
        r = int((promedioFil[x] * r)/promedioFil[len(promedioFil)-x-1])
        g = int((promedioFil[x] * g)/promedioFil[len(promedioFil)-x-1])
        b = int((promedioFil[x] * b)/promedioFil[len(promedioFil)-x-1])
        r1 = int((promedioFil[len(promedioFil)-x-1] * r1) / promedioFil[x])
        g1 = int((promedioFil[len(promedioFil)-x-1] * g1) / promedioFil[x])
        b1 = int((promedioFil[len(promedioFil)-x-1] * b1) / promedioFil[x])
        newIm.putpixel((y,x),(r,g,b))
        newIm.putpixel((y,h-x-1),(r1,g1,b1))
newIm.save("fldrimg/shiftHorizontal",img.format)
# for x in xrange(mitadIm):
#     for y in xrange(w): # recorre para abajo                                                                                                         
#         r,g,b = img.getpixel((x,y))
#         r1,g1,b1 = img.getpixel((w-x-1,y))
#         r = int((promedioFil[x] * r) / promedioFil[len(promedioFil)-x-1])
#         g = int((promedioFil[x] * g) / promedioFil[len(promedioFil)-x-1])
#         b = int((promedioFil[x] * b) / promedioFil[len(promedioFil)-x-1])
#         r1 = int(((promedioFil[len(promedioFil)-x-1] * r1) / promedioFil[x]))
#         g1 = int(((promedioFil[len(promedioFil)-x-1] * g1) / promedioFil[x]))
#         b1 = int(((promedioFil[len(promedioFil)-x-1] * b1) / promedioFil[x]))
#         newIm.putpixel((x,y),(r,g,b))
#         newIm.putpixel((w-x-1,y),(r1,g1,b1))
# newIm.save("fldrimg/shiftHorizontal",img.format)

