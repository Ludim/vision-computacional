#!/usr/bin/python
#-*- coding: utf-8 -*-
from PIL import Image # para manipulacion de imagenes, asi como guardar una nueva imagen
from sys import argv  # recibir nombre de imagen
import math           # funcion floor
from numpy import *   # shifting, para manipular matriz de pixelacion y obtener la mediana
import mat2Nm
'''
Clase que realiza las siguientes operaciones en imagenes:
    - Shifting horizontal
    - Shifting vertical
    - Shifting diagonal
    - Oscurecer
    - Reflejo de imagen (mirror)
    - Inversion vertical-horizontal
'''

class Individual():
    def __init__(self, image):
        self.i = image
        self.w = image.size[0]
        self.h = image.size[1]
        
    # Por el metodo lightness
    def escalaGrislg(self):
        newIm = Image.new(self.i.mode, self.i.size)
        matriz = self.i.load()
        for x in xrange(self.w):
            for y in xrange(self.h):
                r = matriz[x,y][0]
                g = matriz[x,y][1]
                b = matriz[x,y][2]
                gris = (max(r,g,b) + min (r,b,g))/2
                newIm.putpixel((x,y),(gris,gris,gris))
        newIm.save("gris",self.i.format)
        print newIm.mode

    def shiftHrzntl(self):
        matrizImg = self.i.load()
        promedioFil = mat2Nm.mat2Nm("fil",matrizImg,self.h,self.w)
        mitadIm = int(math.floor(self.h/2))
        print mitadIm
        newIm = Image.new(self.i.mode,self.i.size)
        for y in xrange(self.w):
            for x in xrange(mitadIm):
                r,g,b = self.i.getpixel((y,x))
                r1,g1,b1 = self.i.getpixel((y,self.h-x-1))
                r = int((promedioFil[x] * r)/promedioFil[len(promedioFil)-x-1])
                g = int((promedioFil[x] * g)/promedioFil[len(promedioFil)-x-1])
                b = int((promedioFil[x] * b)/promedioFil[len(promedioFil)-x-1])
                r1 = int((promedioFil[len(promedioFil)-x-1] * r1) / promedioFil[x])
                g1 = int((promedioFil[len(promedioFil)-x-1] * g1) / promedioFil[x])
                b1 = int((promedioFil[len(promedioFil)-x-1] * b1) / promedioFil[x])
                newIm.putpixel((y,x),(r,g,b))
                newIm.putpixel((y,self.h-x-1),(r1,g1,b1))
        newIm.save("shiftHorizontal",self.i.format)

def main():
    a = Individual(Image.open("operaciones/fldrimg/1"))
    a.escalaGrislg()
    a.shiftHrzntl()
    
if __name__ == "__main__":
    main()
