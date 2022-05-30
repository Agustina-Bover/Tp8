"""
 Programa que solicita el ingreso de un número natural
y determinar e imprimir un mensaje informando su pariedad.
"""

P = "" # pariedad
N = int(input("Ingrese un número natural: "))
assert N > 0, "El número no es natural"

if N % 2 == 0:
    P = "PAR"
else:
    P = "IMPAR"

print(f"N es {P}.")
