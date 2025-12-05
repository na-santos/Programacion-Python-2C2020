#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:18:54 2020

@author: noelia
"""

#Este ejercicio está relacionado con un error muy común en Python. Escribí una definición de una clase Canguro que tenga:

#como cadena del objeto Canguro y de los contenidos de su marsupio.

class Canguro():
    def __init__(self,nombre):
        self.nombre= nombre
        self.contenido_marsupio = []
        
    def meter_en_marsupio(self,a):
        self.contenido_marsupio.append(a)
        
    def __str__(self):
        return f'({self.nombre}, {self.contenido_marsupio})'
        
#%%
        
# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro(): ##porque no estaban los parentesis?
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre): #Estaba mal definir la lista vacia aca
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = [] # la defini aca.

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print(cangurito)

#Estaba mal definir la lista vacía en el init, así que la definí vacía adentro.
# De todas formas me parece que sería útil incorporarlo como un 
# parametro definido por el usuario porque ya de entrada podría 
#agregarle contenido al marsupio, pero no se bien como hacer eso. 