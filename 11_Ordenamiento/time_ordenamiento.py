#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:35:39 2020

@author: nsantos
"""
#Ejercicio 11.8:

import random
import ordenar_insercion_1 as ins
import ordenar_seleccion_1 as sel
import burbujeo_1 as bur
import merge_sort_1 as mer
import matplotlib.pyplot as plt
import timeit as tt
import numpy as np

#%%
#Ejercicio 11.4

def generar_lista(N):
    ''' Genera una lista de largo N
    con elementos del 1 al 1000 de forma aleatoria]'''
    lista = [random.randint(1,1000) for j in range(N)]
    return lista

#%%

listas = []
for N in range(1, 257):
    ''' Genera una lista con listas de diferentes largos (de 1 a 257)'''
    listas.append(generar_lista(N))
   
#%%


def experimento_timeit(listas, num, metodo):
    """
    Realiza un experimento usando timeit para evaluar un método
    de ordenamiento de listas con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método para cada lista.
    """
    tiempos= []
    
    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo= tt.timeit(metodo+'(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos.append(tiempo)
        
    # paso los tiempos a arrays
    tiempos = np.array(tiempos)
    
    return tiempos


#%%%

metodos = ['sel.ord_seleccion', 'ins.ord_insercion', 'bur.ord_burbujeo','mer.merge_sort']
tiempos_metodos = []
for metodo in metodos:
    tiempos_metodos.append(experimento_timeit(listas, 3, metodo))
        
plt.plot(tiempos_metodos[0], label = 'Selección')
plt.plot(tiempos_metodos[1], label = 'Inserción')
plt.plot(tiempos_metodos[2], 'x', label = 'Burbujeo')
plt.plot(tiempos_metodos[3], label = 'Merge sort')
plt.xlabel('N (Largo de la lista)')
plt.ylabel('Tiempo de ejecución')
plt.legend(loc='best')
        


#¿Coinciden las curvas con lo que habías predicho estimando el número de operaciones?

# No exactamente. Tarda más burbujeo que que selección!
# Incluso insercion tarda casi lo mismo o incluso un poco más que seleccion.
# El más rápido es merge sort
