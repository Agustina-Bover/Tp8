"""
 Programa que solicita el ingreso de un número real
y determina si el mismo pertenece o no a uno de los intervalos dados.
"""

I = "" # intervalo
X = float(input("Ingrese un valor numérico real: "))

if (X >= -1) and (X < 0):
    I = "pertenece al intervalo [-1;0)"
elif (X > 0) and (X <= 1):
    I = "pertenece al intervalo (0;1]"
else:
    I = "no pertenece a ningun intervalo."

print(f"'{X}' {I}")
