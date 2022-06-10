#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.
print("\nCalculadroa de salario\n")
hora=input("Numero de horas trabajadas:")
costo=input("Coste por hora: ")
sal=int(hora)*int(costo)
print("Usted cobra:",sal)