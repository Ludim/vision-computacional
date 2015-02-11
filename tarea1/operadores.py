#!/usr/bin/python
#-*- coding: utf-8 -*-

from PIL import Image
from sys import argv
import math
from matplotlib.pylab import hist, show
import cv
from numpy import *
'''
Clase que tiene los operadores encargados para la tarea 1:
  Operaciones:
     Individual
        - Shifting horizontal
        - Shifting vertical
        - Shifting diagonal
        - Oscurecer una imagen (ya)
        - Presentar una imagen con su reflejo.(ya)
        - Presentar uan imagen con su inversion vertical-horizontal (esto no es voltear la imagen vertica horizontal??, NO EL EFECTO ESPEJO HORIZONTAL VERTICAL) (ya???)
     Grupal
      Permitir al usuario elegir entre diferentes operaciones
        - Aclarado (ya)
        - Copiado (ya)
        - Escala de grises (ya)
        - Imagen binaria (ya) => umbral???
        - Umbral (ver diapositiva 47) es para obtener bordes (ya)
        - Negativo (ya)
        - Elongación o contraste de una imagen*  (cuando se tiene un rango ej 100 - 125 a 50 a 200) 
             Q0 = P0 *gamma + beta
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
        frecuencias = {}
        for i in xrange(0,256):
            frecuencias[i] = 0

        for x in xrange(self.w):
            for y in xrange(self.h):
                colorPromedio = (matrizPix[x,y][0] + matrizPix[x,y][1] + matrizPix[x,y][2])/3
                #colorPromedio = matrizPix[x,y][0]
                listaPixeles.append(colorPromedio)
                #print colorPromedio
                if colorPromedio in frecuencias:
                     frecuencias[colorPromedio] = frecuencias[colorPromedio] + 1
        print "FRECUENCIAS"
        #http://progpython.blogspot.mx/2011/09/histogramas-con-python-matplotlib.html
        #http://pythonya.appspot.com/detalleconcepto?deta=Los%20diccionarios%20tratados%20como%20objetos
        print frecuencias.values()
        print
        hist(frecuencias.values(), 256,(0,255))
        show()
            
        print frecuencias
        pixMenor = min(listaPixeles)
        pixMayor = max(listaPixeles)
        print "Pix menor ", pixMenor
        print "Pix mayor ",pixMayor
        
        # hay que ver como cambia el histograma
        #gamma = pixMayor + 150
        #beta = pixMenor + 1
        #gamma  = 10
        #beta = 50
        scale_factor = 255 / (pixMayor - pixMenor)
        #http://homepages.inf.ed.ac.uk/rbf/BOOKS/VERNON/Chap004.pdf
        for x in xrange(self.w):
            for y in xrange(self.h):
                r,g,b = self.i.getpixel((x,y))
                r = int((int((r + pixMayor) * 2.55) + int((r - pixMenor) * 2.55))/2)
                g = int((int((g + pixMayor) * 2.55) + int((g - pixMenor) * 2.55))/2)
                b = int((int((b + pixMayor) * 2.55) + int((b - pixMenor) * 2.55))/2)
#                g = int((g + pixMayor) * 2.55)
#                b = int((b + pixMayor) * 2.55)
                #r = (r * gamma + beta)/255
                #g = (g * gamma + beta)/255
                #b = (b * gamma + beta)/255
                if r <= 0 or g <= 0 or b <= 0:
                    r,g,b = 0,0,0
                elif r >= 255 or g >= 255 or b >= 255:
                    r,g,b = 255,255,255
                self.newIm.putpixel((x,y),(r,g,b))
                
        self.newIm.save("fldrimg/elonga", self.i.format)
        matrizPix = self.newIm.load() 
        listaPixeles = []
        frecuencias = {}
        for i in xrange(0,256):
            frecuencias[i] = 0

        for x in xrange(self.w):
            for y in xrange(self.h):
                colorPromedio = (matrizPix[x,y][0] + matrizPix[x,y][1] + matrizPix[x,y][2])/3
                listaPixeles.append(colorPromedio)
                if colorPromedio in frecuencias:
                     frecuencias[colorPromedio] = frecuencias[colorPromedio] + 1
        print "FRECUENCIAS"
        print frecuencias.values()
        print
        hist(frecuencias.values(), 256,(0,255))
        show()
            
        print frecuencias

    def shiftHor(self):
        # primero mejor intenter con una matriz pequena
        # 
        centro = int(math.floor((self.w)/2))
        print centro
        # primero obtener las medias de cada columna
        matriz = self.i.load()
        mediaCol = []
        for y in xrange(self.h):
            media = 0
            for x in xrange(self.w):
                media = ((matriz[x,y][0] + matriz[x,y][1] + matriz[x,y][2]) / 3) + media
            media = media / self.w
            mediaCol.append(media)
            #print media
        print "Media de cada columna: ",mediaCol 
        print len(mediaCol)
        
        for y in xrange(self.h):
            for x in xrange(self.w): # recorre para abajo
                # obtener pixel de la otra esquina
                r,g,b = self.i.getpixel((self.w-10-y,x))
                r = (mediaCol[y] * r) / mediaCol[len(mediaCol)-y-1]
                g = (mediaCol[y] * g) / mediaCol[len(mediaCol)-y-1]
                b = (mediaCol[y] * b) / mediaCol[len(mediaCol)-y-1]
                self.newIm.putpixel((x,y),(r,g,b))
        self.newIm.save("fldrimg/shifth",self.i.format)


    def mirrorHorizontal(self):
        w = self.w * 2
        h = self.h
        newIm = Image.new(self.i.mode, (w,h))        
        matriz = self.i.load()
        for x in xrange(self.w):
            for y in xrange(self.h):
                r = matriz[x,y][0]
                g = matriz[x,y][1]
                b = matriz[x,y][2]
                newIm.putpixel((x,y),(r,g,b))
                newIm.putpixel((w-x-1,y),(r,g,b))
        newIm.save("fldrimg/espejo",self.i.format)

    def mirrorVertical(self):
        matriz = self.i.load()
        for x in xrange(self.w):
            for y in xrange(self.h):
                r = matriz[x,y][0]
                g = matriz[x,y][1]
                b = matriz[x,y][2]
                self.newIm.putpixel((self.w-x-1,self.h-y-1),(r,g,b))
        self.newIm.save("fldrimg/vertical",self.i.format)

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
    #operador.elongacion()
    #operador.shiftHor()
    operador.mirrorHorizontal()
    operador.mirrorVertical()
if __name__ == '__main__':
  main()
