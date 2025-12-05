#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:58:54 2020

@author: nsantos
"""
#Ejercicio 10.9: Pascal
    
def pascal(n,k):
    '''Triángulo de Pascal
    calcula el valor que se encuentra en la fila n y columna k'''
    if k>n:
        return print('Fuera del triangulo')
    elif k == 0 or n==k:
        return 1
    else:
        return pascal(n-1,k) + pascal(n-1,k-1)

