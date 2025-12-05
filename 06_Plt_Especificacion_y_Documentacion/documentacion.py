#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:39:47 2020

@author: noelia
"""

#Ejercicio 6.8: Funciones y documentación

#%%
def valor_absoluto(n):
    ''' Devuelve el valor absoluto de n
    Pre: Recibe un número.
    Pos: Devuelve un número mayor a cero, que es el valor absoluto de n.'''
    if n >= 0:
        return n
    else:
        return -n
#No hay invariantes de ciclo.

#%%
def suma_pares(l):
    ''' Suma los números pares presentes en la lista
    Pre: Recibe una lista de numeros 
    Pos: Devuelve un número entero, que es la suma de
    los numeros pares de la lista'''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

# El invariante de ciclo es res. Antes de cada iteración corresponde a la
    # suma de los números pares anteriores de la lista. 
#%%
    
def veces(a, b):
    ''' Suma a b veces
    Pre: a es un numero y b es un entero positivo
    Pos: devuelve un numero, que es el resultado de sumar b veces a '''
    res = 0
    nb = b
    while nb != 0:
        res += a
        nb -= 1
    return res
# El invariante de ciclo es nb, y tmb res?

#%%
def collatz(n):
    res = 1
    ''' Devuelve la cantidad de pasos que deben hacerse para llegar
   desde n hasta 1 según la siguiente operacion: 
   si n es par n/2, si n es impar 3n+1.
   Pre: n es un numero entero positivo
   Pos: devuelve un numero entero positivo, que es la cantidad pasos que 
   debió realizarse para llegar a 1 según la la siguiente operacion: 
   si n es par n/2, si n es impar 3n+1.
   '''

    while n!=1:
        if n % 2 == 0: #si es par
            n = n//2 
        else:
            n = 3 * n + 1
            print(n)
        res += 1

    return res

# El invariante de ciclo es res