"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    datos_por_identificador = {}

    with open("files/input/data.csv", "r") as archivo:
        for fila in archivo:
            elementos = fila.strip().split("\t")
            lista_pares = elementos[4].split(",")

            for entrada in lista_pares:
                llave, numero = entrada.split(":")
                numero = int(numero)

                if llave in datos_por_identificador:
                    datos_por_identificador[llave].append(numero)
                else:
                    datos_por_identificador[llave] = [numero]
    
    resultado_ordenado = []  
    for llave, numeros in datos_por_identificador.items():  
        resultado_ordenado.append((llave, min(numeros), max(numeros)))  

    resultado_ordenado.sort()
    return resultado_ordenado
    
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
