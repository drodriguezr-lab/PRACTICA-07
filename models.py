

#Aplica eliminacion gaussiana para convertir la matriz M en una matriz triangular superior. Modifica una copia de la matriz
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
