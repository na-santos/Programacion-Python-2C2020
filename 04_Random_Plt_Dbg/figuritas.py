#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:28:56 2020

@author: noelia
"""

#¿Cuántas figuritas hay que comprar para completar el álbum del Mundial?

#Álbum con 670 figuritas.
#Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
#Cada paquete trae cinco figuritas.

import random
import numpy as np 


def crear_album(figus_total):
    return np.zeros((figus_total))

def album_incompleto(A):  
    esta_incompleto = True
    if np.nonzero(A == 0)[0].size==0:
        esta_incompleto=False
    return esta_incompleto

# Ejercicio 4.17: Comprar


def comprar_figu(figus_total):
    return random.randint(0,figus_total-1)
        
#Ejercicio 4.18: Cantidad de compras

    
def cuantas_figus(figus_total):
    album=crear_album(figus_total)
    compras = 0
    while album_incompleto(album):
        compras+=1
        album[comprar_figu(figus_total)] = 1
    return compras
        
#Ejercicio 4.19:

n_repeticiones = 1000
figus_total=6
cuantas_f=[cuantas_figus(figus_total) for i in range(n_repeticiones)]


promedio = np.mean(cuantas_f)        
        
#Ejercicio 4.20:
        
n_repeticiones = 100
figus_total=670
cuantas_f=[cuantas_figus(figus_total) for i in range(n_repeticiones)]

promedio = np.mean(cuantas_f)   

#Ejercicio 4.21:

posiciones = np.arange(0,670,1)
paquete=random.choices(posiciones,k=5)

#Ejercicio 4.22:

def comprar_paquete(figus_total,figus_paquete):
    posiciones=np.arange(0,figus_total,1)
    paquete = np.array(random.choices(posiciones,k=figus_paquete))
    return paquete

#Ejercicio 4.23:

def cuantos_paquetes(figus_total,figus_paquete):
    album=crear_album(figus_total)
    compras = 0
    while album_incompleto(album):
        compras+=1
        album[comprar_paquete(figus_total,figus_paquete)] = 1
    return compras
        
#Ejercicio 4.24:
        
n_repeticiones = 100
figus_total=670
figus_paquete = 5
cuantas_f=[cuantos_paquetes(figus_total,figus_paquete) for i in range(n_repeticiones)]

promedio = np.mean(cuantas_f)

#Ejercicio 4.25:

cuantas_f=np.array(cuantas_f)
casos = sum(cuantas_f<=850)
probabilidad =casos/len(cuantas_f)

#Ejercicio 4.26: Plotear el histograma

import matplotlib.pyplot as plt

plt.hist(cuantas_f,bins=25)

#Ejercicio 4.27:

def prob_acumulada(cuantas_f,prob):
    cuantas_f=np.array(cuantas_f)
    probabilidad= 1
    fig =sorted(cuantas_f)
    j= len(fig)
    while probabilidad > prob:
        j-= 1
        casos = sum(cuantas_f<=fig[j])
        probabilidad =casos/len(cuantas_f)
    return fig[j]

prob_acumulada(cuantas_f,0.9)

#1117

#Ejercicio 4.28:
    
#Repetí suponiendo que no hay figuritas repetidas en un paquete. ¿Cuánto cambian las probabilidades?

#Ejercicio 4.29: Cooperar vs competir

#Por último, suponé que cinco amigues se juntan y deciden compartir la 
#compra de figuritas y el llenado de sus cinco álbumes solidariamente. 
#Calculá cuántos paquetes deberían comprar si deben completar todos. 
#Hacé 100 repeticiones y compará el resultado con la compra individual 
#que calculaste antes.

