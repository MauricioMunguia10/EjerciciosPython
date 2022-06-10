#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
#calcule el índice de masa corporal y lo almacene en una variable, 
#y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
#es el índice de masa corporal calculado redondeado con dos decimales.
print("\nCalculadora de IMC\n")
peso=input("Ingrese su peso en kg:")
est=input("Ingrese su estatura en m:")
imc=round((float(peso))/(float(est)*float(est)),2)
print(f"Su IMC es:{imc}")