#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 09:41:40 2020

@author: noelia
"""

# fileparse.py
import csv

#Ejercicio 5.6
    
    
def parse_csv(nombre_archivo, select = None, types=None,has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        registros = []
        if has_headers: #Si es true armo el diccionario a partir de los encabezados
            # Lee los encabezados del archivo
            encabezados = next(filas)

            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                    # Se convierten los elementos de cada fila segun el tipo que se paso    
                if types: 
                    fila = [func(val) for func, val in zip(types, fila) ]
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        else: # Si es false armo la lista de tuplas
                for fila in filas:
                    if not fila:    # Saltear filas vacías
                        continue
                    if not types: # Si no indicaron el tipo de cada elemento de la fila creo la tupla
                        fila = tuple([val for val in fila ])
                    else: # si indicaron el type los convierto
                        fila = tuple([func(val) for func, val in zip(types, fila) ])
                    registros.append(fila)
    return registros    

#Faltaria arreglarlo por si quiero seleccionar algunas columnas en el caso de que no haya headers
