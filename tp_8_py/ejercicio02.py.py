"""
Determinar a que intervalo pertenece. [-1;0) o (0;1]
"""
def intervalos (numero):
    """
    Comprueba a que intervalo corresponde el numero
    """
    resultado=""
    if numero>=-1 and numero<0:
        resultado="pertenece al intervalo [-1;0)"
    elif numero>0 and numero<=1:
        resultado="pertenece al intervalo (0;1]"
    else:
        resultado="no pertenece a ningun intervalo"
    return resultado
X=float(input("Ingrese un numero--> "))
print (f"{X} {intervalos(X)}")
