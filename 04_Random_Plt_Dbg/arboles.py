#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:59:16 2020

@author: noelia
"""
#%%
#Ejercicio 3.18: Lectura de todos los árboles

import csv

def leer_arboles(nombre_archivo):
	with open(nombre_archivo, 'rt') as f:
		rows=csv.reader(f) 
		headers = next(rows) 
		arboles = [] # lista de diccionarios con la informacion de los parques
		for n,row in enumerate(rows,start=1):
			record=dict(zip(headers,row)) 
			arboles.append(record)
	return(arboles)


nombre_archivo='arbolado-en-espacios-verdes.csv'
arboleda=leer_arboles(nombre_archivo) # esto es una lista de diccionarios

#%%

#Ejercicio 3.19: Lista de altos de Jacarandá

H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']


import matplotlib.pyplot as plt
nombre_archivo = 'arbolado-en-espacios-verdes.csv'
arboleda = leer_arboles(nombre_archivo)
plt.hist(H,bins=25)
plt.xlabel("alto (m)")
plt.ylabel("N° de cuentas")
plt.title("Histograma de altura para Jacarandá")


#%%
#Ejercicio 3.20: Lista de altos y diámetros de Jacarandá

import numpy as np
import matplotlib.pyplot as plt

HD=[(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

#[(5.0, 10.0),
# (5.0, 10.0),
# ...
# (17.0, 40.0)]

HD = np.array(HD)
plt.scatter(HD[:,1],HD[:,0], s=20, c='r', alpha=1)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")

#¿Ves alguna relación entre el diámetro y el alto de los Jacarndás? ¿Te parece que es una relación lineal o de otro tipo?
#Veo alguna relación, parece lineal para pequeños valores de diametro-alto.
#%%

#Ejercicio 3.21: Diccionario con medidas
 
def medidas_de_especies(especies,arboleda):
    diccionario = { especie: [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies }       
    return diccionario

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
dic = medidas_de_especies(especies,arboleda)

## asi lo pensé inicialmente
#diccionario = { especie: [] for especie in especies }       
# quiero que cada clave tenga asociado una lista de tuplas.
# Uso lo que hice en el ejercicio anterior para hacer un for e ir recorriendo
# todas las especies. 
#for especie in especies:
#    HD=[(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
#    diccionario[especie]= HD
# finalmente lo que llame HD lo puse adentro de [] de la primer linea (eso es lo que esta arriba)


arboleda = leer_arboles(nombre_archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)

eucalipto =np.array(medidas['Eucalipto'])
palo_borracho =np.array(medidas['Palo borracho rosado'])
jacaranda = np.array(medidas['Jacarandá'])


plt.scatter(eucalipto[:,1],eucalipto[:,0], s=20, c='r', alpha=1,label="Eucalipto")
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Eucalipto")
plt.scatter(palo_borracho[:,1],palo_borracho[:,0], s=20, c='b', alpha=1,label="Palo borracho rosado")
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Palo borracho rosado")
plt.scatter(jacaranda[:,1],jacaranda[:,0], s=20, c='k', alpha=1,label="Jacarandá")
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.legend(loc='best')
plt.title("Relación diámetro-alto")
plt.xlim(0,250)
plt.ylim(0,50) 

# ¿Se mantienen las relaciones que viste en el ejercicio anterior 
#para las tres especies? ¿Hay diferencias entre las especies? 
#Para un mismo alto, ¿cuál tiene mayor diámetro (tipicamente)?

#Si bien para las distintas especies hay diferencias 
#En general las tendencias son similares
# Tipicamente para un mismo alto el Eucalipto tiene mayor diametro

