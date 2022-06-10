#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa
#y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también 
#funcione cuando el día o el mes se introduzcan con un solo carácter.
print("\nFecha de nacimiento\n")
fecha=input("Introduzca su fecha de nacimiento (dd/mm/aaaa):")
fecha.split("/")
print("Dia=> "+fecha.split("/")[0])
print("Mes=> "+fecha.split("/")[1])
print("Año=> "+fecha.split("/")[2])