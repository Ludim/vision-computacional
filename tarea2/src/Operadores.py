#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image

class Operadores:
    def __init__(self,image):
        if image.mode == 'L':
            print 'Sorry in this moment only works with image in RGBA or RGB'
        self.img = image#.resize((450,450))
        self.matrizPixel = self.img.load()
        self.width= self.img.size[0]
        self.height= self.img.size[1]
        self.newImag = Image.new(self.img.mode, self.img.size)

    def imprimirMatrizSalida(self):
        archivoOutput = open("output.txt", "w") # matriz cuando se le aplica un operador
        matrizImg = self.newImag.load()
        for x in xrange(self.width):
            for y in xrange(self.height):
                r = matrizImg[x,y][0]
                archivoOutput.write(str(r)+str(", "))
            archivoOutput.write("\n\n")
        archivoOutput.close()
        print(" > Matriz de salida guardada en archivo output.txt")

    def grayScale(self,output):
        archivoInput = open("output.txt", "w") # matriz cuando se le aplica un operador
        print " > Cambiando a escala de grises"
        for x in range(self.width):
            for y in range(self.height):
                red = self.matrizPixel[x,y][0]
                green = self.matrizPixel[x,y][1]
                blue = self.matrizPixel[x,y][2]
                gray = int((max(red,green,blue) + min (red,blue,green))/2)
                self.newImag.putpixel((x,y),(gray,gray,gray))
                archivoInput.write(str(gray)+str(", "))
            archivoInput.write("\n\n")
        self.newImag.save("../img/"+output,self.img.format)
        print " > Matriz de entrada guarda en archivo input.txt"
        archivoInput.close()
        nombreImgSalida = "../img/"+output # regresamos el nombre del archivo
        print " > Nombre imagen escala de gris: "+ nombreImgSalida
        return nombreImgSalida # regresamos el nombre del archivo

#op = Operadores(Image.open('../img/flor'))
#op1 = Operadores(Image.open('../img/flor'))
#op2 = Operadores(Image.open('../img/cumple'))
#op3 = Operadores(Image.open('../img/silla'))
#op4 = Operadores(Image.open('../img/golpe'))
#op5 = Operadores(Image.open('../img/pelea'))
#op.grayScale("florgris")
#op1.grayScale("florgris")
#op2.grayScale("cumplegris")
#op3.grayScale("sillagris")
#op4.grayScale("golpegris")
#op5.grayScale("peleagris")
