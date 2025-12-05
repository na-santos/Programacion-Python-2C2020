#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:00:14 2020

@author: nsantos
"""
#Ejercicio 10.14: precio_alquiler ~ superficie
import numpy as np
import matplotlib.pyplot as plt


def ajuste_lineal_simple(x,y):
    '''Realiza un ajuste lineal por cuadrados minimos
    Devuelve la pendiente y la ordenada de la recta'''
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

#%%

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

a, b = ajuste_lineal_simple(superficie, alquiler)

grilla_x = np.linspace(50, 200, num = 100)
grilla_y = grilla_x*a + b

g = plt.scatter(superficie, alquiler)
plt.title('Ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.xlabel('Superficie')
plt.ylabel('Alquiler')

plt.show()

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())



