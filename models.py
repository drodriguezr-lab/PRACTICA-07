

#Aplica eliminacion gaussiana para convertir la matriz M en una matriz triangular superior. Modifica una copia de la matriz
#Ejercicio 1
# Parte 1
def matrizTriangularSuperior(M):
    # Hacemos una copia para no modificar la matriz original
    A = M.copy().astype(float)  # Convertimos a float para evitar problemas
    n = A.shape[0]
    for k in range(n):  # Para cada columna (pivote)
        # Verificamos que el pivote no sea cero (evitamos división por cero)
        if abs(A[k, k]) < 1e-10:
            print(f"Advertencia: Pivote casi cero en posición ({k}, {k})")
            continue 
        for i in range(k + 1, n):  # Para cada fila debajo del pivote
            factor = A[i, k] / A[k, k] 
            for j in range(k, n):  # Hacemos cero los elementos debajo del pivote
                A[i, j] = A[i, j] - factor * A[k, j]
    return A

#Parte 2
def matrizTriangularSuperior2(T):
    # Hacemos una copia para no modificar la matriz original
    A = T.copy().astype(float)  # Convertimos a float para evitar problemas
    n = A.shape[0]
    for k in range(n-1,-1,-1):  # Empezamos desde la última fila
        # Verificamos que el pivote no sea cero (evitamos división por cero)
        if abs(A[k, k]) < 1e-10:
            print(f"Advertencia: Pivote casi cero en posición ({k}, {k})")
            continue 
        for i in range(k -1, -1,-1):  # Filas por encima de la fila k
            factor = A[i, k] / A[k, k] 
            for j in range(k, n):  # Solo necesitamos desde la columna k en adelante
            
                A[i, j] = A[i, j] - factor * A[k, j]
    return A
    
#Parte 3
def Diag(M):
    # Paso 1: Convertir a triangular superior
    U = matrizTriangularSuperior(M)
    # Paso 2: Convertir a matriz diagonal
    D = matrizTriangularSuperior2(U)
    # Extrae y devuelve solo la diagonal principal
    diagonal = np.diag(np.diag(D))
    return diagonal


#Ejercicio 3
#Parte 1
#Calcular la proyección del vector u sobre el vector v.
def proyeccion(u, v):
    # <u, v> = u · v
    productoInterno = np.dot(u, v)
    # ||v||²
    normavCuadrado = np.dot(v, v)
    if normavCuadrado == 0:
        raise ValueError("El vector v no puede ser el vector cero")
    
    return (productoInterno / normavCuadrado) * v
