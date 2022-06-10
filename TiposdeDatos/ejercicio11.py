#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
#Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
#final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
#depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular 
#y mostrar por pantalla la cantidad de ahorros tras el primer, 
#segundo y tercer años. Redondear cada cantidad a dos decimales.
from sqlite3 import adapt


print("\nCuenta de ahorros\n")
salini=float(input("Ingrese su saldo inicial:"))
def interes(a): 
    if a==1:
        inte=salini+(salini*.04)
        return round(inte,2) 
    else:
        inte=float(salini*((1.04)**(a)))
        return round(inte,2)
#uno=salini+(salini*.04)
#dos=uno+(uno*0.04)
#tres=dos+(dos*0.04)
new_template="""
    CUENTA
    Saldo inicial:{sal}
    Saldo primer año:{saluno}
    Saldo segundo año:{saldodos}
    Saldo tercer año:{saltres}
    """
print(new_template.format(sal=salini,saluno=interes(1),saldodos=interes(2),saltres=interes(3)))
#print('\n',uno,dos,tres)