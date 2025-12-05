#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:59:16 2020

@author: noelia
"""
#%%
#Ejercicio 3.18: Lectura de todos los árboles

import csv

def leer_parque(nombre_archivo):
	with open(nombre_archivo, 'rt') as f:
		rows=csv.reader(f) 
		headers = next(rows) 
		arboles = [] # lista de diccionarios con la informacion de los parques
		for n,row in enumerate(rows,start=1):
			record=dict(zip(headers,row)) 
			arboles.append(record)
	return(arboles)


nombre_archivo='arbolado-en-espacios-verdes.csv'
arboleda=leer_parque(nombre_archivo) # esto es una lista de diccionarios

#%%

#Ejercicio 3.19: Lista de altos de Jacarandá

H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']


#%%
#Ejercicio 3.20: Lista de altos y diámetros de Jacarandá

HD=[(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

#[(5.0, 10.0),
# (5.0, 10.0),
# ...
# (17.0, 40.0)]

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