#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:03:00 2020

@author: noelia
"""
#%%
import random

#Ejercicio 4.6: Generala servida

def tirar():
        tirada=[]
        for i in range(5):
            tirada.append(random.randint(1,6)) 
        return tirada
    
tirada=tirar()
                
def es_generala(tirada):
    i=0
    es = False
    while i<7:
        i+=1
        if tirada.count(i) == 5:
            es=True 
    return es 



N = 1000000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

#Tiré 100000 veces, de las cuales 86 saqué generala servida.
#Podemos estimar la probabilidad de sacar generala servida mediante 0.000860.

#Tiré 1000000 veces, de las cuales 789 saqué generala servida.
#Podemos estimar la probabilidad de sacar generala servida mediante 0.000789.

#¿Por qué varían más los resultados obtenidos con N = 100000 que con N = 1000000? 
#¿Cada cuántas tiradas en promedio podrías decir que sale una generala servida? 
#¿Cómo se puede calcular la probabilidad de forma exacta?

# Porque tengo menos estadística 
# 1e6/780 = 1267 en promedio.
#6*(1/6)**5 es la probabilidad exacta  0.0007716049382716047

#%%
#Ejercicio 4.7

from collections import Counter
import random 

def tirar(n):
    tirada=[]
    for i in range(n):
        tirada.append(random.randint(1,6)) 
    return tirada
    

    
def es_generala():
    tirada=tirar(5)
    salida=False
    if all(tirada[0] == dado for dado in tirada): # Devuelve True si todos son True, todos los dados iguales
        salida=True
    else:
        for i in range(2): # puedo tirar dos veces mas 
            a=Counter(tirada).most_common(1) # me fijo que elemento se repite más
            tirada = tirar(5-a[0][1]) #Tiro [5- la cantidad de veces que salió el más repetido] dados
            if all(a[0][0] == dado for dado in tirada): # Me fijo que todos los elementos sean iguales
                salida=True #Si pasa es True y corto el for. Si no tiro una vez mas
            break 
    return salida


N = 100000
G = sum([es_generala() for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala no necesariamente servida.')
print(f'Podemos estimar la probabilidad de sacar generala no necesariamente servida mediante {prob:.6f}.')

#Tiré 100000 veces, de las cuales 1292 saqué generala no necesariamente servida.
#Podemos estimar la probabilidad de sacar generala no necesariamente servida mediante 0.012920.
    
#No llegue a escribir mejor que hacer cuando todos los dados son distintos en 
#la primera tirada, ahi me conviene tirar todos los dados de nuevo. 

