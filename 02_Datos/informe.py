import csv

def leer_camion(nombre_archivo):
	camion=[]
	with open(nombre_archivo, 'rt') as f:
		rows=csv.reader(f) 
		headers = next(rows) 
		for n,row in enumerate(rows,start=1):
			record=dict(zip(headers,row))
			try:
				camion.append({'nombre':record['nombre'],'cajones':int(record['cajones']),'precio':float(record['precio'])})
			except ValueError:
				print(f'Fila {n}: No pude interpretar: {row}')
				continue
	return(camion)


def leer_precios(nombre_archivo):
	precios={}
	with open(nombre_archivo, 'rt') as f:
		rows=csv.reader(f) 
		for n,row in enumerate(rows,start=0):
			try:
				precios[row[0]] = float(row[1]) 
			except IndexError:
				print(f'Fila {n}: No pude interpretar: {row}')
			continue
	return(precios)


camion =leer_camion('camion.csv')
print(camion)
#[{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}, {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}, {'nombre': 'Caqui', 'cajones': 150, 'precio': 103.44}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}, {'nombre': 'Durazno', 'cajones': 95, 'precio': 40.37}, {'nombre': 'Mandarina', 'cajones': 50, 'precio': 65.1}, {'nombre': 'Naranja', 'cajones': 100, 'precio': 70.44}]

camion =leer_camion('fecha_camion.csv')
print(camion)
#[{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}, {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}, {'nombre': 'Caqui', 'cajones': 150, 'precio': 103.44}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}, {'nombre': 'Durazno', 'cajones': 95, 'precio': 40.37}, {'nombre': 'Mandarina', 'cajones': 50, 'precio': 65.1}, {'nombre': 'Naranja', 'cajones': 100, 'precio': 70.44}]

precios = leer_precios('precios.csv')
print(precios)

#Fila 30: No pude interpretar: []
#{'Lima': 40.22, 'Uva': 24.85, 'Ciruela': 44.85, 'Cereza': 11.27, 'Frutilla': 53.72, 'Caqui': 105.46, 'Tomate': 66.67, 'Berenjena': 28.47, 'Lechuga': 24.22, 'Durazno': 73.48, 'Remolacha': 20.75, 'Habas': 23.16, 'Frambuesa': 34.35, 'Naranja': 106.28, 'Bruselas': 15.72, 'Batata': 55.16, 'Rúcula': 36.9, 'Radicheta': 26.11, 'Repollo': 49.16, 'Cebolla': 58.99, 'Cebollín': 57.1, 'Puerro': 27.58, 'Mandarina': 80.89, 'Ajo': 15.19, 'Rabanito': 51.94, 'Zapallo': 24.79, 'Espinaca': 52.61, 'Acelga': 29.26, 'Zanahoria': 49.74, 'Papa': 69.35}

#Balance

costo=0
recaudado = 0
for s in camion:
	recaudado+= precios[s['nombre']]*s['cajones']
	costo += s['cajones']*s['precio']

print('Costo:', costo, 'Recaudado:', recaudado, 'Ganancia:', round(recaudado-costo,2))

#Costo: 47671.15 Recaudado: 62986.1 Ganancia: 15314.95


