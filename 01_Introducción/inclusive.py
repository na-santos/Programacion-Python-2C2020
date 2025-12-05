#inclusive.py

frase = 'Todos somos programadores'
#frase = 'Los hermanos sean unidos porque ésa es la ley primera'
#frase='¿Cómo transmitir a los otros el infinito Aleph?'
#frase = 'Todos, tu también'
palabras = frase.split()
frase_t=[]

for palabra in palabras:
	if len(palabra)>1: # ojo con palabras que tienen una unica letra.	
		if palabra[-1]=='o':
			palabra=palabra[:-1]+'e'	
		elif palabra[-2]=='o':
			palabra=palabra[:-2]+'e'+palabra[-1]
	frase_t.append(palabra)

frase_t = ' '.join(frase_t)
print(frase_t)	

#Salidas
#Todes somes programadores
#Les hermanes sean unides porque ésa es la ley primera
#¿Cóme transmitir a les otres el infinite Aleph?
#Todos, tu también

	
#Primer problema, signos de pregunta o exclamación, puntos, comas.
# Hay palabras que no deberían modificarse por ejemplo cómo

