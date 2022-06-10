#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero
#e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

print("\nNombre\n")
nombre=input("Ingrese su nombre:")
num=int(input("Ingrese un numero:"))
i=1
while i<=num:
    print(nombre)
    i+=1
