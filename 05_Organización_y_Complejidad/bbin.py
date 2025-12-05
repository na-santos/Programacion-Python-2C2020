#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:51:39 2020

@author: noelia
"""

#Ejercicio 5.11: Búsqueda binaria

#%%
def donde_insertar(lista, x, verbose = True):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    esta=False
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio
            esta=True
        else: 
            if izq==medio and lista[medio]<x:#si el borde izquierdo coindice con el medio (fin de la particion) 
                pos=medio+1 #en el medio mas uno deberia estar x si el valor en el medio es menor que x
            elif izq==medio and lista[medio]>x: #El otro caso en el que el valor en el medio es mayor que x 
                pos=medio #entonces en esa posicion tiria x
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos,esta #Agregue este boolean para poder utilizarla en la funcion insertar

#Esto tiene un problema si hay numeros repetidos en la lista.

def insertar(lista,x):    
    pos,esta = donde_insertar(lista,x)
    if esta: #si x esta en la lista
        return pos #devuelve la posicion
    else:
        lista.insert(pos,x) #si x no esta en la lista lo inserta en la posicion que corresponde
        return pos,lista #devuelve la posicion y la lista con x agregado

#donde_insertar([0,2,4,6], 4)
#insertar([0,2,4,6], 4)
#donde_insertar([0,2,4,6], 3)
#insertar([0,2,4,6], 3) 
    