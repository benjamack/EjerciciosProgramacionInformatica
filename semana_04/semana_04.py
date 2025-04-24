# === Archivos y lectura ===
import csv

# Ruta al archivo CSV de arbolado
arbolado_csv = '/Users/benja/Desktop/MIA-MaestriaIA/Programacion-Informatica/EjerciciosProgramacionInformatica/semana_04/arbolado-en-espacios-verdes.csv'

# === Ejercicio 1 ===
def arboles_parque(nombre_archivo, nombre_parque):
    arboles = {}
    with open(nombre_archivo, encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["espacio_ve"].strip().upper() == nombre_parque.strip().upper():
                arboles[fila["id_arbol"]] = fila
    return arboles

# === Ejercicio 2 ===
def arbol_mas_popular(nombre_parque):
    arboles = arboles_parque(arbolado_csv, nombre_parque)
    conteo = {}
    for arbol in arboles.values():
        especie = arbol["nombre_com"]
        conteo[especie] = conteo.get(especie, 0) + 1
    return max(conteo, key=conteo.get)

# === Ejercicio 3 ===
def n_mas_altos(nombre_parque, n):
    arboles = arboles_parque(arbolado_csv, nombre_parque)
    alturas = {}
    for arbol in arboles.values():
        especie = arbol["nombre_com"]
        altura = float(arbol["altura_tot"])
        if especie not in alturas or altura > alturas[especie]:
            alturas[especie] = altura
    lista = list(alturas.items())
    return sorted(lista, key=lambda x: x[1], reverse=True)[:n]

# === Ejercicio 4 ===
def altura_promedio(nombre_parque, especie):
    arboles = arboles_parque(arbolado_csv, nombre_parque)
    total = 0
    cantidad = 0
    for arbol in arboles.values():
        if arbol["nombre_com"] == especie:
            total += float(arbol["altura_tot"])
            cantidad += 1
    return total / cantidad if cantidad > 0 else None

# === Ejercicio 5 ===
def parques_con_mas_arboles():
    conteo = {}
    with open(arbolado_csv, encoding='utf-8') as archivo:
        for fila in csv.DictReader(archivo):
            parque = fila["espacio_ve"]
            conteo[parque] = conteo.get(parque, 0) + 1
    return sorted(conteo.items(), key=lambda x: x[1], reverse=True)

def parques_mas_altos_en_promedio():
    alturas = {}
    cantidades = {}
    with open(arbolado_csv, encoding='utf-8') as archivo:
        for fila in csv.DictReader(archivo):
            parque = fila["espacio_ve"]
            altura = float(fila["altura_tot"])
            alturas[parque] = alturas.get(parque, 0) + altura
            cantidades[parque] = cantidades.get(parque, 0) + 1
    promedios = [(p, alturas[p] / cantidades[p]) for p in alturas]
    return sorted(promedios, key=lambda x: x[1], reverse=True)

def parques_mas_diversos():
    especies_por_parque = {}
    with open(arbolado_csv, encoding='utf-8') as archivo:
        for fila in csv.DictReader(archivo):
            parque = fila["espacio_ve"]
            especie = fila["nombre_com"]
            especies_por_parque.setdefault(parque, set()).add(especie)
    diversidad = [(p, len(e)) for p, e in especies_por_parque.items()]
    return sorted(diversidad, key=lambda x: x[1], reverse=True)

def especie_mas_frecuente_ciudad():
    conteo = {}
    with open(arbolado_csv, encoding='utf-8') as archivo:
        for fila in csv.DictReader(archivo):
            especie = fila["nombre_com"]
            conteo[especie] = conteo.get(especie, 0) + 1
    return max(conteo.items(), key=lambda x: x[1])

def razon_exoticas_autoctonas():
    exoticas = 0
    autoctonas = 0
    with open(arbolado_csv, encoding='utf-8') as archivo:
        for fila in csv.DictReader(archivo):
            origen = fila["origen"].strip().lower()
            if origen == "exótico":
                exoticas += 1
            elif origen == "nativo/autóctono":
                autoctonas += 1
    return exoticas / autoctonas if autoctonas > 0 else float('inf')

# === Bloque principal ===
if __name__ == "__main__":
    parque = "CENTENARIO"

    print("Árbol más popular en CENTENARIO:")
    print(arbol_mas_popular(parque))

    print(f"\n3 especies más altas en {parque}:")
    print(n_mas_altos(parque, 3))

    print(f"\nAltura promedio del 'Jacarandá' en {parque}:")
    print(altura_promedio(parque, "Jacarandá"))

    print("\nParques con más árboles:")
    print(parques_con_mas_arboles()[:5])

    print("\nParques con árboles más altos en promedio:")
    print(parques_mas_altos_en_promedio()[:5])

    print("\nParques con más variedad de especies:")
    print(parques_mas_diversos()[:5])

    print("\nEspecie más común en toda la ciudad:")
    print(especie_mas_frecuente_ciudad())

    print("\nRazón entre especies exóticas y autóctonas:")
    print(razon_exoticas_autoctonas())
