#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:44:39 2020

@author: nsantos
"""
#Ejercicio 10.13: Hojas ISO y recursión


def A(n):
    '''Devuelve una tupla con las medidas de la hoja A(n)
    en milimetros segun la norma ISO (ancho,largo).
    n debe ser entero mayor o igual que cero'''
    if n==0:
        ancho=841
        largo=1189
        return ancho, largo
    else:
         ancho, largo = A(n-1)
         if ancho>largo: 
             return ancho//2,largo
         else:
             return ancho,largo//2
         
            