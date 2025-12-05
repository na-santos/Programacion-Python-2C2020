# camion_commandline.py

import csv
import sys

def costo_camion(nombre_archivo):
	costo = 0 
	with open(nombre_archivo, 'rt') as f:
		rows=csv.reader(f) #Saca las comillas dobles en los string y ya entiende que tiene que separar por comas.
		headers = next(rows) #Ignoro el header
		for row in rows:
			try:
				costo = costo + float(row[1])*float(row[2])
			except ValueError:
				print('Faltan datos!')
				continue
	return(costo)


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)

#Salidas en la terminal

# camion_commandline.py
# Costo total: 47671.15
# camino_commandline.py camion.csv
# Costo total: 47671.15
# camino_commandline.py missing.csv
#Faltan datos!
#Faltan datos!
#Costo total: 30381.15

