#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:35:41 2020

@author: nsantos
"""
#Ejercicio 10.2: Números triangulares

import math

def numero_triangular(n):
     if n == 1:
         t = 1
     else:
         t = numero_triangular(n-1) + n
     return t
 
#%%    
#Ejercicio 10.3: Dígitos

def digitos(n):
     l = [int(i) for i in str(n)]
     if len(l) == 1:
        dig = 1
     else:
        n = int(str(n)[:-1])
        dig = digitos(n) + 1
     return dig
 
#%%
#Ejercicio 10.4: Potencias
 
def es_potencia(n,b):
    if n/b == 1 or n == 1:
        return True
    elif n % b != 0:
        return False 
    else:    
        return es_potencia(n/b,b)
          
#%%
##Ejercicio 10.5: Subcadenas

def posiciones_de(a,b, pos = []):
    if a.endswith(b):
        p=len(a)-len(b)
        pos.append(p)
    if len(a) == 1:
        return pos[::-1]
    else: 
        return posiciones_de(a[:-1],b,pos)


sub = posiciones_de('Un tete a tete con Tete', 'te')

sub = posiciones_de('quiero comer chocolate con chocotorta chorizo', 'cho',[])

#%%

#Ejercicio 10.6: Paridad


          
def par(n):
    if n == 1 or par(n-1) == True:
        return False
    else:
        return True 
        
        
    
def impar(n):
    if n == 1 or impar(n-1) == False:
        return True
    else:
        return False 

#%%

##Ejercicio 10.7: Máximo

def maximo(a, b = 0):
    if a[-1] > b: 
       b = a[-1]
    if len(a) == 1:
        return b
    else:
        return max(a[:-1])
         
    
#%%

#Ejercicio 10.8: Replicar

def replicar(lista, n, new=[]):
    if len(lista)!= 0: 
        new.extend(n*[lista[-1]])
    else:
        return new[::-1]
    return replicar(lista[0:-1],n,new)

a = replicar([1, 3, 3, 7], 2) 

#%%

#Ejercicio 10.9: Pascal

    

def pascal(n,k):
    if k>n:
        return print('Fuera del triangulo')
    elif k == 0 or n==k:
        return 1
    else:
        return pascal(n-1,k) + pascal(n-1,k-1)
    
    
#%%

#Ejercicio 10.10: Combinatorios


combinaciones(['a', 'b', 'c'], 2)
aa ab ac ba bb bc ca cb cc
    
    
def combinaciones(lista,n,s=''):
    if len(lista)!= 0: 
        s += 2*lista[-1]+' ' + 2*   
    else:
        return s[::-1]
    return combinaciones(lista[0:-1],n,s)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
           