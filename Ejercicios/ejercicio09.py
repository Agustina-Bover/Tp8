"""
 Programa que solicita el ingreso de un número
e imprime un mensaje informando su multiplicidad con 3.
"""

M = "" # multiplicidad
A = int(input("Ingrese un numero natural: "))
assert isinstance(A, int) and A > 0, "Ups, no se ha ingresado un número natural."

if A % 3 != 0:
    M = "no "

print(f"{A} {M}es múltiplo de 3.")
