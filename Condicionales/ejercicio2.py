#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
#introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
print("Validacion de contraseña")
firstPasword = input("Introduzca su contraseña:")
secondPasword = input("Confirme su contraseña:")
if firstPasword.lower() == secondPasword.lower():
    print("Su contraseña coincide.")
else:
    print("La contraseña no coincide.")