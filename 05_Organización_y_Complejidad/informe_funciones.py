#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:18:51 2020

@author: noelia
"""
#Ejercicio 5.8
import csv
from fileparse import parse_csv
#%%
def leer_camion(nombre_archivo):
    ''' Lee un csv con tres columnas, la primera corresponde a la fruta, 
   el segundo cantidad de cajones y la tercera el precio del cajon.
   Devuelve una lista de diccionarios. 
    '''
    camion = parse_csv(nombre_archivo, select=['nombre','cajones','precio'], types=[str,int,float])
    return(camion)

#%% 
def leer_precios(nombre_archivo):
    ''' Lee un csv con dos columnas, la primera corresponde a la fruta, 
   la segunda el precio del cajon.
   Devuelve un diccionario  '''
    lista_precios = parse_csv('precios.csv',types=[str,float], has_headers=False)
    return dict(lista_precios)


#%%

def hacer_informe(camion,precios):
    informe=[]
    for s in camion:
        informe.append((s['nombre'],s['cajones'],s['precio'],precios[s['nombre']]-s['precio']))
    return(informe)

#%%


def tabla(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    encabezado=''
    for header in headers: 
        encabezado+=f'{header:>10s}'
    print(encabezado)
    print('---------- ---------- ---------- ----------')
    for fila in informe:
        d=dict(zip(headers,fila))
        print('{Nombre:>10s} {Cajones:10d} ${Precio:10.2f} {Cambio:>10.2f}'.format_map(d))

#%%
    
#def imprimir_informe(informe):
#    tabla()
     
 #%%

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion,precios)
    return tabla(informe)    
    

#informe_camion('camion.csv', 'precios.csv')

#files = ['camion.csv', 'camion2.csv']
#for name in files:
#    print(f'{name:-^43s}')
#    informe_camion(name, 'precios.csv')
#    print()
