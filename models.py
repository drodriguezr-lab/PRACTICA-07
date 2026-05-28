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

#Ejercicio 2
#Parte 1
def factorizacionLU(A):
    A = A.copy().astype(float)  # Trabajamos con una copia
    n = A.shape[0]
    # Inicializamos L como matriz identidad
    L = np.eye(n)
    for j in range(n):  # columna pivote
        for i in range(j+1, n):  # filas debajo del pivote
            if abs(A[j, j]) < 1e-12:  # Pivote cercano a cero
                raise ValueError("Pivote cero encontrado. Se necesita pivoteo (PA=LU).")
            factor = A[i, j] / A[j, j]
            L[i, j] = factor                    # Guardamos el multiplicador en L
            A[i, j:] -= factor * A[j, j:]       # Eliminación gaussiana       
    U = A  # Lo que queda de A después de la eliminación es U
    return L, U

#Parte 2






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

#Parte 2
def GramSchmidtQR(A):
    A = np.array(A, dtype=float)
    m, n = A.shape
    
    # Inicializamos Q y R
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    
    # u1 = v1 (primera columna)
    u = A[:, 0].copy()
    normaU = np.linalg.norm(u)
    
    Q[:, 0] = u / normaU
    R[0, 0] = normaU
    
    for k in range(1, n):
        u = A[:, k].copy()
        
        # Restamos las proyecciones sobre las columnas anteriores de Q
        for j in range(k):
            proj = proyeccion(u, Q[:, j])
            u = u - proj
            R[j, k] = np.dot(Q[:, j], A[:, k])  # <qj, vk>
        
        # Normalizamos
        normaU = np.linalg.norm(u)
        if normaU < 1e-10:
            raise ValueError("Las columnas de A no son linealmente independientes")
            
        Q[:, k] = u / normaU
        R[k, k] = normaU
    
    return Q, R

#Parte 3
#Prueba la descomposición QR y verifica que Q @ R ≈ A
def probarQR(A, nombre="Matriz"):
    print(f"\n{'='*60}")
    print(f"{nombre}:")
    print(A)
    
    Q, R = GramSchmidtQR(A)
    
    print("\nMatriz Q:")
    print(np.round(Q, decimals=6))
    
    print("\nMatriz R:")
    print(np.round(R, decimals=6))
    
    # Reconstrucción
    A_reconstruida = Q @ R
    
    print("\nA reconstruida (Q @ R):")
    print(np.round(A_reconstruida, decimals=6))
    
    # Verificación de precisión
    error = np.linalg.norm(A - A_reconstruida)
    print(f"\nError ||A - Q@R|| = {error:.2e}")
    print("La reconstrucción fue un éxito" if error < 1e-8 else " Falló la verificación")


