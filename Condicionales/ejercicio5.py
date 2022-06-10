#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
#iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte 
#al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
print("Pagos tributarios")
age = int(input("Ingrese su edad:"))
income = float(input("Especifique sus ingresos mensuales:"))
if age >= 16:
    if income >= 1000:
        print("Usted debe de presentar su pago tributario.")
    else:
        print("Usted no debe presentar pago tributario.")
else:
    print("Usted no debe presentar pago tributario.")