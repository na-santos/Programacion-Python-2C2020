#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:06:31 2020

@author: noelia
"""

import pandas as pd

df = pd.read_csv('OBS_SHN_SF-BA.csv')

df.head()

df = pd.read_csv('OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

df['2-19-2014']

df['12-25-2014':].plot()

df['10-15-2014':'12-15-2014'].plot()

# Ejercicio 7.10
#Trabajemos con una copia de este fragmento:

dh = df['12-25-2014':].copy()

delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 20 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()

