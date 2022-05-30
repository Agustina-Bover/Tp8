"""
Programa que solicita el ingreso de números enteros hasta detectar el ingreso de un número negativo.
"""

C = 0 # contador
B = 1

print("Ingrese números")
while B > 0:
    B = int(input(" >> "))
    C += 1

print (f"La cantidad de numeros ingresados fueron: {C}")
