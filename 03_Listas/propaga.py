#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:27:20 2020

@author: noelia
"""

#Ejercicio 3.9: Propagacion

def propagar(lista):   
    for i in range(1,len(lista)-1): # Primero recorro la lista 
        if lista[i]==1 and not lista[i-1]==-1: # En cada posicion me fijo si en la posicion i tengo un 1 y el i-1 es 0
            lista[i-1] = 1 # reemplazo por 1 el anterior
        if lista[i]==1 and not lista[i+1]==-1: # Me fijo si el elemento i es 1 y el i+1 es 0
            lista[i+1] = 1 # reemplazo por 1 al siguiente
    lista.reverse() #salgo del for e invierto la lista que obtuve, en las lineas que siguen hago lo mismo pero para la lista que obtuve invertida
    for i in range(1,len(lista)-1): #Recorro la lista que obtuve pero invertida
        if lista[i]==1 and not lista[i-1]==-1:
            lista[i-1] = 1
        if lista[i]==1 and not lista[i+1]==-1:
            lista[i+1] = 1
    lista.reverse() # La vuelvo a invertir para recuperar el orden original 
    return lista


propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
#[0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
propagar([ 0, 0, 0, 1, 0, 0])
#[ 1, 1, 1, 1, 1, 1]

