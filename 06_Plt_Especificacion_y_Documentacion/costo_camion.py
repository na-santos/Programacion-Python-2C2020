from informe_funciones import leer_camion
import sys


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

def main(parametros):
    ''' Lee una una lista de parámetros en la línea de comandos 
        y produce la tabla.  '''
    if len(sys.argv) != 2 and sys.argv[0]!='':
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
    elif len(sys.argv) ==2:
        camion= sys.argv[1]
        costo=costo_camion(camion)
    elif sys.argv[0]=='':
        camion=parametros[1]
        costo=costo_camion(camion)
    return print(f'Total cost: {costo}')

if __name__ == '__main__':
    main(sys.argv)



#import costo_camion
#>>> costo_camion.main(['costo_camion.py', 'Data/camion.csv'])
#Total cost: 47671.15


    