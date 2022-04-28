import csv
import operator

def objetivo1():
    global archivo
    archivo = 'Proyecto-Usuarios-de-Bici-Publica/2021_bici.csv'
    
    with open(archivo, 'r', encoding='utf-8') as csvfile:
        recorridos_bici = list(csv.DictReader(csvfile))

    # Contar la cantidad de filas en la base
    print ("El total de usuarios que utilizó las bicis públicas de CABA fueron =", len(recorridos_bici))

def objetivo2():
    # Se dividirá en dos partes, 1ro extraer de la base el listado de ORIGENES -con repeticiones 
    with open(archivo, 'r', encoding='utf-8') as csvfile:
        recorridos_bici = list(csv.DictReader(csvfile))
    
    global origenes_rep
    origenes_rep = []

    for row in recorridos_bici:
        origenes_rep.append(row['nombre_estacion_origen'])

    # 2do que me cuente cuantas veces se repite ese dato
    # Tengo que crear un diccionario y que lo vaya llenando

    global origenes
    origenes = {}

    for elemento in origenes_rep:
        clave = elemento
        valor = origenes_rep.count(clave)
        origenes[clave] = valor

    print('La cantidad de estaciones de ORIGEN son = ', len(origenes))
    
    # 3ro que me ordene por las más utilizadas
    origenes = sorted(
        origenes.items(),
        key = lambda kv: kv[1], reverse = True)

    print('El top 5 de estaciones de ORIGEN más utilizadas son =', origenes[0:5])

    print('El listado total de estaciones es = ', origenes)
    
def objetivo3():
    # Se utiliza misma metodología que en el paso anterior pero para DESTINO 
    with open(archivo, 'r', encoding='utf-8') as csvfile:
        recorridos_bici = list(csv.DictReader(csvfile))
    
    global destino_rep
    destino_rep = []

    for row in recorridos_bici:
        destino_rep.append(row['nombre_estacion_destino'])

    global destinos
    destinos = {}

    for elemento in destino_rep:
        clave = elemento
        valor = destino_rep.count(clave)
        destinos[clave] = valor

    print('La cantidad de estaciones de DESTINO son = ', len(destinos))
    
    destinos = sorted(
        destinos.items(),
        key = lambda kv: kv[1], reverse = True)

    print('El top 5 de estaciones de DESTINO más utilizadas son =', destinos[0:5])

    print('El listado total de estaciones es = ', destinos)

def objetivo4():
    # Finalmente que le pregunte al usuario si quiere exportar la información 
    
    respuesta = str(input('Ingrese SI/NO\n'))
    respuesta = respuesta.upper()

    if respuesta == 'SI':
        with open('Proyecto-Usuarios-de-Bici-Publica\origenes_resultados.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Origen','Repeticiones'])
            writer.writerows(origenes)
        with open('Proyecto-Usuarios-de-Bici-Publica\destinos_resultados.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Origen','Repeticiones'])
            writer.writerows(destinos)

    elif respuesta == 'NO':
        print('Finaliza el análisis')

    else:
        print('La opción seleccionada no es correcta. Finaliza el análisis')


if __name__ == '__main__':

    print("Estudio de transporte en bicicleta CABA")
    
    print("¿Cuántas personas utilizaron en el 2021 las bicis públicas en CABA?")
    objetivo1()

    print("Análisis de las estaciones de ORIGEN más utilizadas")
    objetivo2()

    print("Análisis de las estaciones de DESTINO más utilizadas")
    objetivo3()

    print("¿Desea exportar los datos en CSV?")
    objetivo4()
