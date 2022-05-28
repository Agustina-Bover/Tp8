"""
Se pide que, utilizando solamente la operación de suma,
calcule el resultado de la operación P * Q e imprima el valor
de P, de Q y de P * Q.
"""
P=int(input("ingresa el numero multiplicando: "))
Q=int(input("ingresa el numero multiplicador: "))
rta=0
for i in range (Q):
    rta+=P
print (f"P= {P}")
print (f"Q= {Q}")
print (f"P*Q= {rta}")
