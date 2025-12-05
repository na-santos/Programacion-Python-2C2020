#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:59:30 2020

@author: noelia
"""

from datetime import timedelta
from datetime import datetime
from datetime import date
#%%
#Ejercicio 7.1: Segundos vividos

#Escribí una función a la que le pasás tu fecha de nacimiento como 
#cadena en formato 'dd/mm/AAAA' 
#(día, mes, año con 2, 2 y 4 dígitos, separados con barras normales) 
#y te devuelve la cantidad de segundos que viviste (asumiendo que naciste a las 00:00hs de tu fecha de nacimiento).

def vida(nacimiento):
    ''' Devuelve la cantidad de segundos vividos
    Pre: Fecha de nacimiento pasada como string dd/mm/AAAA
    Pos: Devuelve un numero que es la cantidad de segundos transcurridos desde las 00:00 hs de fecha de nacimiento'''
    resta= datetime.now() - datetime.strptime(nacimiento, '%d/%m/%Y')
    return resta.total_seconds()