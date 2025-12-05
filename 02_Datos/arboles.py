#Ejercicio 2.22: Lectura de los árboles de un parque

def leer_parque(nombre_archivo, parque):
	with open(nombre_archivo, 'rt') as f:
		rows=csv.reader(f) 
		headers = next(rows) # largo 17
		arboles = [] # lista de diccionarios con la informacion del parque
		for n,row in enumerate(rows,start=1):
			record=dict(zip(headers,row))
			if record['espacio_ve']==parque:
				arboles.append(record)
	return(arboles)


nombre_archivo='arbolado-en-espacios-verdes.csv'
parque='GENERAL PAZ'
lista_arboles=leer_parque(nombre_archivo,parque) # esto es una lista de diccionarios
#len(lista_arboles) = 690

#Ejercicio 2.23: Determinar las especies en un parque

def especie(lista_arboles):
	arboles = []
	for s in lista_arboles:
		arboles.append(s['nombre_com'])
	unicas_especies=set(arboles)
	return(unicas_especies)

especies=especie(lista_arboles) #esto es un conjunto

#Ejercicio 2.24: Contar ejemplares por especie

from collections import Counter

def contar_ejemplares(lista_arboles):
	ejemplares = Counter()
	for s in datos_arboles:
       		ejemplares[s['nombre_com']] += 1
	return(ejemplares)

ejemplares = contar_ejemplares(lista_arboles) #esto es una colleccion

parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']

for parque in parques:
	datos_arboles =leer_parque(nombre_archivo,parque)
	ejemplares=contar_ejemplares(datos_arboles)
	cinco=ejemplares.most_common(5) #diccionario. 
	print(parque,cinco)

#GENERAL PAZ [('Casuarina', 97), ('Tipa blanca', 54), ('Eucalipto', 49), ('Palo borracho rosado', 44), ('Fenix', 40)]
#ANDES, LOS [('Jacarandá', 117), ('Tipa blanca', 28), ('Ciprés', 21), ('Palo borracho rosado', 18), ('Lapacho', 12)]
#CENTENARIO [('Plátano', 137), ('Jacarandá', 45), ('Tipa blanca', 42), ('Palo borracho rosado', 41), ('Fresno americano', 38)]

#Ejercicio 2.25: Alturas de una especie en una lista



def obtener_alturas(lista_arboles,especie):
	alturas_especie = []
	for s in lista_arboles:
		if s['nombre_com']==especie:
			alturas_especie.append(float(s['altura_tot']))
	return(alturas_especie)		



parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
for parque in parques:
	datos_arboles =leer_parque(nombre_archivo,parque)
	alturas=obtener_alturas(datos_arboles,'Jacarandá') # es una lista 
	print(parque,'Altura promedio:',round(sum(alturas)/len(alturas),2),'Altura máxima:', round(max(alturas),2))

#GENERAL PAZ Altura promedio: 10.2 Altura máxima: 16.0
#ANDES, LOS Altura promedio: 10.54 Altura máxima: 25.0
#CENTENARIO Altura promedio: 8.96 Altura máxima: 18.0


#Ejercicio 2.26: Inclinación promedio por especie de una lista, falta chequear.

def obtener_inclinaciones(lista_arboles,especie):
	inclinacion_especie = []
	for s in lista_arboles:
		if s['nombre_com']==especie:
			inclinacion_especie.append(float(s['inclinacio']))
	return(inclinacion_especie)		

#Ejercicio 2.27: Especie con el ejemplar más inclinado

def especimen_mas_inclinado(lista_arboles):
	maximo_por_especie={}
	especies=especie(lista_arboles)
	for esp in especies:	
		try:
			maximo=max(obtener_inclinaciones(lista_arboles,esp))
			maximo_por_especie[maximo]=esp
		except ValueError:
				print(f'No hay ejemplares de', esp)
				continue
	print('Especie:', maximo_por_especie[max(maximo_por_especie)]+',','Inclinación máxima:',max(maximo_por_especie))


parque='CENTENARIO' #ver como se como esta escrito el nombre
lista_arboles=leer_parque(nombre_archivo,parque)
especimen_mas_inclinado(lista_arboles)
#Especie: Falso Guayabo (Guayaba del Brasil), Inclinación máxima: 80.0


######### Ejercicio 2.28: Especie con más inclinada en promedio

def especimen_promedio_mas_inclinada (lista_arboles):
	media_por_especie={}
	unicos_arboles=especie(lista_arboles)
	for especies in unicos_arboles:
		inclina=obtener_inclinaciones(lista_arboles,especies)	
		media=sum(inclina)/len(inclina)
		media_por_especie[media]=especies
	print('Especie más inclinada en promedio:', media_por_especie[max(media_por_especie)]+',','Inclinación promedio:', max(media_por_especie))

parque='ANDES, LOS' #ver como se como esta escrito el nombre
datos_arboles=leer_parque(nombre_archivo,parque)
especimen_promedio_mas_inclinada(datos_arboles)

#Especie más inclinada en promedio: Álamo plateado, Inclinación promedio: 25.0


#Preguntas extras: ¿Qué habría que cambiar para obtener la especie con un ejemplar más inclinado de toda la ciudad y no solo de un parque? ¿Podrías dar la latitud y longitud de ese ejemplar? ¿Y dónde se encuentra (lat,lon) el ejemplar más alto? ¿De qué especie es?


#Lista de parques

def lista_parques(nombre_archivo):
	parques=[]
	with open(nombre_archivo, 'rt') as f:
		rows=csv.reader(f) 
		headers = next(rows) # largo 17
		for row in rows:
			parques.append(row[10])
	unicos_parques=set(parques)
	return(unicos_parques)

parques=lista_parques(nombre_archivo)


for parque in parques:
	lista_arboles=leer_parque(nombre_archivo,parque)
	especimen_mas_inclinado(lista_arboles)


# Aca me lista el mas inclinado de cada parque, pero para poder recuperar la informacion del mas inclinado de toda la ciudad deberia cambiar las funciones anterior para guardar la posicion.





