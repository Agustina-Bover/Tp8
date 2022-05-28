"""
MIENTRAS el valor ingresado en B sea
POSITIVO, calcular la cantidad de números ingresados
e imprimirla en un mensaje.
"""
contador=0
B=1
while B>0:
    B=int(input("Ingresar numero:"))
    contador+=1
print (f"La cantidad de numeros ingresados fueron: {contador}")
