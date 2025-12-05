from informe_funciones import leer_camion


def costo_camion(nombre_archivo):
    costo=0
    camion=leer_camion(nombre_archivo)
    for s in camion:
        try:
            ncajones = s['cajones']
            precio = s['precio']
            costo += ncajones*precio
        except ValueError:
            continue
    return costo


costo = costo_camion('camion.csv')

#47671.15




    