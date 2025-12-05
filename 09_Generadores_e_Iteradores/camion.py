#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:28:32 2020

@author: noelia
"""

# camion.py
# 9.3 y 9.14

class Camion:

    def __init__(self, lotes):
        self._lotes = lotes
    
    def __iter__(self):
        return self._lotes.__iter__()

    def precio_total(self):
        ''' calcula el precio total del camion'''
        return sum(l.costo() for l in self._lotes)
    
    def __len__(self):
        return len(self._lotes)

    def __getitem__(self, index):
        return self._lotes[index]

    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self._lotes)

    def contar_cajones(self):
        ''' cuenta el total de cajones del camion'''
        from collections import Counter
        cantidad_total = Counter()
        for l in self._lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    

#no estoy segura si tmb puedo reescribir contar cajones usando expresiones generadores
