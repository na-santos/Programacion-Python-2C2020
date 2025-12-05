
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 17:41:14 2020

@author: noelia
"""

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def costo(self):
        return self.cajones*self.precio
    
    def vender(self,vendidos):
        self.cajones -= vendidos
        
    def __repr__(self):
        return f'Lote({self.nombre},{self.cajones},{self.precio})'

