#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
#y muestre por pantalla el número de euros y el número de céntimos del precio introducido
print("\nPrecio de productos\n")
precio=input("Ingrese el precio en euros con dos decimaales:")
print(f"El precio es de {precio.split('.')[0]} euros con {precio.split('.')[1]} centimos.")