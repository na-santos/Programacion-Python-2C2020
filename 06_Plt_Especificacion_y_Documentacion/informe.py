#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:18:51 2020

@author: noelia
"""
#Ejercicio 5.8
import csv
from fileparse import parse_csv
import sys
#%%
def leer_camion(nombre_archivo):
    ''' Lee un csv con tres columnas, la primera corresponde a la fruta, 
   el segundo cantidad de cajones y la tercera el precio del cajon.
   Devuelve una lista de diccionarios. 
    '''
    with open(nombre_archivo) as f:
        camion = parse_csv(f, select=['nombre','cajones','precio'], types=[str,int,float])
    return(camion)

#%% 
def leer_precios(nombre_archivo):
    ''' Lee un csv con dos columnas, la primera corresponde a la fruta, 
   la segunda el precio del cajon.
   Devuelve un diccionario  '''
    with open(nombre_archivo) as f:
        lista_precios = parse_csv(f,types=[str,float], has_headers=False)
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

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion,precios)
    return tabla(informe)    
#%%    
    
def main(parametros):
    ''' Lee una una lista de parámetros en la línea de comandos 
        y produce la tabla.  '''
    if len(sys.argv) != 3 and sys.argv[0]!='':
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    elif len(sys.argv) ==3:
        camion= sys.argv[1]
        precios = sys.argv[2]
        tabla=informe_camion(camion,precios)
    elif sys.argv[0]=='':
        camion=parametros[1]
        precios=parametros[2]
        tabla=informe_camion(camion, precios)
    return tabla


if __name__ == '__main__':
    main(sys.argv)

#%% Prueba
#import informe
#informe.main(['informe.py', 'camion.csv', 'precios.csv'])