import numpy as np

#Ejercicio 1
#Parte 1
# Pruebas con diferentes tamaños
for n in [3, 4, 5]:
    print(f"\n=== Matriz de tamaño {n}x{n} ===")
    M = np.random.random((n, n))
    print("Matriz original:")
    print(np.round(M, decimals=4))
    
    U = matrizTriangularSuperior(M)
    print("\nMatriz Triangular Superior:")
    print(np.round(U, decimals=4))
    

#Parte 2
# Pruebas para MatrizTriangularSuperior2(T) con diferentes tamaños
for n in [3, 4, 5]:
    print(f"\n=== Matriz de tamaño {n}x{n} ===")
    M = np.random.random((n, n))
    print("Matriz original:")
    print(np.round(M, decimals=4))
    
    U = matrizTriangularSuperior(M)
    print("\nMatriz Triangular Superior:")
    print(np.round(U, decimals=4))
    
    D = matrizTriangularSuperior2(U)
    print("\nMatriz Triangular Superior:")
    print(np.round(D, decimals=4))


#Parte 3
#Pruebas para Diag(D)
for n in [3, 4, 5]:
    print(f"\n{'='*60}")
    print(f"Matriz de tamaño {n} x {n}")
    print(f"{'='*60}")
    
    M = np.random.random((n, n))
    print("Matriz Original:")
    print(np.round(M, decimals=4))
    
    D = Diag(M)
    print("\nMatriz Diagonal obtenida:")
    print(np.round(D, decimals=6))

#Ejercicio 2
#Parte 1
# Ejemplo 
# Pruebas con diferentes tamaños
for n in [3, 4, 5]:
    print(f"\n{'='*60}")
    print(f"Matriz de tamaño {n} x {n}")
    print(f"{'='*60}")
    
    A = np.random.random((n, n))
    
    try:
        L, U = factorizacionLU(A)
        
        print("Matriz Original A:")
        print(np.round(A, 6))
        
        print("\nMatriz L (triangular inferior):")
        print(np.round(L, 6))
        
        print("\nMatriz U (triangular superior):")
        print(np.round(U, 6))
        
        # Verificación
        LU = L @ U
        error = np.max(np.abs(A - LU))
        print(f"\nError máximo |A - L×U| = {error:.2e}")
        
        if error < 1e-10:
            print("Factorización correcta")
        else:
            print("Error grande en la factorización")
            
    except ValueError as e:
        print(f"Error: {e}")
#Parte 2
# Ejemplo con una matriz 4x4
np.random.seed(123)
A = np.random.random((4, 4))

L, U = factorizacionLU(A)

print("Matriz Original A:")
print(A)

print("\n" + "*"*70)
print("Producto L × U:")
print(L @ U)

print("\nDiferencia (debería ser casi cero):")
print(np.abs(A - L @ U))

#Ejercicio 3
#Parte 1
# Ejemplo 
u = np.array([1, 2, 3])
v = np.array([1, 1, 8])
proj = proyeccion(u, v)

print("u =", u)
print("v =", v)
print("Proyección =", np.round(proj, decimals=4))
