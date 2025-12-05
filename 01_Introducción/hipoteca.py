# hipoteca.py

#David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))

#Salida
# Total pagado 966279.6

#Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.

#Modificá el programa para incorporar estos pagos extra y que imprima el monto total pagado junto con la cantidad de meses requeridos.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
adelanto =1000.0

while saldo > 0:
	if mes<12: #solo menor porque arranco contando desde cero
		saldo = saldo * (1+tasa/12) - pago_mensual-adelanto
		total_pagado = total_pagado + pago_mensual+adelanto
		mes +=1
	else:
		saldo = saldo * (1+tasa/12) - pago_mensual
		total_pagado = total_pagado + pago_mensual
		mes +=1

print('Total pagado', round(total_pagado, 2),'en',mes,'meses')

#Salida
#Total pagado 929965.62 en 342 meses

#¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?

#Ya que estamos, corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra =1000.0
pago = 0


while saldo > 0:
	if pago_extra_mes_comienzo<=mes+1 and pago_extra_mes_fin>=mes+1 :
		pago = pago_mensual+pago_extra 
	else:
		pago=pago_mensual
	if saldo>pago:
		saldo = saldo * (1+tasa/12) - pago
		total_pagado = total_pagado + pago
		mes +=1
	else:
		pago = saldo*(1+tasa/12)
		saldo = saldo*(1+tasa/12) - pago
		total_pagado = total_pagado + pago
		mes +=1
	f'{mes} {total_pagado:0.2f} {saldo:0.2f}'

f'Total pagado: {total_pagado:0.1f}'
f'Meses: {mes}'


#Salida

#'1 2684.11 499399.22'
#'2 5368.22 498795.94'
#'3 8052.33 498190.15'
#'4 10736.44 497581.83'
#'5 13420.55 496970.98'
#....
#'307 872021.77 6137.36'
#'308 874705.88 3478.83'
#'309 877389.99 809.21'
#'310 878202.57 0.00'

#'Total pagado: 878202.6'
#'Meses: 310'

#####################################################################
# Pruebo si esta ultima version funciona para el ej 1.8

#pago_extra_mes_comienzo = 1
#pago_extra_mes_fin = 12
#pago_extra =1000.0

#'Total pagado: 97992.41'
# 'Meses: 342'

# Pruebo si funciona para el ej 1.7 

#pago_extra_mes_comienzo = 0
#pago_extra_mes_fin = 0
#pago_extra = 0

# 'Total pagado: 966278.03'
# Debería ser 'Total pagado 966279.6'?
# no me da igual, no entiendo porque 



