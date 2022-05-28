"""
Ingresar 6 pares de números naturales que representan
notas de parciales, en las variables N1 y N2, y que calcule e imprima el promedio de cada par de
notas.
"""
for i in range (6):
    N1=float(input("Ingrese Nota 1: "))
    N2=float(input("Ingrese Nota 2: "))
    promedio= (N1+N2)/2
    print (f"El promedio de ambas notas es: {promedio}")
