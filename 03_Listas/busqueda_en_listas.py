#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 16:50:29 2020

@author: noelia
"""

#Ejercicio 3.6: Búsquedas de un elemento

def buscar_u_elemento(lista, e):
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si entontramos a e
            pos = i  # guardamos su posición
    return pos #Me devuelve la ultima posicion en la que aparece

#buscar_u_elemento([1,2,3,2,3,4],1)
#0
#buscar_u_elemento([1,2,3,2,3,4],2)
#3
#buscar_u_elemento([1,2,3,2,3,4],3)
#4
#buscar_u_elemento([1,2,3,2,3,4],5)
#-1


#Agregale a tu programa busqueda_en_listas.py una función buscar_n_elemento() 
#que reciba una lista y un elemento y devuelva la cantidad de veces que aparece 
#el elemento en la lista. Probá también esta función con algunos ejemplos.
    
def buscar_n_elemento(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    j=0 #Agrego un contador
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si entontramos a e
            j +=1 #aumento en 1 el contador
            pos = i  # guardamos su posición
    return pos,j

#buscar_n_elemento([1,2,3,2,3,4],1)
#0,1
#buscar_n_elemento([1,2,3,2,3,4],2)
#3,2
#buscar_n_elemento([1,2,3,2,3,4],3)
#4,2
#buscar_n_elemento([1,2,3,2,3,4],5)
#-1,0

#Ejercicio 3.7
def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía 
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en el primer elemento de la lisa en vez de cero
    for e in lista: # Recorro la lista y voy guardando el mayo
        if e > m:
            m = e
    return m

#maximo([1,2,7,2,3,4])
#7
#maximo([1,2,3,4])
#4
#maximo([-5,4])
#4
#maximo([-5,-4])
#-4

def minimo(lista):
    '''Devuelve el minimo de una lista, 
    la lista debe ser no vacía.
    '''
    # m guarda el mínimo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayo
        if e < m:
            m = e
    return m


