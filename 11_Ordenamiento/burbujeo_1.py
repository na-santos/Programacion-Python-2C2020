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
    for j in range(len(lista)-1,-1,-1):
        compara_elementos_sucesivos(lista,j)


        
def compara_elementos_sucesivos(lista,j):
    i = 0
    while i<j:
        if lista[i + 1] < lista[i]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
        i+=1




