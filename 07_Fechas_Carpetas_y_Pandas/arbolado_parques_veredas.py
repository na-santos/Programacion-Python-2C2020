#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:19:10 2020

@author: noelia
"""

#Abrí ambos datasets a los que llamaremos df_parques y df_veredas.

import pandas as pd

name_veredas = 'arbolado-publico-lineal-2017-2018.csv'
name_parques = 'arbolado-en-espacios-verdes.csv'
df_veredas = pd.read_csv(name_veredas)
df_parques = pd.read_csv(name_parques)

#%%

cols_vereda = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']
cols_parque = ['nombre_cie', 'diametro', 'altura_tot']


df_tipas_veredas  = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][cols_vereda].copy()
df_tipas_parques  = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols_parque].copy()

df_tipas_veredas=df_tipas_veredas.rename(columns={"diametro_altura_pecho": "diametro", "altura_arbol": "altura"})
df_tipas_parques=df_tipas_parques.rename(columns={"nombre_cie": "nombre_cientifico", "altura_tot": "altura"})


#%%
    
df_tipas_parques.insert(3, "ambiente",['parque']*len(df_tipas_parques), True) 
df_tipas_veredas.insert(3, "ambiente",['vereda']*len(df_tipas_veredas), True) 


#%%

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
   
df_tipas.boxplot('diametro',by = 'ambiente')

df_tipas.boxplot('altura',by = 'ambiente')

#%%%%%%%%%%%%%%%%%%%%%%

#Si creo que conviene hacer una funcion que reciba como input el nombre 
#cientifico (o sus dos versiones)
