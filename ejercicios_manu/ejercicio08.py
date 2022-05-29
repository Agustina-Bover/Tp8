"""
 Programa que solicita el ingreso de 6 pares de números naturales
y retorna el promedio de cada par.
"""

for i in range(6):
    print(f"Ingrese el par de notas [{i + 1}]:")
    N1 = int(input(" >> "))
    N2 = int(input(" >> "))
    assert (N1 >= 0 and N2 >= 0) and (N1 <= 10 and N2 <= 10), "Nota inválida."

    promedio = float((N1 + N2) / 2)
    print(f"Promedio: {promedio}\n")
