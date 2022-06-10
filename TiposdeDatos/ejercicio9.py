#Escribir un programa que pregunte al usuario una cantidad a invertir, 
#el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
print("\nInversion\n")
canInv=float(input("Ingrese la cantidad a invertir:"))
intAnual=float(input("Ingrese el interes anual:"))
años=float(input("Ingrese el numero de alos a invertir:"))
#exponecnial: **
total=round(canInv*(intAnual/100+1)**años,2)
print(f"Al concluir {años}años,usted tendra:{total}")
