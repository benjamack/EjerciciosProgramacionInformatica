#%%
import random
import numpy as np

##Las figuritas del mundial
##Cada año de Mundial de fútbol se publica un álbum de figuritas. Además del evento deportivo, cada Mundial provoca revuelo alrededor del llenado del álbum. Todos los años de mundiales los medios repiten la misma pregunta acerca de la cantidad de paquetes necesarios para lograr llenar el álbum.

##En el 2014 hasta se hizo referencia a un paper en el artículo periodístico.

##En el 2022, el álbum del Mundial de Qatar requería reunir 860 figuritas para completarse, y se generó un gran revuelo en torno a su colección y distribución. El año que viene vuelve a jugarse el Mundial y, seguramente, volverá a publicarse el álbum correspondiente. ¿Cómo podemos estimar cuántas figuritas vamos a necesitar comprar para completar un álbum?

##El objetivo de esta actividad es modelar y hacer un programa en Python que responda la pregunta: ¿cuántas figuritas hay que comprar para completar el álbum del Mundial?

##La resolución deberá guardarse en un archivo semana_03.py y subirse al repositorio que se cargó en el formulario.

##Datos:
##Álbum con 860 figuritas.
##Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
##Cada paquete trae cinco figuritas.



#%%
##Ejercicio 1: Crear
##Implementá la función crear_album(figus_total) que devuelve un álbum (vector) vacío con figus_total espacios para pegar figuritas.

def crear_album(figus_total):
    album=np.zeros(figus_total, dtype=int)
    return album



# %%
## Ejercicio 2: Incompleto
## ¿Cuál sería el comando de Python que nos dice si hay al menos un cero en el vector que representa el álbum? ¿Qué significa que haya al menos un cero en nuestro vector?
## Implementá la función album_incompleto(A) que recibe un vector y devuelve True si el álbum A no está completo y False si está completo.
## Esta función y la anterior son realmente sencillas --cada una puede escribirse en una sola línea. En otro contexto quizas podrías usar directamente esa línea y evitarte definir la función. Sin embargo, en esta etapa nos parece interesante que organices tu código definiendo estas funciones, por más que tengan solo una línea de código cada una.
def album_incompleto(A):
    if 0 in A:
        return True
    else:
        return False
    


# %%
## Ejercicio 3: Comprar
## Implementá una función comprar_figu(figus_total) que reciba el número total de figuritas que tiene el álbum 
## (dado por el parámetro figus_total) y devuelva un número entero aleatorio que representa la figurita que nos tocó.
## Para esto, podés usar la función random.randint(a, b) que devuelve un número entero aleatorio entre a y b (incluidos).
def comprar_figu(figus_total):
    figu=random.randint(0,figus_total-1)
    return figu



# %%
## Ejercicio 4: Cantidad de compras
## Implementá la función cuantas_figus(figus_total) que, dado el tamaño del álbum (figus_total), genere un álbum nuevo, simule su llenado 
## y devuelva la cantidad de figuritas que se debieron comprar para completarlo.
## Para esto, deberás usar las funciones que definiste antes.

## cuantas_figus(figus_total) debe devolver un número entero que representa la cantidad de figuritas compradas para completar el álbum.
## Vamos a plantear un while que se va a repetir mientras el álbum esté incompleto.
## En cada iteración del while, se va a comprar una figurita y se va a pegar en el álbum.
## Cuando el álbum esté completo, se va a salir del while y se va a devolver la cantidad de figuritas compradas.
def cuantas_figus(figus_total):
    album=crear_album(figus_total)
    figus_compradas=0
    while album_incompleto(album):
        figu=comprar_figu(figus_total)
        album[figu]=album[figu]+1
        figus_compradas+=1
    return figus_compradas 


# %%
## Ejercicio 5:
## Ejecutá n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6 y guardá en una lista los resultados obtenidos en 
## cada repetición. Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, para completar el álbum de seis figuritas.


# %%
## Ejercicio 6:
## Escribí una función llamada experimento_figus(n_repeticiones, figus_total) que simule el llenado de n_repeticiones álbums de figus_total figuritas y 
## devuelva el número estimado de figuritas que hay que comprar, en promedio, para completar el álbum.
## Para esto, una posibilidad es que la función experimento_figus() llame a la función cuantas_figus() tantas veces como lo indica el parámetro 
## n_repeticiones y guarde los resultados parciales en una lista, a partir de la cual luego realice el promedio.
## ¿Cuál es el resultado para 100 repeticiones en un álbum de 860 figuritas?
def simulaciones(n_repeticiones,figus_total):
    resultados=[]
    for _ in range(n_repeticiones):
        resultado=cuantas_figus(figus_total)
        resultados.append(resultado)
    promedio=sum(resultados)/n_repeticiones
    return promedio


#%%
## Ejercicios con paquetes
## Ejercicio 7:
## Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 860. Tené en cuenta que, como en la vida real, puede haber 
## figuritas repetidas en un paquete.
def comprar_figus(figus_total):
    figus = np.array([random.randint(0, figus_total - 1) for _ in range(5)])
    return figus


#%%
## Ejercicio 8:
## Implementá una función comprar_paquete(figus_total, figus_paquete) que, dado el tamaño del álbum (figus_total) y la cantidad de figuritas por 
## paquete (figus_paquete), genere un paquete (lista) de figuritas al azar.
def comprar_paquete(figus_total, figus_paquete):
    paquete=[]
    for _ in range(figus_paquete):
        figu=comprar_figus(figus_total)
        paquete.append(figu)
    return paquete


#%%
## Ejercicio 9:
## Implementá una función cuantos_paquetes(figus_total, figus_paquete) que dado el tamaño del álbum y la cantidad de figus por paquete, genere un 
## álbum nuevo, simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo.
def cuantos_paquetes(figus_total, figus_paquete):
    album=crear_album(figus_total)
    paquetes_comprados=0
    while album_incompleto(album):
        paquete=comprar_paquete(figus_total, figus_paquete)
        album[paquete]=album[paquete]+1
        paquetes_comprados+=1
    return paquetes_comprados


#%%
## Ejercicio 10:
## Calculá n_repeticiones = 100 veces la función cuantos_paquetes, utilizando figus_total = 860, figus_paquete = 5. Guarda los resultados obtenidos 
## en una lista y calculá su promedio. Si los recursos de la computadora lo permiten, hacelo con 1000 repeticiones.

# %%

# %%
if __name__ == "__main__":
    
    n_repeticiones=1000
figus_total=6
resultados=[]

for _ in range(n_repeticiones):
    resultado = cuantas_figus(figus_total)
    resultados.append(resultado)

    figus_necesarias = cuantas_figus(860)
print(f"Se necesitaron {figus_necesarias} figuritas para completar el álbum.")

print(resultados)

# Calculamos el promedio
promedio = sum(resultados) / n_repeticiones
print(f"En promedio, se necesitan {promedio:.2f} figuritas para completar un álbum de {figus_total}.")

resultados=simulaciones(n_repeticiones,figus_total)

promedio=simulaciones(100,6)
print(promedio)

print(comprar_paquete(850, 5))

paquetes_necesarios = cuantos_paquetes(860, 5)
print(f"Se necesitaron {paquetes_necesarios} paquetes para completar el álbum.")

print(resultados)

paquetes_necesarios = cuantos_paquetes(figus_total, 5)

for _ in range(n_repeticiones):
    resultado = cuantos_paquetes(figus_total,5)
    resultados.append(resultado)

# Calculamos el promedio
promedio = sum(resultados) / n_repeticiones
print(f"En promedio, se necesitan {promedio:.2f} figuritas para completar un álbum de {figus_total}.")