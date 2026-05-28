

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
    

