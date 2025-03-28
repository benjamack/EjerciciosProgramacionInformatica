###Ejercicio 1: Invertir una lista
# Escribir una función invertir_lista(lista) que dada una lista devuelva otra que tenga los mismos elementos pero en el orden inverso. 
# Es decir, el que era el primer elemento de la lista de entrada deberá ser el último de la lista de salida y análogamente con los demás elementos.

def invertir_lista(lista):
    return lista[::-1]

lista = [1,2,3,4,5]

lista_invertida = invertir_lista(lista)
print(lista_invertida)

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
        if nro %2 == 0:
            nro / 2
        else:
            nro = 3 * nro + 1
        pasos += 1
    return pasos