#Creamos una matriz
matriz1 = [[1, 2, 3, 4], [-5, 6, 7, 8], [9, 0, 1, 2]]
print("Matriz 1: \n", matriz1, "\n")
matriz2 = [[3, 4, 5, 6], [7, 8, 9, 0], [1, 2, 3, -4]]
print("Matriz 2: \n", matriz2, "\n")

#Realizamos una operación entre las matrices
suma1 = matriz1 + matriz2
print("La suma de lasdos matrices es: \n", suma1, "\n")

#Imprimimos posiciones específias de la matriz
print("Lista en la primer fila: \n", matriz1[0], "\n")
print("Ítem en la fila 2, posición 2: \n", matriz2[1][1], "\n")


#Realizamos una resta de matrices
def resta1(m, n):
    '''Resta dos matrices'''
    if len(n) != len(m):
        print(
            "Recuerda que las dos matrices deben tener el mismo número de filas"
        )
    lis = []
    for i in range(0, len(m)):
        lis.append([])
        for j in range(0, len(m[0])):
            lis[i].append(m[i][j] - n[i][j])
    return lis


print(resta1(matriz1, matriz2))


#Multiplicamos la matriz por un escalar
def multiplicacion1(number, suma1):
    '''Multiplica una matriz por un escalar'''
    lis = []
    for i in range(0, len(suma1)):
        lis.append([])
        for j in range(0, len(suma1[0])):
            lis[i].append(suma1[i][j] * number)
    return lis


print(multiplicacion1(3, matriz1))

print("\nCOMPARAMOS CON NUMPY\n")

#Importamos la libreria
import numpy as nmp

#Almacenamos las secuencias
array1 = nmp.array([1, -2, 3, 4, 5, -6, 7])
array2 = nmp.array([0, -1.2, -3, 4, 5, -6, 7])
print("Arreglo 1: \n", array1, "\n")
print("Arreglo 2: \n", array2, "\n")

#Arreglo de ceros en tipo float
acero1 = nmp.zeros(5, dtype=float)
print("Arreglo de ceros en tipo float: \n", acero1, "\n")

#Arreglo de ceros, con dimensión orientada por el sistema
acero2 = nmp.zeros((3, 8), dtype=int)
print("Arreglo de ceros con dimensión esspecífica: \n", acero2, "\n")

#Arreglo de unos
auno1 = nmp.ones(7)
print("Arreglo de unos: \n", auno1, "\n")

#Arreglo para imprimir un número la veces que sea necesario para llenar unas dimeniones específicas
full1 = nmp.full((4, 7), 14)
print("Arreglo full: \n", full1, "\n")

#Arreglo con rangos (incluidos floats)
arange1 = nmp.arange(-7, 1.4)
print("Arreglo arange: \n", arange1, "\n")

#Arreglo con un valor específico de repeticiones con misma distancia entre dos puntos
linspace1 = nmp.linspace(-7, 14, 7)
print("Arreglo linspace: \n", linspace1, "\n")

#Imprimimos elementos específicos
print("Elementos de array 1 y 2")
print(array1[-7])
print(array1[1:])

#Realizamos una multiplicacion entre arreglos
multiplicacion2 = array1 * array2
print("\nMultiplicacion entre el arreglo 1 y 2: \n", multiplicacion2, "\n")

#Realizamos una multiplicación por escalar
multiplicacion3 = array1 * 14
print("Multiplicacion por un escalar: \n", multiplicacion3, "\n")

#Comparamos dos arreglos
comparacion1 = array1 > array2
print("¿El arreglo 1 es mayor que el 2?: \n", comparacion1, "\n")

#Verificamos que al menos uno de los elementos sea verdadero
comparacion2 = any(array1 < array2)
print("¿Por lo menos un elemento del arreglo 1 es menor que los del 2?: \n",
      comparacion2, "\n")

#Verificamos que todos los elementos sean verdaderos
comparacion3 = all(array1 < array2)
print("¿Todos los elementos del arreglo 1 son menores que los del 2?: \n",
      comparacion3, "\n")

#Verificamos si los elementos son iguales
comparacion4 = array1 != array2
print("¿El arreglo 1 es diferente al 2?: \n", comparacion4, "\n")

print("\nREALIZAMOS OPERACIONES CON MATRICES EN NUMPY\n")

#Creamos las matrices
matriz3 = nmp.matrix([[1, 2, 3], [4, -5, 6], [7, 8, 9]])
matriz4 = nmp.matrix([[0, -1, 2], [3, 4, 5], [6, 7, 8]])
print("Matriz 3: \n", matriz3, "\n")
print("Matriz 4: \n", matriz4, "\n")

#Elevamos la matriz a una potencia
potencia1 = matriz4**2
print("Elevamos la matriz 4 a una potencia de 7: \n", potencia1, "\n")

#Restamos dos matrices
resta1 = matriz3 - matriz4
print("Restamos la matriz 4 a la 3: \n", resta1, "\n")
