#%%
###Ejercicio 1: Invertir una lista
# Escribir una función invertir_lista(lista) que dada una lista devuelva otra que tenga los mismos elementos pero en el orden inverso. 
# Es decir, el que era el primer elemento de la lista de entrada deberá ser el último de la lista de salida y análogamente con los demás elementos.
#%%
def invertir_lista(lista):
    return lista[::-1]

def invertir_lista(lista):
    res = []
    for i in range(len(lista)):
        res.append(lista[len(lista) - 1 - i])
    return res
# Otra forma de hacerlo es usando el método reverse() de las listas

###lista = [1,2,3,4,5]

###lista_invertida = invertir_lista(lista)
###print(lista_invertida)



#%%
###Ejercicio 2: Conjetura de Collatz
# Escribir una función que compute la conjetura de Collatz para un número entero dado. La misma se puede enunciar como:

# Empezamos con un número entero positivo,
# Lo evaluamos, si el número es par entonces lo dividimos entre 2. Si es impar, entonces se multiplica por 3 y se le suma 1.
# Al resultado lo volvemos a evaluar y nuevamente aplicamos las operaciones correspondientes hasta que obtengamos un 1.
# Retornar la cantidad de pasos realizados.
# Esto no se ha demostrdo pero funciona para todos los casos probados.

# La función debe llamarse collatz(nro).

def collatz(nro):
    pasos = 0
    while nro != 1:
        if nro % 2 == 0:
            nro = nro / 2
        else:
            nro = 3 * nro + 1
        pasos += 1
    return pasos

print(collatz(15))

#%%
## Ejemplo visto en clase:
def collatz(n):
    if n == 1:
        return 0
    else:
        if n % 2 == 0:
            n= n // 2
        else:
            n = 3 * n + 1
        return 1 + collatz(n)
print(collatz(4))

## 📚 ¿Qué es una función recursiva?
## Es una función que se llama a sí misma para resolver un problema más pequeño, hasta llegar a un caso base que corta la repetición.
## 🧠 Explicación de cómo funciona:
## factorial(6) llama a factorial(5)
## factorial(5) llama a factorial(4)
## ...
## Hasta que llega a factorial(0), que devuelve 1
## A partir de ahí, se resuelven todas las multiplicaciones hacia arriba

#%%
# Función recursiva para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo: 6! = 720
print(factorial(6))



#%%
###Ejercicio 3: Diccionarios
# Dado un diccionario que dadas ciertas claves (que serán strings) tiene ciertas definiciones (lista de strings), dar dos funciones:
# contar_definiciones(d) que dado un diccionario devuelve otro diccionario con las mismas claves y para cada una de ellas la cantidad de definiciones que tiene.
# cantidad_de_claves_letra(d, l) que dado el diccionario d devuelve la cantidad de entradas (claves) que comienzan con la letra l.

# Creación de diccionario con múltiples definiciones
mi_diccionario = {
    "Matías": ["hincha de Boca", "le gusta el fútbol"],
    "Daniela": ["fan de Racing"],
    "Benja": ["Boca"],
    "Leo": ["le gusta el helado", "River", "baila"]
}
#%%
# Contar definiciones
def contar_definiciones(d):
    nuevo_dic = {}
    for clave in d:
        nuevo_dic[clave] = len(d[clave])
    return nuevo_dic
#%%
# cantidad_de_claves_letra(d, l)
def cantidad_de_claves_letra(d, l):
    contador = 0
    for clave in d:
        if clave.startswith(l):
            contador += 1
    return contador

### print(contar_definiciones(mi_diccionario))

### print(cantidad_de_claves_letra(mi_diccionario, "L"))



#%%
### Ejercicio 4: Propagación
# Vamos a modelar una fila con varios fósforos uno al lado del otro. Los fósforos pueden estar en tres estados: nuevos, prendidos fuego o ya gastados (carbonizados). Representaremos esta situación con una lista L con un elemento por fósforo, que en cada posición tiene un 0 (nuevo), un 1 (encendido) o un -1 (carbonizado). El fuego se propaga inmediatamente de un fósforo encendido a cualquier fósforo nuevo que tenga a su lado. Los fósforos carbonizados no se encienden nuevamente.
# Escribir una función llamada propagar que reciba una lista con 0’s, 1’s y -1’s y devuelva la lista en la que los 1’s se propagaron a sus vecinos con 0.
# Por ejemplo:
## >>> propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
## [ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
## >>> propagar([ 0, 0, 0, 1, 0, 0])
## [ 1, 1, 1, 1, 1, 1]

def propagar(fosforos):
    # Creamos una copia para no modificar la original
    resultado = fosforos.copy()

    # 🔥 Propagación de izquierda a derecha
    prendido = False  # Variable que indica si hay fuego activo
    for i in range(len(resultado)):
        if resultado[i] == 1:
            prendido = True  # Encontramos fuego, comienza propagación
        elif resultado[i] == -1:
            prendido = False  # Fósforo quemado bloquea el fuego
        elif resultado[i] == 0 and prendido:
            resultado[i] = 1  # Se prende si hay fuego activo

    # 🔥 Propagación de derecha a izquierda
    prendido = False
    for i in range(len(resultado)-1, -1, -1):  # Recorremos al revés
        if resultado[i] == 1:
            prendido = True
        elif resultado[i] == -1:
            prendido = False
        elif resultado[i] == 0 and prendido:
            resultado[i] = 1

    return resultado

### print(propagar([0, 0, 0, -1, 1, 0, 0, -1, 0, 1, 0, 0]))
