# Para la resolucion del problema se asume que para que una manzana este rodeada debe encontrarse TOTALMENTE rodeada por otras 
# manzanas, es decir, las manzanas de los extremos no entran en el calculo. En base a esto necesitamos que nuestra matriz sea 
# como minimo de 3x3.

import random


def imprimirmatriz(mat):
    for fila in mat:
        for col in fila:
            print(f"{col:3}", end="")
        print()

        
def calcular_vecinos(matriz,i,j):
    dim = len(matriz)-1
    suma = 0
    if (i>0 and i<dim) and (j>0 and j<dim):
        # sumo los valores del cuadrado de 3x3 de manzanas
        for sub_i in range(i-1,i+2):
            for sub_j in range(j-1,j+2):
                suma = suma + matriz[sub_i][sub_j]
        # resto el valor de la manzana central
        suma = suma - matriz[i][j]
    else:
        pass
    return suma        
        
        
# ingresar dimension matriz
n = int(input("Ingrese el tamaño de la matriz: "))
while n<1:
    print("Tamaño inválido. Debe ser mayor que 0")
    n = int(input("Ingrese el tamaño de la matriz: "))
print()

# Creamos la matriz directamente con los números al azar usando listas por comprensión anidadas
matriz = [[random.randint(0,99) for columna in range(n)] for fila in range(n)]

imprimirmatriz(matriz)

# lista que contiene [fila,columna,suma]
lista_resultado = [0,0,0]
# recorrer matriz buscando las coordenadas de la mayor cantidad de habitantes
for i in range(n):
    for j in range(n):
        resultado = calcular_vecinos(matriz,i,j)
        if resultado > lista_resultado[2]:
            lista_resultado = [i,j,resultado]
            
# imprimir la conclusion
print()
if lista_resultado[2]>0:
    print(f'La manzana con mayor cantidad de vecinos esta ubicada en la fila {lista_resultado[0]} y columna {lista_resultado[1]}, con {lista_resultado[2]} vecinos')
else:
    print('El calculo no se pudo realizar por las dimensiones de la matriz o porque no existen habitantes en las manzanas')
