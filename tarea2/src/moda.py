#!/usr/bin/python
#-*- coding: utf-8 -*-

# Programa para obtener la moda de una vecindad

# tengo un diccionario
# las keys son el color del pixel
# los valores son el numero de veces que se repite el pixel
d = {10:4,5:2,9:2,11:4}
print d
# una vez que tenemos las frecuencias se puede obtener la moda :D

# primero guardamos los valores y keys
k = d.keys()
print k
v = d.values()
print v
# obtenemos el mayor de los valores que quiere decir que 
# es el pixel que se repite mas veces
#m = max(v)
moda = []

# recorremos la lista de keys para obtener cual es el pixel
# que se repite mas
j = 0
for i in v:
    if max(v) == i:
        moda.append(k[j])
    j+=1

print "moda: ",moda,",",max(v) 
# si hay mas de dos numeros como moda entonces aplicamos
# promedio entre las dos para poner el nuevo pixel
if len(moda) > 1:
    print "hay mad de dos numeros como moda"
    print "Colo pixel ", sum(moda)/len(moda)
