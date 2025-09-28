#1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos)
#Reglas:
#- Asignar en variables los datos de tu nombre, salario, edad y compañía para un
#usuario e identificar sus tipos de variables
#- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
#conversión de datos
#- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
#tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
#tiene un bono del 5% en el mes diciembre”
#- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
#salario, según corresponda.

nombre = "Bruno Díaz"
salario = 1650
edad = "21" #edad tipo Str
compañia = "Luxar"

print(type(nombre))
print(type(salario))
print(type(edad))
print(type(compañia))

edad_i = int(edad) #edad tipo Int

bono1 = (salario ** 2) + (salario * 0.10)
bono2 = (salario ** 2) + (salario * 0.05)

if edad_i > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    print("Bono final: {}".format(bono1))

if edad_i < 30:
    print("Usted tiene un bono de 5% en el mes de diciembre")
    print("Bono final: {}".format(bono2))