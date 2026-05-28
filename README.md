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

## Ejercicio 2:
En este ejercicio deberán implementar el método para encontrar la factorización LU de una
matriz cuadrada.
* Paso 1:

Programen una función que calcule la factorización LU de una matriz cuadrada, A, de tamaño n×n y que regrese tanto la matriz triangular inferior L, como la matriz triangular superior U. Una vez que hayas terminado prueba tu función con distintas matrices cuadradas usando el comando python A = np.random.random((n,n)) con diferentes valores para n
* 1. La matriz L inicialmente es la matriz identidad con el mismo número de renglones
de A. Si se utilizó la operación Ri = Ri + c*Pivotej entonces en la posición L[i, j] se
coloca -c.
* 2. La matriz U es la matriz que queda en al escalonar A.
Información: Cuando no es posible factorizar una matriz de la forma LU, lo que se aplica es
la factorización P ⋅ A=L ⋅U, donde P es una matriz de permutación.

* Paso 2:

Corrobora que el producto de matrices LU regresa la matriz original A a la que se le 
encontró la factorización.
Para llevar a cabo el producto de matrices LU puedes utilziar la siguiente linea de código 

L.dot(U)

print(A)

print('*************************************')

print(np.dot(L, U))

## Ejercicio 3:

En este ejercicio te toca programar la descomposición QR de una matriz A. La idea es usar el Proceso de Gram-Schmidt:
* Paso 1:

Programa una función que calcule la proyección de un vector u sobre otro vector v

* Paso 2:

Programa una función que calcule la descomposición Q R de una matriz A y que regrese las matrices Q y R.

* Paso 3:

Prueba tu función con diferentes matrices y corrobora que el producto de matrices Q R regresa la matriz original A a la que se le encontró la factorización. Para llevar a cabo el producto de matrices Q R puedes utilizar la siguiente línea de código Q.dot(r)
