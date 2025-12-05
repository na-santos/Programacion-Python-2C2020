#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:46:59 2020

@author: nsantos
"""

import numpy as np
import matplotlib.pyplot as plt 

def ajuste_lineal_simple(x,y):
    '''Realiza un ajuste lineal por cuadrados minimos
    Devuelve la pendiente y la ordenada de la recta'''
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

#%%
np.random.seed(3141) # semilla para fijar la aleatoriedad
N=50
indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0) # residuos
dep_vars = 2 + 3*indep_vars + 2*indep_vars**2 + r # relación cuadrática

x = indep_vars
y = dep_vars
plt.scatter(x,y)
plt.title('scatterplot de los datos')
plt.show()

a, b = ajuste_lineal_simple(x, y)

grilla_x = np.linspace(start = 0, stop = 10, num = 1000)
grilla_y = grilla_x*a + b
g = plt.scatter(x = x , y = y)
plt.title('ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()

errores = y - (x*a + b)
print("ECM", (errores**2).mean())

xc = x**2
ap, bp = ajuste_lineal_simple(xc, y)
grilla_y_p = (grilla_x**2)*ap + bp
plt.scatter(x,y)
plt.plot(grilla_x, grilla_y, c = 'green')
plt.plot(grilla_x, grilla_y_p, c = 'red')
plt.title('ajuste lineal con x^2')
plt.show()

yhat = (x**2)*ap + bp       # valores estimados
residuos = y - yhat         # diferencia entre el valor original y el estimado
ecm = (residuos**2).mean()  # error cuadrático medio
print("ECM:", ecm)

#%%
from sklearn import linear_model

x = indep_vars
xc = x**2
y = dep_vars

def ajuste(X,y,name):
    lm = linear_model.LinearRegression()
    lm.fit(X,y)
    errores = y - (lm.predict(X))
    print(name)
    print("ECM:", (errores**2).mean()) 
    print("Ord al origen:", lm.intercept_)
    print("Pendientes:", lm.coef_)
    return lm.intercept_, lm.coef_

X = np.concatenate((x.reshape(-1,1),xc.reshape(-1,1)),axis=1)
ord1, pend1 = ajuste(X,y,'x+x**2')
X = xc.reshape(-1,1)
ord2, pend2 = ajuste(X,y,'x**2')
X = x.reshape(-1,1)
ord3, pend3 = ajuste(X,y,'x')

# dep_vars = 2 + 3*indep_vars + 2*indep_vars**2 
# El mejor es claramente el que tiene x y x**2, tanto 
# en terminos de los coeficientes como del ECM. 
grilla_x = np.linspace(start = 0, stop = 10, num = 1000)

grilla_y3 = grilla_x*pend3 + ord3

grilla_y2 = (grilla_x)**2*pend2 + ord2

grilla_y1 = (grilla_x)**2*pend1[1] + (grilla_x)*pend1[0] + ord1

plt.scatter(x,y,label='Data original')
plt.plot(grilla_x,grilla_y1,'g', label='x**2+x')
plt.plot(grilla_x,grilla_y2,'k',label='x**2')
plt.plot(grilla_x,grilla_y3,'r',label='x')
plt.legend(loc='best')

#%%% 10.17 y 10.18

def pot(x,n):
    X=x.reshape(-1,1)
    for i in range(n-1):
        X=np.concatenate((X,(x**(i+2)).reshape(-1,1)),axis=1)
    return X

def AIC(k, ecm, num_params):
    '''Calcula el AIC de una regresión lineal múltiple de 'num_params' parámetros, ajustada sobre una muestra de 'k' elementos, y que da lugar a un error cuadrático medio 'ecm'.'''
    aic = k * np.log(ecm) + 2 * num_params
    return aic

def ajuste(x,y,n):
    lm = linear_model.LinearRegression()
    X = pot(x,n)
    lm.fit(X,y)
    errores = y - (lm.predict(X))
    ECM = (errores**2).mean()
    print("Grado del polinomio", n)
    print("Cantidad de parametros", n+1)
    print("ECM:",ECM ) 
    print("AIC:", AIC(50,ECM,n+1)) 
    print('#############')


for n in range(1,9):
    ajuste(x,y,n)