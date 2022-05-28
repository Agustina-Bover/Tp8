"""
Ingresar un número natural en la variable N. Determinar e imprimir un mensaje informando: si ‘N
es PAR’ o si ‘N es IMPAR’
"""
def par_impar (numero):
    """
    Determina si el numero es par o impar
    """
    resultado=""
    if numero % 2==0:
        resultado= " es par"
    else:
        resultado= " es impar"
    return resultado
N=int(input("Ingrese un numero "))
print (f"{N}{par_impar(N)}")
