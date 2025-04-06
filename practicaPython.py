import numpy as np

#%%
### Ej 1: Suma y multiplicación
numero1 = 5
numero2 = 10

suma = numero1 + numero2
producto = numero1 * numero2
print(suma, producto)
# %%
### Ej 2: Condicion de pago de impuesto
sueldo = [100, 300, 50, 6000, 5000, 1000, 500, 40, 7000]

for i in sueldo:
    if i < 3000:
        print("No paga impuestos")
    else:
        impuesto = i * 0.1
        print(f"Debe pagar {impuesto} dólares como impuesto")
# %%
### Ej 3: Alumno reprobado, regular o promocionado
nota = [5, 6, 4, 2, 8, 5, 7, 3, 9]

for i in nota:
    if i >= 7:
        print("Promocionado")
    else:
        if 4<=i<7:
            print("Regular")
        else:
            print("Reprobado")
    
# %%
### Entre 3 números elegir el mas grande
num1 = 4
num2 = 6
num3 = 2

if num1 > num2 and num1 > num3:
    print(num1)
else:
    if num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)

num1 = [100, 300, 50, 6000, 5000, 1000, 500, 40, 7000]
num2 = [464, 836, 34, 9543, 8464, 2539, 262, 24, 4765]
num3 = [566, 474, 362, 7589, 9363, 3633, 3732, 29, 3956]

for i in range(len(num1)):
    if num1[i] > num2[i] and num1[i] > num3[i]:
        print(num1[i])
    elif num2[i] and num2[i] > num3[i]:
        print(num2[i])
    else:
        print(num3[i])
# %%
### Contamos hasta 100
x = 1
while x<100:
    x=x+1
    print(x)

# %%
x=1
suma=0
while x<10:
    valor=2*x
    suma=suma+valor
    x=x+1
promedio=suma/10
print(suma,promedio)

# %%
import random
piezas=1
aptos=0
n=100
while piezas<n:
    largo=random.uniform(1.0,1.5)
    if largo >=1.2 and largo<=1.3:
        aptos+=1
    piezas+=1
print(f"Tenemos {aptos} piezas aptas")
print(piezas)


# %%
x=0
for i in range(10):
    valor=5
    suma=suma+valor
    promedio=suma/10
    x+1
print(suma)
print(promedio)

# %%
import random
x=0
aprobados=0
desaprobados=0
for i in range(10):
    notas=random.randint(1,10)
    if notas >= 7:
        aprobados+=1
    else:
        desaprobados+=1
print(aprobados,desaprobados)


# %%
# ----------------------------------------
# CONSIGNAS DE PRÁCTICA: ÁLBUM DE FIGURITAS
# ----------------------------------------
import random
import numpy as np
#%%
# EJERCICIO 1: Crear un álbum vacío
# Crear una función llamada crear_album(figus_total)
# que reciba la cantidad total de figuritas y devuelva
# una lista o vector con todos ceros del largo indicado.
def crear_album(figus_total):
    album=np.zeros(figus_total, dtype=int)
    return album

#%%
# EJERCICIO 2: Verificar si el álbum está incompleto
# Crear una función llamada album_incompleto(album)
# que reciba una lista y devuelva True si hay al menos
# un cero, y False si está completo (sin ceros).
def album_incompleto(A):
    if 0 in A:
        return True
    else:
        return False
#%%
# EJERCICIO 3: Comprar una figurita
# Crear una función llamada comprar_figu(figus_total)
# que devuelva un número entero aleatorio entre 0 y figus_total - 1,
# representando una figurita obtenida al azar.
def comprar_figu(figus_total):
    figu=random.randint(0,figus_total - 1)
    return figu

#%%
# EJERCICIO 4: Simular el llenado de un álbum
# Crear una función cuantas_figus(figus_total) que cree un álbum vacío,
# y simule la compra de figuritas (de a una) hasta completarlo.
# Debe devolver la cantidad de figuritas compradas.
def cuantas_figus(figus_total):
    album=crear_album(figus_total)
    figus_compradas=0
    while album_incompleto(album):
        figu=comprar_figu(figus_total)
        album[figu]=album[figu]+1
        figus_compradas+=1
    return figus_compradas

figus_necesarias = cuantas_figus(860)
print(f"Se necesitaron {figus_necesarias} figuritas para completar el álbum.")


#%%
# EJERCICIO 5: Estimar el promedio con muchas simulaciones
# Ejecutar cuantas_figus(figus_total) 1000 veces (por ejemplo, con figus_total = 6),
# guardar los resultados en una lista y calcular el promedio de figuritas necesarias.
n_repeticiones=1000
figus_total=6

def simulaciones(n_repeticiones,figus_total):
    resultados=[]
    for _ in range(n_repeticiones):
        resultado=cuantas_figus(figus_total)
        resultados.append(resultado)
    return resultados

resultados=simulaciones(n_repeticiones,figus_total)

promedio=sum(resultados)/n_repeticiones
print(promedio)


#%%
# EJERCICIO 6: Generalizar el experimento
# Crear una función experimento_figus(n_repeticiones, figus_total)
# que haga lo mismo que el ejercicio 5 pero usando parámetros.
# Debe devolver el promedio de figuritas necesarias.
def simulaciones(n_repeticiones,figus_total):
    resultados=[]
    for _ in range(n_repeticiones):
        resultado=cuantas_figus(figus_total)
        resultados.append(resultado)
    promedio=sum(resultados)/n_repeticiones
    return promedio

resultados=simulaciones(n_repeticiones,figus_total)

promedio=simulaciones(100,6)
print(promedio)

# EJERCICIO 7: Simular un paquete de 5 figuritas
# Simular la generación de un paquete con 5 figuritas al azar,
# donde puede haber repetidas. Guardar las figuritas en una lista.

# EJERCICIO 8: Crear la función comprar_paquete
# Crear una función comprar_paquete(figus_total, figus_paquete)
# que devuelva una lista con figus_paquete figuritas aleatorias (puede haber repetidas).

# EJERCICIO 9: Cuántos paquetes se necesitan
# Crear una función cuantos_paquetes(figus_total, figus_paquete)
# que compre paquetes hasta llenar el álbum, y devuelva cuántos paquetes fueron necesarios.

# EJERCICIO 10: Repetir la simulación con paquetes
# Crear una función experimento_paquetes(n_repeticiones, figus_total, figus_paquete)
# que repita el experimento anterior muchas veces y devuelva el promedio de paquetes comprados.

# %%
