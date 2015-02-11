#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from sys import argv
import math
'''
Clase basica para aplicar filtro a una imagen. Los filtros son:
     - Aclarado
     - Negativo
     - B/N
     - Decolorar (lo blanco lo aclara, lo negro lo oscurece, para los demas colores fijar un umbral)
Autor: Ludim Sanchez Lopez
'''

class Filtro():
    def __init__(self,image):
        self.i = image
        self.w = image.size[0]
        self.h = image.size[1]
        self.newIm = Image.new(self.i.mode,self.i.size)

    def imagenOriginal(self):
        for x in xrange(self.w):
            for y in xrange(self.h):
                r,g,b = self.i.getpixel((x,y))
                self.newIm.putpixel((x,y),(r,g,b))
        self.newIm.save("fldrimg/original",self.i.format)
        
    def aclararImagen(self):
        for x in xrange(self.w):
            for y in xrange(self.h):
                r,g,b = self.i.getpixel((x,y))
                self.newIm.putpixel((x,y),(r+100,g+100,b+100))
        self.newIm.save("fldrimg/aclara",self.i.format)

    def negativo(self):
        for x in xrange(self.w):
            for y in xrange(self.h):
                r,g,b = self.i.getpixel((x,y))
                self.newIm.putpixel((x,y),(255-r,255-g,255-b))
        self.newIm.save("fldrimg/negativo",self.i.format)
    
    def blancoNegro(self):
        RANGE = 127
        for x in xrange(self.w):
            for y in xrange(self.h):
                r,g,b = self.i.getpixel((x,y))
                if (r+g+b) > RANGE: # negro
                    self.newIm.putpixel((x,y),(0,0,0))
                else: #blanco
                    self.newIm.putpixel((x,y),(255,255,255))
        self.newIm.save("fldrimg/2_c",self.i.format)
        
    # http://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
    # POr el metodo lightness
    def escalaGrisLg(self):
        for x in xrange(self.w):
            for y in xrange(self.h):
                r,g,b = self.i.getpixel((x,y))
                gris = (max(r,g,b) + min (r,b,g))/2
                self.newIm.putpixel((x,y),(gris,gris,gris))
        self.newIm.save("fldrimg/grislg",self.i.format)

    # Por el metodo luminosity
    def escalaGrisLm(self):
        for x in xrange(self.w):
            for y in xrange(self.h):
                r,g,b = self.i.getpixel((x,y))
                gris = int(0.21*r + 0.72*g + 0.07*b)
                self.newIm.putpixel((x,y),(gris,gris,gris))
        self.newIm.save("fldrimg/grislm",self.i.format)
        self.newIm.show()

def main():
    nameIm = argv[1]
    print "My image: ",nameIm
    filtro = Filtro(Image.open(nameIm))
    #filtro.movIzq()
    #filtro.aclararImagen()
    #filtro.negativo()
    #filtro.blancoNegro()
    #filtro.escalaGrisLm()
    #filtro.escalaGrisLg()
    #filtro.imagenOriginal()

if __name__ == '__main__':
    main()
