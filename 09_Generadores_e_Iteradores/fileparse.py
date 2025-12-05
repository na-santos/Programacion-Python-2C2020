

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 09:41:40 2020

@author: noelia
"""

# fileparse.py
import csv

#Ejercicio 6.1
    
def parse_csv(file, select = None, types=None,has_headers=True,silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    filas = csv.reader(file)
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
        for i,fila in enumerate(filas):
            if not fila:    # Saltear filas vacías
                continue
                # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
                    # Se convierten los elementos de cada fila segun el tipo que se paso  
            try:
                if types: 
                    fila = [func(val) for func, val in zip(types, fila) ]
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {i+1}: No pude convertir {fila}')
                    print(f'Row {i+1}: Motivo:',e)
                continue 
                # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
    else: # Si es false armo la lista de tuplas
        if select != None:
            raise RuntimeError("Para seleccionar, necesito encabezados.")
        for j,fila in enumerate(filas):
            if not fila:    # Saltear filas vacías
                continue
            if not types: # Si no indicaron el tipo de cada elemento de la fila creo la tupla
                fila = tuple([val for val in fila ])
            else: # si indicaron el type los convierto
                try: 
                    fila = tuple([func(val) for func, val in zip(types, fila) ])
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {i+1}: No pude convertir {fila}')
                        print(f'Row {i+1}: Motivo:',e)
                    continue 
                registros.append(fila)
    return registros  

#%% Pruebas
#archivo = 'missing.csv'
#archivo = 'precios.csv'

#with open(archivo) as f:
#      registros =parse_csv(f, types = [str, int, float],silence_errors=True)
      #parse_csv(f, select = ['name','precio'], has_headers = False)
