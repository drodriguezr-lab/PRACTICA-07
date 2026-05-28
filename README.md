## PRÁCTICA 07 Práctica 7: Diagonalización Por Método De Gauss, Factorización LU y Factorización QR

##  INTEGRANTES 
* Rodríguez Rodríguez Diego


## Uso e instalación
Instalamos los siguientes paquetes:
1. `numpy` como np


## Ejercicio 1:
En este ejercicio deberán implementar el método de eliminación Gaussiana para diagonalizar una matriz cuadrada.

* Paso 1:

Programa una función que reciba una Matriz cuadrada de tamaño n×n, M, y que por medio del método de eliminacion Gaussiana regrese una Matriz triangular superior. Una vez que hayas terminado prueba tu función con distintas matrices cuadradas usando el comando. M = np.random.random((n,n)) con diferentes valores para $n$

* Paso 2:

Programa una función que reciba una Matriz cuadrada de tamaño n× n, T, que además sea triangular superior (como la que obtenemos al usar las función que programaste en el paso 1) y que se encargue de eliminar todos los elementos superiores a la diagonal usando una vez más el método de eliminación Gaussiana.

* Paso 3:

Finalmente, programa una función que reciba una Matriz cuadrada de tamaño n×n, M, y que mande a llamar las dos funciones que programaste anteriormente, de forma que al final regrese la diagonal de la matriz que obtuviste al final del procedimiento
def Diag(D):
