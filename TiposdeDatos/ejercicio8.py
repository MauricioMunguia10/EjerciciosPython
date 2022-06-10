#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m>
#da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
#y <c> y <r> son el cociente y el resto de la división entera respectivamente.
print("Division")
n=input("Ingrese un numero:")
m=input("Ingrese otro numero:")
div=0
casev=input("Seleccione entre division exacta(ex) o inexacta(inex):")
if casev=='ex':
    div=round(int(n)/int(m),3)
    print(f"El resultado es:{div}")
elif casev=='inex':
    div=int(n)//int(m)
    sobra=int(n)%int(m)
    print(f"El resultado es:{div} y sobra:{sobra}")
else:
    print("Opcion no seleccionada")