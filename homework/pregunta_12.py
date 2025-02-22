"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    suma_por_simbolo = {}

    with open("files/input/data.csv", "r") as archivo:
        for fila in archivo:
            elementos = fila.strip().split("\t")
            simbolo = elementos[0]
            lista_pares = elementos[4].split(",")

            suma_valores = 0
            for entrada in lista_pares:
                numero = int(entrada.split(":")[1])
                suma_valores += numero

            if simbolo in suma_por_simbolo:
                suma_por_simbolo[simbolo] += suma_valores
            else:
                suma_por_simbolo[simbolo] = suma_valores

    return dict(sorted(suma_por_simbolo.items()))

    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
