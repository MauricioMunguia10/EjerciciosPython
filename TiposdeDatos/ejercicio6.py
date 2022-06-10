#Escribir un programa que lea un entero positivo, , introducido por el usuario y 
# después muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
print("Sumatoria de 1 hasta el nuemro introducido.")
num=input("Selecciona un numero: ")
n=int(num)
sumt=(n*(n+1))/2
print(f"La suma desde 1 hasta {n} es:{sumt}")