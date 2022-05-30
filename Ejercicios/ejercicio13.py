"""
 Programa que solicita el ingreso de dos números naturales
y realiza la multiplicación (sumas repetitivas) del primero por el segundo.
"""

print("Ingrese multiplicando y multiplicador:")
P = int(input(" >> ")) # multiplicando
Q = int(input(" >> ")) # multiplicador
assert P > 0 and Q > 0, "Se ingresaron números no naturales."

RTA = 0

for i in range(Q):
    RTA += P

print(f"P: {P}\nQ: {Q}\nP * Q -> {P} * {Q} = {RTA}")
