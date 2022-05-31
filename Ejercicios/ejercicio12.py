"""
 Programa que solicita el ingreso de 10 números enteros
y retorna la cantidad de números positivos, negativos y ceros ingresados.
"""

P = 0 # positivos
N = 0 # negativos
C = 0 # ceros

print("Ingrese números:")
for i in range(10):
    X = int(input(" >> "))

    if X > 0:
        P += 1
    elif X < 0:
        N += 1
    else:
        C += 1

print(f"Se ingresaron {C} ceros,\n\t      {P} números positivos\n\t    y {N} números negativos.")
