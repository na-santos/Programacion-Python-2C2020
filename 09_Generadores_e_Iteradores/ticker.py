#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:07:59 2020

@author: noelia
"""

# ticker.py

from vigilante import vigilar
import csv

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
        

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows
           
def filtrar_datos(filas, nombres):
   for fila in filas:
       if fila['nombre'][0:-1] in nombres: # acá hay un espacio
           yield fila


def ticker(camion_file, log_file, fmt):
        import formato_tabla as ft
        import informe
        from vigilante import vigilar
        camion = informe.leer_camion(camion_file)
        filas = parsear_datos(vigilar(log_file))
        filas = filtrar_datos (filas, camion)
        formateador = ft.crear_formateador(fmt)
        formateador_enc = formateador.encabezado(['nombre', 'precio', 'volumen'])
        for fila in filas:
            print(formateador.fila([fila['nombre'], str(fila['precio']), str(fila['volumen'])]))
       # Me queda un none 
            
if __name__ == '__main__':
    lines = vigilar('mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)

