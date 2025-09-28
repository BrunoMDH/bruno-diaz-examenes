#2.Crear un entorno virtual y aplicar lo siguiente (4 ptos):
#Reglas:
#- El nombre del entorno virtual tendrá el nombre con la siguiente estructura
#(apellido_nombre_edad)
#- Instalar las siguientes librerías: Django: 5.0.6, fastapi: 0.112.0, numpy: 2.0.0 y
#aws (última versión)
#- Generar el archivo de requirements.txt (mostrar las librerías instaladas)
#- Caso: Reporte de calificaciones:
#Se tiene un alumno con calificaciones en tres cursos:
#Matemáticas: 17, Ciencia: 14, Historia: 15
#Cada curso tiene un peso diferente en la nota final:
#Matemáticas: 40%, Ciencia: 30%, Historia: 30%
#Realizar lo que se pide a continuación:
#Calcula la nota final ponderada del alumno.
#Muestra un mensaje como: "La nota final es: 15.6" con 1 decimal.
#Evalúa si el alumno aprueba (nota final >= 13.0). Muestra un mensaje booleano:
#"¿Aprobado?: True" o "¿Aprobado?: Sí"
#Genera una cadena resumen que diga:
#"El estudiante obtuvo una nota final de 15.6 y su estado final es: Aprobado"
#En caso no apruebe indicar lo contrario en los mensajes.

#Reporte de calificaciones
nota_mat = 17
nota_sci = 14
nota_his = 15

#Cálculo de ponderado
peso_mat = 0.40
peso_sci = 0.30
peso_his = 0.30
ponderado = (nota_mat * peso_mat) + (nota_sci * peso_sci) + (nota_his * peso_his)

#Nota final
print("La nota final es: {:.1f}".format(ponderado))

#Comprobar si aprobó
if ponderado >= 13.0:
    print("¿Aprobado?: Sí")
    print("El estudiante obtuvo una nota final de {:.1f} y su estado final es: Aprobado".format(ponderado))
if ponderado <= 13.0:
    print("¿Aprobado?: No")
    print("El estudiante obtuvo una nota final de {:.1f} y su estado final es: Desaprobado".format(ponderado))