"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    datos_por_caracter = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            elementos = linea.strip().split("\t")
            valor_numerico = int(elementos[1])
            caracter = elementos[0]
            

            if caracter in datos_por_caracter:
                datos_por_caracter[caracter].append(valor_numerico)
            else:
                datos_por_caracter[caracter] = [valor_numerico]

    resultado_ordenado = sorted((caracter, max(numeros), min(numeros)) for caracter, numeros in datos_por_caracter.items())

    return resultado_ordenado
    
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
