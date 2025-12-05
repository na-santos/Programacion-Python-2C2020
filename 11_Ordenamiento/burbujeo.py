#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 17:24:33 2020

@author: nsantos
"""
def ord_burbujeo(lista):
    '''Ordena una lista de elementos según el método de burbujeo y devuelve
     la cantidad de operaciones realizadas.
     Pre: los elementos de la lista deben ser comparables.
     Post: la lista está ordenada.'''
    contador =  0
    for j in range(len(lista)-1,-1,-1):
        contador += compara_elementos_sucesivos(lista,j)
        #print("DEBUG: ", lista)
    return contador
        
def compara_elementos_sucesivos(lista,j):
    i = 0
    while i<j:
        if lista[i + 1] < lista[i]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
        i+=1
    return i #Devuelve la cantidad de comparaciones

#l = [0, 9, 3, 8, 5, 3, 2, 4]
#l = [1, 2, -3, 8, 1, 5, 1, 2, -3, 8, 1, 5]
#l = [1, 2, 3, 4, 5]
#l = [0, 9, 3, 8, 5, 3, 2, 4]
#l = [10, 8, 6, 2, -2, -5]
#l = [2, 5, 1, 0]

