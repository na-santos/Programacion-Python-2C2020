#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:18:08 2020

@author: nsantos
"""
# Ejercicio 11.12

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np

iris_dataset = load_iris()

KN= []
DT = []
RF =[]

for i in range(1,1000): 
    
    # Partición aleatoria del data set, en data de entretamiento y data de testeo
    X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'])
    
    # KNeighbors
    knn = KNeighborsClassifier(n_neighbors = 1)
    knn.fit(X_train, y_train) # entreno al modelo 
    y_pred = knn.predict(X_test) # predicciones 
    KN.append(knn.score(X_test, y_test)) #score
    
    #  DecisionTree
    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)  # entreno al modelo
    y_pred = dt.predict(X_test) # predicciones
    DT.append(dt.score(X_test, y_test)) #score
    
    #  RandomForest
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train) # entreno al modelo
    y_pred = rf.predict(X_test) # predicciones
    RF.append(rf.score(X_test, y_test)) #score

#Este es el mejor    
print("Score promedio KNeighbors:", np.mean(KN))   
 
print("Score promedio Decision Tree:", np.mean(DT))   

print("Score promedio Random Forest:", np.mean(RF))   

# Hago un histograma para ver como están distribuidos los scores. 

fig, axs = plt.subplots(3,sharex=True)
axs[0].hist(KN,label= 'KN')
axs[0].legend(loc='best')
axs[1].hist(DT,label= 'DT')
axs[1].legend(loc='best')
axs[2].hist(RF,label= 'RF')
axs[2].legend(loc='best')
plt.legend(loc='best')
