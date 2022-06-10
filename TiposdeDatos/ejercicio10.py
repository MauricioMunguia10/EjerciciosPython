#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
#Suele hacer venta por correo y la empresa de logística les cobra por peso de
#cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán
#en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
#Escribir un programa que lea el número de payasos y muñecas vendidos en el último 
#pedido y calcule el peso total del paquete que será enviado.

#gramos
pesopay=112
pesomuñeca=75
print("\nLogistica\n")
pay=int(input("Ingrese el numero de payasos vendidos"))
muñecas=int(input("Ingrese el numero de muñecas vendidas"))
peso=(pay*pesopay)+(muñecas*pesomuñeca)
if peso>=1000:
    kg=peso/1000
    #g=peso%1000
    print(f"Usted va a enviar {pay} payasos y {muñecas} muñecas.\nEl peso total del pedido es de: {kg} kg.")
else:
    print(f"Usted va a enviar {pay} payasos y {muñecas} muñecas.\nEl peso total del pedido es de: {peso} g.")
    


