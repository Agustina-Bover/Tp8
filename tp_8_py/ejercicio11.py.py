"""
 HASTA que la suma de los valores ingresados en Z
sea mayor a 500. Determinar e imprimir la cantidad de
números ingresados.
"""
contador=0
Z=0
anterior=0
while Z!=500:
    anterior=Z
    Z=int(input("Ingresar un numero:"))
    Z=Z+anterior
    contador+=1
print (f"Z={Z}")
print(f"La cantidad de numeros ingresados fueron:{contador}")
