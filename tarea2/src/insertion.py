#!/usr/bin/python2


# algoritmo tomado del libro de introduccion a los algoritmos
def insertionSort(array):
    print array
    j = 1
    for j in xrange(len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i-=1
        array[i+1] = key
    print array

    media = 0
    for j in array:
        media += j
        print media
    print media/len(array)

def main():
    ejercicio1_1 = [3.4,2.8,4.4,2.5,3.3,4.0,4.8,5.6,5.2,2.9,3.7,3.0,3.6,2.8,4.8]
    ejercicio1_3_se = [227,222,218,217,225,218,216,229,228,221]
    ejercicio1_3_ce = [219,214,215,211,209,218,203,204,201,205]
    insertionSort(ejercicio1_3_ce)

main()
