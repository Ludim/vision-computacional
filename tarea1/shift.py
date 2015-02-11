import numpy
from PIL import Image

def PIL2arra(img):
    return numpy.array(img.getdata(), numpy.uint8)
   
#img = Image.open("fldrimg/2")#.convert("L")
#print img
#arr = numpy.array(img)#.getdata()).reshape(img.size[0],img.size[1],3)
print numpy.array([[1,2,3,4],[4,5,6,4],[7,8,9,4]])
#numpy.array([[1,2,3],[4,5,6],[7,8,9]])
a = numpy.array([[1,2,3,4],[4,5,6,4],[7,8,9,4]])
print "Promedio columnas    ",len(numpy.median(a, axis = 0))
print "Promedio filas ",len(numpy.median(a, axis = 1))


img = Image.open("fldrimg/grislg")
w = img.size[0]
print w
h = img.size[1]
print h
matrizImg = img.load()
#print arr
# la imagen debe estar en escala de grises
matriz = []
for i in range(h):
    matriz.append([])
    for j in range(w):
        valor = (matrizImg[j,i][0] + matrizImg[j,i][1] + matrizImg[j,i][2]) / 3
        matriz[i].append(valor)

#print numpy.array(matriz)
matrixNm = numpy.array(matriz)
for x in matrixNm:
    print x
print "Promedio columnas ",len(numpy.median(matrixNm,axis=0))
print "Promedio filas    ",len(numpy.median(matrixNm,axis=1))
