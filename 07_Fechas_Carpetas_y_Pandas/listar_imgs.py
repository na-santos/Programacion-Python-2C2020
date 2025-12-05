#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:43:49 2020

@author: noelia
"""

#Ejercicio 7.5: Recorrer el árbol de archivos


import os

def main(camino):
    if len(camino) != 2:
        raise SystemExit('Uso adecuado: listar_imgs.py directorio')
    directorio = camino[1]
    for root, dirs, files in os.walk(directorio):
        # me devuelve el pwd, los directorios qe hay alli, y las files. 
        for name in files:
            if 'png' in name:
                print(name)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        main(['listar_imgs.py','directorio'])