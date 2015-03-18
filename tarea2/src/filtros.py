#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Ludim Sanchez'

from PIL import Image
import ImageDraw
from Operadores import Operadores
import math # para funcion techo (ceil)
#import # importar el archivo en el que se tiene la funcion para guardar las matrices
        #en archivo, asi como el operador de escala de gris

class Filtros:
    def __init__(self,image):
        self.img = image#.resize((450,450))
        self.matriz = self.img.load()
        self.w = image.size[0]
        self.h = image.size[1]
        self.newImg = Image.new(self.img.mode, self.img.size)

    # Regresa los vecinos del pixel dado
    def vecinos(self,x,y):
        listaVecinos = []
        #print x,",",y,
        try: # esquina superior izquierda
            listaVecinos.append(self.matriz[x-1,y-1][0])
        except IndexError: pass
        try: # arriba
            listaVecinos.append(self.matriz[x,y-1][0])
        except IndexError: pass
        try: # esquina superior derecha
            listaVecinos.append(self.matriz[x+1,y-1][0])
        except IndexError: pass
        try: # izquierda
            listaVecinos.append(self.matriz[x-1,y][0])
        except IndexError: pass
        try: # derecha
            listaVecinos.append(self.matriz[x+1,y][0])
        except IndexError: pass
        try: # esquina inferior izquierda
            listaVecinos.append(self.matriz[x-1,y+1][0])
        except IndexError: pass
        try: # abajo
            listaVecinos.append(self.matriz[x,y+1][0])
        except IndexError: pass
        try: # esquina inferior derecha
            listaVecinos.append(self.matriz[x+1,y+1][0])
        except IndexError: pass
        return listaVecinos

    def media(self,output): #promedio
        print ' > Aplicando filtro media'
        for x in xrange(self.w):
            for y in xrange(self.h):
                vecinos = self.vecinos(x,y) # usar otra forma for[-1,0,1] para usar menos memoria
                media = sum(vecinos) / len(vecinos) # sum funcion en python para sumar elementos de una lista
                self.newImg.putpixel((x,y),(media,media,media))
        self.newImg.save("../img/"+output+"media",self.img.format)

    def mediana(self,output): # la de en medio
        print ' > Aplicando filtro mediana'
        for x in xrange(self.w):
            for y in xrange(self.h):
                vecinos = self.vecinos(x,y)
                vecinos.sort()
                if len(vecinos) % 2 == 0:  # par
                    mediana = (vecinos[(len(vecinos)/2)] + vecinos[(len(vecinos)/2)+1])/2
                    self.newImg.putpixel((x,y),(mediana,mediana,mediana))
                else:
                    mediana = vecinos[int(math.ceil(len(vecinos)/2))]
                    self.newImg.putpixel((x,y),(mediana,mediana,mediana))
        self.newImg.save("../img/"+output+"mediana",self.img.format)

    # mediana en base al pseudocodigo del libro
    def medianaLibro(self,output):
        print ' > Aplicando filtro mediana'
        for x in xrange(self.w):
            for y in xrange(self.h):
                vecinos = self.vecinos(x,y)
                minP = min(vecinos)
                maxP = max(vecinos)
                if self.matriz[x,y][0] < minP:
                    self.newImg.putpixel((x,y),(minP,minP,minP))
                elif self.matriz[x,y][0] > maxP:
                    self.newImg.putpixel((x,y),(maxP,maxP,maxP))
                else:
                    self.newImg.putpixel((x,y),(self.matriz[x,y][0],self.matriz[x,y][0],self.matriz[x,y][0]))
        self.newImg.save("../img/"+output+"mediana2",self.img.format)


    def moda(self,output):
        print ' > Aplicando filtro moda'
        for x in xrange(self.w):
            for y in xrange(self.h):
                vecinos = self.vecinos(x,y)
                frecuencias = {}
                #print vecinos," ",
                for i in xrange(len(vecinos)):
                    if vecinos[i] in frecuencias:
                        frecuencias[vecinos[i]] = frecuencias[vecinos[i]] + 1
                    else:
                        frecuencias[vecinos[i]] = 1
                #print frecuencias," "
                k = frecuencias.keys()
                v = frecuencias.values()
                moda = []
                j = 0
                for i in v:
                    if max(v) == i:
                        moda.append(k[j])
                    j+=1
                if len(moda) > 1: 
                    # hay mas de dos numeros como moda entonces aplicamos
                    # promedio entre las dos para poner el nuevo pixel
                    moda = int(sum(moda)/len(moda))
                else:
                    moda = moda.pop()
                self.newImg.putpixel((x,y),(moda,moda,moda))                
        self.newImg.save("../img/"+output+"moda",self.img.format)

    def salPimienta(self,output):
        print ' > Aplicando filtro sal y pimienta'
        for x in xrange(self.w):
            for y in xrange(self.h):
                pixelAct = self.matriz[x,y][0]
                if pixelAct == 0 or pixelAct == 255:
                    vecinos = self.vecinos(x,y)
                    pixelAct = int(sum(vecinos)/len(vecinos))
                self.newImg.putpixel((x,y),(pixelAct,pixelAct,pixelAct))
        self.newImg.save("../img/"+output+"salpimienta",self.img.format)

if __name__ == '__main__':
    #nameIm = argv[1]
    directorio = '../img/'
    imagen = 'SaltAndPeppermediana' #'umbral'#Chita_16umbral'#flor'
    # cambiamos primero la imagen de entrada a escala de grises
    try:
        op = Operadores(Image.open(directorio+imagen)) # cuando se intenta crear el objeto y la entrada es en blanco y negro entonces regresa un error (image.mode = 'L')
        imgGris = op.grayScale(imagen+"gris")
        filtro = Filtros(Image.open(imgGris))
        print '\n',' > Imagen: '+ directorio+imagen
        filtro.media(imagen)
        filtro.mediana(imagen)
        filtro.medianaLibro(imagen)
        filtro.moda(imagen)
        filtro.salPimienta(imagen)
        print 
    except:
        print ' > Lo siento en este momento solo funciono con imagenes en escala de RGB o RGBA'

