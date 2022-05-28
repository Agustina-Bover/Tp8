"""
Ingresar 10 números enteros usando la variable X. Determinar
e imprimir un mensaje informando: la cantidad de números POSITIVOS,
la cantidad de números NEGATIVOS y, la cantidad de CEROS ingresados.
"""
positivos=0
negativos=0
ceros=0
X=0
for i in range (10):
    X=int(input("Ingresar un numero:"))
    if X==0:
        ceros+=1
    elif X>0:
        positivos+=1
    elif X<0:
        negativos+=1
print (f"La cantidad de numeros ceros = {ceros}")
print (f"La cantidad de numeros positivos = {positivos}")
print (f"La cantidad de numeros negativos = {negativos}")
