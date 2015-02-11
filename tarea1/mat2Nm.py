import numpy
def mat2Nm(prom,matrizImg,h,w):
    matriz = []
    for i in range(h):
        matriz.append([])
        for j in range(w):
            valor = (matrizImg[j,i][0] + matrizImg[j,i][1] + matrizImg[j,i][2]) / 3
            matriz[i].append(valor)
    matrixNm = numpy.array(matriz)
    print "Promedio columnas ",len(numpy.median(matrixNm,axis=0))
    print "Promedio filas ",len(numpy.median(matrixNm,axis=1))
    if prom == "col":
        promedioCol = numpy.median(matrixNm,axis=0)
        return promedioCol
    elif prom == "fil":
        promedioFil = numpy.median(matrixNm,axis=1)
        return promedioFil


