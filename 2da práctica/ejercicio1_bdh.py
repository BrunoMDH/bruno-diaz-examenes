# 1. Escriba un programa donde tendrá los siguientes requisitos (3 ptos):
# Reglas:
# - Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
# un diccionario donde las claves serán los nombres de los estudiantes y sus
# valores serán listas con 3 notas.
# - Calcular el promedio de cada estudiante.
# - Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
# y el valor sea otro diccionario con:
# promedio: que será el promedio de notas
# estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
# - Mostrar en pantalla el estudiante con mayor promedio

NOTA_APROBATORIA = 11

def procesar_notas(estudiantes):
    resultado = {}

    for nombre, notas in estudiantes.items():
        if len(notas) < 3:
            raise ValueError("El estudiante {} debe tener al menos 3 notas".format(nombre))

        promedio = sum(notas) / len(notas)
        estado = "aprobado" if promedio >= NOTA_APROBATORIA else "desaprobado"

        resultado[nombre] = {"promedio": promedio, "estado": estado}

    mejor_estudiante = None
    mejor_promedio = -1

    for nombre, datos in resultado.items():
        if datos["promedio"] > mejor_promedio:
            mejor_promedio = datos["promedio"]
            mejor_estudiante = nombre

    print("El estudiante con mayor promedio es {} con {:.2f}".format(mejor_estudiante, resultado[mejor_estudiante]['promedio']))

    return resultado


estudiantes = {"Bruno": [15, 17, 16], "Fernando": [9, 10, 8], "Bryan": [18, 17, 19], "Jose": [11, 12, 10]}

resultado = procesar_notas(estudiantes)

print("Resultados:")
for estudiante, datos in resultado.items():
    print("{}: Promedio = {:.2f}, Estado = {}".format(estudiante, datos['promedio'], datos['estado']))

