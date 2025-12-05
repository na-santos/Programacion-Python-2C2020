#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 16:17:42 2020

@author: noelia
"""

# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: Los errores encontrados eran semánticos. El primero: devolvía 
#True si el último elemento de la expresión era a. Estaba quedandome solamente
# con la información del último caracter y en ningun lugar quedaba guardada la 
#información sobre el resto de los caracteres.
#Directamente borré el for que recorria los caracteres de "expresion"
# y me fije si el caracter 'a' está en "expresión". En ese caso devuelve True.
# El segundo error semántico: No reconocía las "A" mayusculas así que agregué una línea para que 
# pasé los caracteres a minuscula con .lower()
#    A continuación va el código corregido
def tiene_a(expresion):
    expresion=expresion.lower()
    if 'a' in expresion:
        return True
    else:
        return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

...

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
# Primer error: sintáctico. el def, while e if no tenian los dos puntos al 
# final. Se los agregué.
# Segundo error: sintáctico. Decía "Falso" en vez de "False"
# Tercer error: sintáctico. en el if se usaba un único '=' en vez de '=='
# Cuarto error: semántico. No identifica las mayusculas, hago lo mismo que en el ej anterior
# expresion.lower().
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    expresion = expresion.lower()
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

# La función devuelve el primer return "que se cumple". 
tiene_a('UNSAM 2020') # cuandono encuentra ninguna 'a'  directamente da False (que es 
#ultimo return, acá no identifica las mayusculas)
tiene_a('La novela 1984 de George Orwell')#Cuando hay una da True
#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: Error en tiempo de ejecución cuando expresion = 1984. Solo 
#entiende strings. Entonces agregué un str(expresion) antes de calcular en len 
# y de pasar a minusculas.
#  A continuación va el código corregido
def tiene_uno(expresion):
    expresion=str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
