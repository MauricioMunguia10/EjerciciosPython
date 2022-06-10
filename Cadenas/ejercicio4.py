#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension
#donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
#Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla
#el número de teléfono sin el prefijo y la extensión.
print("\nNumero de telefono\n")
num=input("Ingrese un numero telefonico con el siguiente formato:\ncodigo de pais,numero de telefono y extension.")
print(f"El numero es:\n prefijo {num[0:3]}, numero {num[3:13]}, extension {num[13:15]}")
