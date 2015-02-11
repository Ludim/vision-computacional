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
