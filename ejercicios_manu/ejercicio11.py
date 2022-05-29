"""
Programa que solicita el ingreso de números enteros hasta que la suma de estos supere a 500.
"""

A = 0 # anterior
C = 0 # contador
Z = 0

print("Ingrese números")
while Z < 500:
    A = Z

    Z = int(input(" >> "))
    assert isinstance(Z, int) and Z < 500, "Qué poco emocionante lo tuyo..."

    Z += A
    C += 1

print(f"Se ingresaron {C} números, con total: {Z}\nLa suma de los mismos ", end = "")
if Z > 500:
    print(f"superó a 500 por {Z - 500} unidades.")
else:
    print("no superó a 500.")
