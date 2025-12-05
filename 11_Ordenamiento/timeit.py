#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:29:36 2020

@author: nsantos
"""
import timeit as tt
import ordenar_seleccion as sel
import numpy as np
import matplotlib.pyplot as plt
import random

#%%
tt.timeit('time.sleep(1)',number = 1)
tt.timeit('"-".join(str(n) for n in range(100))', number = 1)
tt.timeit('"-".join(str(n) for n in range(100))', number = 10000)

#%%

def generar_lista(N):
    random.seed(31415)
    lista = [random.randint(1,1000) for j in range(N)]
    return lista
#%%

listas = []
for N in range(1, 256):
    listas.append(generar_lista(N))
   
#%%
    
def experimento_timeit_seleccion(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método para cada lista.
    """
    tiempos_seleccion = []
    
    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('sel.ord_seleccion(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    
    return tiempos_seleccion
#%%

tiempos_seleccion = experimento_timeit_seleccion(listas, 100)
plt.plot(tiempos_seleccion)

#Me quedó un poco mas arriba que el que muestran ellos.