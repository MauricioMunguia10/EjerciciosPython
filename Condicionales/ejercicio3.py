#Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
#Si el divisor es cero el programa debe mostrar un error.
print("Division")
anum = int(input("Ingrese el numerador:"))
bnum = int(input("Ingrese el denominador:"))
if bnum == 0:
    print("Error: El denominador no puede ser cero.")
else:
    print("El resultado es:", anum/bnum)