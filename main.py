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



#Ejercicio 3
#Parte 1
# Ejemplo 
u = np.array([1, 2, 3])
v = np.array([1, 1, 8])
proj = proyeccion(u, v)

print("u =", u)
print("v =", v)
print("Proyección =", np.round(proj, decimals=4))
