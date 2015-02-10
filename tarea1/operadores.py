#!/usr/bin/python
#-*- coding: utf-8 -*-

from PIL import Image
from sys import argv
import math
from matplotlib.pylab import hist, show
'''
Clase que tiene los operadores encargados para la tarea 1:
  Operaciones:
     Individual
        - Shifting horizontal
        - Shifting vertical
        - Shifting diagonal
        - Oscurecer una imagen
        - Presentar una imagen con su reflejo. 
        - Presentar uan imagen con su inversion vertical-horizontal (esto no es voltear la imagen vertica horizontal??, NO EL EFECTO ESPEJO HORIZONTAL VERTICAL)
     Grupal
      Permitir al usuario elegir entre diferentes operaciones
        - Aclarado (ya)
        - Copiado (ya)
        - Escala de grises (ya)
        - Imagen binaria (ya) => umbral???
        - Umbral (ver diapositiva 47) es para obtener bordes
        - Negativo (ya)
        - Elongación o contraste de una imagen*  (cuando se tiene un rango ej 100 - 125 a 50 a 200) 
             Q0 = P0 *gamma + beta
diferencia entre aumento de brillo y aclarado de una imagen?
'''
class Operador():
    def __init__(self,image):
        self.i = image
        self.w = image.size[0]
        self.h = image.size[1]
        self.newIm = Image.new(self.i.mode, self.i.size)
    
    # TOMAR UNA IMAGEN ESCALA DE GRISES Y VER QUE TANTO AFECTA
    def elongacion(self):
        # primero obtener el pixel mas grande y el mas pequeno
        matrizPix = self.i.load() 
        listaPixeles = []
#        frecuencias = {}
#        for i in xrange(0,256):
#            frecuencias[i] = 0

        for x in xrange(self.w):
            for y in xrange(self.h):
                colorPromedio = (matrizPix[x,y][0] + matrizPix[x,y][1] + matrizPix[x,y][2])/3
                #colorPromedio = matrizPix[x,y][0]
                listaPixeles.append(colorPromedio)
                #print colorPromedio
                # if colorPromedio in frecuencias:                    
                #     frecuencias[colorPromedio] = frecuencias[colorPromedio] + 1
        # print "FRECUENCIAS"
        # # http://progpython.blogspot.mx/2011/09/histogramas-con-python-matplotlib.html
        # # http://pythonya.appspot.com/detalleconcepto?deta=Los%20diccionarios%20tratados%20como%20objetos
        # print frecuencias.values()
        # print
        # hist(frecuencias.values(), 256,(0,255))
        # show()
            

        #print frecuencias
        pixMenor = min(listaPixeles)
        pixMayor = max(listaPixeles)
        print "Pix menor ", pixMenor
        print "Pix mayor ",pixMayor
        
        # hay que ver como cambia el histograma
        for x in xrange(self.w):
            for y in xrange(self.h):
                r,g,b = self.i.getpixel((x,y))
                #print r,g,b
                r = ((r - pixMenor) / (pixMayor - pixMenor)) * r#255
                g = ((g - pixMenor) / (pixMayor - pixMenor)) * g#255
                b = ((b - pixMenor) / (pixMayor - pixMenor)) * b#255
                #print r,g,b
                self.newIm.putpixel((x,y),(r,g,b))
        self.newIm.save("fldrimg/elonga", self.i.format)
        

    # def shiftingHorizontal(self):
    #     # primero saco la media de cada columna
    #     for x in xrange(self.w):
    #         for y in xrange(self.h):
    #             r,g,b = self.i.getpixel((x,y))
    #             self.i.putpixel((x,y),(r,g,b))
    #     self.newIm.save("fldrimg/izq",self.i.format)

    # def shiftingVertical(self,mover,cuantosPixeles):
    #     print 'hola'
    #     return 1
        
    def umbral(self):
        print 'umbral'
        UMBRAL = 127 
        for x in xrange(self.w):
            for y in xrange(self.h):
                r,g,b = self.i.getpixel((x,y))
                if (r+g+b)/3 > UMBRAL:
                    self.newIm.putpixel((x,y),(255,255,255))
                else:
                    self.newIm.putpixel((x,y),(0,0,0))
        self.newIm.save("fldrimg/umbral",self.i.format)
                    



def main():
    nameIm = argv[1]
    print "My image: ", nameIm
    operador = Operador(Image.open(nameIm))
    #operador.shiftingHorizontal()
    #operador.umbral()
    operador.elongacion()


if __name__ == '__main__':
  main()
