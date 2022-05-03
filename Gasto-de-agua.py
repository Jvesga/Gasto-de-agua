"""Programa para calcular el gasto de agua"""

print("---------------------------------")
print("--Coste de agua de una vivienda--")
print("---------------------------------")

x = int(input("Ingrese el numero de metros cubicos gastados: "))

if x < 50:
    z = 10000
elif x >= 50 and x <= 200:
    z = 10000 + (2000 *(x - 50))    
elif x > 200:
    z = 10000 + (3000 *(x - 50))    

print("-EL valor a pagar es de " + str(z) + " pesos")
