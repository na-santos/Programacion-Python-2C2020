#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:19:17 2020

@author: noelia
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
# Ejercicio 4.14 
temperaturas= np.load('Temperaturas.npy')
plt.hist(temperaturas,bins=30)
plt.xlabel("Temperatura (°C)")
plt.ylabel("Cuentas")