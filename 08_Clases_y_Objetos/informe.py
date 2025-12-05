#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:18:51 2020

@author: noelia
"""
#Ejercicio 5.8
import csv
from fileparse import parse_csv
import lote
import formato_tabla
#%%
def leer_camion(nombre_archivo):
    ''' Lee un csv con tres columnas, la primera corresponde a la fruta, 
   el segundo cantidad de cajones y la tercera el precio del cajon.
   Devuelve una lista con instancias de la clase lote
    '''
    with open(nombre_archivo) as f:
        camion_dicts = parse_csv(f, select=['nombre','cajones','precio'], types=[str,int,float])
    camion = [ lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]   
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
    ''' Lista de tuplas
    con (nombre, cajones, precio, diferencia) '''
    informe=[]
    for s in camion:
        informe.append((s.nombre,s.cajones,s.precio,precios[s.nombre]-s.precio))
    return(informe)

#%%

def imprimir_informe(informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [ nombre, str(cajones), '$'+f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)

#%%

def informe_camion(nombre_archivo_camion, nombre_archivo_precios,fmt):
    '''
    Crea un informe por camion a partir de archivos camion y precio.
    '''
    # Leer archivos con datos
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)

    # Obtener los datos para un informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
    
#%%    
    
def main(parametros):
    ''' Lee una una lista de parámetros en la línea de comandos 
        y produce el informe.  '''
    if len(parametros) != 4:
        raise SystemExit('Uso adecuado: informe.py archivo_camion archivo_precios fmt')
    camion=parametros[1]
    precios=parametros[2]
    fmt=parametros[3]
    tabla=informe_camion(camion, precios,fmt)
    return tabla


if __name__ == '__main__':
    import sys 
    if len(sys.argv) ==4:
        main(sys.argv)
    else:
        print('Soy modulo principal') 
        print('Necesito 4 parametros') 
        main(['informe.py','camion.csv','precios.csv','txt'])
else:
    print('No soy modulo principal')

#%% Prueba
#import informe
#informe.main(['informe.py', 'camion.csv', 'precios.csv','fmt'])