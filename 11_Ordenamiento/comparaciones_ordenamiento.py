#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 11:46:51 2020

@author: nsantos
"""

import random
import ordenar_insercion as ins
import ordenar_seleccion as sel
import burbujeo as bur
import merge_sort as mer
import matplotlib.pyplot as plt

#%%
#Ejercicio 11.4

def generar_lista(N):
    ''' Genera una lista de largo N
    con elementos del 1 al 1000 de forma aleatoria]'''
    lista = [random.randint(1,1000) for j in range(N)]
    return lista

#%%
def experimento(N):
    ''' Genera una lista de largo N y cuenta la cantidad de operaciones
    realizadas por diferentes metodos de ordenamiento: seleccion, insercion, 
    burbujeo y merge sort'''
    lista = generar_lista(N)
    lista1 = lista.copy() #hago copias porque cada vez que corro un metodo de modifica la lista original
    lista2 = lista.copy()
    lista3 = lista.copy()
    lista4 = lista.copy()
    cont_sel = sel.ord_seleccion(lista1)
    cont_ins = ins.ord_insercion(lista2)
    cont_bur = bur.ord_burbujeo(lista3)
    cont_merge = mer.merge_sort(lista4)[1]
    return  cont_sel, cont_ins, cont_bur, cont_merge

#def comparaciones(N):
#    seleccion = []
#    inserccion = []
#    burbujeo = []
#    for k in range(1,100):
#        s, i, b = experimento(10)
#        seleccion.append(s)
#        inserccion.append(i)
#        burbujeo.append(b)
#        print(sum(seleccion)/len(seleccion),sum(inserccion)/len(inserccion), sum(burbujeo)/len(burbujeo))


#%%
#Ejercicio 11.5

seleccion = []
inserccion = []
burbujeo = []
merge =[]
for N in range(1,257):
    #cuento la cantidad de operaciones realizadas por cada metodo praa diferentes 
    #largos de listas
    s, i, b, m = experimento(N)
    seleccion.append(s)
    inserccion.append(i)
    burbujeo.append(b)
    merge.append(m)
    
        
plt.plot(seleccion, label = 'Selección')
plt.plot(inserccion, label = 'Insercción')
plt.plot(burbujeo, 'x', label = 'Burbujeo')
plt.plot(merge, label = 'Merge sort')
plt.xlabel('N (Largo de la lista)')
plt.ylabel('Cantidad de comparaciones')
plt.legend(loc='best')
        

#¿Cómo dirías que crece la complejidad de estos métodos? 
#¿Para cuáles depende de la lista a ordenar y para cuáles solamente depende del largo de la lista?

#Por burbujeo y selección la cantidad de comparaciones depende del largo de la lista
#La complejidad es en ambos casos N*(N-1)/2.
#Por insercción depende de qué lista se genere. 

#Extra: ¿Las curvas de complejidad quedaron suaves? ¿Se te ocurre cómo hacer para suavizarlas?
#La que es ruidosa es la de insercción justamente porque depende de como sea la lista.
# Podría repetirse para cada N k veces la experiencia y tomar un promedio.  