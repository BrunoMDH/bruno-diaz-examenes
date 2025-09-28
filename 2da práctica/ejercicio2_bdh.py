# 2. Usando el concepto de funciones (3 ptos):
# Reglas:
# - Crear una función normalizar_nombres(nombres)
# - El parámetro recibe una lista de string de nombres (6 como mínimo)
# - Este quitará el espacio antes y después si lo hubiera
# - Convierte en tipo título
# - Si hubiera más nombre los debe separar (si debe haber el caso en el input de
# datos)
# - Devuelve también eliminando duplicados manteniendo el orden de la primera
# - No mutará la lista original

def normalizar_nombres(nombres):

    if len(nombres) < 6:
        raise ValueError("La lista debe contener al menos 6 nombres")

    resultado = []
    vistos = set()

    for nombre in nombres:
        partes = nombre.strip().title().split()
        for parte in partes:
            if parte not in vistos:
                resultado.append(parte)
                vistos.add(parte)

    return resultado


nombres = [" bruno ", "renzo", "María rosa", "MABEL", "nicolas", " bobbi", "jose antonio"]

try:
    normalizados = normalizar_nombres(nombres)
    print("Lista original: {}".format(nombres))
    print("Lista normalizada: {}".format(normalizados))
except ValueError as e:
    print("Error:", e)
