"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    conteo_por_identificador = {}

    with open("files/input/data.csv", "r") as archivo:
        for fila in archivo:
            elementos = fila.strip().split("\t")
            lista_pares = elementos[4].split(",")

            for entrada in lista_pares:
                llave, numero = entrada.split(":")
                numero = int(numero)

                if llave in conteo_por_identificador:
                    conteo_por_identificador[llave] += 1
                else:
                    conteo_por_identificador[llave] = 1

    conteo_ordenado = {}
    for llave, cantidad in sorted(conteo_por_identificador.items()):
        conteo_ordenado[llave] = cantidad

    return conteo_ordenado

    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
