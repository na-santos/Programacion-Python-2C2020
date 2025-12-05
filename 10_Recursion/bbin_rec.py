#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:06:40 2020

@author: nsantos
"""
#Ejercicio 10.11: Búsqueda binaria


def bbinaria_rec(lista, e):
    ''' Busqueda binaria de e en lista ordenada.
    Devuelve True si e esta y False si no'''
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] == e:
            res = True
        elif lista[medio] > e:
            return bbinaria_rec(lista[0:medio],e)
        else:               
            return bbinaria_rec(lista[medio+1:],e)
    return res




#bbinaria_rec([1, 3, 5], 0)
#bbinaria_rec([1, 3, 5], 1)
#bbinaria_rec([1, 3, 5], 2)
#bbinaria_rec([1, 3, 5], 3)
#bbinaria_rec([1, 3, 5], 5) 
#bbinaria_rec([1, 3, 5], 6)
#bbinaria_rec([], 0)
#bbinaria_rec([1], 1)
#bbinaria_rec([1], 3)
#bbinaria_rec([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],18)
