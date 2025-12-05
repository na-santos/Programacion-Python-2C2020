#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:13:23 2020

@author: noelia
"""
#%%
# Ejercico 3.8 

def invertir_lista(lista):
    invertida = []
    l =len(lista)
    for i in range(1,l+1):
        invertida.append(lista[-i])
        print(i)
    return invertida


#invertir_lista([1, 2, 3, 4, 5])
#[5, 4, 3, 2, 1]
#invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
#['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']

