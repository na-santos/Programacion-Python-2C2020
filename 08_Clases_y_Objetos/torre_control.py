#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:08:04 2020

@author: noelia
"""

class TorreDeControl():
    def __init__(self):
        self.arribos = []
        self.partidas= []
        
    def nuevo_arribo(self, x):
        self.arribos.append(x)

    def nueva_partida(self, x):
        self.partidas.append(x)
    
    def ver_estado(self):
        s = '' 
        for obj in self.arribos:
            s +=' '+ str(obj)
        print(f'Vuelos esperando para aterrizar:{s}')
        p = ''
        for obj in self.partidas:
            p +=' '+ str(obj)
        print(f'Vuelos esperando para despegar:{p}')
    
    def asignar_pista(self):
        if len(self.arribos)==0 and len(self.partidas)==0 :
            print('No hay vuelos en espera')
        elif len(self.arribos)!=0 and len(self.partidas)!=0:
            a = self.arribos.pop(0)
            print(f'El vuelo {a} aterrizó con éxito.')
        elif len(self.arribos)==0 and len(self.partidas)!=0:
            a = self.partidas.pop(0)
            print(f'El vuelo {a} despegó con éxito.')
        
#%%
            
#torre = TorreDeControl()
#torre.nuevo_arribo('AR156')
#torre.nueva_partida('KLM1267')
#torre.nuevo_arribo('AR32')
#torre.ver_estado()
#Vuelos esperando para aterrizar: AR156, AR32
#Vuelos esperando para despegar: KLM1267

#torre.asignar_pista()
#El vuelo AR156 aterrizó con éxito.
#>>> torre.asignar_pista()
#El vuelo AR32 aterrizó con éxito.
#>>> torre.asignar_pista()
#El vuelo KLM1267 despegó con éxito.
#>>> torre.asignar_pista()
#No hay vuelos en espera.

