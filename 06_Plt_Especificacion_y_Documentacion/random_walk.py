#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:13:03 2020

@author: noelia
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

#%%
N = 100000 #cantidad de pasos de la caminata

n_caminatas = 12 #numero de caminatas

colors = cm.rainbow(np.linspace(0, 1, n_caminatas)) # vector de colores

lista=[] # Guardo las caminatas en una lista

maximo = [] # Voy a guarda la maxima distancia al origen (valor absoluto)
# de cada caminata


fig = plt.figure()
plt.subplot(2, 1, 1) 

for j in range(n_caminatas):
    caminata = randomwalk(N)
    maximo.append(max(abs(caminata)))
    lista.append(caminata)
    plt.plot(caminata,color=colors[j])
plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
plt.title(f'Caminatas al azar de {N} pasos')

plt.subplot(2, 2, 3) 
plt.plot(lista[maximo.index(max(maximo))],color=colors[maximo.index(max(maximo))])
#Me quedo con la caminata que tiene la maxima distancia al origen (para algun paso)
plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
plt.title(f'Trayectoria que más se aleja')


plt.subplot(2, 2, 4) 
plt.plot(lista[maximo.index(min(maximo))],color=colors[maximo.index(min(maximo))]) 
#Me quedo con la caminata que tiene la minima distancia al origen (para algun paso)
plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
plt.title(f'Trayectoria que menos se aleja')

fig.tight_layout()

#Podria mejorar la forma en que defino la caminata que mas y menos se aparta

