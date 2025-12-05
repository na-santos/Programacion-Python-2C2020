#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:01:33 2020

@author: noelia
"""
import random 

def mano():
    valores=[1,2,3,4,5,6,7,10,11,12]
    palos = ['oro', 'copa','espada','basto']
    naipes=[(valor,palo) for valor in valores for palo in palos]
    return random.sample(naipes,k=3)


def envido():
    manos=mano()
    envido=0
    cont=0
    pal = [m[1] for m in manos] #los palos de la mano
    val_env = [m[0] if m[0]<10 else m[0]*0 for m in manos] #los valores de la mano
    for m in range(len(pal)): #Quizas podria escribirlo mejor porque estoy reocrriendo palos repetidos
        if pal.count(pal[m])==2:# si hay dos palos iguales
            envido=20
            cont+=val_env[m] 
        elif pal.count(pal[m])==3: #Si hay tres palos iguales.
            envido=20
            cont=sum(val_env)-min(val_env) #sumo las dos mayores
        else:
            envido=max(val_env)
    envido+=cont
    return envido

envidos = [envido() for i in range(1000000)]
prob_31=envidos.count(31)/len(envidos) #7 y 4, 6 y 5
prob_32=envidos.count(32)/len(envidos) # 5 y 7
prob_33=envidos.count(33)/len(envidos) # 7 y 6

print(prob_31,prob_32,prob_33)
#0.021837 0.010822 0.011203
#32 y 33 son casi iguales las probabilidades poruqe hay un par de cartas en cada caso
# 31 es mas alta la prob, tengo dos pares de cartas que me suman 31
