#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:55:08 2020

@author: noelia
"""

# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()


#%%
        
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end='')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end='')
        print()        
        
#%%

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
#%%
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print('<tr><th>'+'</th><th>'.join(headers)+'</th></tr>')
    def fila(self, data_fila):
        print('<tr><td>'+'</td><td>'.join(data_fila)+'</td></tr>')
        
#%%
        
def crear_formateador(fmt):
    if fmt == 'txt':
        formateador = FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = FormatoTablaCSV()
    else:
        formateador = FormatoTablaHTML()
    return(formateador)   
        
#%%
    
    
def imprimir_tabla(informe, atrs, formateador):
    ''' Imprime una tabla mostrando, de una lista de objetos de tipo arbitrario, 
    una lista de atributos especificados por el usuario atrs. 
    aceptar cualquier instancia de la clase FormatoTabla para definir el 
    formato de la salida.
    '''
    formateador.encabezado(atrs) 
    for lote in informe: 
        row=[]
        for atr in atrs:
           row.append(str(getattr(lote, atr)))
        formateador.fila(row)

        


