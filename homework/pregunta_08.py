"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    datos_por_cantidad = {}

    with open("files/input/data.csv", "r") as archivo:
        for fila in archivo:
            elementos = fila.strip().split("\t")
            simbolo = elementos[0]
            cantidad = int(elementos[1])

            if cantidad not in datos_por_cantidad:
                datos_por_cantidad[cantidad] = set()

            datos_por_cantidad[cantidad].add(simbolo)

    resultado_ordenado = []
    for cantidad, simbolos in datos_por_cantidad.items():
        resultado_ordenado.append((cantidad, sorted(list(simbolos))))

    resultado_ordenado.sort()
    return resultado_ordenado
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
