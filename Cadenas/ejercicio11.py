#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y 
#muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario 
#con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total 
#con 8 dígitos enteros y 2 decimales.

print("\nCompras\n")
opc=''
name=[]
uni=[]
precio=[]
i=0
while opc!='no':

    name.append(input("Ingrese el nombre del producto:"))
    uni.append(input("Ingrese el numero de unidades del producto:"))
    precio.append(input("Ingrese el precio del producto:"))
    opc=input("Agregar otro producto? (si/no):")
    i+=1

print("Nombre       Cantidad       Precio       Total")
n=0
while n<i:
    print(f"{name[n]}           {uni[n]:}        {precio[n]}         {float(uni[n])*float(precio[n])}")
    n+=1
