#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 17:33:55 2020

@author: noelia
"""

import os
import time


def vigilar(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)  # Mover el índice 0 posiciones desde el EOF
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue  
        else:
            yield line


#%% Ej 9.6
#if __name__ == '__main__':
#   for line in vigilar('mercadolog.csv'):
#        fields = line.split(',')
#        nombre = fields[0].strip('"')
#        precio = float(fields[1])
#        volumen = int(fields[2])
#        if volumen > 1000:
#            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')

#%% Ej 9.7 

if __name__ == '__main__':
    import informe
    camion = informe.leer_camion ('camion.csv')
    for line in vigilar('mercadolog.csv'):  
        fields = line.split(',')
        nombre = fields[0].strip(' "')
        precio = float(fields[1])
        volumen = int(fields[2])
        if nombre in camion:    
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
            
