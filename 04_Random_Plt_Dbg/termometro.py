#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:25:30 2020
np.save('filename', a)
@author: noelia
"""
import random 
import numpy as np

#%%
#Ejercicio 4.11: Gaussiana + 4.13
#La función random.normalvariate(mu,sigma) genera números aleatorios según esta distribución de probabilidades. Por ejemplo, usando mu = 0 y sigma = 1 podemos generar 6 valores aleatorios así:

#for i in range(6):
#        print(f'{random.normalvariate(0,1):.2f}', end=', ')
N = 999
mediciones =np.zeros((N))
for i in range(N):
        mediciones[i]=random.normalvariate(37.5,0.2)
        
np.save('Temperaturas', mediciones)
maximo=mediciones.max()
minimo=mediciones.min()
promedio=mediciones.sum()/mediciones.size
mediana=np.sort(mediciones)[int(N/2)]


