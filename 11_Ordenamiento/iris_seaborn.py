#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:04:51 2020

@author: nsantos
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:34:36 2020

@author: nsantos
"""
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns

#%%

iris_dataset = load_iris()

# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names

iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset['feature_names'])
# y hacemos una matriz de gráficos de dispersión, asignando colores según la especie
pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)


#%%%
#Ejercicio 11.10: Seaborn

iris_dataframe['target'] = iris_dataset['target']
sns.pairplot(data = iris_dataframe, hue = 'target')
